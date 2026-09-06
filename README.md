# SKILLs

A library of reusable [agent skills](https://agentskills.io): each skill is a
`SKILL.md` procedure an LLM coding agent loads and follows. Every skill is
project-agnostic (no hardcoded paths, names, or services) and self-contained
(one directory: `SKILL.md` plus optional reference files and scripts).

Install them with `npx skills`, as a Claude Code plugin, or as a git
submodule.

## Available skills

| Skill | Purpose |
| --- | --- |
| [advisor](advisor/SKILL.md) | Reads a research project like a principal investigator: what prior ideas it combines, which parts of its setup are outdated, what your lab can afford, and the cheapest experiment that proves or kills each claim. |
| [aesthete](aesthete/SKILL.md) | Designs, builds, and reviews web interfaces that meet WCAG 2.2, honor a supplied brand or design system, and avoid the templated look of generated UI. |
| [author-skill](author-skill/SKILL.md) | Turns a task history, workflow, or procedure into a reusable SKILL.md that another agent can follow with no memory of the original session. |
| [caveman](caveman/SKILL.md) | Compresses replies into terse phrasing that keeps every technical fact, and can rewrite a prose file in place. |
| [fact-check](fact-check/SKILL.md) | Checks a document claim by claim against retrieved sources, quotes the evidence behind every verdict, and changes nothing until you approve each correction. |
| [git-commit](git-commit/SKILL.md) | Drafts and reviews Conventional Commits messages, and can commit and push in one step. |
| [humanize](humanize/SKILL.md) | Rewrites AI-sounding prose so it reads like its writer, keeping every claim's original strength. |
| [lit-review](lit-review/SKILL.md) | Produces a literature review in which every citation traces to a paper retrieved from OpenAlex, arXiv, or Crossref, never memory. |
| [peer-review](peer-review/SKILL.md) | Reviews a paper the way an adverse referee would, pressing on claims, design, analysis, limitations, and novelty. |
| [pl-theorist](pl-theorist/SKILL.md) | Brings a programming-languages theorist's discipline to design, code, review, and tests, tuned per language. |
| [ponder](ponder/SKILL.md) | Answers an open question and shows its work, sourcing every load-bearing claim and testing the strongest rival explanation. |
| [ponytail](ponytail/SKILL.md) | Forces the laziest solution that works: standard library and native features before custom code or new dependencies. |
| [read-pdf](read-pdf/SKILL.md) | Extracts text and metadata from a PDF and answers questions about it with page-cited evidence, without OCR. |
| [reframe](reframe/SKILL.md) | Turns a design or planning discussion into a testable direction judgment with costed routes and evidence that could prove it wrong. |
| [search-web](search-web/SKILL.md) | Searches the web, Wikipedia, and the scholarly record for an agent whose harness has no search tool, and pulls the readable text out of a page. |
| [setup-env](setup-env/SKILL.md) | Provisions a project's development toolchain in userspace, with no sudo, no docker, and nothing assumed present but uv. |
| [summon](summon/SKILL.md) | Hands work to another agent: whether to delegate at all, what the delegate must be told, how to keep parallel agents off each other's ground, and how to judge what comes back. |
| [thematic-analysis](thematic-analysis/SKILL.md) | Develops themes from qualitative text under one named school, backing each theme with verbatim extracts and counts, with defaults tuned for feedback and ticket data. |

## Installing

### With a skills manager

Install every skill, or pick individual ones, into whichever agents you use:

```bash
npx skills add BTreeMap/SKILLs --all
npx skills add BTreeMap/SKILLs --skill fact-check --skill git-commit
```

### As a Claude Code plugin

```bash
claude plugin marketplace add BTreeMap/SKILLs
claude plugin install btm-skills@btm-skills
```

### As a git submodule

Pins an exact commit and updates on your schedule; the bundled sync workflow
below automates the update. Add the library at `.github/skills` and alias it
for Claude:

```bash
(
  set -eu
  if git submodule status -- .github/skills >/dev/null 2>&1; then
    echo "Already recorded: repairing the checkout to the recorded pointer."
    git submodule update --init -- .github/skills
  else
    echo "Adding the skills submodule."
    git submodule add https://github.com/BTreeMap/SKILLs.git .github/skills
  fi
  mkdir -p .claude
  ln -sfn ../.github/skills .claude/skills
  git add -- .gitmodules .claude/skills .github/skills
  if git diff --cached --quiet -- .gitmodules .claude/skills .github/skills; then
    echo "Already up to date."
  else
    git commit -m "chore: Add agent skills submodule" \
      -- .gitmodules .claude/skills .github/skills
  fi
)
```

The block is safe to re-run; advancing the recorded pointer is a separate
step (see Staying current).

Clone consuming projects with submodules included:

```bash
git clone --recurse-submodules <your-repo-url>
# or, on an existing checkout:
git submodule update --init --recursive
```

## Staying current

### Manually

This route needs neither a third-party action nor extra permissions:

```bash
git submodule update --remote -- .github/skills
git commit -m "chore(skills): Bump skills submodule" -- .github/skills
```

### Automatically

The bundled workflow fast-forwards the `.github/skills` pointer to the
upstream tip twice a day, one commit per configured branch (default: `main`,
`master`, `dev`):

```bash
(
  set -eu
  mkdir -p .github/workflows
  if [ ! -e .github/workflows/sync-skills.yml ]; then
    echo "Installing the sync workflow."
    cp .github/skills/sync-skills.example.yml .github/workflows/sync-skills.yml
  elif ! cmp -s .github/skills/sync-skills.example.yml \
      .github/workflows/sync-skills.yml; then
    echo "sync-skills.yml differs from the bundled example; leaving it as is." >&2
  fi
  git add -- .github/workflows/sync-skills.yml
  if git diff --cached --quiet -- .github/workflows/sync-skills.yml; then
    echo "Already up to date."
  else
    git commit -m "chore: Enable agent skills auto-sync workflow" \
      -- .github/workflows/sync-skills.yml
  fi
)
```

Copy the workflow in as a real file: GitHub Actions silently ignores
symlinked files under `.github/workflows`.

The workflow is third-party code running with `contents: write`. Its
containment:

* The jobs skip cloning and checkout entirely, so no submodule code and no
  git hook runs.
* The token is split across two jobs: a read-only job decides what to bump, a
  `contents: write` job only creates the commit and moves the ref.
* Commits go through the Git Data API with no author, committer, or signature
  field, the documented condition under which GitHub signs a bot commit with
  its own key. The bumps therefore satisfy a `Require signed commits` ruleset
  with no stored key or bypass actor.
* The upstream is whatever URL the branch records for the gitlink, so a fork
  with the same layout works unchanged; `upstream-url` and `upstream-ref`
  inputs override it.

If your organization restricts third-party actions, allowlist
`BTreeMap/SKILLs/.github/workflows/sync-skills.yml@main`.

## Repository layout

```text
<skill-name>/SKILL.md          canonical; one directory per skill
skills/<skill-name>            vendor-neutral hub; one symlink per skill
.github/skills -> ../skills    GitHub Copilot, and the submodule mount
.claude/skills -> ../skills    Claude Code
.claude-plugin/                plugin and marketplace manifests
```

Every vendor path is one symlink to `skills/`, so another agent costs one
link. Edit skills at the root and keep every alias a symlink. The CI gate
writes and prunes the aliases and regenerates the skill list in
`marketplace.json`, the address installers resolve each skill by.

Git preserves symlinks on Linux and macOS; on Windows, enable Developer Mode or
configure Git to create symlinks before cloning.

## Contributing

Conventions, the CI gate, and the frontmatter protocol live in
[AGENTS.md](AGENTS.md); the authoring procedure is
[author-skill](author-skill/SKILL.md). CI repairs mechanical findings
(formatting, ordering, aliases) on every push and fails only on what needs a
person.

## License

[MIT](LICENSE)
