"""
Skool Community Scraper
A tool to scrape posts and comments from your Skool community.
"""

import os
import time
import json
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class Post:
    """Represents a Skool community post"""
    id: str
    title: str
    content: str
    author: str
    timestamp: datetime
    likes: int
    comments_count: int
    url: str
    category: str = ""
    comments: List[Dict] = None

    def __post_init__(self):
        if self.comments is None:
            self.comments = []

@dataclass
class Comment:
    """Represents a comment on a Skool post"""
    id: str
    content: str
    author: str
    timestamp: datetime
    likes: int
    replies: List[Dict] = None

    def __post_init__(self):
        if self.replies is None:
            self.replies = []

class SkoolScraper:
    """Main scraper class for Skool communities"""
    
    def __init__(self, community_url: str, headless: bool = True):
        self.community_url = community_url
        self.headless = headless
        self.driver = None
        self.wait = None
        self.posts = []
        
    def setup_driver(self):
        """Initialize the Chrome WebDriver"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self, email: str, password: str) -> bool:
        """Login to Skool"""
        try:
            self.driver.get("https://www.skool.com/login")
            
            # Wait for and fill email
            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
            
            # Fill password
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.send_keys(password)
            
            # Click login button
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for successful login (check for dashboard or community page)
            self.wait.until(
                EC.any_of(
                    EC.url_contains("/dashboard"),
                    EC.url_contains("/community")
                )
            )
            
            print("✅ Successfully logged in to Skool")
            return True
            
        except TimeoutException:
            print("❌ Login failed - timeout waiting for login completion")
            return False
        except Exception as e:
            print(f"❌ Login failed: {str(e)}")
            return False
    
    def navigate_to_community(self):
        """Navigate to the specified community"""
        try:
            self.driver.get(self.community_url)
            
            # Wait for community page to load
            self.wait.until(
                EC.any_of(
                    EC.presence_of_element_located((By.CLASS_NAME, "post")),
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='post']")),
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".feed-item"))
                )
            )
            
            print(f"✅ Successfully navigated to community: {self.community_url}")
            return True
            
        except TimeoutException:
            print("❌ Failed to load community page")
            return False
        except Exception as e:
            print(f"❌ Error navigating to community: {str(e)}")
            return False
    
    def scroll_and_load_posts(self, max_posts: int = 50):
        """Scroll down to load more posts"""
        posts_loaded = 0
        scroll_attempts = 0
        max_scroll_attempts = 10
        
        while posts_loaded < max_posts and scroll_attempts < max_scroll_attempts:
            # Scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            # Count current posts
            post_elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-testid='post'], .post, .feed-item")
            current_count = len(post_elements)
            
            if current_count > posts_loaded:
                posts_loaded = current_count
                print(f"📄 Loaded {posts_loaded} posts...")
            else:
                scroll_attempts += 1
                
            time.sleep(1)
        
        print(f"✅ Finished loading posts. Total found: {posts_loaded}")
        return post_elements[:max_posts]
    
    def extract_post_data(self, post_element) -> Optional[Post]:
        """Extract data from a single post element"""
        try:
            # Extract post ID
            post_id = post_element.get_attribute("data-post-id") or \
                     post_element.get_attribute("id") or \
                     str(hash(post_element.get_attribute("outerHTML")))[1:10]
            
            # Extract title/content - try multiple selectors
            title_selectors = [
                ".post-title",
                "[data-testid='post-title']",
                "h1, h2, h3",
                ".content-title"
            ]
            
            title = ""
            for selector in title_selectors:
                try:
                    title_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    title = title_elem.text.strip()
                    break
                except NoSuchElementException:
                    continue
            
            # Extract content
            content_selectors = [
                ".post-content",
                "[data-testid='post-content']",
                ".content-body",
                ".post-text",
                "p"
            ]
            
            content = ""
            for selector in content_selectors:
                try:
                    content_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    content = content_elem.text.strip()
                    break
                except NoSuchElementException:
                    continue
            
            # If no title found, use first part of content as title
            if not title and content:
                title = content[:100] + "..." if len(content) > 100 else content
            
            # Extract author
            author_selectors = [
                ".author-name",
                "[data-testid='author']",
                ".post-author",
                ".user-name"
            ]
            
            author = "Unknown"
            for selector in author_selectors:
                try:
                    author_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    author = author_elem.text.strip()
                    break
                except NoSuchElementException:
                    continue
            
            # Extract timestamp
            timestamp = datetime.now()  # Default to now if not found
            time_selectors = [
                "[data-testid='timestamp']",
                ".timestamp",
                ".post-time",
                "time"
            ]
            
            for selector in time_selectors:
                try:
                    time_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    time_text = time_elem.get_attribute("datetime") or time_elem.text
                    # Add parsing logic here based on Skool's time format
                    break
                except NoSuchElementException:
                    continue
            
            # Extract likes and comments count
            likes = 0
            comments_count = 0
            
            # Try to find likes
            like_selectors = [".like-count", "[data-testid='likes']", ".likes"]
            for selector in like_selectors:
                try:
                    like_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    likes_text = like_elem.text.strip()
                    likes = int(''.join(filter(str.isdigit, likes_text))) or 0
                    break
                except (NoSuchElementException, ValueError):
                    continue
            
            # Try to find comments count
            comment_selectors = [".comment-count", "[data-testid='comments']", ".comments"]
            for selector in comment_selectors:
                try:
                    comment_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    comments_text = comment_elem.text.strip()
                    comments_count = int(''.join(filter(str.isdigit, comments_text))) or 0
                    break
                except (NoSuchElementException, ValueError):
                    continue
            
            # Get post URL
            post_url = self.driver.current_url
            try:
                link_elem = post_element.find_element(By.CSS_SELECTOR, "a")
                href = link_elem.get_attribute("href")
                if href and href.startswith("http"):
                    post_url = href
            except NoSuchElementException:
                pass
            
            return Post(
                id=post_id,
                title=title,
                content=content,
                author=author,
                timestamp=timestamp,
                likes=likes,
                comments_count=comments_count,
                url=post_url
            )
            
        except Exception as e:
            print(f"⚠️ Error extracting post data: {str(e)}")
            return None
    
    def scrape_posts(self, max_posts: int = 50) -> List[Post]:
        """Main method to scrape posts from the community"""
        print(f"🚀 Starting to scrape posts from {self.community_url}")
        
        # Load posts by scrolling
        post_elements = self.scroll_and_load_posts(max_posts)
        
        # Extract data from each post
        scraped_posts = []
        for i, post_element in enumerate(post_elements, 1):
            print(f"📝 Processing post {i}/{len(post_elements)}")
            post_data = self.extract_post_data(post_element)
            if post_data:
                scraped_posts.append(post_data)
        
        self.posts = scraped_posts
        print(f"✅ Successfully scraped {len(scraped_posts)} posts")
        return scraped_posts
    
    def save_to_json(self, filename: str = None):
        """Save scraped posts to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"skool_posts_{timestamp}.json"
        
        filepath = os.path.join("Skool", filename)
        
        # Convert posts to dictionaries
        posts_data = []
        for post in self.posts:
            post_dict = {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author,
                "timestamp": post.timestamp.isoformat(),
                "likes": post.likes,
                "comments_count": post.comments_count,
                "url": post.url,
                "category": post.category
            }
            posts_data.append(post_dict)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(posts_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Saved {len(posts_data)} posts to {filepath}")
        return filepath
    
    def save_to_csv(self, filename: str = None):
        """Save scraped posts to CSV file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"skool_posts_{timestamp}.csv"
        
        filepath = os.path.join("Skool", filename)
        
        # Convert posts to DataFrame
        posts_data = []
        for post in self.posts:
            posts_data.append({
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author,
                "timestamp": post.timestamp.isoformat(),
                "likes": post.likes,
                "comments_count": post.comments_count,
                "url": post.url,
                "category": post.category
            })
        
        df = pd.DataFrame(posts_data)
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        print(f"💾 Saved {len(posts_data)} posts to {filepath}")
        return filepath
    
    def close(self):
        """Close the browser driver"""
        if self.driver:
            self.driver.quit()
            print("🔒 Browser closed")

def main():
    """Main function to run the scraper"""
    # Load configuration from environment variables
    email = os.getenv("SKOOL_EMAIL")
    password = os.getenv("SKOOL_PASSWORD") 
    community_url = os.getenv("COMMUNITY_URL")
    headless = os.getenv("HEADLESS_MODE", "True").lower() == "true"
    
    if not all([email, password, community_url]):
        print("❌ Missing required environment variables. Please check your .env file.")
        print("Required: SKOOL_EMAIL, SKOOL_PASSWORD, COMMUNITY_URL")
        return
    
    # Initialize scraper
    scraper = SkoolScraper(community_url, headless=headless)
    
    try:
        # Setup browser
        print("🌐 Setting up browser...")
        scraper.setup_driver()
        
        # Login
        print("🔐 Logging in...")
        if not scraper.login(email, password):
            return
        
        # Navigate to community
        print("📍 Navigating to community...")
        if not scraper.navigate_to_community():
            return
        
        # Scrape posts
        posts = scraper.scrape_posts(max_posts=50)
        
        if posts:
            # Save results
            scraper.save_to_json()
            scraper.save_to_csv()
            
            print(f"\n📊 Scraping Summary:")
            print(f"   • Total posts: {len(posts)}")
            print(f"   • Community: {community_url}")
            print(f"   • Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("❌ No posts were scraped")
            
    except KeyboardInterrupt:
        print("\n⚠️ Scraping interrupted by user")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
    finally:
        # Always close the browser
        scraper.close()

if __name__ == "__main__":
    main()