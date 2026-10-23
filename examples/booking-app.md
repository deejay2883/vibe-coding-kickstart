# Example: a salon booking MVP

This is an illustrative conversation showing the intended workflow, not a captured live-host test or a customer testimonial.

**You:** I want to build a salon booking app. I cannot code. Quick mode, please.

**Skill:** What should a customer be able to complete in the first version: request an appointment, reserve a confirmed slot, or pay for a booking?

**You:** Request an appointment. The salon will confirm it manually. No payments yet.

**Skill:** Who will try the first version with you?

**You:** One salon owner and five customers. Use fictional names for the demo. Give me a handoff.

## Example handoff

**Goal:** test whether one salon and its customers find appointment requests useful.

**Confirmed first slice:** a customer requests an appointment; the salon confirms it manually. Pilot audience: one owner and five customers. Demo uses fictional names. Payments are out of scope.

**Proposed approach:** create a local prototype with synthetic requests before introducing real customer data. Keep the stack unselected until the coding assistant checks the project context.

**Proposed acceptance criteria:** a valid request appears once in the owner's queue; missing required information produces a clear error; the customer sees that the request is pending, not confirmed; repeated submission does not create duplicate requests.

**Unknown:** who can view requests, how the owner signs in, what contact information may be collected, and how confirmations reach customers. These remain unresolved for live use.

**Verification:** all checks are planned, not run.

**Next step:** build the synthetic request flow and review it with the salon owner. Use the interview to resolve access and data decisions before real-customer use.

## Try another phase

> We already have a working booking app. We changed permissions. Help me plan regression testing without restarting discovery.

The interview should switch to the change, preservation of existing behavior, affected roles, and expected results. Report your actual experience through the repository's feedback form.
