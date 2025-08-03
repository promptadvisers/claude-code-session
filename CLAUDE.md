# Claude Code Configuration Project

## Project Overview
This is a fully configured Claude Code environment with enhanced capabilities through MCP servers, custom agents, and workflow commands. The setup provides a comprehensive toolkit for development, research, content creation, and automation tasks.

## Key Features
- **9 MCP Servers** for web automation, content extraction, security analysis, and more
- **5 Specialized Agents** for writing, reviewing, organizing, summarizing, and research
- **Custom Commands** for common workflows and project management
- **Comprehensive Documentation** and setup guides

## MCP Servers Available
1. **browser-mcp** - Basic browser automation and web interactions
2. **firecrawl** - Advanced web scraping and content extraction
3. **playwright** - Robust browser automation and testing
4. **n8n-mcp** - Workflow automation and process management
5. **semgrep** - Static code analysis and security scanning
6. **Ref** - Documentation and API reference tools
7. **exa** - AI-powered web search and research
8. **21st-dev-magic** - Development utilities and tools
9. **puppeteer-mcp-claude** - Puppeteer browser automation

## Specialized Agents
- **writer** - Expert content creation and documentation
- **reviewer** - Code quality and security review specialist
- **organizer** - Project structure and file organization
- **summarizer** - Content and conversation summarization
- **researcher** - Information gathering and analysis

## Custom Commands
- `/help [topic]` - Comprehensive help on any topic
- `/plan [project]` - Create detailed project plans with tasks
- `/organize [target]` - Organize files and project structure
- `/review [target]` - Perform thorough code/content reviews
- `/summarize [content]` - Create summaries and extract key points

## Quick Start
1. **Get Help**: Use `/help` or ask "help me with [topic]"
2. **Plan Projects**: Use `/plan` or say "create a plan for [project]"
3. **Use Agents**: Say "use the writer agent to..." or mention @writer
4. **Web Automation**: Just describe what you want to automate
5. **Research**: Ask to "research [topic]" or "find information about [subject]"

## Natural Language Usage
Instead of memorizing commands, use natural language:
- "Help me organize this project" → Activates organize command
- "Review this code for security issues" → Uses reviewer agent + Semgrep
- "Research the latest trends in AI" → Uses researcher agent + Exa MCP
- "Automate this website interaction" → Uses appropriate browser automation MCP
- "Summarize our conversation" → Uses summarizer agent

## Documentation
Full documentation is available in `.claude/docs/`:
- `complete-guide.md` - Full setup and usage guide
- `cheat-sheet.md` - All shortcuts and commands reference
- `agents-guide.md` - How to use and create agents
- `mcp-servers-guide.md` - When to use which MCP server

## Project Structure
```
.claude/
├── docs/          # All documentation and guides
├── commands/      # Custom slash commands
├── agents/        # Agent configurations
├── hooks/         # Event hooks (for future use)
└── settings.json  # Project configuration
CLAUDE.md          # This project context file
```

## Environment Variables (Optional)
For enhanced functionality, you can set these environment variables:
```bash
export FIRECRAWL_API_KEY="your-firecrawl-key"
export N8N_API_URL="your-n8n-instance-url"
export N8N_API_KEY="your-n8n-api-key"
export SEMGREP_APP_TOKEN="your-semgrep-token"
export REF_API_KEY="your-ref-api-key"
export EXA_API_KEY="your-exa-api-key"
export MAGIC_API_KEY="your-21st-dev-magic-key"
```

## Usage Philosophy
This setup is designed to make Claude Code incredibly powerful while keeping it intuitive. You don't need to remember specific commands or server names - just describe what you want to accomplish in natural language, and Claude will automatically:

1. **Select the right MCP server** for web automation, research, or analysis tasks
2. **Choose the appropriate agent** for specialized work like writing or reviewing
3. **Use custom commands** for structured workflows like planning or organizing
4. **Combine multiple tools** for complex, multi-step tasks

The goal is to have a seamless, intelligent assistant that automatically uses the best tools for each situation while maintaining the flexibility to be explicit when needed.

## Getting Started
1. Use `/help` to see what's available
2. Try natural language requests like "help me plan a new project"
3. Explore the documentation in `.claude/docs/`
4. Experiment with different agents and MCP servers
5. Create your own custom commands and agents as needed

This setup turns Claude Code into a comprehensive development and productivity environment that adapts to your needs!