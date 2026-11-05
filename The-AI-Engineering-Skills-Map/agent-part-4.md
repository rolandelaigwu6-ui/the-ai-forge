# The AI Engineering Skills Map — Part 4: Coding Agents

**Source:** Andrew Ng and DeepLearning.AI, “The AI Engineering Skills Map Part 4 — Coding Agents”

## Purpose

Using coding agents effectively means steering them through coding and other work, such as data analysis or system operations. The tools and models evolve quickly, so developers need an ongoing practice of experimentation and learning.

## A common workflow

1. **Plan.** Brainstorm, research, experiment, and understand the existing codebase. Write requirements, technical design, and architecture into a specification, then make an execution plan. Review assumptions and look for security gaps or unnecessary complexity.
2. **Execute.** Have the agent build the system with an appropriate level of autonomy. Test and verify the result with automated checks, human review, or both.
3. **Deploy and monitor.** Deploy with suitable CI/CD and human gates. Use agents to monitor logs, identify issues, and propose or make improvements.

The workflow is iterative, and its depth depends on the project. A quick prototype may need only a short prompt, while a large existing system may need a carefully researched and reviewed specification. Verification or production feedback can send the work back to planning or implementation.

## Five skills for using coding agents

1. **Direct the workflow.** Decide how much time and effort to spend on research, planning, specification, architecture, execution, and review. Balance speed, cost, technical risk, and human effort. Keep human ownership where it matters, and break work into steps that can be verified.

2. **Enable agent autonomy.** Choose whether to work interactively, delegate larger tasks, or give an agent a goal and let it iterate. Manage context so later work includes important findings, user feedback, and changed assumptions. Coordinate parallel agents and human attention when useful. Set permissions and action gates to reduce risks such as leaks or data loss.

3. **Review the work.** Treat agent output as uncertain. Match functional and behavioral checks to the task; these can include tests, user-flow checks, screenshots, evaluation sets, and LLM-as-judge. Automate checks when possible, verify that they measure the intended outcomes, and improve them over time. Use agentic code review and security or architecture audits, with human review where needed. Verify deployment and support monitoring and incident response.

4. **Customize the agent and its environment.** Give agents useful context and tools through skills, plugins, and MCP servers, removing obsolete additions when appropriate. Use hooks for repeatable work such as reviews or CI/CD. Maintain project guidance (for example, `AGENTS.md` or `CLAUDE.md`), preserve state and learnings across sessions and agents, establish navigable codebase conventions, and manage agent-generated debt. Coordinate context across team members.

5. **Understand coding-agent foundations.** Know how agents search code, use context windows and tools, interact with subagents, and combine an LLM with a harness. This helps identify failures such as overengineering, missing verification, stopping before completion, or risky actions. Use this mental model to provide the right context and intervene when an agent goes off track.

## Main takeaway

Effective agent use is usually an iterative process that combines agent work with skilled human judgment. Long autonomous runs can sometimes help, but their practical value depends on the task and cost; they are not a substitute for steering, verification, and timely intervention.

## Scope note

This file summarizes **Part 4 only**, focused on using coding agents from planning through execution, deployment, and monitoring.
