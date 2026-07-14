# Production Readiness Checklist

Status: Reusable portfolio checklist
Purpose: Make each portfolio project look and behave like a commercial system without overstating its real deployment stage.

Use this checklist for each portfolio project brief. Mark items `N/A` only with a short reason.

## 1. Product Boundary

- [ ] Target user is named.
- [ ] Paid/billable workflow is named.
- [ ] Primary user action is clear.
- [ ] System output is clear.
- [ ] Human review point is clear.
- [ ] What the system does not do is clear.
- [ ] Stage label is clear: prototype, production-aligned, production-ready, live production.

## 2. Demo And Data Boundary

- [ ] Public demo uses synthetic, licensed, or demo-safe data.
- [ ] Demo data is documented.
- [ ] Real customer data is not required for the public path.
- [ ] Data retention expectations are stated.
- [ ] Export/delete story is stated, even if not implemented yet.
- [ ] No real confidential source text is published by accident.

## 3. Deployment Shape

- [ ] Local run command exists.
- [ ] Deployment target is named.
- [ ] Environment variables are documented.
- [ ] Secrets are not committed.
- [ ] Config differs cleanly between local, demo, and live environments.
- [ ] Health check exists or is planned.
- [ ] Backup/restore expectation is stated if persistent data exists.

## 4. Users, Tenants, And Access

- [ ] Authentication provider is selected or clearly deferred.
- [ ] Authorization roles are named.
- [ ] User/workspace/tenant boundary is represented in the data model.
- [ ] Admin/user distinction is clear.
- [ ] Invite or onboarding path is sketched.
- [ ] Passwords are never handled directly unless the project owns a secure auth implementation.

## 5. Billing Or Invoicing Path

- [ ] Billing model is stated: subscription, per-report, retainer, invoice, or manual billing.
- [ ] Test-mode integration target is named when applicable.
- [ ] Invoice trigger is named.
- [ ] Customer/account record shape is sketched.
- [ ] Billing status affects access or delivery where relevant.
- [ ] Manual invoicing fallback is acceptable for early consulting-style use.

## 6. AI Boundary

- [ ] Model calls are isolated behind a service or adapter boundary.
- [ ] Prompts/config are versioned or traceable.
- [ ] Structured outputs are validated.
- [ ] Deterministic checks run before model judgment where possible.
- [ ] Human review is required before high-impact outputs.
- [ ] Model/provider choice can change without rewriting the product.
- [ ] Failure modes are documented.

## 7. Evidence, Audit, And Observability

- [ ] Important actions have audit events.
- [ ] Source ingestion is traceable.
- [ ] Generated findings cite supporting evidence.
- [ ] Human approvals/rejections are recorded.
- [ ] Errors are recorded with enough context to debug.
- [ ] Basic metrics or traces exist for slow/failing steps.
- [ ] There is a way to explain why an output was produced.

## 8. Security And Safety

- [ ] Secrets use environment variables or secret store.
- [ ] Prompt injection or untrusted-document risk is named if documents are processed.
- [ ] Uploaded files are constrained by type and size.
- [ ] Output disclaimers match the domain risk.
- [ ] No legal, medical, financial, or compliance advice is claimed unless qualified.
- [ ] Dependency/security scan path is stated when deployable.

## 9. Evaluation And Quality

- [ ] Golden/demo cases exist.
- [ ] Regression checks exist for deterministic behavior.
- [ ] Eval harness exists or is planned for nondeterministic model behavior.
- [ ] Failure examples are preserved.
- [ ] Acceptance criteria are written.
- [ ] Manual review rubric exists for subjective output quality.

## 10. Cutover Checklist

- [ ] What must change before real users is listed.
- [ ] What must change before real customer data is listed.
- [ ] What must change before charging money is listed.
- [ ] Remaining legal/compliance/security questions are listed.
- [ ] Go/no-go criteria are listed.
- [ ] First real customer onboarding path is sketched.

