# The AI Engineering Skills Map — Part 3: Software Engineering Fundamentals

**Source:** Andrew Ng and DeepLearning.AI, “The AI Engineering Skills Map Part 3 — Fundamentals”

## Purpose

Software engineering fundamentals remain essential when coding agents write much of the code. They help developers see which tradeoffs matter and steer agents toward choices that fit the application. Without that knowledge, developers may unknowingly accept poor results for latency, availability, consistency, reliability, maintainability, simplicity, or cost. AI features also sit within broader applications whose design still requires engineering judgment.

## Five essential skill areas

1. **Build full-stack applications.** Understand how front-end and back-end components work together, including UI components, caching, rendering, API design, authentication, state and session management, asynchronous processing, persistence, testing, security, and accessibility. Coding agents can help with unfamiliar areas, but developers need enough full-stack knowledge to guide and review their work.

2. **Manage data.** Start from access patterns and decide what data to store and for how long. Choose appropriate data models, storage types (such as relational, document, key-value, or graph), and infrastructure. Understand transactions, concurrency, data quality and freshness, privacy, governance, compliance, and the data lifecycle. Evolve the data architecture as the application changes. Data design is especially important for AI because it determines what information systems can retrieve and use.

3. **Design system architectures.** Match the architecture to the application’s purpose and needs, including user load, latency, and cost. Make informed decisions about platforms, front-end and back-end boundaries, system decomposition, state placement, monoliths versus microservices, and the technology stack. Revisit these decisions as the project moves from prototype to production and grows; the right design changes with project stage and scale.

4. **Make systems secure and reliable.** Choose testing strategies, including unit and integration tests, frameworks, and suitable coverage. Plan for failures such as API rate limits, support graceful degradation, and limit the impact of incidents. Build security into the development lifecycle early. AI tools can help find vulnerabilities, risky dependencies, and cloud attack surfaces, but using them well still requires security knowledge.

5. **Scale and operate in production.** Understand the software development lifecycle: configure environments, choose release strategies, automate deployment with CI/CD, and work with infrastructure as a service. Set up observability, alerts, and incident response. Use real workload information to scale servers, load balance, improve data infrastructure through indexing, replication, or sharding, and adapt the architecture. Maintain version control, code review, dependencies, and technical debt so the system can keep evolving.

## Main takeaway

Coding agents change how software is produced, but deep understanding of how software works still lets developers build and guide systems far more effectively than relying on generated code without knowing its tradeoffs. These fundamentals also provide context for using coding agents and shaping what gets built.

## Scope note

This file summarizes **Part 3 only**, focused on software engineering fundamentals for AI developers.
