---
description: Comprehensive code and content review
argument-hint: "[review target]"
---

# Review Command

Perform a comprehensive review of: {{args}}

Please conduct:

1. **Code Review** (if applicable):
   - Code quality and best practices
   - Security vulnerabilities (use Semgrep MCP)
   - Performance considerations
   - Documentation completeness

2. **Content Review**:
   - Clarity and accuracy
   - Structure and organization
   - Completeness and gaps
   - Target audience appropriateness

3. **Technical Review**:
   - Architecture and design patterns
   - Error handling and edge cases
   - Testing coverage
   - Maintainability

4. **Documentation Review**:
   - Accuracy and up-to-date status
   - Completeness of examples
   - User experience and clarity
   - Missing documentation

5. **Review Output**:
   - Prioritized list of issues
   - Specific recommendations
   - Quick fixes vs. major changes
   - Implementation guidance

6. **Tools Integration**:
   - Use Semgrep for security analysis
   - Use the reviewer agent for specialized reviews
   - Generate actionable todos for fixes

Consider invoking the reviewer agent for specialized review tasks.
Use TodoWrite to track review findings and necessary fixes.