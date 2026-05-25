# Gated Decision Pipeline References

<!--
This folder holds knowledge that applies across evaluations, not to one item.

What lives here:
- The decline log: every declined item and its tagged reason. The decide stage
  writes to this. Over time it keeps decisions consistent (the same kind of
  item gets the same answer) and reveals the team's rejection patterns.
- Prior evaluations of similar items, for comparison and consistency.
- Comparables and recent activity the team tracks.
- The team's standards as they apply at the evaluation level.

This is L3 reference, shared across the queue. Keeping it separate from _config
means the standing criteria (what the team takes on, how it decides) stay clean
while the accumulating record of actual evaluations grows here.

The decline log is the asset that makes decisions compound: a team that can see
why it declined its last hundred items decides its next hundred faster and more
consistently.

Starting state: empty. The decline log and the rest fill on first use. A stage
contract that names a file here treats it as optional until you populate it —
the absence is not an error, it is a workspace that has not run yet.
-->
