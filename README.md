# GenLayer AI Source Claim Auditor

A GenLayer Intelligent Contract that audits a claim against provided source text.

## What it does

The contract accepts:

- source text
- claim

Then it returns:

- SUPPORTED
- CONTRADICTED
- UNCLEAR

with one short reason.

## GenLayer features used

- `gl.eq_principle.prompt_non_comparative`
- source-based validation
- public write method: `audit_claim`
- public view method: `get_last_audit`

## Test

Source:
GenLayer introduces Intelligent Contracts that can connect AI models and web data with blockchain applications.

Claim:
GenLayer uses Intelligent Contracts with AI.

Result:
SUPPORTED.

## Contract address

0xE296DC29629e102e94FE1A5E19D2382b3e873DB9
