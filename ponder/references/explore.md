# Explore: Decompose, Bundle, Weigh

Load when the probe leaves material questions open. Frame leaves, bundle
work, admit rounds, and decide when to stop.

## From question to leaves

Load `framing`; apply its moves to the question and probe records. Its ready
frame is the input to decomposition.

Turn open work into sub-questions one retrieval act can settle. Decompose by
governing principle. Each leaf names a mechanism and retrievable claim.

- Put dependent sub-questions in the draft's `[~]` chain; keep ledger leaves
  independent.
- 3 to 10 leaves covers the worked range. Past 10, fold near-duplicates
  before searching; below 3 still works.
- The leaf set is adaptive: add delegate discoveries as
  `"origin": "spawned"` and retire superseded leaves.

Register leaves as `leaves` entries in the round's `note` batch (schema in
the spine): keywords, question, origin. The output echoes the minted
identifiers; reference them by those.

## Bundled fan-out

Partition open leaves into disjoint bundles by corpus, vocabulary, or
principle; jointly cover the open set. Prefer fewer, fuller bundles.

Delegate through `/summon fanout`, one delegate per bundle. In each brief:
the objective is the bundle's leaf questions verbatim plus the session
question for scope; the evidence names the retrieval tools (web search and
fetch, `/lit-review` for scholarly corpora, `/read-pdf` for PDFs) and any
probe source the bundle builds on; the rules and the contract are the
fragments in `brief`; the bounds name the other bundles. Summon's mode table
decides when a bundle runs inline instead; the ledger state is the same
either way, and delegate identity stays outside it.

Delegates read source pages and return closure proposals; they write
nothing. The lead judges each return under summon's review, checks inflated
source-class tags against the spine definitions, then admits the round
through `note`.

## Admitting a round

Deduplicate sources, then admit spawned leaves, sources, closes, and
checkpoint as one `note` batch. On rejection, apply every listed fix and
resend once. Close deliberately abandoned leaves as `unresolved` with reason
`not_pursued` and its explanation.

## Checkpoint and the leave-or-stay call

Close each round with a `checkpoints` entry in the round's `note` batch,
carrying the round's declared search count (sum of delegates'
`searches_spent`); the same output returns the updated yield table.

Falling yield prompts a reframe-or-stop decision. Apply these bounds:

- Two unproductive rounds: stop, close remaining open leaves as
  `unresolved`, and draft.
- Begin saturation judgment one round past the declared focus.
- Run one to three rounds. A fourth-round need triggers reframing and
  folding.
- For one-round questions, use the floor rule.

## Frame discipline

Use anomalous evidence to test the frame. Before a `retrieved` close, name
its falsifier. Close contradicted premises as `refuted`; they feed Rival.
