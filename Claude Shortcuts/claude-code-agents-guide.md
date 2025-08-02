# Claude Code Agents & Subagents Guide

## What Are Agents and Subagents?

Agents and subagents are specialized AI assistants within Claude Code that operate independently with their own context and focused capabilities. Think of them as expert consultants you can call in for specific tasks.

## Key Differences

- **Main Claude Code**: Your general-purpose assistant with full context of your conversation
- **Agents/Subagents**: Fresh-start specialists that handle specific tasks in isolation

## How They Work

1. **Separate Context**: Each agent starts fresh without knowledge of your previous conversation
2. **Custom Instructions**: They follow specialized system prompts tailored to their purpose
3. **Tool Restrictions**: You can limit which tools they can access for security
4. **Automatic or Manual**: Claude can delegate to them automatically or you can invoke them directly

## Creating Agents

Use the `/agents` command or say something like:
- "Create a debugging specialist agent"
- "I need an agent that only reviews Python code"
- "Set up a data analysis assistant"

When creating an agent, you'll define:
1. **Name**: Short, descriptive identifier
2. **Description**: What the agent specializes in
3. **System Prompt**: Detailed instructions for behavior
4. **Tool Access**: Which tools it can/cannot use

## When to Use Agents

### Perfect Use Cases

1. **Code Reviews**
   - Create a "code-reviewer" agent that focuses solely on quality, security, and best practices
   - Invoke after significant code changes
   - Keeps review feedback separate from implementation discussion

2. **Debugging Sessions**
   - A "debugger" agent that specializes in error analysis
   - Starts fresh to avoid confusion from previous attempts
   - Can systematically approach problems without context bias

3. **Data Analysis**
   - "data-scientist" agent for SQL queries and data insights
   - Isolated environment prevents accidental data modifications
   - Focused on analysis without getting distracted by other code

4. **Testing**
   - "test-writer" agent that creates comprehensive test suites
   - Follows specific testing frameworks and patterns
   - Ensures consistent test quality

5. **Documentation**
   - "doc-writer" agent for creating clear, consistent documentation
   - Follows specific style guides
   - Doesn't get confused by implementation details

### When NOT to Use Agents

1. **Continuous Development**
   - When you need context from previous work
   - For iterative improvements on the same code
   - When referencing earlier decisions or discussions

2. **Quick Tasks**
   - Simple one-off commands
   - Tasks that benefit from conversation context
   - When the overhead of context switching isn't worth it

3. **Cross-functional Work**
   - Tasks requiring knowledge of multiple parts of your project
   - When you need to maintain state between operations
   - Integration work that spans different areas

## Best Practices

### Agent Design

1. **Single Purpose**
   ```
   Good: "Security auditor that checks for vulnerabilities"
   Bad: "Helper that does security, performance, and formatting"
   ```

2. **Clear Boundaries**
   ```
   Good: "Only reviews TypeScript code in the src/ directory"
   Bad: "Reviews any code anywhere"
   ```

3. **Specific Instructions**
   ```
   Good: "Use ESLint rules from .eslintrc and focus on accessibility"
   Bad: "Review code for issues"
   ```

### Tool Restrictions

- **Minimal Access**: Give agents only the tools they need
- **Read-Only for Reviewers**: Code reviewers shouldn't need write access
- **No System Commands**: Restrict Bash access for security-focused agents

### Example Agent Setups

1. **Strict Code Reviewer**
   ```
   Name: strict-reviewer
   Description: Enforces coding standards and security practices
   Tools: Read-only file access, no execution capabilities
   Prompt: "You are a senior engineer focused on code quality..."
   ```

2. **Performance Optimizer**
   ```
   Name: perf-optimizer
   Description: Identifies and fixes performance bottlenecks
   Tools: Read, Write, Profiling tools
   Prompt: "Analyze code for performance issues, focusing on..."
   ```

3. **Test Generator**
   ```
   Name: test-gen
   Description: Creates comprehensive test suites
   Tools: Read, Write, Test execution
   Prompt: "Generate tests achieving >90% coverage using Jest..."
   ```

## Integration Strategies

### Automatic Delegation
Claude Code can automatically use agents when it detects relevant tasks:
- "Review this PR" → Automatically uses code-reviewer agent
- "Debug this error" → Automatically uses debugger agent

### Explicit Invocation
You can specifically request an agent:
- "Use the security-auditor agent to check this code"
- "Have the doc-writer agent create API documentation"

### Agent Chaining
Combine multiple agents for complex workflows:
1. test-gen creates tests
2. strict-reviewer reviews both code and tests
3. perf-optimizer ensures efficiency

## Performance Considerations

- **Latency**: Agents start fresh, adding 1-2 seconds overhead
- **Context Loss**: No memory of previous conversations
- **Token Efficiency**: Clean slate can be more efficient for focused tasks

## Summary

Agents excel when you need:
- Specialized expertise without context pollution
- Consistent, repeatable processes
- Security through isolation
- Fresh perspectives on problems

Avoid agents when you need:
- Contextual continuity
- Quick, simple tasks
- Integrated development flow
- Stateful operations

Think of agents as bringing in a specialist consultant - great for specific expertise, but not for day-to-day collaboration.