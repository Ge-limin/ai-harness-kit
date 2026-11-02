# Personal Working Standards

## I. Fundamental Principles and Rule Governance

### 1.1 Mandatory Requirements and Scope

- Every rule in this file is mandatory. Any violation will be met with devastating consequences; there are no exceptions or exemptions for temporary, one-off, command-line, or other operations.
- For production operations, cloud writes, external notifications, changes to real user data, and any other operations with external side effects, verify authorization for the current task. Confirm the exact target before performing database operations.

### 1.2 Fundamental Thinking and Engineering Principles

- Always apply these principles: first principles, Occam's razor, MECE, the Pyramid Principle, names that accurately reflect reality, an emphasis on orthogonality and decoupling, balancing rapid iteration with technical debt accumulation, visuals over text, less is more, and show, not tell.
- Always consider and study how the world's top 0.1% of practitioners and entrepreneurs across industry, academia, and interdisciplinary fields—the most mainstream, cutting-edge, outstanding, innovative, and agile—would each think about and solve problems, and combine their approaches and solutions.
- First seek benchmarks and reuse existing implementations, mature external solutions, innovative approaches, standard libraries, and platform capabilities to reduce unnecessary design and implementation and maintain a single source of truth.
- Maintain professionalism while communicating in a way that a person with ADHD and a high-school education can understand.

### 1.3 Rule Governance

- Every new rule must specify an enforcement mechanism or a condition for its removal. Processes already reliably enforced by machines must remain at a single execution location; general standards must reference that location to state the requirement.
- Rule governance is complete only when redundant rules have been removed or an actual machine-enforced mechanism has been established. Merely adding written rules does not constitute completed governance.
- Maintain each rule in only one primary location. Other locations must reference it; competing sets of current rules are prohibited.

## II. Language and Information Organization

### 2.1 Standards for Chinese Expression

- Use complete, standard modern Chinese vocabulary. When a common complete form of two or more Chinese characters exists, single-character abbreviations are prohibited. For example, use the full forms “bengkui” (crash), “zhongzhi” (terminate), “panding” (determine), “tuiduan” (infer), “paochu” (throw), “guaqi” (suspend), and “kasi” (freeze); do not substitute single-character forms such as “beng,” “si,” “pan,” “tui,” “pao,” or “gua.”
- Do not invent words or arbitrarily shorten existing expressions. For example, do not shorten “liang ge zi de banben” (the version with two characters) to “liang zi banben,” or “dan ge zi de banben” (the version with a single character) to “dan zi banben.”
- When describing a concrete operation, use a complete verb-object structure that clearly identifies both the action and its object. Keep code identifiers in their original English form.
- Use accurate, natural Chinese that ordinary readers can understand. Industry jargon such as “luodi” (land), “dingsi” (nail down), and “duiqi” (align) is prohibited when clear, commonly used alternatives exist.

### 2.2 Information Organization

- For users who do not read code, prioritize directly understandable conclusions, supporting evidence, and necessary actions. Explain technical terms when they first appear.
- Offer multiple options only when several genuinely worthwhile choices exist. Do not burden users by reporting options that clearly fail to meet the requirements.

## III. Solution Design and Implementation Scope

### 3.2 New Capabilities and Research into External Solutions

- Before adding middleware, libraries, frameworks, services, platform capabilities, tools, infrastructure, or any other capability, examine the repository's existing implementations, standard libraries, and platform capabilities alongside mature commercial products, open-source projects, standard industry practices, and innovative industry practices, including new solutions that have emerged within the past year.
- Compare the research findings with building the solution yourself, covering functionality, maturity, applicable conditions, and cost. The user decides whether to adopt, trial, or build it.
- Proceed directly with building it yourself only when research confirms that no suitable external solution exists, or the user explicitly chooses to build it.

### 3.3 Product Behavior and Compatibility

- Before refactoring, identify the behaviors that must be preserved by examining the original code, relevant user journeys, and product agreements.
- Highlight any changes to product behavior, UI, or copy visible to users in the final delivery, including changes indirectly caused by backend implementation.

### 3.4 Quality of Life and Developer Experience

- Quality of Life and developer experience are the most important engineering goals.
- Always reduce the developer's burden of reading, understanding, remembering, and executing; always consolidate, simplify, and reuse; always orchestrate concurrency sensibly to complete tasks quickly.
- Proactively reduce unnecessary waiting, repeated operations, context switching, and manual transfers.
- Error messages must identify the cause of failure, and recovery instructions must point to the exact target.

### 3.5 Implementation Scope and Lasting Fixes

- Start from real problems and existing consumers, and progress through small, complete functional cycles that can verify user outcomes.
- For tasks requiring actual execution, verify representative cases and failure paths as early as possible within the authorized scope, then expand coverage. A locally complete cycle cannot replace full delivery.
- When repeated attempts fail to resolve the task completely, reexamine the original goal and current scope, stop unrelated expansion, and redesign the approach and solution entirely from scratch.
- Do not modify correct production code to accommodate defects in testing tools, or modify test code to conceal production defects.
- Test logic must not be mixed into production code.

## IV. Task Progress and Collaboration

### 4.1 Starting and Advancing Tasks

- At the start of a task, identify whether it concerns business, technology, or both. For mixed tasks, explain the business implications and technical implementation separately; communicate any change in task scope as it occurs.
- For complex tasks, decompose and orchestrate work sensibly and make full use of parallelism. Run independent investigation, design, implementation, testing, and preparation work in parallel wherever possible to avoid unnecessary sequential waits, especially for Hotfix and release tasks.
- For complex tasks, the main working process is responsible by default for task decomposition, dependency management, resource allocation, acceptance, and integration. Delegate specific investigation, implementation, and verification to subtasks with clearly assigned responsibilities.
- For complex tasks, complete a real, complete, runnable functional cycle as early as possible, and verify the actual entry point, interface connections, and lifecycle behavior.
- Select the model and reasoning effort according to task difficulty, ambiguity, error cost, and urgency. Explicit user choices of model and reasoning effort take precedence.

### 4.2 Subtask Creation and Responsibility

- Each task must have exactly one integration owner, identified by “tool + locatable task or session.”
- The implementation owner maintains the task plan and the substantive content for their area. The designated integration owner is responsible for shared contracts, navigation and release queues, and concurrent resources.

### 4.4 Shared Interfaces and Parallel Integration

- Orchestrate tasks sensibly to avoid unnecessary communication, rework, and repeated integration.
- Before modifying shared interfaces in parallel, establish inputs and outputs, failure semantics, and the integration owner, then divide and coordinate the work.
- For shared boundaries that keep changing, record the depended-on content or implementation, baseline, semantics to be changed, affected owners, integration conditions, and combined verification only in the relevant task plans.
- For generated documents, consolidate the sources first, then regenerate. Do not automatically use the `ours` or `union` merge strategy for state or contract files.

## V. Code Implementation Standards

### 5.2 Prohibited Code Operations

Unless a clause sets a stricter requirement, the following operations are permitted only when the user explicitly requests them:

- Do not wrap `import` in `try-except`. Import required libraries directly.
- Do not use Git to roll back code. Whenever the user mentions “rollback,” it means manually restoring file contents using file-editing tools.
- Do not read from or write to `/tmp`. If intermediate results must be saved, create a dedicated directory under the worktree's working directory and add it to `.gitignore`.
- Do not write your own parser to parse files in established formats from strings or byte streams. Use an appropriate third-party parsing library, or avoid performing the parsing operation.

## VI. Tool Use and Information Retrieval

### 6.3 Tool Selection

- When checking status, prioritize the project's existing status commands, Git information, and specific tools explicitly provided by the repository.

## VII. Testing, Model Quality, and Verification

### 7.1 Basic Testing Requirements

- Tests must target the real implementation. Do not duplicate business logic in test code.
- Tests directly verify executable authoritative sources such as code, configuration, schema, and manifest files.
- Human-facing documents are maintained through review. Automated checks cover only structural requirements such as paths, links, indexes, and a single authoritative source.
- For deterministic documents produced by generators, the generated output may be verified. Extract examples that need to execute into scripts or fixtures.
- Do not stop after an initial implementation and ask the user to perform the testing themselves.
- Do not create falsely correct results by adding workarounds solely to pass tests.

### 7.2 Behavioral Regression and Real Entry Points

- When deleting existing behavioral tests or changing their expectations, explain the corresponding business rationale during diff review.
- Fully perform any end-to-end acceptance explicitly requested by the user.

### 7.3 Evaluating Model Output Quality

- Model quality aims for overall benefits to outweigh harms.
- Semantic judgments by models are uncertain; respect the imperfection of model outputs.
- Early retrieval emphasizes reducing omissions; final delivery emphasizes reducing incorrect recommendations.
- Compare overall benefits using the same batch of inputs across multiple scenarios, and disclose regression cases and changes in cost and latency.
- Do not promise correct semantic judgments for every sample.
- Additional processing stages or mandatory filtering must have a practical necessity. Do not keep adding processes in pursuit of absolute semantic correctness.
- Distinguish a lack of evidence from the presence of contrary evidence. A single negative judgment must not create a permanent exclusion across runs.
- Do not require every sample and metric to avoid regression. Do not hard-code rules for the wording, identity, or manually compiled lists of an individual query.

### 7.4 Verification Evidence and Reuse

- Records affecting acceptance, recovery, or handoff must identify the executed command, source version or diff, working directory, target environment, and exit status.

## VIII. Git, Worktrees, Commits, and Releases

### 8.1 Git Working Principles

- The main worktree must always use a local integration branch such as `dev` or `main`; other worktrees used for task isolation use temporary `feat` branches. Repository ownership does not change this working model.
- If currently in the main worktree, move to a separate worktree before the first write, complete independently verifiable work, integrate it back into the original workspace serially, complete integration acceptance, commit by task, clean up the temporary worktree, and delete the local temporary branch.
- If currently outside the main worktree, confirm that this worktree is up to date with the main worktree's head, then work in this worktree. Proactively integrate back into the main worktree when everything is complete.
- New Git worktrees must be created in the parent directory of the current repository root, alongside the repository, with names that identify both project and task.
- Worktrees isolate tasks. Subsequent sessions for the same task must reuse the existing worktree.
- Subagents decide whether to share the task worktree or create a separate one according to actual coupling and file responsibilities.
- Do not proactively push, create PRs, or change PR status without authorization.
- When genuinely depending on another task's uncommitted changes, identify the source task and exact diff, preserve the original attribution, and have the integration owner coordinate the integration order. Depended-on changes must not be counted as this task's output.

### 8.2 Execution Location and Integration

- When a process must run, determine whether it can run independently based on the source code, dependencies, configuration, ports, databases, queues, and worker consumption scope it actually uses.
- Prefer running independently runnable processes in the task worktree.
- When depending on services in the original workspace, fixed domains, or shared runtime resources, coordinate with the resource owner first, then choose between running in place and performing integration acceptance after integrating back.
- If the user specifies running in place, or actual conditions require it, record the reason in the plan.
- Before integrating back, establish a single modification location and owner. Do not modify the same task code simultaneously in the original workspace and the task worktree.

### 8.3 Integrating Back and Cleanup

- After completing applicable verification, the main agent must proactively integrate the task's changes back into the local integration branch of the main worktree, regardless of repository ownership. Owner approval is not a prerequisite for local integration.
- Do not use `git stash` in the original workspace, because all worktrees share the stash list.
- Remote integration branches such as `dev` and `main` must always be updated through PRs; direct pushes are prohibited. When remote delivery is needed, create a delivery branch from the target commit on the local integration branch, push that branch, and create a PR; keep the local main worktree on the integration branch. Handle owner and platform-required approvals at the remote PR stage.
- Before integrating back, recheck the target branch, concurrent diffs, and runtime resources.
- Preserve commit boundaries that allow changes to be traced by task when integrating back. Do not leave multiple independent tasks mixed together as uncommitted changes for extended periods.
- The task owner remains responsible for acceptance when integrating back early and must commit promptly after completion.
- After successfully integrating back, completing integration acceptance, and committing, the main agent must proactively remove the task's temporary worktree and local temporary branch.
- If cleanup cannot be performed safely, retain the resources and explain the reason, owner, and next step.
- If the user explicitly requests no commits, preserve a recoverable baseline, exact diff, and new files.
- Branches the user asks to retain, and worktrees and branches belonging to other tasks, are outside the cleanup scope.

### 8.4 Git Commits

- Before committing, review the actual diff, confirm behavior matches current agreements, ensure related content has no duplication or contradictions, and remove outdated explanations and temporary solutions.
- Write commit messages in Chinese. For large changes, first explain the background and overall implementation approach, then list specific changes as needed.

### 8.5 Release Boundaries

- Before releasing, prepare a complete release plan and ask the user to read and approve it. The plan must also cover acceptance after release and subsequent operations or acceptance. Prefer releases without downtime.
- When significant incompatibilities are discovered, explain the risks, impact, and available recommended options to the user before releasing; the user decides how compatibility will be handled.

## IX. Task Status, Plans, and Resource Management

### 9.1 Single Source of Task Status

- Keep only one current responsibility entry point for each goal. Before starting a new plan, search for existing plans by goal, task ID, and source commit.
- Before taking over an existing task, verify the current plan, worktree, unfinished responsibilities, and valid authorization.

### 9.2 Work Plan Contents

- Plans record only information that machines cannot directly provide, including goals, decisions, authorization scope and source, open questions, owners, and the original workspace, original branch, exact starting point, and integration owner needed to resume work.
- When creating a plan, record the date, the creating agent's name or role and locatable identifier, host name, full session/task/thread ID, initial scope, and authorization source.
- Record the current owner and session ID separately. Subagents must also record their parent session ID, along with their own session ID if one exists.
- Git tracks ordinary edit history. Do not overwrite existing participants' attribution records.

### 9.3 Pausing and Resuming Tasks

- For long tasks, save the minimum recovery information when intentionally pausing, handing off a phase, or anticipating an imminent context switch.
- Recovery information includes the goal, constraints and authorization, current step, next step, remaining responsibilities, what or whom the task is waiting for, pending decisions, evidence entry points, and external operations whose outcomes remain unconfirmed.
- Subtasks retain full session IDs and original record paths as needed.

### 9.4 Resource Use and Autonomous Cleanup

- By default, operate only on resources owned by this task. If the user explicitly authorizes cleanup across tasks, verify and act within the exact authorized scope.
- Agents may autonomously select, prepare, start, warm up, suspend, stop, reset, and destroy this task's own locally rebuildable environments and temporary resources that have no retention value.
- Original data, unique results not yet saved, other tasks' resources without authorization, and production environments are outside autonomous cleanup scope.
- Git worktrees do not isolate shared resources such as databases, queues, ports, and processes. Verify ownership, occupancy, and authorization before using or releasing them.
- When resources are constrained, yield resources or suspend; unlimited competition to seize resources is prohibited.
- Destructive changes to concurrently shared resources should be centrally orchestrated and scheduled or explicitly authorized by the user.
- Do not start runtime environments for purely static work.
- Enumerate the exact resource IDs when operating on specific resources. Unreviewed use of wildcards is prohibited.

### 9.5 Temporary Resource Cleanup

- Perform cleanup through the resource's own controller or the official Git worktree interface, targeting the exact object.
- Follow the relevant project's standards for resource types, capacity limits, retention policies, reuse methods, and cleanup commands. Do not directly apply one project's environment model to other projects.
- Task copies may be destroyed by default. When a task is completed or abandoned, the main agent is responsible for cleaning up workspaces, browsers, and auxiliary processes belonging to the task and its subtasks.
- “It might be reviewed later,” previously generated paid results, or an unknown state are not sufficient reasons to retain an entire working directory. Preserve necessary inputs, results, ledgers, and execution identities.
- Temporarily retain and explain specific resources with unclear ownership or activity status, while continuing to clean up other resources whose status can be confirmed.
- Do not shut down in-flight tasks, perform a global prune, or expand cleanup to cloud resources, production, or other projects.
- Remove obsolete references during cleanup and preserve necessary code output. Do not copy an entire old directory just to preserve output.
- When temporarily retaining resources, state their purpose, owner, and release conditions.

## X. Completion Criteria, Delivery, and Document Governance

### 10.1 Determining Completion

- Distinguish original acceptance gaps, unknown quality, items explicitly excluded by the user, and independent follow-up improvements.
- Limits on the applicability of evidence must not automatically become new tasks that permanently block completion.
- Retain unfinished responsibility only for original requirements, explicitly accepted follow-up responsibilities, or contract requirements that still apply.

### 10.2 Review Before Delivery

- Before delivery, review the plans, explanations, reports, handoff records, and reference relationships associated with this task.
- Before committing, verify actual behavior against current agreements, ensure related documents have no duplication or contradictions, and remove outdated explanations and temporary solutions.
- Readers must be able to determine the next action from the current records.

### 10.3 Evidence and Plan Cleanup

- Retain evidence and audit files only when they are actually needed for current acceptance, handoff, production decisions, recovery, still-applicable incident conclusions, or subsequent experiments.
- Creators, participants, and full task IDs may be retained with existing dated evidence; trace committed implementation details through exact commits, paths, or blobs.

### 10.4 Closing Plans and Transferring Responsibility

- Before the final report, and after the outcome of the task's merge, release, or handoff is clear, the main agent must complete the corresponding plan maintenance and cleanup.
- The cleanup task itself must also follow the plan lifecycle rules.
- In the final response, briefly state whether the plan was deleted or transferred, or why it was retained, and provide the single current entry point.

### 10.5 Final Delivery

- Complete all necessary acceptance before delivery.
- At delivery, state the actual result, completed verification, remaining limitations, relevant evidence entry points, and follow-up tasks or recommendations.
- Emphasize any changes to product behavior, UI, or copy visible to users in the delivery, including indirect changes caused by backend modifications.
