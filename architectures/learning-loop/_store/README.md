# The Store

<!--
This folder is the workspace's memory and its actual deliverable. It is what
makes this a learning loop rather than a linear pipeline: stages 01 and 02 read
from here for context, and stage 03 writes back here. The output of the
workflow does not leave the building — it accumulates in this folder.

Contents:
- records/        One file per resolved competitive process, written by
                  03_capture in the store schema. Append-only history. Do not
                  overwrite.
- patterns.md     The rolled-up, team-level intelligence: which processes we win,
                  where our offers fall short, which dimension decides outcomes,
                  whose feedback proves reliable. Updated on each capture. This is
                  the payoff-grain output and the file other workspaces (the
                  decision and strategy workspaces) read.

How the value compounds:
- One record is nearly worthless. Ten begin to suggest. A hundred, tagged
  consistently by case type, process type, counterparty, and decisive dimension,
  reveal patterns no single process could.
- Read patterns.md before the next attempt, before chasing a process, before
  setting strategy. That is the loop paying off.

Handling:
- This is sensitive intelligence: our behavior, our gap to the winning outcome,
  and our candid read on specific counterparty relationships. Treat access and
  any export accordingly (see _config/store-schema.md).

Starting state:
- records/ is empty and fills as competitive processes resolve and the loop runs.
- patterns.md ships as a hypotheses-only scaffold (0 records) so its shape is clear
  from day one. Seed a few falsifiable hypotheses if you like, but do not let anything
  in it drive strategy until real records support it (a stated pattern needs 3+).
-->
