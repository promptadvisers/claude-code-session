# Skool Community Scraper

A Python tool to scrape posts and comments from your Skool community. Since Skool doesn't provide an official API, this tool uses web scraping to extract community data for analysis and monitoring.

## Features

- 🔐 **Secure Authentication**: Login with your Skool credentials
- 📄 **Post Extraction**: Scrape posts with titles, content, authors, timestamps, likes, and comment counts
- 💾 **Multiple Export Formats**: Save data as JSON or CSV
- 🖥️ **Headless Operation**: Run in background without opening browser window
- ⚡ **Configurable**: Customize scraping parameters via environment variables
- 🛡️ **Error Handling**: Robust error handling and logging

## Installation

1. **Clone or download this project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install ChromeDriver**: Make sure you have Chrome installed and ChromeDriver in your PATH
4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

## Configuration

Create a `.env` file with your settings:

```env
# Skool Community Scraper Configuration
SKOOL_EMAIL=your_email@example.com
SKOOL_PASSWORD=your_password
COMMUNITY_URL=https://www.skool.com/your-community-name
HEADLESS_MODE=True
```

### Configuration Options

- `SKOOL_EMAIL`: Your Skool login email
- `SKOOL_PASSWORD`: Your Skool password
- `COMMUNITY_URL`: Full URL to your Skool community
- `HEADLESS_MODE`: Set to `False` to see the browser window (useful for debugging)

## Usage

### Basic Usage

Run the scraper with default settings (50 posts):

```bash
python skool_scraper.py
```

### Advanced Usage

You can also use the scraper programmatically:

```python
from skool_scraper import SkoolScraper
import os

# Initialize scraper
scraper = SkoolScraper(
    community_url="https://www.skool.com/your-community",
    headless=True
)

try:
    # Setup and login
    scraper.setup_driver()
    scraper.login("your_email@example.com", "your_password")
    scraper.navigate_to_community()
    
    # Scrape posts
    posts = scraper.scrape_posts(max_posts=100)
    
    # Save results
    scraper.save_to_json("my_posts.json")
    scraper.save_to_csv("my_posts.csv")
    
finally:
    scraper.close()
```

## Output Files

The scraper generates two types of output files:

### JSON Format (`skool_posts_YYYYMMDD_HHMMSS.json`)
```json
[
  {
    "id": "post_123",
    "title": "Welcome to the community!",
    "content": "This is the full post content...",
    "author": "John Doe",
    "timestamp": "2024-01-15T10:30:00",
    "likes": 15,
    "comments_count": 8,
    "url": "https://www.skool.com/community/post/123",
    "category": ""
  }
]
```

### CSV Format (`skool_posts_YYYYMMDD_HHMMSS.csv`)
| id | title | content | author | timestamp | likes | comments_count | url | category |
|----|-------|---------|--------|-----------|-------|----------------|-----|----------|
| post_123 | Welcome! | Content... | John Doe | 2024-01-15T10:30:00 | 15 | 8 | https://... | |

## Data Structure

Each scraped post contains:

- **id**: Unique post identifier
- **title**: Post title (or truncated content if no title)
- **content**: Full post content
- **author**: Username of the post creator
- **timestamp**: When the post was created
- **likes**: Number of likes/reactions
- **comments_count**: Number of comments
- **url**: Direct link to the post
- **category**: Post category (if available)

## Troubleshooting

### Common Issues

1. **ChromeDriver not found**
   - Install ChromeDriver: `brew install chromedriver` (Mac) or download from [ChromeDriver website](https://chromedriver.chromium.org/)
   - Make sure ChromeDriver is in your PATH

2. **Login fails**
   - Verify your email and password are correct
   - Check if Skool requires 2FA (not currently supported)
   - Try running with `HEADLESS_MODE=False` to see what's happening

3. **No posts found**
   - Verify the community URL is correct
   - Check if you have access to the community
   - Some communities may have different HTML structures

4. **Slow performance**
   - Reduce `max_posts` parameter
   - Check your internet connection
   - Some communities load slowly

### Debugging

To debug issues, set `HEADLESS_MODE=False` in your `.env` file to see the browser window and what's happening.

## Limitations

- **No Official API**: This tool uses web scraping, which may break if Skool changes their website structure
- **Rate Limiting**: Be respectful and don't overload Skool's servers
- **Authentication**: Currently doesn't support 2FA
- **Dynamic Content**: Some content may not be captured if it loads dynamically
- **Terms of Service**: Make sure you comply with Skool's Terms of Service

## Legal and Ethical Considerations

- ✅ **Use for your own communities**: This tool is intended for community owners to analyze their own data
- ✅ **Respect rate limits**: Don't make too many requests too quickly
- ✅ **Check Terms of Service**: Ensure compliance with Skool's ToS
- ❌ **Don't scrape other people's private communities**
- ❌ **Don't use scraped data maliciously**

## Future Enhancements

Potential improvements:
- Comment scraping functionality
- Real-time monitoring with webhooks
- Member activity tracking
- Analytics dashboard
- Integration with data visualization tools
- Support for multiple communities

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed correctly
3. Verify your environment variables are set properly
4. Try running with debug mode (`HEADLESS_MODE=False`)

## Contributing

Feel free to contribute improvements:
- Better error handling
- Support for more Skool features
- Performance optimizations
- Bug fixes

## License

This tool is for educational and legitimate community management purposes only. Please use responsibly and in accordance with Skool's Terms of Service.