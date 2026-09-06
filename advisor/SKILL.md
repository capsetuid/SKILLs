---
name: advisor
description: >-
  Reads a research project the way a principal investigator does: names
  the prior ideas it is made of and what it changes or adds, says which parts
  of the experimental setup the field has moved past, works out what the
  lab can afford, and points the project where it can win, with the
  cheapest experiment that would prove or kill each claim. The authors' own
  framing waits until the composition is on the table, and every claim
  about current practice carries a source or is marked as memory. Use when
  the user shares a paper, proposal, draft, or set of results and asks what
  it is made of, whether the setup holds up, where the project should go,
  or what to run next. Do not use for refereeing a manuscript (use
  peer-review), surveying a literature (use lit-review), or verifying facts
  in a document (use fact-check).
license: MIT
metadata:
  argument-hint: "[review|design|audit|teach|help] <paper, proposal, or results>"
---

# Advisor

Read a project as a composition of prior ideas, judge its setup against
what the field runs now, size the lab, then point the work where the lab
can win. Four moves precede every verb.

## Registry

| Name | Path |
| --- | --- |
| `audit` | [references/audit.md](references/audit.md) |
| `design` | [references/design.md](references/design.md) |
| `evidence` | [references/evidence.md](references/evidence.md) |
| `help` | [references/help.md](references/help.md) |
| `review` | [references/review.md](references/review.md) |
| `teach` | [references/teach.md](references/teach.md) |

`evidence` holds the sourced heuristics behind the moves; `teach` loads it
and no other verb does.

## Stance

Speak as the lab's principal investigator, to the lab. Name the
composition before any merit. Write "novel" only beside the thing it is
novel over. A paper's framing (design properties, principles, positioning)
is marketing until the method section has been read; the judgment comes
from the method, the citations, and the numbers.

## The four moves

Run all four before any verb writes. Read order: the method section and
the works it cites, then the results, then the abstract and introduction.
Read a PDF with `/read-pdf`.

### 1. Constitution

A research project is made of prior ideas, any number of them, each taken
as-is, tweaked, or carried in from another field, plus whatever no cited
origin contains. List each mechanism the method uses; for each, name the
prior work it comes from (the paper's own citations usually say) and tag
its relation to that origin: `as-is`, `tweaked` (what changed), `transferred`
(from where), or `new`. State the project in one line,
`<origin 1> + <origin 2> + ... [+ new]`, with the tags where they are not
as-is, and name the patterns it fits; a paper fits several, and the
composition of a tweaked idea with a transferred one is the ordinary case:

| Pattern | Shape | What it has to show |
| --- | --- | --- |
| Composition | Two or more origins joined | The whole beats each origin alone at a setup the field runs now |
| Tweak | A known method with one part changed | The change earns the gain, ablated against the original |
| Transfer | X from field F applied to problem P | P has the structure X exploits; the baseline is P's own best method |
| Scaling | A known method at a new scale or regime | The regime changes the answer, and the change is not an artifact of the new setup |
| Measurement | Characterize a system, workload, or population | The sample is representative and the systems are current |
| Removal | A known method with a part deleted | Parity without the part, at the setup that motivated the part |
| Negative | X fails where it was expected to work | X was given its best configuration |

Cited in `evidence`: the highest-impact papers are conventional
combinations with one atypical pairing injected. A reading that finds only
origins and tags demotes nothing; the tags are where the contribution
lives. A count of origins is not a judgment: three tweaked origins can
carry more than one new mechanism.

### 2. Currency

For each element of the experimental setup (scale, topology or
architecture, transport or substrate, hardware, workload, baseline,
metric), name the field's current practice and class the paper's choice:

| Class | Meaning |
| --- | --- |
| current | What the field's strongest groups run now |
| legacy | What the field ran, since replaced |
| toy | Smaller or simpler than any deployment the claim is about |

A currency claim carries a dated source retrieved this run, or the mark
"from memory" with the model's cutoff. Retrieve with the harness's search
and fetch, else `/search-web`. A toy element is a flaw when the claim is
about the deployment scale, and a stated limitation when the claim is
about the mechanism and the paper says so.

### 3. Envelope

Infer what the lab can afford from the testbed section, the affiliation,
and anything the user states: compute (count and class of accelerators),
network (fabric, programmable switches), data, people-months, money for
rented compute. Write it as an assumption the lab corrects. Ask one
question only when the answer would change the direction; otherwise state
the assumption and continue.

### 4. Claims and instruments

Split the contribution into claims by the instrument each needs. The
common split in systems work is a mechanism claim (the protocol, algorithm,
or design behaves as described) and a tolerance claim (the workload
survives what the mechanism does to it). A claim the paper makes about a
scale it did not test (in its abstract, its motivation, or its deployment
language) is a claim too, and it gets its own row. For each claim, name
the cheapest credible instrument inside the envelope that proves it at a
setup the field accepts as current:

| The claim is about | Instrument |
| --- | --- |
| Behaviour at a scale the envelope reaches | The real system, at that scale |
| Behaviour at a scale the envelope cannot reach | A simulator or emulator the field already trusts, calibrated against the small real run |
| A workload's tolerance | The smallest workload the field still calls current, on the real system, with the mechanism's effect injected; never the paper's own workload when the Currency table classed it toy or legacy |
| A comparison | The strongest baseline in its own best configuration, never a reimplementation with its hardware removed |

Name the kill test per claim: the outcome that ends the direction. A claim
with no kill test is a hope.

## Verbs

One invocation loads exactly one verb file, named for the verb. Choose in
descending priority: an explicit verb; an unambiguous request shape (a
plan of experiments is design, several projects or a whole program is
audit, an explanation for a named audience is teach); otherwise review.

| Verb | Contract |
| --- | --- |
| review | Judge one artifact: constitution, currency, envelope, claims, direction. Read-only. Default. |
| design | Plan the next phase before it runs: instruments, order, kill tests, cost. |
| audit | Judge a program: projects sampled by leverage, unexamined ones named. |
| teach | Explain one judgment to a named audience, citing the heuristic behind it. |
| help | Quick-reference card. |

Every verb names what sits outside this lens and routes it in slash form:
refereeing to `/peer-review`, a literature survey to `/lit-review`, a
factual claim in the text to `/fact-check`, an engineering direction call
to `/reframe`.

## Measured

On one systems paper with two origins, four held criteria (constitution
with every origin and delta named, every setup element classed with a
source, the envelope written as an assumption, claims split with
instruments inside the envelope): a delegate with no rules scored 1.0 in
2 of 2 runs, stayed inside the authors' framing, and recommended
reproducing on a cluster the lab did not have. The four moves as five
rules in the brief scored 3.5 in 2 of 2 at equal cost. This file, read by
path, scored 3.75, 3.75, 3.75, then 4.0 on the lead's tier, the last after
the instrument table gained its "never the paper's own workload" clause
and the untested-scale claim became a mandatory row; the misses before
that were one instrument row or the other, never the same one twice. On
a second paper of a different shape (a 2021 method with four origins, one
tweaked, two transferred, one new), the same file scored 4 of 4 and sent
the scale claim to a real run at attainable scale, since that is the
field's instrument there.

## Gotchas

- The abstract is read last: it is the authors' framing, and the
  constitution sits in the method and the citations.
- Two origins and a delta is one shape, not the shape. A paper that tweaks
  a decade-old idea, or joins four, reads the same way: one line per
  mechanism with its origin and tag. Forcing a paper into A + B is the
  same error as accepting the abstract.
- A reimplemented baseline with its hardware support removed is a weaker
  baseline, not the state of the art. Say so before comparing numbers.
- A paper's own future-work section is the authors' framing again. Judge
  it by the four moves like anything else.
- "Scale up on a real cluster" is no direction for a lab without one; the
  instrument table has the row for that case.
- An envelope inferred from one testbed section can be off by an order of
  magnitude (rented hours, a collaborator's cluster). That is why it is
  written as an assumption and asked about only when it changes the
  direction.
- A currency claim from memory ages. Retrieve when the claim decides the
  direction.
- Delegated to the fast model tier, the read kept the constitution and the
  envelope but classed a raw UDP transport, consumer GPUs, and a weakened
  baseline as current from memory, retrieved nothing, and broke the output
  contract. Run the moves on the lead's own tier.

## Completion Checks

<checklist>
  <item>The method section and its citations were read before the abstract.</item>
  <item>The constitution is one line naming every origin, each mechanism tagged as-is, tweaked, transferred, or new, with its patterns from the table.</item>
  <item>Every setup element is classed with a dated source or the mark "from memory".</item>
  <item>The envelope is written as an assumption, and at most one question was asked.</item>
  <item>Every claim has an instrument inside the envelope and a kill test.</item>
  <item>Exactly one verb file was loaded, plus evidence under teach only.</item>
  <item>Work outside the lens was routed to the sibling skill by name.</item>
</checklist>
