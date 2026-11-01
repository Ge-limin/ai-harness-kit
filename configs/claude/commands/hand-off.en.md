---
description: Generate a handoff prompt ready to paste into a new agent session so it can continue the current work seamlessly
argument-hint: "[Optional: the scope you want the next session to focus on or take over]"
---

The user wants to end the current session and hand the work over to a **brand-new agent session with none of this conversation's context**.

Your task: using all the context from the current conversation so far, write **one self-contained handoff prompt** that the user can copy and paste directly into the new session. After reading it, the new agent should be able to continue seamlessly, without needing to ask you any follow-up questions.

$ARGUMENTS

## Output Requirements

- Put the handoff prompt in a **fenced code block** for easy one-click copying. Do not add pleasantries outside the block.
- Address the new agent in the **second person** (“Your task is…,” “The current state is…”). Do not write a summary addressed to the user.
- Assume the reader **knows nothing** about the project or task: use absolute paths throughout; explain every specialized term or abbreviation on first use; do not rely on references that make sense only within this session (“that file” and “the changes just made” must identify the exact file or changes).
- Hand over only information **actually needed to continue the work**. Remove chronological activity logs and abandoned detours that are no longer relevant. Favor precision over length.
- Follow the user's language: if this session has been primarily in Chinese, write in Chinese; if in English, write in English.

## The Handoff Prompt Must Cover (In This Order; Adapt to the Situation Without Forcing Empty Sections)

1. **Goal / North Star** — What the task must ultimately deliver and what success looks like.
2. **Current State** — What has been completed, the current step, and what can or cannot run now. Which files changed (absolute paths) and the key changes.
3. **Remaining Work** — What remains, preferably broken into ordered, independently verifiable steps, each with a `verify:` instruction explaining how to confirm it was done correctly.
4. **Key Context and Pitfalls** — Decisions already made and their reasons, approaches tried that did not work (so the new session does not repeat them), mandatory conventions, hidden dependencies, and environment prerequisites.
5. **Starting Point** — Which files, documents, or SSOTs (single sources of truth) the new session should read first (absolute paths), and which directory and command to start from. If convention files such as `docs/working-plan/README.md`, the project `README.md`/`AGENTS.md`, or `CLAUDE.md` exist, name them explicitly and tell the agent to read them first.

## Before You Begin

- If **critical information is missing** from the current conversation's context (for example, the goal has never been clearly stated, or the state is too ambiguous for a handoff), first tell the user exactly what is missing and briefly confirm it before generating the prompt — do not invent details.
- If `$ARGUMENTS` specifies a handoff scope, focus on that scope and include only the necessary background for everything else.
