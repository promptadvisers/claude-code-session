# MCP Servers Usage Guide: When to Use What

## Overview
With 9 powerful MCP servers at your disposal, choosing the right tool for each situation maximizes efficiency and success rates. This guide provides specific scenarios and decision trees for optimal server selection.

## Your MCP Arsenal
- **browser-mcp** - Basic browser automation
- **firecrawl** - Web scraping and content extraction
- **playwright** - Advanced browser automation and testing
- **n8n-mcp** - Workflow automation platform integration
- **semgrep** - Static code analysis and security scanning
- **Ref** - Reference and documentation tools
- **exa** - AI-powered web search and research
- **21st-dev-magic** - Magic development tools and utilities
- **puppeteer-mcp-claude** - Puppeteer browser automation for Claude

## Scenario-Based Usage Examples

### 1. **Web Content Extraction**
**Scenario**: Need to extract structured data from a website
- **First choice**: `firecrawl` - Purpose-built for content extraction with clean markdown output
- **Fallback**: `playwright` - If firecrawl fails, use Playwright for custom scraping logic
- **When to use**: Product catalogs, news articles, documentation scraping

### 2. **Browser Testing & Automation**
**Scenario**: Testing web applications or complex user interactions
- **First choice**: `playwright` - Most robust for testing with better error handling
- **Fallback**: `puppeteer-mcp-claude` - If Playwright fails or for simpler automation
- **Last resort**: `browser-mcp` - Basic automation when others are too complex
- **When to use**: E2E testing, form submissions, UI interactions

### 3. **Research & Information Gathering**
**Scenario**: Need to find current information or research topics
- **First choice**: `exa` - AI-powered search with intelligent result filtering
- **Fallback**: `firecrawl` + manual URLs - When you have specific sites to search
- **When to use**: Market research, technical documentation, current events

### 4. **Code Security Analysis**
**Scenario**: Analyzing code for vulnerabilities and quality issues
- **Only choice**: `semgrep` - Specialized static analysis tool
- **When to use**: Security audits, code reviews, compliance checks

### 5. **Workflow Automation Setup**
**Scenario**: Creating or managing automated business processes
- **Only choice**: `n8n-mcp` - Direct integration with your n8n workflow platform
- **When to use**: Setting up data pipelines, API integrations, business automation

### 6. **Documentation & Reference Lookup**
**Scenario**: Need to quickly access API docs, code examples, or technical references
- **First choice**: `Ref` - Optimized for documentation and reference materials
- **Fallback**: `exa` - For broader search when Ref doesn't have the specific docs
- **When to use**: API documentation, code examples, technical specifications

### 7. **Development Magic & Utilities**
**Scenario**: Need specialized development tools or unique utilities
- **Only choice**: `21st-dev-magic` - Specialized development ecosystem tools
- **When to use**: Advanced development workflows, specialized utilities

### 8. **Simple Website Monitoring**
**Scenario**: Basic website status checks or simple interactions
- **First choice**: `browser-mcp` - Lightweight for simple tasks
- **Upgrade to**: `playwright` if you need more complex logic
- **When to use**: Health checks, simple form fills, basic navigation

### 9. **Content Migration & Bulk Extraction**
**Scenario**: Moving content from old websites or extracting large datasets
- **First choice**: `firecrawl` - Handles rate limiting and structured extraction
- **Parallel**: `n8n-mcp` - Set up automated workflows for ongoing migration
- **When to use**: CMS migrations, data archiving, content audits

### 10. **Cross-Platform Testing**
**Scenario**: Testing across different browsers and devices
- **Primary**: `playwright` - Built-in cross-browser support
- **Secondary**: `puppeteer-mcp-claude` - Chrome-specific testing if Playwright issues
- **When to use**: Browser compatibility testing, responsive design testing

### 11. **Real-Time Data Monitoring**
**Scenario**: Setting up alerts or monitoring changing web content
- **Setup**: `n8n-mcp` - Create monitoring workflows
- **Data source**: `firecrawl` - Regular content extraction
- **Alerts**: `browser-mcp` - Simple status checks
- **When to use**: Price monitoring, news alerts, system status tracking

### 12. **Security Research & Analysis**
**Scenario**: Investigating security issues or analyzing threats
- **Code analysis**: `semgrep` - Static code vulnerability scanning
- **Web research**: `exa` - Finding security reports and threat intelligence
- **Site analysis**: `playwright` - Dynamic security testing
- **When to use**: Penetration testing prep, vulnerability research, security audits

### 13. **Documentation Generation**
**Scenario**: Creating comprehensive documentation for projects
- **Reference lookup**: `Ref` - Find existing documentation patterns
- **Code analysis**: `semgrep` - Identify code patterns to document
- **Research**: `exa` - Find best practices and examples
- **When to use**: API documentation, code commenting, user guides

### 14. **Automated Reporting**
**Scenario**: Creating regular reports with web data
- **Workflow**: `n8n-mcp` - Set up automated report generation
- **Data collection**: `firecrawl` - Extract data from multiple sources
- **Analysis**: `21st-dev-magic` - Process and format data
- **When to use**: Business intelligence, compliance reporting, performance monitoring

### 15. **Debugging Web Issues**
**Scenario**: Troubleshooting website problems or investigating errors
- **First**: `playwright` - Comprehensive debugging with screenshots and logs
- **Fallback**: `puppeteer-mcp-claude` - Alternative browser automation
- **Simple**: `browser-mcp` - Quick status checks
- **When to use**: Bug investigation, performance analysis, error reproduction

## Decision Tree Guidelines

### For Web Automation Tasks:
```
Complex automation needed? 
  → Yes: playwright → puppeteer-mcp-claude → browser-mcp
  → No: browser-mcp → playwright (if issues)
```

### For Content Extraction:
```
Structured data extraction?
  → Yes: firecrawl → playwright (custom scraping)
  → No: playwright → browser-mcp
```

### For Research Tasks:
```
Need current/AI-filtered results?
  → Yes: exa → firecrawl (specific sites)
  → No: Ref → exa
```

### For Development Tasks:
```
Security analysis? → semgrep
Workflow automation? → n8n-mcp  
Documentation lookup? → Ref
Development utilities? → 21st-dev-magic
```

## Best Practices

### Server Selection Strategy
1. **Start specific**: Use the most specialized tool for your task
2. **Fallback gracefully**: Have a backup plan when primary tool fails
3. **Combine wisely**: Use multiple servers for complex workflows
4. **Monitor performance**: Switch tools if response times are poor

### Performance Optimization
- Use `browser-mcp` for simple tasks to preserve resources
- Reserve `playwright` for complex automation requiring reliability
- Use `firecrawl` for bulk content extraction over custom scraping
- Leverage `n8n-mcp` for tasks that will repeat regularly

### Error Handling
- If Playwright fails → try Puppeteer → then browser-mcp
- If Firecrawl fails → try Playwright with custom selectors
- If Exa returns poor results → try Ref for technical topics
- If any automation fails → check with simpler tool first

## Natural Language Triggers

Instead of specifying servers directly, use these phrases:

**Web Automation**: "automate this website", "test this form", "interact with this page"
**Content Extraction**: "scrape this data", "extract content from", "get text from this site"  
**Research**: "find information about", "research this topic", "search for current data"
**Security**: "analyze this code for security", "check for vulnerabilities", "audit this repository"
**Workflows**: "set up automation for", "create a workflow", "automate this process"
**Documentation**: "find documentation for", "look up API reference", "get code examples"

Claude will automatically select the most appropriate MCP server based on your request context and fallback to alternatives if needed.