# CI economy and release policy

Use this policy for repositories owned by this account. Each repository implements
it in its own workflow and records its release commands in its own runbook.
This document does not automatically change GitHub account settings or repository
workflows. Existing repositories without CI do not need an Actions workflow merely
to inherit the policy.

## Routine work

- Run one PR validation lane; cancel superseded runs of that same PR. Preserve
  release and deployment runs. Avoid repeating the PR suite on every main merge.
- Route checks by changed paths, including deleted files and both sides of
  renames. Unknown code/config paths choose all applicable routine checks.
- Keep lint, types, unit tests, schema/contracts and security/isolation checks
  relevant to a change. Database/auth/runtime/dependency changes retain their
  integration checks. Small native projects still compile changed native sources.
- Documentation-only PRs need a short validation status, without installing app
  dependencies. Do not filter out the whole workflow when its status is required.
- A final status must reject selected failures, cancellations and unexpected skips.
  Use explicit Bash `pipefail` when piping test output through log processors.
- Do not add timers, duplicated matrices, empty test jobs or a central Actions
  orchestration repository. Combine inexpensive checks when this preserves useful
  failure reporting. Keep necessary operational monitoring at a justified cadence.

## Release work

Reserve complete coverage, browser/device/native-host replay and large dataset
regression for explicit release validation, Store uploads and major backend
releases. A repository may retain a focused build/integration check in ordinary
PRs when it protects an interface or cannot be replaced by a cheap check.

Record one immutable commit SHA for the complete release lane and release those
same bytes. A version tag or manual validation is not authorization to publish
or deploy. Keep product-specific acceptance and publication approval requirements.
Direct pushes, if permitted, must receive the applicable checks before release.

Required release inputs must fail closed when absent. A successful build with an
unexecuted E2E/replay/dataset test is not release acceptance. Report `NOT RUN`,
`FAILED` or `UNKNOWN` explicitly, preserving each product's device, store,
production, data-integrity and security requirements.

## Runners, storage and dependencies

- Use standard Linux for dependency-heavy builds, databases and browsers. Use
  `ubuntu-slim` only for short tasks that need neither privileged Docker/services
  nor unsupported native tooling. Validate the actual runner before relying on it.
- Use macOS only for an actual Apple build requirement. Do not adopt larger or
  self-hosted runners without measuring total cost and security/maintenance impact.
- Use committed lockfiles and cache downloads by lockfile/runtime. Keep compiler
  caches separate for different toolchains and build configurations; rebuild the
  selected source rather than treating a cached binary as acceptance evidence.
- Set job timeouts. Retain ordinary failure diagnostics for seven days and release
  artifacts for fourteen days unless a product has an explicit longer evidence need.
- Avoid unused browser/SDK installations. Do not upload PR binaries when only
  release artifacts are used. Avoid broad downloads of unrelated large assets.
- Keep useful Dependabot and public standard-runner checks: their execution does
  not carry the same paid-runner cost as private ordinary Actions runs.

## Accounting and review

Use account billing for actual paid spend and job records for workflow optimisation.
Keep gross usage, free allowance/credits and net charges separate. Missing billing
or run coverage is unknown, never zero. Round per job where the pricing model does,
and include storage, reruns and release workload when forecasting.

Recheck savings over a full billing month after rollout. Maintain an account-wide
Actions budget with alerts and a spending stop, allowing an explicit release reserve.
Repository YAML does not cap account spend. Reassess a guardrail separately from
the frequency and scope of validation; lowering a cap can block paid release jobs.
