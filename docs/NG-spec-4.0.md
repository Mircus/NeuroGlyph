# NeuroGlyph Specification — Version 4.0

> **Status:** Stable Draft · 2025-11-08  
> **Scope:** Extends v3.7 with **Nested Conversations**, **Self‑Reference**, **Conversation Groups**, and a unified **Event/Policy/Budget** model.  
> **Audience:** Implementers of NeuroGlyph runtimes, agent frameworks, and tooling.

---

## 0. Conformance & RFC Keywords

- The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.
- A NeuroGlyph **engine** is any program that parses NeuroGlyph tokens and executes/mediates actions among human/AI agents.
- A **transcript** is an ordered set of NeuroGlyph **blocks** (message turns) and **events**.

---

## 1. Overview (What Changed Since v3.7)

v4.0 is a conservative extension of v3.7. All valid v3.7 transcripts remain valid, with these additions:

1) **Nested Conversations**: hierarchical threads with controlled inheritance and merge semantics.  
2) **Self‑Reference**: first‑class access to prior blocks, partial ranges, and token‑level transforms.  
3) **Conversation Groups**: multi‑party orchestration with roles, permissions, routing, and consensus deliverables.  
4) **Unified Events**: typed, addressable events with topic routing and durable handlers.  
5) **Policy & Budget**: portable guardrails and resource caps declarable in‑line.  
6) **Namespaces & Macros**: vendor extensions and reusable templates without breaking portability.

> Migration: No token is removed. A few are **deprecated** in favor of unified forms (see §14).

---

## 2. Core Model (Recap + Additions)

A NeuroGlyph **block** is a set of tokens (slash‑prefixed commands) producing **effects** and optionally a **deliverable**.

**Existing core tokens (v3.7, still valid):**  
`/act, /focus, /context, /mind, /intent, /zoom, /deliverable, /collective, /channel, /query, /dialectic, /note, /trigger, /meta, /transform, /introspect, /bridge, /source`

**New core tokens (v4.0):**  
- **/thread** — create/enter/manage nested threads (§3)  
- **/merge** — merge threads or ranges (§3.4)  
- **/self** — self‑reference the current block (§4)  
- **/ref** — reference prior content by address (§4)  
- **/quote** — quote ranges with provenance (§4)  
- **/group** — create/modify conversation groups (§5)  
- **/route** — direct a block to targets (members, roles, agents) (§5.3)  
- **/event** — declare/emit typed events (§6)  
- **/on** — subscribe handlers to events (§6)  
- **/policy** — attach guardrails/constraints (§7)  
- **/budget** — declare resource limits (time/tokens/tools) (§7)  
- **/macro** — define reusable block templates (§8)  
- **/use** — expand a macro with arguments (§8)  
- **/var, /let** — set and bind named values (§8)  
- **/trace** — toggle or scope transcript tracing/redaction (§9)

> Engines SHOULD surface friendly errors for unknown tokens and MUST preserve tokens verbatim for transparency.

---

## 3. Nested Conversations

### 3.1 Thread Fundamentals

Each block belongs to a **thread** identified by a path‑like **thread id** (e.g., `main`, `paper/figures`, `main/research/hypothesis`).  
Threads form a rooted tree. By default, all blocks go to `main`.

- **/thread** MAY create a new thread and/or enter it:
```text
/thread(
  /id:"paper/analysis",
  /parent:"paper",
  /mode:"inherit"   # or "isolate"
  /enter:true
)
```
- **/mode** determines **context inheritance**:  
  - `"inherit"` (default): child sees parent `/context`, `/mind`, `/policy` (read‑only unless overridden).  
  - `"isolate"`: child starts with a minimal context; explicit imports via `/ref` or `/policy(import:...)`.

### 3.2 Enter / Exit

```text
/thread(/enter:true, /id:"paper/analysis")
# ... work inside child ...
/thread(/enter:false)  # exit to parent
```

Entering without `/id` means “re‑enter the last child of the current thread” (SHOULD be supported).

### 3.3 Thread Properties

```text
/thread(
  /id:"exp/A",
  /tags:["exploration","draft"],
  /owners:["Mirco","Agent-R"],
  /visibility:"group"    # "private" | "group" | "public"
)
```

### 3.4 Merging Threads

```text
/merge(
  /from:"paper/analysis",
  /into:"paper",
  /strategy:"reconcile",   # "append" | "squash" | "reconcile"
  /conflict:"annotate"     # "fail" | "take_from" | "take_into" | "annotate"
)
/deliverable:merge_plan
```

- **append**: linearize blocks after `/into` tail.  
- **squash**: summarize `/from` into a single composite block.  
- **reconcile**: structured diff + integration per token type.  
- On conflicts, **annotate** MUST produce an explicit diff with `/quote` ranges.

---

## 4. Self‑Reference & Content Addressing

### 4.1 Addresses

Any block/range MAY be addressed as:
```
thread:path#bNN..bMM/tokens[k..l]
```
- `bNN` = block index within the thread (1‑based).  
- `tokens[k..l]` = inclusive token slice in that block.

### 4.2 Referencing

```text
/ref(
  /target:"paper/analysis#b3..b6",
  /as:"prior_findings"
)
/quote(/target:"paper#b12/tokens[3..7]")
```

- `/ref` binds a **symbolic handle** for later use in the same block.  
- `/quote` injects literal content (engine SHOULD add provenance).

### 4.3 Self Block Handle

```text
/self(/as:"this")
/transform(
  /source:@this,
  /operation:"normalize dialectic notes → bullets"
)
```

- `@this` is a reserved handle produced by `/self`.

### 4.4 Transform Semantics

- Transforms MUST be **pure** (no side‑effects) and produce explicit outputs (e.g., updated `/note`, synthesized `/deliverable`).  
- Engines SHOULD support a “dry‑run” flag for `/transform` via `/policy(simulate:true)`.

---

## 5. Conversation Groups

### 5.1 Declaration

```text
/group(
  /id:"Pisa-Demo",
  /members:["Mirco","Agent-A","Agent-B"],
  /roles:{ "Owner":["Mirco"], "Analyst":["Agent-A"], "Scribe":["Agent-B"] },
  /perm:{ "Owner":"all", "Analyst":["act","transform"], "Scribe":["note","deliver"] }
)
```

- Membership and roles are **stateful**; engines MUST persist group state across turns.

### 5.2 Consensus Patterns

Deliverables for groups:
- `group_decision`, `consensus_record`, `vote_tally`, `assignment_plan`

```text
/dialectic(
  /note:"Option A: fast demo",
  /note:"Option B: thorough analysis"
)
/act:call_vote
/deliverable:vote_tally
```

### 5.3 Routing

```text
/route(
  /to:"role:Analyst",      # "member:<name>" | "role:<role>" | "group:<id>" | "agent:<id>"
  /cc:["role:Scribe"],
  /mode:"multicast"        # "broadcast" | "multicast" | "dm"
)
```

- Engines MUST enforce `/perm` before delivering routed blocks.

---

## 6. Unified Events

### 6.1 Emit & Subscribe

```text
/event(
  /topic:"character_complete",
  /data:{ "name":"Aris Thorne" },
  /scope:"thread"    # "thread" | "group" | "global"
)

/on(
  /topic:"character_complete",
  /handler:"notify_user",
  /where:"thread:paper",
  /once:false
)
```

- Topics are strings, SHOULD use `kebab-case`.  
- `/scope` constrains delivery domain; engines MUST honor it.  
- Handlers are named actions resolvable by the engine runtime.

### 6.2 Event Ordering

- Events are **totally ordered per thread** and **causally ordered** across threads.  
- Engines MUST attach **monotonic ids**: `evt-<ts>-<seq>`.

---

## 7. Policy & Budget

```text
/policy(
  /safety:"strict",
  /guard:[
    "no PII exfiltration",
    "cite sources for medical claims"
  ],
  /import:["parent.policy"],     # import parent policy bundle
  /simulate:false
)
/budget(
  /time:"2m",
  /tokens:8000,
  /tools:{ "web.search":5, "code.run":2 }
)
```

- Policies are **advisory or enforced** depending on engine configuration.  
- Budgets are soft caps by default; `/policy(enforce_budgets:true)` makes them hard caps.

---

## 8. Macros, Variables, Namespaces

### 8.1 Macros

```text
/macro(
  /name:"debate",
  /params:["topic"],
  /body:(
    /channel:dialogue
    /query:@topic
    /dialectic(
      /note:"Thesis …",
      /note:"Antithesis …"
    )
  )
)
/use("debate", "Quantum causality")
```

### 8.2 Variables

```text
/let theme:"Layered progression"
/var k:5
/note:"Repeat @theme exactly @k times in examples."
```

### 8.3 Namespaces

- Vendor tokens MUST use **prefix form**: `/x-acme.plan`, `/x-labs.guard`.  
- Engines MUST preserve unknown namespaced tokens verbatim.

---

## 9. Trace & Redaction

```text
/trace(
  /level:"full",     # "off" | "summary" | "full"
  /redact:["PII","secrets"],
  /scope:"thread:paper/analysis"
)
```

- Redaction rules apply to stored transcripts and `/quote` outputs.  
- Engines SHOULD watermark redacted blocks.

---

## 10. Semantics (Formal Outline)

Let **C** be a conversation graph: `(T, E)` where `T` are threads, `E` are edges “parent-of”.  
A block **B** evaluates to `(State', Deliverable?, Events*)` under environment `Γ` (context, mind, policy, budget).

- **Thread Enter** creates a child environment `Γ_child` with inheritance per `/mode`.  
- **Merge** defines a partial function `μ : Transcript_from × Transcript_into → Transcript_into` parameterized by strategy.  
- **Ref/Quote** are pure; they read from the immutable **canonical transcript** view per `/trace`.  
- **Policy/Budget** extend `Γ` with constraints checked pre‑ and post‑evaluation.  
- **Events** deliver to subscribers with scope‑constrained visibility; handlers are evaluated like `/act` with `evt` bound.

Temporal assertions (CTL‑like) MAY be applied per thread:  
```
AG (¬ unsafe)       # always safe
EF decision_made    # eventually decision made
A[ request U response ]
```

---

## 11. Grammar (ABNF Sketch)

```
block        = *( token LF ) [ deliverable LF ]
token        = "/" name [ ":" value ] [ "(" fields ")" ]
name         = 1*( ALPHA / DIGIT / "-" / "_" )
fields       = *( field )
field        = LWSP "/" name ":" value ["," / LF]
value        = quoted / scalar / object / array / symbol
quoted       = DQUOTE *CHAR DQUOTE
symbol       = "@" name
deliverable  = "/deliverable" ":" name
LF           = %x0A
```

This grammar is permissive; engines MAY support richer JSON‑like values for `object`/`array`.

---

## 12. Standard Deliverables (v4 Additions)

- `merge_plan` — structured diff of a merge (§3.4)  
- `group_decision`, `consensus_record`, `vote_tally`, `assignment_plan` (§5.2)  
- `protocol_trace` — detailed execution trace for audits (§9)

All v3.7 deliverables remain valid.

---

## 13. Canonical Examples

### 13.1 Nested Research Workflow

```text
# main thread
/act:seed
/focus:"Weak values → operator paths"
/context:"Quantum semantics project"
/mind:["Mirco","Agent-Q"]
/intent:"formalize QOPS example"
/deliverable:discourse_update

# fork analysis
/thread(/id:"qops/analysis", /parent:"main", /mode:"inherit", /enter:true)
/act:derive
/note:"Compute simple path-space weak value"
/deliverable:discourse_update

# quote back into main
/thread(/enter:false)
/ref(/target:"qops/analysis#b1", /as:"ana")
/quote(/target:@ana)
/deliverable:discourse_update
```

### 13.2 Group Vote With Budget & Policy

```text
/group(/id:"Pisa-Demo", /members:["Mirco","Agent-A","Agent-B"])
/policy(/safety:"strict", /guard:["no PII"], /enforce_budgets:true)
/budget(/time:"1m", /tokens:2000)

/route(/to:"group:Pisa-Demo", /mode:"broadcast")
/dialectic(
  /note:"Option A: Live demo",
  /note:"Option B: Recorded walkthrough"
)
/act:call_vote
/deliverable:vote_tally
```

### 13.3 Events & Handlers Across Threads

```text
/thread(/id:"novel/char", /parent:"novel", /enter:true)
/act:create_character
/character:(/name:"Aris Thorne", /goal:"Protect atmosphere")
/event(/topic:"character_complete", /data:{"name":"Aris Thorne"}, /scope:"group")

# elsewhere
/on(/topic:"character_complete", /handler:"notify_user", /where:"group:WritersRoom")
```

---

## 14. Backward Compatibility & Deprecations

- `/trigger_condition` **DEPRECATED** → use `/event` + `/on` (v4 unified events).  
- Ad‑hoc tokens for thesis/antithesis **DEPRECATED** → use `/dialectic` with `/note` and `/query`.  
- `/collective_mind` **DEPRECATED** → use `/group` + `/mind`.

Engines SHOULD accept the deprecated forms but MUST emit warnings.

---

## 15. Security & Governance

- **Policy bundles** MAY reference external signed profiles.  
- **Trace redaction** MUST be applied before external export.  
- **Role/Perm checks** MUST gate `/route` deliveries and `/merge` affecting threads owned by others.

---

## 16. Versioning & Negotiation

```text
/version:"4.0"     # explicit declaration
```
- Engines MAY respond with `/version:"3.7"` and fall back to shared subset.  
- A transcript without `/version` is assumed compatible with the engine’s default (SHOULD be ≥ 3.7).

---

## 17. Test Matrix (Implementers)

- Create/enter/exit nested threads (inherit vs isolate).  
- Merge strategies and conflict annotation.  
- Self‑reference addresses, quoting slices.  
- Group routing with role/perm enforcement.  
- Event emission/handling across scopes.  
- Policy/budget enforcement and redaction.  
- Macro expansion with variables and namespace preservation.

---

## 18. License

This specification is available under a permissive open specification license. Vendors MAY implement compatible supersets via namespaced extensions.
