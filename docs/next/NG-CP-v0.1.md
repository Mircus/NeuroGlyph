# NG‑CP v0.1 — NeuroGlyph Creative Profile (Film/Game/TV)

> **Status:** Draft profile · 2025-11-08  
> **Compatible with:** NG‑spec 4.0 (nested threads, groups, events, policy/budget, macros)  
> **Goal:** Minimal domain tokens for film‑grade workflows without breaking NG portability (namespaced tokens only).

---

## 1. Namespaces

- `/film.*` — story, scene/shot, camera, edit timeline
- `/vfx.*` — plates, tasks, comps, renders
- `/music.*` — cues, stems, spotting, mix
- `/sound.*` — dialogue, ADR, Foley, M&E
- `/review.*` — sessions, pins/notes, signoffs
- `/asset.*` — registration, versioning, hashes, lineage
- `/sched.*` — calendars, call sheets, dependencies
- `/budget.*` — line items, reports (extends NG `/budget`)
- `/rights.*` — licenses, releases, credit rules

> Engines that don't recognize these tokens MUST preserve them verbatim per NG 4.0 (§8.3).

---

## 2. Canonical Token Definitions (Minimal)

### 2.1 Story & Breakdown
```text
/film.story( /title, /logline, /series?, /episode? )

/film.scene(
  /id, /slug, /pages:float, /location, /cast:[...],
  /script_ref?, /notes?
)

/film.shot(
  /id, /type, /cam, /lens, /fps:int, /tc:"HH:MM:SS:FF",
  /description?, /plate?:bool, /vfx?:bool, /notes?
)
```
**Deliverables:** `shotlist`, `scene_breakdown`

### 2.2 Asset Graph & Provenance
```text
/asset.register(
  /urn, /kind, /hash, /src,
  /parents:[urns]?, /tags:[...]?, /owner?
)
```
**Deliverables:** `asset_card`, `asset_catalog`

### 2.3 Editorial / Timeline
```text
/film.edit.timeline( /id, /rate, /aspect, /working_color?, /display_color?, /tracks:[{ /v | /a }] )

/film.edit.clip(
  /track, /src, /in:"TC", /out:"TC", /pos:"TC",
  /xfer?:"straight|dissolve|wipe", /note?
)
```
**Deliverables:** `edit_sequence`, `otio_export`

### 2.4 VFX Tasks & Renders
```text
/vfx.task( /shot, /vendor?, /stage:"prep|matchmove|comp|fx|paint", /notes? )
/vfx.render( /shot, /farm, /params:{ res, color, frames } )
```
**Events:** `render/queued|done|failed`, `shot/assigned|ready|approved`

### 2.5 Music & Sound
```text
/music.cue( /id, /scene, /mood, /tempo:int, /palette, /stem:[...] )
/sound.adr( /scene, /char, /lang, /status:"queued|recorded|approved" )
```

### 2.6 Review & Approvals
```text
/review.session( /target:"scene|shot|cut", /stage, /moderator? )
/review.pin( /target, /tc, /note, /by )
/review.signoff( /scope, /stage, /by:[...] )
```
**Deliverables:** `dailies_report`, `approval_record`

### 2.7 Scheduling & Budget
```text
/sched.call( /day:"YYYY-MM-DD", /unit, /scene:[...], /calltime, /wrap, /dept:[...] )
/budget.line( /code, /est:number, /actual:number?, /note? )
/budget.report( /period )
```

### 2.8 Rights & Compliance
```text
/rights.license( /asset, /terms:{ territory, media, term }, /owner, /proof )
/rights.release( /person, /scene:[...], /status:"pending|signed" )
```
**Policies:** safety/union/credit guards via NG `/policy`.

---

## 3. Event Topics (Canonical)

- `shot/assigned`, `shot/ready`, `shot/approved`
- `plate/ingested`, `render/queued|done|failed`
- `review/note`, `edit/locked`, `music/cue/approved`
- `rights/cleared`, `schedule/updated`, `budget/overrun`

> MUST include `/data` payload with minimal identifiers (shot id, cut id, etc.).

---

## 4. Baseline Invariants (MUST)

- **Timecode:** `tc` is absolute source TC; `rate` given per timeline; declare drop/non‑drop where relevant.
- **Color:** timeline declares `working_color` and `display_color` (e.g., `ACEScg → Rec.709`).
- **Asset URNs:** `urn:ng:asset:<category>/<name>@vN`; every media reference SHOULD include a hash.
- **Approvals:** `/review.signoff` must include identities and timestamps (engine attaches canonical metadata).
- **Reproducibility:** `/vfx.render` declares params; engine logs tool versions for audit.
- **Privacy & Safety:** redaction defaults on export; policy gates for stunts, minors, and sensitive locations.

---

## 5. Mapping to NG 4.0

- Threads: `project/sequence/scene/shot` via `/thread`.
- Departments: `/group` roles + `/route` delivery.
- Provenance: `/ref` & `/quote` pull prior notes into new reviews.
- Events: unified `/event` + `/on` handlers.
- Policy/Budget: NG `/policy` and `/budget` to enforce limits & guardrails.
- Macros: reusable flows for dailies, VFX turnover, edit lock.

---

## 6. Interop (Non‑normative)

- **OTIO/EDL/AAF:** engines SHOULD support at least OTIO export for `edit_sequence` deliverables.
- **Renders:** farm adapters MAY map `/vfx.render` to Deadline/AWS Thinkbox/etc.
- **Sheets:** `/sched.call` MAY round‑trip to Google Sheets/Excel via adapters.

---

## 7. Test Matrix

- Story/scene/shot → shotlist
- Dailies review → report with pins
- VFX turnover → tasks + render event
- Music cue → approval flow
- Edit clips → export OTIO
- Rights/license → policy gate
- Budget variance → warning event

---

## 8. License

Open profile under permissive spec license. Vendors MAY add namespaced extensions.
