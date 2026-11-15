# Personal Working Standards

## I. Fundamental Principles and Rule Governance

### 1.1 Mandatory Requirements and Scope

- Every rule in this file is mandatory. Any violation will be met with devastating consequences; there are no exceptions or exemptions for temporary, one-off, command-line, or other operations.
- For production operations, cloud writes, external notifications, changes to real user data, and any other operations with external side effects, verify authorization for the current task. Confirm the exact target before performing database operations.

### 1.2 Fundamental Thinking and Engineering Principles

- Always apply these principles: first principles, Occam's razor, MECE, the Pyramid Principle, names that accurately reflect reality, an emphasis on orthogonality and decoupling, balancing rapid iteration with technical debt accumulation, visuals over text, less is more, and show, not tell.
- Always consider and study how the world's top 0.1% of practitioners and entrepreneurs across industry, academia, and interdisciplinary fields—the most mainstream, cutting-edge, outstanding, innovative, and agile—would each think about and solve problems, and combine their approaches and solutions.
- First seek benchmarks and reuse existing implementations, mature external solutions, innovative approaches, standard libraries, and platform capabilities to reduce unnecessary design and implementation and maintain a single source of truth.
- Treat the current codebase as a product you will maintain for the long term. Make implementation decisions proactively and take responsibility for code quality and future maintenance costs. When you find duplication, confusion, or unsuitable structures, proactively refactor, simplify, and clean them up so that every delivery makes the system easier to develop further.
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

### 3.1 Complete Solution Design

- During design and refactoring, proactively identify implicit state machines within the current scope, making their states and transitions clear, consistent, and verifiable.

### 3.2 New Capabilities and Research into External Solutions

- Before adding middleware, libraries, frameworks, services, platform capabilities, tools, infrastructure, or any other capability, examine the repository's existing implementations, standard libraries, and platform capabilities alongside mature commercial products, open-source projects, standard industry practices, and innovative industry practices, including new solutions that have emerged within the past year.
- Compare the research findings with building the solution yourself, covering functionality, maturity, applicable conditions, and cost. The user decides whether to adopt, trial, or build it.
- Proceed directly with building it yourself only when research confirms that no suitable external solution exists, or the user explicitly chooses to build it.

### 3.3 Product Behavior and Compatibility

- Before implementation, identify the product behavior this task is authorized to change and the user experience and interface agreements that must be preserved. Refactoring, simplification, deduplication, and experience improvements must stay within this scope.
- For user-visible changes not explicitly included in the task, explain the specific changes, reasons, and impact and obtain the user's agreement before implementation. This includes UI, copy, workflows, defaults, feature entry points, feedback, error recovery behavior, and experience changes indirectly caused by backend modifications. Design and experience adjustments explicitly authorized by the user may be completed autonomously within the agreed scope.
- Before delivery, review the actual diff and disclose all user-visible changes caused by the task, explaining before-and-after differences by user action or scenario. Explicitly list removals, hidden elements, changes to default behavior, and compatibility impacts. Do not substitute generic descriptions such as “experience improvements,” “refactoring,” or “simplification” for specific explanations. Disclosures must match the implementation and validation results.

### 3.4 User, Developer, and Agent Experience

- User experience (UX), developer experience (DX), and agent experience (AX) are the most important engineering goals. Every design and decision should improve all three, making systems more intuitive, easier to understand, operate, and evolve, while keeping existing capabilities reliable and usable.
- Always reduce the developer's burden of reading, understanding, remembering, and executing; always consolidate, simplify, and reuse; always orchestrate concurrency sensibly to complete tasks quickly.
- Proactively reduce unnecessary waiting, repeated operations, context switching, and manual transfers. Consolidate usable entry points, steps, and duplicate versions where appropriate. Provide a simple, complete default workflow, with one action for common operations wherever possible; retain modes and options only for real differences in use.
- Do not use unnecessary secondary explanatory text or auxiliary labels. Prefer to explain functionality through layout, hierarchy, spacing, and the interactions themselves. If extra text is needed to make the interface understandable, the design has a problem; improve the design before adding explanations. Do not generate slogan-style copy or turn the interface into an instruction manual.
- Error messages must identify the cause of failure, and recovery instructions must point to the exact target.

### 3.5 Implementation Scope and Lasting Fixes

- When adding or changing configuration, environment variables, or related dependencies, coordinate completion across all applicable environments as one task, configure each for its actual purpose, and verify that the settings take effect. Include necessary settings for development, testing, staging, production, CI/CD, and other applicable environments in the same implementation and acceptance scope; do not wait until release to discover omissions. For settings requiring additional authorization or currently lacking execution prerequisites, identify the specific gaps, owners, and completion timing in advance, include them in the same plan, promptly request necessary authorization, and follow through to completion. Updating configuration templates or passing validation in a single environment does not establish that all configuration is complete.

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
- The implementation owner maintains the existing task entry and the substantive content for their area. The designated integration owner is responsible for shared contracts, navigation and release queues, and concurrent resources.
- Use Orca Runs to manage multi-agent dispatches, dependencies, messages, and intermediate results; the Run records task and dispatch identities. Pi `subagent` calls do not automatically join the Orca task graph. Dispatch through Orca when supervised collaboration is required.
- Start new subtasks with independent context by default. Each task prompt must include its goal, necessary file paths, current decisions, and acceptance requirements. Apply this through the host tool's context inheritance parameter; in Pi, explicitly set `inherit_context: false`. Inherit the parent context only when the subtask requires the full discussion and a concise handoff is insufficient, and explain why in the task prompt. Continue follow-up work in the original subtask session where possible; in Pi, use `resume`.

### 4.4 Shared Interfaces and Parallel Integration

- Orchestrate tasks sensibly to avoid unnecessary communication, rework, and repeated integration.
- Before modifying shared interfaces in parallel, establish inputs and outputs, failure semantics, and the integration owner, then divide and coordinate the work.
- For changing shared boundaries, add only dependencies, semantic changes, owners, and integration conditions missing from machine records to the existing task entry. Assign one owner to shared rules; other tasks reference that source.
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
- Do not use Computer Use to operate Rancher, including login, API key creation or revocation, configuration, or cluster administration. The user performs Rancher UI operations with precise instructions from the agent; do not bypass this restriction with other browser automation. Authorized official API and CLI operations remain subject to existing permission rules.

## VII. Testing and Verification

### 7.1 Testing Investment and Long-Term Value

- Distinguish current verification from long-term tests. Assume that functionality, implementation, and strategies will change rapidly. Every change must receive verification matched to its actual risks, but does not require permanent new tests by default. One-off scripts, experiments, manual operations, and temporary checks can all provide evidence for the current change; only parts worth maintaining belong in long-term regression testing.
- Decide additions, retention, and deletion by sustained value. Consider useful lifetime, unique protection, maintenance costs, failure investigation costs, and execution waits together. Test counts, coverage percentages, age, change frequency, and directory classification cannot individually determine retention. Delete tests whose benefits fall below their ongoing costs, without requiring one-for-one replacements.
- Prioritize stable, important outcomes. Long-term tests should prioritize important user journeys, external interface contracts, permissions, money, data persistence, repeat execution, failure recovery, and resource ownership. Prefer retaining tests that have uncovered real defects and can independently identify regressions. Do not freeze internal structure, wiring, call order, current copy, or exploratory strategies into long-term constraints by default.

### 7.2 Verification Entry Points and Execution

- Verify through real consumer entry points and reduce duplicate protection. Target actual implementations and user outcomes directly, covering necessary success and failure paths. Give the most direct, effective entry point primary responsibility for each risk; add tests at other layers only when they provide unique value. Do not duplicate business logic in tests and use that duplicate to prove the implementation correct.
- Match verification intensity to the risks of the change. Prefer existing entry points and choose the smallest effective scenarios that expose the current problem; when fixing a defect, prefer existing test cases and confirm they expose the original defect. For shared state, database migrations, or lifecycle behavior, verify relevant combinations and execution orders; passing isolated runs cannot replace explicitly required combined verification. Once necessary checks pass, do not repeat or expand testing without new changes or unresolved issues. Do not use this as a reason to unilaterally expand general testing frameworks or add comprehensive gates.
- Assess the value of CI blocking separately. Run fast, relevant, reliable checks in daily CI; schedule expensive verification according to actual change risks and release stages. Blocking checks must have clear protection targets and actionable failures. Proactively reduce repeated runs, repeated environment setup, and unnecessary advance planning and intermediate artifacts.
- Clean up the entire dependency chain when deleting tests. Remove fixtures, helpers, scripts, CI jobs, release validators, and current documentation references that have lost their consumers; preserve independently reusable data under §7.4. Verify through actual execution entry points that selection, failure propagation, and summaries remain correct, avoiding situations where a workflow has been removed but other validators still require it.
- Fix real problems and keep verification honest. When tests fail, first distinguish product defects, test defects, and environment problems. Do not conceal problems by deleting valid protection, loosening correct expectations, ignoring failures, or modifying correct production code. Tests must clean up temporary data created by the current run, restore shared state they changed, and release resources occupied by the run on abnormal exit, preventing one failure from contaminating subsequent results.
- Tests directly verify executable authoritative sources such as code, configuration, schema, and manifest files. Maintain human-facing documents through review; automated checks cover only structural requirements such as paths, links, indexes, and a single authoritative source. Do not read human-facing documents to lock in natural-language wording or example implementations, or bind checks to frequently changing hashes, version numbers, specific text, or styles. For deterministic documents produced by generators, generated output may be verified; extract examples that need to execute into scripts or fixtures.
- Fully perform any end-to-end acceptance explicitly requested by the user. Do not stop after an initial implementation and ask the user to perform the testing themselves.

### 7.3 Evaluating Model Output Quality

- Allow reasonable error and do not pursue false precision. Systems with inherent uncertainty, such as randomized large-model outputs, recommendation rankings, and statistical estimates, should not be held to unrealistic absolute correctness. Focus on identifying systemic problems.

- Model quality aims for overall benefits to outweigh harms.
- Semantic judgments by models are uncertain; respect the imperfection of model outputs.
- Early retrieval emphasizes reducing omissions; final delivery emphasizes reducing incorrect recommendations.
- Compare overall benefits using the same batch of inputs across multiple scenarios, and disclose regression cases and changes in cost and latency.
- Do not promise correct semantic judgments for every sample.
- Additional processing stages or mandatory filtering must have a practical necessity. Do not keep adding processes in pursuit of absolute semantic correctness.
- Distinguish a lack of evidence from the presence of contrary evidence. A single negative judgment must not create a permanent exclusion across runs.
- Do not require every sample and metric to avoid regression. Do not hard-code rules for the wording, identity, or manually compiled lists of an individual query.

### 7.4 Verification Evidence and Reuse

- Prefer to accumulate and reuse initialization data, test data, edge cases, and defect reproduction samples prepared during development. Retain reusable material long term through the project's existing local data or testing entry points. Do not habitually discard it when a task ends, and do not require a definite plan for its next use. Organize, deduplicate, and retire data as appropriate, considering the cost of preparing it again, maintenance costs, and practical uses.

- The implementation owner explains important coverage tradeoffs during diff review, using existing verification entry points without adding test ledgers, approval layers, or coverage goals.
- Distinguish verification evidence from repository checks, local databases, external read-only checks, and production execution.
- Records affecting acceptance, recovery, or handoff must identify the executed command, source version or diff, working directory, target environment, and exit status.

## VIII. Git, Worktrees, Commits, and Releases

### 8.1 Git Working Principles

- Keep the main session at the project's designated engineering entry point for coordination, integration, and acceptance. Agents manage business-repository worktrees through Orca; users need not switch sessions or directories. Each project declares its own entry point; do not impose company-private paths on other projects.
- Keep the main worktree on a local integration branch such as `dev` or `main`. Create or reuse a task worktree only when repository files need modification; queries, discussions, and remote operations do not require a new worktree.
- Orca is the sole interface for creating, associating, and cleaning up worktrees. Follow Orca's configured locations; do not bypass Orca with raw Git commands to create or remove worktrees.
- At startup, confirm the task baseline and relevant main-worktree changes, preserve other tasks' uncommitted changes, and integrate qualifying commits promptly under §8.3.
- Worktrees isolate tasks. Subsequent sessions for the same task must reuse the existing worktree.
- Subagents decide whether to share the task worktree or create a separate one according to actual coupling and file responsibilities.
- Do not proactively push, create PRs, or change PR status without authorization.
- When genuinely depending on another task's uncommitted changes, identify the source task and exact diff, preserve the original attribution, and have the integration owner coordinate the integration order. Depended-on changes must not be counted as this task's output.

### 8.2 Execution Location and Integration

- When a process must run, determine whether it can run independently based on the source code, dependencies, configuration, ports, databases, queues, and worker consumption scope it actually uses.
- Prefer running independently runnable processes in the task worktree.
- When depending on services in the original workspace, fixed domains, or shared runtime resources, coordinate with the resource owner first, then choose between running in place and performing integration acceptance after integrating back.
- If the user specifies running in place, or actual conditions require it, add the reason to the existing task entry.
- Task environments support development and isolated verification; daily environments support post-integration use and combined verification. Pin release acceptance to an exact candidate commit and its build, so acceptance cannot drift with the daily branch. Select and manage environments through the project's existing engineering entry point.
- Limin defaults to the project's existing Air entry point for heavy tests; lightweight static checks may run locally. Other members use their own project environments; Air is not a team-wide prerequisite.
- Before integrating back, establish a single modification location and owner. Do not modify the same task code simultaneously in the original workspace and the task worktree.

### 8.3 Integrating Back and Cleanup

- Once an independently verifiable commit passes applicable checks, the worker immediately reports the commit, usable scope, and verification results. The main session arranges serial background integration of qualifying commits into the local integration branch and may delegate execution to an integration task, without waiting for the entire task to finish. The main session remains responsible for combined acceptance, remaining work, and final delivery; intermediate reports do not end that responsibility. Repository-owner approval is not a prerequisite for local integration.
- Do not use `git stash` in the original workspace, because all worktrees share the stash list.
- Remote integration branches such as `dev` and `main` must always be updated through PRs; direct pushes are prohibited. When remote delivery is needed, create a delivery branch from the target commit on the local integration branch, push that branch, and create a PR; keep the local main worktree on the integration branch. Handle owner and platform-required approvals at the remote PR stage.
- Before integrating, verify the target branch and relevant runtime resources. The later integrator reviews only concurrent semantics and combined behavior relevant to the change; unrelated commits do not require rechecking every task.
- Preserve commit boundaries that allow changes to be traced by task when integrating back. Do not leave multiple independent tasks mixed together as uncommitted changes for extended periods.
- The task owner remains responsible for acceptance when integrating back early and must commit promptly after completion.
- Once the task and delivery are complete and no active references remain, the main agent cleans up its temporary worktree and local temporary branch through Orca. Reuse the worktree while the task continues; integrating an intermediate commit does not trigger deletion.
- If cleanup cannot be performed safely, retain the resources and explain the reason, owner, and next step.
- If the user explicitly requests no commits, preserve a recoverable baseline, exact diff, and new files.
- Branches the user asks to retain, and worktrees and branches belonging to other tasks, are outside the cleanup scope.

### 8.4 Git Commits

- Before committing, review the actual diff, confirm behavior matches current agreements, ensure related content has no duplication or contradictions, and remove outdated explanations and temporary solutions.
- Write commit messages in Chinese. For large changes, first explain the background and overall implementation approach, then list specific changes as needed.

### 8.5 Release Boundaries

- Before releasing, prepare a release plan covering the complete delivery process and submit it to the user for review and approval as a whole. By default, include deployment, configuration changes, data migrations, data supplementation, backfills or recomputation, feature enablement, post-release acceptance, and any other necessary follow-up operations. Specify the execution order, impact scope, and completion criteria. Include all known necessary operations in the same review; do not separate work after deployment into undisclosed follow-up tasks. Once approved, execute the plan through to completion. Operations added or materially changed during execution require an updated plan and renewed confirmation. Prefer releases without downtime.
- When significant incompatibilities are discovered, explain the risks, impact, and available recommended options to the user before releasing; the user decides how compatibility will be handled.

## IX. Task Status, Plans, and Resource Management

### 9.1 Single Source of Task Status

- Reuse one current responsibility entry for each goal, preferably an existing Linear issue, Orca Run, or project task entry. Do not create plans, reports, or evidence documents by default.
- Before taking over, use the existing entry to verify authorization, owners, unfinished responsibilities, and relevant worktrees. Reference facts already recorded by Git, CI, and Orca directly.

### 9.2 Work Plan Contents

- Human records add only decisions, authorization, dependencies, and handoff information missing from existing entries. Do not duplicate status, identities, commits, or execution records already available in Linear, Orca, Git, or CI.
- Create a minimal supplementary record only when existing entries cannot support resuming the work, and reference the task entry and owner. Git tracks ordinary edit history.

### 9.3 Pausing and Resuming Tasks

- On pause or handoff, add only unrecorded next steps, waiting dependencies, open decisions, and external operations with unconfirmed outcomes to the existing task entry. Resume from that entry and its linked Git, CI, and Orca state.

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

- Clean up exact resources through their owning controllers; manage worktree cleanup exclusively through Orca.
- Follow the relevant project's standards for resource types, capacity limits, retention policies, reuse methods, and cleanup commands. Do not directly apply one project's environment model to other projects.
- Task copies may be destroyed by default. When a task is completed or abandoned, the main agent is responsible for cleaning up workspaces, browsers, and auxiliary processes belonging to the task and its subtasks. When cleaning up workspaces or resetting environments, look for data worth reusing and preserve it according to section 7.4.
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

- Before delivery, review the content actually changed and affected references. Maintain any existing supplementary task records without creating a new review document.
- Before committing, verify actual behavior against current agreements, ensure related documents have no duplication or contradictions, and remove outdated explanations and temporary solutions.
- Readers must be able to determine the next action from the current records.

### 10.3 Evidence and Plan Cleanup

- Retain evidence and audit files only when they are actually needed for current acceptance, handoff, production decisions, recovery, still-applicable incident conclusions, or subsequent experiments.
- Creators, participants, and full task IDs may be retained with existing dated evidence; trace committed implementation details through exact commits, paths, or blobs.

### 10.4 Closing Plans and Transferring Responsibility

- Report completion or transfer in the existing task entry. Maintain only supplementary records that actually exist and still carry responsibility; delete completed plans without continuing value.
- The final report references commits, verification results, and real gaps. Provide a current task entry only when responsibility remains.

### 10.5 Final Delivery

- Complete all necessary acceptance before delivery.
- At delivery, state the actual result, completed verification, remaining limitations, relevant evidence entry points, and follow-up tasks or recommendations.
- Emphasize any changes to product behavior, UI, or copy visible to users in the delivery, including indirect changes caused by backend modifications.
