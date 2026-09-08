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
an existing skill against the Agent Skills standard.

<directives>

  <directives for="anatomy">
    <rule>Store the skill in a kebab-case directory containing a file named exactly `SKILL.md`.</rule>
    <rule>Begin the file with YAML frontmatter restricted to Agent Skills spec fields (agentskills.io), in this order: `name`, `description`, then only as needed `license`, `compatibility`, `metadata`, `allowed-tools`. Never emit agent-specific extension fields such as `argument-hint` or `when_to_use`; record such hints as quoted string values under `metadata`.</rule>
    <rule>Set `name` equal to the directory name: 1-64 characters; lowercase letters, numbers, and hyphens; no leading, trailing, or consecutive hyphens. Name a task skill with an imperative verb phrase, the command a user would speak (e.g., `fact-check`, `read-pdf`, `git-commit`); name a persona or stance skill with a single noun (e.g., `caveman`, `ponytail`). Never append filler nouns like `-protocol`, `-helper`, or `-skills`.</rule>
    <rule>Write `description` as a `>-` folded block scalar, 1-1024 characters, third person, in two movements: first a capability statement carrying the skill's key search terms, then trigger conditions starting "Use when". Put routing to a confusable sibling in `## Redirects`; keep the library's descriptions together under the gate's 7,000-character budget. The description sits in context whether or not the skill runs, so give it the deliverable and one or two guarantees the reader can hold the skill to, in the reader's vocabulary, and names no internal record, phase, or file the body defines, no library the skill calls, and no verb or level the argument hint lists. Target 100 to 150 tokens.</rule>
    <rule>Give every skill `metadata.argument-hint`, the one place its invocation grammar is spelled: one bracket group per independent choice, ordered as a user types them (`"[lite|full|ultra] [design|review|help]"`); a skill with no vocabulary names its subject (`"[file-or-section]"`). Re-check it whenever a verb, level, or mode changes.</rule>
    <rule>Set `license: MIT` so a skill vendored out of this repository retains its terms.</rule>
    <rule>Add `compatibility` (max 500 characters) only when the skill requires specific runtimes, system packages, or network access; most skills omit it.</rule>
    <rule>Use Markdown `##` or `###` headings for internal structure.</rule>
    <rule>Open the body with one to three sentences under the title stating what the skill does and delivers, naming no sibling. Put every task belonging to a sibling or outside the skill in one `## Redirects` section directly after `## Registry`, or first where none exists, one bullet each: condition, colon, then the sibling in slash form or, with no sibling, the plain action to take instead. Route per verb from the spine where two personas pair verb for verb ("`/pl-theorist`, same verb").</rule>
    <rule>Command a sibling skill's capability in slash form as an unconditional instruction ("read PDFs with `/read-pdf`"); the library is consumed as a set, so siblings are present. A fallback chain answers an environment condition (no network, an unreachable file) and names the degraded path.</rule>
    <rule>Address bundled files by registered name, never by path. Declare every path exactly once, in a `## Registry` table that is the first `##` section of `SKILL.md` and maps each name to its path. A name is the basename without `.md`, backticked. List every bundled file; mark a file no run loads, such as a maintainer protocol, in its first line. When a table is keyed by verb, mode, or level and each row loads the file of that name, say so once above the table and drop the column, naming any row that deviates. Use a name as an address, the object of a word that says what it is ("load `brief`", "the template in `report`"). Keep the literal path in runnable commands. Cite the file that owns the topic; when ownership moves, move every citation in the same change. Reference files cite siblings by name only and never link: references stay one level deep from `SKILL.md`.</rule>
    <rule>Define each topic in exactly one file. Where a value, threshold, or enumeration is restated in a second file, replace the copy with an attribution naming its owner. Attribute only toward a file guaranteed to be in context when the copy is read (the spine, or a kernel co-loaded with it); a file the skill loads alone keeps its own copies.</rule>
    <rule>Wrap all examples, templates, and payloads strictly in XML tags to prevent instruction bleed. The tag set is closed: `directives` holding `rule`, `checklist` holding `item`, `procedure` holding `phase` and `step`, `examples` holding `example` holding `before`, `after`, `variant` and `context`, plus `template` and `commands`. A tag names what kind of block it is and nothing else; what the block is about goes in `for`, so a new subject never mints a new tag. Name every tag in kebab-case and leave a blank line before an opening tag: CommonMark's tag name admits letters, digits and hyphens but never an underscore, and an HTML block opens only on a complete tag that no paragraph runs into. When a payload holds code or markup a formatter would rewrap, open `<![CDATA[` on its own line inside the tag. Miss either and the payload is paragraph text, which a formatter rewraps into unparseable code.</rule>
  </directives>

  <directives for="execution">
    <rule>Target this skill exclusively at agent-facing procedures.</rule>
    <rule>When distilling from a session, extract only verified tool calls and successful commands from its history.</rule>
    <rule>When the skill's value is a judgment (a persona, a review, a reading), test the draft before writing it up: brief a delegate through `/summon` with the draft and a held-out case, score the return against criteria fixed in advance, and change the text until it holds. The scores and the runs stay out of the skill.</rule>
    <rule>Parameterize every project-specific value (paths, scopes, hostnames, service and package names) or derive it from the consuming repository at runtime. Tie a skill to a language, framework, or directory layout only when that ecosystem is its purpose, stated in the description.</rule>
    <rule>Lead with the action; condition first ("If X, do Y"). Imperatives; a fragment only where its role stays clear.</rule>
    <rule>Each sentence gives an instruction, a decision rule, needed context, or an example. State a rule once; cite its owner only when that owner is in the reader's context. Keep rationale only where it changes a decision.</rule>
    <rule>Delete greetings, praise, wind-ups, heading restatements, process history, summaries, slogans, and unsupported rankings. Replace metaphors, invented labels, and theatrical contrasts with the concrete action or condition.</rule>
    <rule>Cut filler hedges; keep uncertainty, evidence strength, scope, negation, and necessary-versus-sufficient distinctions. Keep terms, commands, schemas, literals, numbers, units, citations, permissions, safety boundaries, intentional bad examples, and quoted sources.</rule>
    <rule>State the pattern to follow; name a banned form only where it must be recognized (secrets, em-dashes, spec violations).</rule>
    <rule>Write under `/caveman lite`; sweep with `/humanize`. Patterns are signals, not banned words. Invent no abbreviations; strip no grammar; when a cut is in doubt, count tokens, not words.</rule>
    <rule>When a shorter form makes a weaker agent guess, keep the explicit form: no step implied, no assumption unstated.</rule>
    <rule>Carry only what changes what the agent does, since every invocation pays for the whole text: the contract (what a verb takes, returns, and refuses), the routing (when to reach for this verb, this level, or a sibling skill), and the judgments the agent owns. Leave out which library, service, or endpoint implements a verb, since the agent chooses a verb and never a vendor. Leave out policy, licensing, and terms-of-use framing. Leave out anything the script already states at the moment it matters: a `signal:` line, a rejection hint, or a `next` field. Hold the `description` to a stricter cut, since it sits in context whether or not the skill runs.</rule>
    <rule>State a contract in a docstring or comment in at most two lines, then one further sentence only where a reader would otherwise make the wrong call. Put history in the commit: what the code replaced, which bug prompted it, and what an earlier shape did wrong.</rule>
    <rule>A skill that hands work to another agent commands `/summon` and supplies only what summon's caller table asks for: the unit one delegate closes, the record it hands over, the rules of its own that unit can break, its return shape by registered name, its cap, and the gate the lead admits the return through. Mode, brief shape, bounds, sizing, trust, and review of the return are summon's: restate none of them, and carry no worker prompt, delegation threshold, or cost figure in the skill.</rule>
    <rule>Never emit em-dash characters (U+2014); use a hyphen, a comma, a colon, or restructure the sentence.</rule>
  </directives>

  <directives for="scripts">
    <rule>Design the script as the symbolic half; the skill text tells the agent, the neuro half, how to consume its output.</rule>
    <rule>Give the script the exact, decidable checks: invariants (existence, size, encoding, identity), structural equality, digests, atomic writes, backups. Hard-fail (nonzero exit) only on an invariant violation.</rule>
    <rule>Emit heuristic judgments as advisory signal lines, never as refusals, that state their evidence (ratios, matched rules, best-guess classification); the skill text instructs the agent to weigh signals against user intent.</rule>
    <rule>Gate destructive or hard-to-reverse effects on an exact witness: a marker file, an identity record, or an explicit flag the caller must pass. Provide an undo path (verified backup) where the agent's judgment could be wrong.</rule>
    <rule>When a check is skipped or vacuous, say so in the script's output.</rule>
    <rule>Document the script's full command surface and output conventions in SKILL.md, with one line beside the commands reserving source reading for user-instructed troubleshooting.</rule>
    <rule>Mint identifiers in the script: the agent supplies two or three keywords, the script returns the lowercase dash-joined slug plus a 128-bit entropy suffix (b32hexencode(os.urandom(16)).decode().rstrip("=").lower()) and echoes it in every output. Take the full identifier in later calls; resolve a keyword subset as the recovery path for an identifier lost to context compression, signal and re-echo it on use, and error with candidates on ambiguity. Keep a natural key (DOI, path) where one exists.</rule>
    <rule>Keep the command surface uniform: one record is a batch of one, sibling record kinds share one plural-array container schema, every subcommand addresses its subject the same way, and each effect has exactly one spelling. Each asymmetry costs the consuming agent a re-read of help text.</rule>
    <rule>Pass configuration as command-line parameters and free-form content on stdin. Keep closed vocabularies, counts, booleans, paths, and minted identifiers as flags, since they are shell-safe; read prose, queries, regexes, and any JSON body as one JSON object from stdin or `--file`, with no inline spelling. Give a parameter that takes a literal `@path`, which reads the file, and `-`, which reads stdin, with `@@` starting a literal `@`: the agent can write any value it holds without quoting it through a shell. Keep the bare spelling for a parameter that is only ever a path, so `@` marks a path exactly where a literal is also possible. Treat argv as untrusted input: reject a malformed argument line as a bounded, located exit-1 rejection. Name the subject in every call, since several agents may share one state root, and hold no ambient current-subject state. Keep identifiers cheap by instructing the agent to bind the command path and session identifier to shell variables (reused while the shell persists, re-bound after a reset) and to chain a round's calls in one shell invocation.</rule>
    <rule>Make a skill that bundles Python a member of the repository's uv workspace, the member being the skill's `scripts/` directory: it holds `scripts/pyproject.toml`, a `scripts/src/btm_<skill>/` package, and `scripts/tests/`, is listed in the root `pyproject.toml`, and keeps every coding element inside `scripts/` so the skill directory stays documentation. Expose one entry point, the member's `[project.scripts]` console command `btm-<skill>`, and document its invocation as one shell binding, `R="env -u VIRTUAL_ENV uv run --project $(realpath <skill-root>/scripts) btm-<skill>"`, where `realpath` is required because uv resolves the project path lexically and an alias path such as `.claude/skills/<skill>/` has no workspace root among its lexical ancestors; a skill never invokes a host `python` and never a module path. Put logic shared across members once in the kernel package `btm-corekit` under `.corekit/`, declared as `dependencies = ["btm-corekit"]` with the source `btm-corekit = { workspace = true }`. Compose the kernel's gate mechanics (`SessionStore` creation and meta, `EventLog`, `Admission` with `Pool`, `read_batch` and `rejection`, `wire_pad` and `wire_clean`) and add only the member's record semantics; redefine no kernel symbol. Note in `compatibility` that the skill runs from a full repository checkout.</rule>
    <rule>Decode every shape that crosses a boundary with one pydantic model. Model a wire kind with variants as a union discriminated on its tag, a state file as a record, and an untrusted value as a refined alias (`Slug`, `Doi`, `Count`) rather than a bare `str` or `int`. Keep in the script only what a model cannot see: resolving a reference against live state, minting, and proving a cross-record link exists. Set `extra="forbid"` where the agent writes the file, so a typo is named, and `extra="ignore"` where another writer owns it. Subclass the kernel's `Model`, frozen and refusing unknown fields; pass `uv run mypy`, which runs strict over every member's `src/` with the pydantic plugin.</rule>
    <rule>Return every fix in one rejection: decode rows one at a time, and check the values of a malformed row that resolve against something outside it. Name the field to edit in each location (`findings[0].claim`) and attach the entry's schema fragment as the hint.</rule>
    <rule>Use three shapes and no fourth: a `Model` serialized with `dump` for a record parsed from or written to disk, a `TypedDict` for a view a command computes and indexes, and `dict[str, JSON]` for the document a command emits.</rule>
    <rule>Keep durable light state (backups, logs, resumable sessions) under `${XDG_STATE_HOME:-$HOME/.local/state}/btm-skills/<skill-name>/` (`%LOCALAPPDATA%\btm-skills\` on Windows) in purpose-named subdirectories (`backups/`, `logs/`, `sessions/`). Put heavy or regenerable artifacts (downloads, toolchains, caches, extractions) in temporary space under a directory named for its owner, as `/setup-env` prefixes its roots with `denv`. Write logs as JSONL, one timestamped record per line, capped at write time by trimming or one-step rotation. Ship a `clean` verb in every script that writes state: remove one target or `--all` and report the bytes freed.</rule>
    <rule>Keep mechanical, idempotent repairs in the script (e.g., delete a corrupt artifact on digest mismatch); leave judgment calls to the agent, informed by the script's diagnostics.</rule>
    <rule>Mark a network request's origin by one shared convention, first defined wins: `BTM_USER_AGENT`, sent verbatim as the User-Agent; else `BTM_CONTACT`, else the constant `skills@oss.joefang.org`, in the derived header `btm-skills/1.0 (<skill-name>; mailto:<contact>)`. Disclose the contact through polite request pools (an OpenAlex or Crossref `mailto` parameter) only from a contact-derived identity; mark a verbatim override with nothing else. Read the variables in the script alone; mention them in no skill text.</rule>
  </directives>

  <procedure for="distillation">
    <phase for="extraction">
      <step>Reconstruct the verified path exclusively from executed tool calls.</step>
      <step>Isolate points of failure, surprises, and backtracks for the Gotchas section.</step>
    </phase>
    <phase for="generalization">
      <step>Retain only the verified, successful path.</step>
      <step>Keep the why of a choice only where it changes a judgment call.</step>
      <step>Specify exact tools, flags, branches, and expected results for every step.</step>
      <step>Limit length to approximately 500 lines.</step>
      <step>Offload bulky reference data to sibling files.</step>
    </phase>
  </procedure>

  <checklist>
    <item>Directory is kebab-case; file is exactly `SKILL.md`.</item>
    <item>Frontmatter contains only Agent Skills spec fields in canonical order; `name` matches the directory; `description` is a `>-` folded block within 1024 characters following the capability-then-"Use when" form, leaves sibling routing to `## Redirects`, and leaves the library's descriptions under 7,000 characters in total; `metadata.argument-hint` matches the verbs, levels, and modes the body declares.</item>
    <item>Delegation, where the skill has any, goes through `/summon` with only the caller's own unit, record, rules, return shape, cap, and gate stated.</item>
    <item>Procedure strictly reflects the verified path with zero abandoned attempts.</item>
    <item>Project-specific values are parameterized or dynamically derived.</item>
    <item>Every step specifies exact tools, flags, and expected outputs.</item>
    <item>Examples and templates reside exclusively within XML blocks.</item>
    <item>Any bundled script hard-fails only on exact invariants; heuristic judgments surface as advisory signals, and no trust decision is silent.</item>
    <item>Any network-touching script resolves its request origin by the `BTM_USER_AGENT` / `BTM_CONTACT` / project-contact chain, and no `SKILL.md` mentions those variables.</item>
    <item>Every sentence carries a rule, condition, input, or example; a `/humanize` sweep finds no inflation vocabulary, wind-ups, or filler.</item>
    <item>Gotchas section contains non-obvious traps.</item>
    <item>No placeholder text remains outside intentional templates.</item>
    <item>Reproduction Test: the document text alone lets a fresh agent execute the procedure without external memory or clarifying questions.</item>
  </checklist>

  <directives for="output">
    <rule>Output the finalized SKILL.md file directly into the codebase or as a raw Markdown block.</rule>
    <rule>Omit all conversational filler, preambles, summaries, and concluding remarks.</rule>
  </directives>
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

* Apply changes only in `build` and `refactor`; keep every other verb read-only.
* Give the same verb the same contract in every persona; vary only the lens.
* In a read-only verb, name what is outside the lens and route it to the
  sibling skill in slash form.
* Dispatch by explicit verb, then by unambiguous request shape, then by the
  persona's declared default verb.
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
      <step>Regenerate the lockfile using the repository's native command: `make lock`.</step>
      <step>Commit both the manifest and the lockfile together.</step>
      Gotcha: editing the lockfile manually causes CI drift; regenerate it via the build tool.
    </after>
  </example>

  <example for="frontmatter-routing">
    <context>Writing trigger-based descriptions.</context>
    <before>This skill helps format python code using black and flake8.</before>
    <after>Formats and lints Python code with Black and Flake8. Use when asked to format Python, lint a file, or run either tool.</after>
  </example>

  <example for="parameterization">
    <context>Removing incidental project specifics.</context>
    <before>Run the build script located at `/users/joe/projects/manifold/scripts/build.sh`.</before>
    <after>Execute the build script located at `<repository-root>/scripts/build.sh`.</after>
  </example>

  <example for="xml-isolation">
    <context>Fencing reference material to prevent instruction bleed.</context>
    <before>
      Your config file should look like this:
      { "port": 8080 }
    </before>
    <after>
      Create the configuration file using this schema:
      <template for="config">
      { "port": 8080 }
      </template>
    </after>
  </example>
</examples>
