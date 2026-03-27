# Learning — Project management facade discipline

**Date**: 2026-03-27

## Pattern

When designing project-management skills, especially facades like `/project-manager`, it is safer to treat the **artifact and module layer as primary** and the facade as an optional, thin dispatcher. The real system is:

- canonical ledgers (trigger log, deliverable map, claim register, submission log, change log)
- explicit project-management capabilities (state sensing, trigger capture, deliverable trace, decision support, submission freeze, learning capture)

The facade’s only legitimate roles are:

- consolidate disoriented state into a clear view
- propose or transparently dispatch low-risk orientation actions
- emit receipts describing what it inferred, which capability it invoked, and which artifacts were touched

It must **not** become a hidden orchestrator that silently changes strategy, priorities, or structure.

## Why this matters

It is very easy for a “nice” `/project-manager` to accumulate responsibilities until it effectively owns the workflow. That violates the Oracle stance of “External brain, not command” and makes it harder to audit decisions. Anchoring on artifacts and explicit modules preserves transparency and makes it easier to evolve or replace individual capabilities over time.

## How to use it

- Start implementation with ledgers and explicit modules, not facades.
- When a facade is added, enforce guardrails: low-risk auto actions only, explicit human confirmation for strategic changes, and visible operation receipts.
- Use retrospectives and handoff notes to freeze architectural decisions so that future work does not unconsciously re-centralize control in a singleton.
