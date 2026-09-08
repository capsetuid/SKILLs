---
name: author-skill
description: >-
  Turns a procedure or task history into a SKILL.md another agent can follow
  with no memory of the original session, and reviews existing skills
  against the Agent Skills standard. Use when asked to create, refactor,
  review, or distill a skill.
license: MIT
metadata:
  argument-hint: "[skill name or path]"
---

# Author Skill

Distill a procedure into a `SKILL.md` a fresh agent can follow, and review
an existing skill against the Agent Skills standard. Minimize loaded tokens
while preserving reliable execution; correctness, safety, and clarity
outrank brevity.

<directives>

  <directives for="frontmatter">
    <rule>Restrict the YAML header to Agent Skills spec fields (agentskills.io), in this order: `name`, `description`, then only as needed `license`, `compatibility`, `metadata`, `allowed-tools`. Put agent-specific hints such as `argument-hint` under `metadata` as quoted strings.</rule>
    <rule>Store the skill at `<name>/SKILL.md` and set `name` equal to the directory name: 1-64 characters of lowercase letters, digits, and hyphens, none leading, trailing, or doubled. Name a task skill as the imperative a user would speak (`fact-check`, `read-pdf`); name a persona as one noun (`caveman`, `ponytail`). Add no filler noun (`-helper`, `-protocol`).</rule>
    <rule>Write `description` as a `>-` folded scalar, 1-1024 characters, third person: first what the skill does and delivers, with the one or two guarantees a reader can hold it to and its key search terms; then triggers starting "Use when". Name no internal record, phase, file, library, verb, or level. Target 100 to 150 tokens; keep the library's descriptions together under 7,000 characters.</rule>
    <rule>Spell the invocation grammar once, in `metadata.argument-hint`: one bracket group per independent choice, in the order a user types them (`"[lite|full|ultra] [design|review|help]"`); a skill with no vocabulary names its subject (`"[file-or-section]"`). Update it whenever a verb, level, or mode changes.</rule>
    <rule>Set `license: MIT`. Add `compatibility` (at most 500 characters) only for runtimes, system packages, network access, or a full repository checkout the skill needs.</rule>
  </directives>

  <directives for="layout">
    <rule>Open the body with one to three sentences under the title: the task and the deliverable, naming no sibling.</rule>
    <rule>Declare every bundled file once, in a `## Registry` table that is the first `##` section, mapping a name to a path. A name is the basename without `.md`, in backticks; mark a file no run loads in its first line. Everywhere else, use the name alone: as the object of a word that says what it is ("load `brief`", "the template in `report`"), never as a bare value. Keep literal paths only in runnable commands.</rule>
    <rule>When a table is keyed by verb, mode, or level and each row loads the file of that name, say so once above the table and drop the column, naming any row that deviates.</rule>
    <rule>Put every task that belongs to a sibling or lies outside the skill in one `## Redirects` section directly after `## Registry` (first when there is no Registry; absent when there is nothing to redirect): one bullet per task, the condition, a colon, then the sibling in slash form or, with no sibling, the plain action to take instead. Where two personas pair verb for verb, route from the spine per verb ("`/pl-theorist`, same verb").</rule>
    <rule>Order the remaining sections by execution need: invariants, then procedure, then reference material, then gotchas, then completion checks. Use a heading that names a task, decision, contract, or reference topic. Number a list when order matters; bullet it otherwise; use a table only when shared columns make lookup cheaper.</rule>
    <rule>Keep `SKILL.md` near 500 lines with the core contracts, routing, and indispensable judgments; move bulky material to `references/`, loaded under a stated condition. Keep references one level deep: a reference cites a sibling by name and never links to it.</rule>
    <rule>Wrap every example, template, and payload in XML from the closed tag set: `directives` holding `rule`, `checklist` holding `item`, `procedure` holding `phase` and `step`, `examples` holding `example` holding `before`, `after`, `variant`, and `context`, plus `template` and `commands`. A tag names the kind of block; put the subject in `for`. Write tags in kebab-case, leave a blank line before an opening tag, and open `<![CDATA[` on its own line inside a tag whose payload a formatter would rewrap.</rule>
    <rule>Command a sibling skill's capability in slash form as an unconditional step ("read PDFs with `/read-pdf`"). Answer an environment condition (no network, unreachable file) with a fallback chain that names the degraded path.</rule>
  </directives>

  <directives for="content">
    <rule>Carry only what changes what the agent does: the contract (what a verb takes, returns, and refuses), the routing, and the judgments the agent owns. Leave out which library or endpoint implements a verb, policy and licensing framing, and anything the script states at the moment it matters (a `signal:` line, a rejection hint, a `next` field).</rule>
    <rule>Define success by observable outputs or checks. Separate required behavior from optional advice: "must" for a requirement, "may" for permission, "can" for a capability.</rule>
    <rule>State a prerequisite before the step that needs it. State branches, fallbacks, and stopping conditions at the step they apply to.</rule>
    <rule>Give judgment criteria, not persona labels such as "expert" or "rigorous".</rule>
    <rule>Define each topic in one file. Where a second file would restate a value, threshold, or enumeration, cite the owner instead, and only when that owner is in context when the copy is read (the spine, or a kernel loaded with it); a file loaded alone keeps its own copy.</rule>
    <rule>Parameterize every project-specific value (paths, scopes, hostnames, service and package names) or derive it from the consuming repository at runtime. Tie a skill to a language, framework, or layout only when that ecosystem is its purpose, stated in the description.</rule>
    <rule>When distilling from a session, keep only verified tool calls and successful commands; write the current rule, and keep a failure only as an actionable gotcha.</rule>
    <rule>When a skill's value is a judgment (a persona, a review, a reading), test the draft before finalizing: brief a delegate through `/summon` with the draft and a held-out case, score the return against criteria fixed in advance, and change the text until it holds. Keep the scores and runs out of the skill.</rule>
    <rule>Use an example to resolve a likely mistake, never to decorate a clear rule. Make every positive example conform to this standard; label an intentional counterexample.</rule>
    <rule>State a contract in a docstring or comment in at most two lines, plus one sentence only where a reader would otherwise make the wrong call. Put history in the commit.</rule>
  </directives>

  <directives for="writing">
    <rule>Write direct, neutral instructions. Lead with the verb; put a condition before its dependent action ("If X, do Y"). Name the actor where responsibility could be ambiguous. Keep "it", "this", and "the latter" locally unambiguous.</rule>
    <rule>Split obligations that execute independently; keep clauses together when splitting would hide their dependency. Use grammatical sentences in prose; use a fragment only in a label, table, or checklist where its role stays clear.</rule>
    <rule>Make each sentence supply an action, a condition, a decision rule, necessary context, or a useful example. Delete greetings, praise, wind-ups, heading restatements, process history, summaries that add no check, slogans, and unsupported rankings or claims of uniqueness.</rule>
    <rule>Keep rationale only where it changes a decision or prevents a likely error. Replace a slogan or metaphor with the action or condition it implies. Keep a contrast only where it separates plausible choices or enforces a boundary.</rule>
    <rule>Use one term for one concept; define an unfamiliar term at first use. Remove unnecessary words before shortening meaningful ones. Invent no abbreviation or shorthand and drop no grammar as a presumed saving.</rule>
    <rule>Preserve negations, exceptions, exclusivity, scope, necessary-versus-sufficient distinctions, uncertainty and evidential strength, numbers, units, thresholds, execution order, stopping conditions, permissions, and irreversible-action boundaries. Preserve commands, identifiers, literals, schemas, error strings, quotations, and intentional bad examples. Cut only empty hedges.</rule>
    <rule>State the pattern to follow; name a banned form only where it must be recognized (secrets, em-dashes, spec violations). Never emit an em-dash (U+2014).</rule>
    <rule>Reject a shorter rewrite when a fresh, less capable agent would have to guess. Claim a token reduction only when measured with a named tokenizer; report word and character counts as such.</rule>
    <rule>Draft under `/caveman lite`; sweep with `/humanize`, treating its patterns as signals, never as a banned-word list.</rule>
  </directives>

  <directives for="delegation">
    <rule>Hand work to another agent through `/summon`, supplying only what its caller table asks for: the unit one delegate closes, the record it receives, the rules of this skill that unit can break, the return shape by registered name, the cap, and the gate the lead admits the return through. Leave mode, brief shape, bounds, sizing, trust, and review of the return to summon; carry no worker prompt, delegation threshold, or cost figure.</rule>
  </directives>

  <directives for="scripts">
    <rule>Give the script the exact, decidable checks (existence, size, encoding, identity, structural equality, digests, atomic writes, backups) and hard-fail only on an invariant violation. Emit every heuristic as an advisory signal line stating its evidence, and have the skill text weigh signals against user intent. When a check is skipped or vacuous, say so in the output.</rule>
    <rule>Gate a destructive or hard-to-reverse effect on an exact witness (a marker file, an identity record, an explicit flag) and provide an undo path. Keep mechanical, idempotent repairs in the script; leave judgment calls to the agent.</rule>
    <rule>Document the full command surface and output conventions in `SKILL.md`, with one line beside the commands reserving source reading for user-instructed troubleshooting.</rule>
    <rule>Keep the command surface uniform: one record is a batch of one, sibling record kinds share one plural-array container, every subcommand names its subject the same way, and each effect has one spelling.</rule>
    <rule>Mint identifiers in the script: the agent supplies two or three keywords; return the lowercase dash-joined slug plus a 128-bit suffix (`b32hexencode(os.urandom(16)).decode().rstrip("=").lower()`) and echo it in every output. Accept a keyword subset as recovery for a lost identifier, signaling and re-echoing it, and error with candidates on ambiguity. Keep a natural key (DOI, path) where one exists.</rule>
    <rule>Pass configuration as flags and free-form content as one JSON object on stdin or `--file`: closed vocabularies, counts, booleans, paths, and identifiers are shell-safe; prose, queries, regexes, and JSON bodies are not, so give them no inline spelling. Let a literal parameter also take `@path` and `-`, with `@@` starting a literal `@`; keep a path-only parameter bare. Reject a malformed argument line as a located exit-1 rejection. Name the subject in every call and hold no ambient current-subject state; instruct the agent to bind the command and the session identifier to shell variables and chain a round's calls in one invocation.</rule>
    <rule>Make a skill that bundles Python a uv workspace member rooted at `scripts/`: `scripts/pyproject.toml`, `scripts/src/btm_<skill>/`, `scripts/tests/`, listed in the root `pyproject.toml`, with no code outside `scripts/`. Expose one entry point, the console command `btm-<skill>`, invoked through one binding, `R="env -u VIRTUAL_ENV uv run --project $(realpath <skill-root>/scripts) btm-<skill>"`; `realpath` is required because uv resolves the project path lexically and an alias path has no workspace root above it. Invoke no host `python` and no module path.</rule>
    <rule>Put logic shared across members once in the kernel `btm-corekit` under `.corekit/`, declared as `dependencies = ["btm-corekit"]` with source `btm-corekit = { workspace = true }`. Compose its gate mechanics (`SessionStore`, `EventLog`, `Admission` with `Pool`, `read_batch` and `rejection`, `wire_pad` and `wire_clean`) and add only the member's record semantics; redefine no kernel symbol.</rule>
    <rule>Decode every boundary-crossing shape with one pydantic model: a wire kind with variants as a union discriminated on its tag, a state file as a record, an untrusted value as a refined alias (`Slug`, `Doi`, `Count`). Subclass the kernel's frozen `Model`; set `extra="forbid"` where the agent writes the file and `extra="ignore"` where another writer owns it. Keep in the script only what a model cannot see: resolving against live state, minting, proving a cross-record link. Pass `uv run mypy`, strict with the pydantic plugin.</rule>
    <rule>Return every fix in one rejection: decode rows one at a time, check the values of a malformed row that resolve outside it, name the field to edit (`findings[0].claim`), and attach the entry's schema fragment as the hint.</rule>
    <rule>Use three shapes and no fourth: a `Model` serialized with `dump` for a record on disk, a `TypedDict` for a view a command computes and indexes, and `dict[str, JSON]` for the document a command emits.</rule>
    <rule>Keep durable light state (backups, logs, sessions) under `${XDG_STATE_HOME:-$HOME/.local/state}/btm-skills/<skill-name>/` (`%LOCALAPPDATA%\btm-skills\` on Windows) in purpose-named subdirectories. Put heavy or regenerable artifacts in temporary space under a directory named for its owner. Write logs as JSONL, one timestamped record per line, capped at write time. Ship a `clean` verb that removes one target or `--all` and reports the bytes freed.</rule>
    <rule>Mark a network request's origin by one convention, first defined wins: `BTM_USER_AGENT` sent verbatim; else `BTM_CONTACT`, else `skills@oss.joefang.org`, in the header `btm-skills/1.0 (<skill-name>; mailto:<contact>)`. Disclose the contact through polite pools (an OpenAlex or Crossref `mailto` parameter) only from a contact-derived identity. Read the variables in the script alone; mention them in no skill text.</rule>
  </directives>

  <directives for="output">
    <rule>Write the finished `SKILL.md` into the codebase, or return it as one raw Markdown block, with nothing before or after it.</rule>
    <rule>Before finalizing, check the edit for lost meaning, altered scope or order, weakened gates, and broken references.</rule>
  </directives>

  <checklist>
    <item>Frontmatter holds only spec fields in canonical order; `name` matches the directory; the description follows the capability-then-"Use when" form and the library's descriptions total under 7,000 characters; the argument hint matches the body's verbs, levels, and modes.</item>
    <item>The opening paragraph names task and deliverable; Registry is the first `##`; Redirects follows it with condition-colon-destination bullets.</item>
    <item>Every bundled file is cited by registered name; examples, templates, and payloads sit in closed-set XML tags.</item>
    <item>Every step names exact tools, flags, inputs, outputs, and stopping conditions; project-specific values are parameterized or derived.</item>
    <item>Delegation, where any, goes through `/summon` with only the caller's unit, record, rules, return shape, cap, and gate.</item>
    <item>Each sentence supplies an action, condition, rule, context, or example; a `/humanize` sweep finds no filler; negations, numbers, literals, and boundaries survived every cut.</item>
    <item>Any bundled script hard-fails only on invariants, signals heuristics, reports skipped checks, follows the member layout, and resolves its request origin by the `BTM_USER_AGENT` / `BTM_CONTACT` / default chain with no `SKILL.md` naming those variables.</item>
    <item>Gotchas hold non-obvious traps; no placeholder text remains outside templates.</item>
    <item>A fresh agent can execute the skill from its text alone, with no session memory or clarifying question.</item>
  </checklist>
</directives>

## Persona verbs

Dispatch a persona through verbs. Implement from this table the verbs the
lens can honor, each with the table's contract:

| Verb | Contract |
| --- | --- |
| design | Plan before code exists |
| build | Write new code |
| refactor | Rewrite existing code, behavior preserved |
| review | Judge a change: total over the diff, sound areas named |
| audit | Judge a codebase: sampled by blast radius, unexamined areas named |
| test | Derive checks from the lens's own laws |
| teach | Explain a judgment, calibrated to audience |
| help | Quick-reference card |

* Apply changes only in `build` and `refactor`; keep every other verb
  read-only.
* Give the same verb the same contract in every persona; vary only the
  lens.
* In a read-only verb, name what is outside the lens and route it to the
  sibling skill in slash form.
* Dispatch by explicit verb, then by unambiguous request shape, then by
  the persona's declared default verb.
* Load one verb file per invocation, registered under the verb's name.
* Add verbs beyond the core freely (`ponytail` carries `debt` and `stats`);
  give a verb name one meaning across the library, and reuse a name another
  skill already carries with that skill's meaning.
* Offer levels only where the lens needs them: `lite | full | ultra`
  (advise / enforce, the default / maximalist). Persist a level until
  changed and keep it orthogonal to verbs.

## Examples

<examples>

  <example for="distillation">
    <context>Converting raw history into a reproducible step.</context>
    <before>I tried bumping the dependency directly, the lockfile drifted and CI failed, then I realized this repo regenerates the lock via `make lock`, so I ran that and CI passed.</before>
    <after>
      <step>Regenerate the lockfile with the repository's command: `make lock`.</step>
      <step>Commit the manifest and the lockfile together.</step>
      Gotcha: editing the lockfile by hand drifts CI; regenerate it.
    </after>
  </example>

  <example for="description">
    <context>Writing a routing description.</context>
    <before>This skill helps format python code using black and flake8.</before>
    <after>Formats and lints Python code with Black and Flake8. Use when asked to format Python, lint a file, or run either tool.</after>
  </example>

  <example for="parameterization">
    <context>Removing incidental project specifics.</context>
    <before>Run the build script located at `/users/joe/projects/manifold/scripts/build.sh`.</before>
    <after>Run the build script at `<repository-root>/scripts/build.sh`.</after>
  </example>

  <example for="xml-isolation">
    <context>Fencing a payload so it reads as data.</context>
    <before>
      Your config file should look like this:
      { "port": 8080 }
    </before>
    <after>
      Create the configuration file from this template:
      <template for="config">
      { "port": 8080 }
      </template>
    </after>
  </example>
</examples>
