# NeuroGlyph User Guide — v3.7‑Aligned Examples & Patterns

> **Version:** 2025-11-08  
> **Alignment:** Conforms to *NeuroGlyph — Complete Specification & Usage Manual (v3.7+)*.  
> **Scope:** Quick patterns for research, creative work, persistent tasks, analogy making, meta‑dialogue, and audiovisual turns.

---

## 1) Quick‑Start Conversation (Research)

🚀 **/act**:seed  
👁️ **/focus**:"weak measurement"  
🧭 **/context**:"quantum foundations"  
🤝 **/mind**:Mirco ↔ (Agent, Audience)  
🧠 **/intent**:"evoke conceptual responses"  
🔍 **/zoom**:in  
📦 **/deliverable**:discourse_update

**Interpretation:** Launch a focused discussion addressed to both an agent and a broader audience.

> **Spec refs:** core tokens `/act, /focus, /context, /mind, /intent, /zoom, /deliverable` (Sec. 2.1); deliverable `discourse_update` (Sec. 6.5).

---

## 2) Creative Co‑Writing Session (Collective)

👥 **/collective**:"WritersRoom"  
🤝 **/mind**:[Ann; Ben; Story‑Master]  
🚀 **/act**:begin_story  
👁️ **/focus**:"The Last Sunstone"  
🎨 **/palette**:"High fantasy, melancholic, autumnal"  
🗺️ **/setting**:"The Whispering Valley"  
🏗️ **/structure**:"Five‑act tragedy"  
📦 **/deliverable**:world_bible

**Turn 2 — Ann introduces a character**  
🚀 **/act**:introduce_character  
🎭 **/character**:(  
  /name:"Kaelen";  
  /description:"Old cartographer haunted by an unfinished map";  
  /goal:"Find the Sunstone to see his wife again"  
)  
📦 **/deliverable**:character_sheet

> **Spec refs:** `/collective` team id and `/mind` participants (Sec. 2.1); creative tokens `/palette, /setting, /structure, /character` and deliverables `world_bible, character_sheet` (Sec. 5.1–5.2).

---

## 3) Open‑Ended Philosophical Dialogue

🚀 **/act**:begin_dialogue  
💬 **/channel**:dialogue  
👁️ **/focus**:"Consciousness in AI"  
❓ **/query**:"Is phenomenal consciousness a byproduct of complexity, or does it require biology?"  
📦 **/deliverable**:discourse_update

**Agent follow‑up (dialectic form):**  
🚀 **/act**:continue_dialogue  
♊ **/dialectic**:(  
  📝 /note:"Thesis — IIT: consciousness arises with high information integration." ;  
  📝 /note:"Antithesis — Searle: biological naturalism ties it to neurons." ;  
  ❓ /query:"Could a simulation instantiate real qualia?"  
)  
📦 **/deliverable**:discourse_update

> **Spec refs:** `/channel, /query` (Sec. 6.1); `/dialectic` (Sec. 6.3); `/note` (Sec. 2.1); `discourse_update` (Sec. 6.5).

---

## 4) Persistent, Triggered Project (Book Writing)

🚀 **/act**:write_novel **… /ongoing**  
🤝 **/mind**:User ↔ Gemini  
👁️ **/focus**:"The Last Signal"  
🎨 **/palette**:"Solarpunk, hopeful"  
🏗️ **/structure**:"Episodic"  
⚡ **/trigger**:"on character_complete → 🚀 contact_user"  
📦 **/deliverable**:decision_record

**Trigger fires later:**  
🚀 **/act**:contact_user  
⚡ **/trigger**:character_complete  
🎭 **/character**:( /name:"Dr. Aris Thorne"; /description:"Bioengineer in underground arboretum"; /goal:"Protect atmospheric balance" )  
❓ **/query**:"Introduce Aris as ally or antagonist?"  
📦 **/deliverable**:narrative_beat

> **Spec refs:** `… /ongoing` (Sec. 6.2); `/trigger` (Sec. 2.2); creative deliverables (Sec. 5.2).

---

## 5) Structural Analogy Project

🚀 **/act**:find_analogy  
🧱 **/compose**:(  
  /task_A:( 🤝:MusicAI; 🚀 /act:analyze_domain; 👁️:"J.S. Bach's fugues"; 🧠 /intent:"formal"; 🔍:"Extract principles of theme, inversion, resolution"; 📦:formal_model );  
  /task_B:( 🤝:MathAI;  🚀 /act:analyze_domain; 👁️:"Proofs by induction";     🧠 /intent:"formal"; 🔍:"Base case, recursion, closure";              📦:formal_model )  
)  
🔀 **/bridge**:"Map musical to mathematical"  
♊ **/dialectic**:"Synthesize principle of layered progression"  
📦 **/deliverable**:analogical_map

> **Spec refs:** `/compose, /bridge, /dialectic` (Secs. 2.1, 6.3); `/intent` must be 🧠 (Sec. 2.1); `analogical_map` (Sec. 6.5).

---

## 6) Meta‑Dialogue and Self‑Modifying Tasks

🚀 **/act**:review_conversation  
🧾 **/source**:previous_dialogue_block  
🧠🧠 **/meta**:"Is this chain of queries coherent?"  
🔬 **/introspect**:"Detect scope mismatches between /focus and /intent"  
📦 **/deliverable**:discourse_update

**Agent transforms prior block:**  
🧪 **/transform**:(  
  /operation:"clarify intent ↔ focus mismatch";  
  /output:"Insert 🧠 /intent blocks to disambiguate scope."  
)  
📦 **/deliverable**:improved_query_stack

> **Spec refs:** meta‑layer `/meta, /source, /transform, /introspect` (Sec. 6.4); deliverables `discourse_update, improved_query_stack` (Sec. 6.5).

---

## 7) Visual & Sonic Conversations

🚀 **/act**:compose_piece  
🎼 **/motif**:"5‑note ascending melody"  
🎨 **/palette**:"Minimalist, music box + felt piano"  
📦 **/deliverable**:score_fragment

> **Spec refs:** creative tokens and deliverables (Sec. 5.1–5.2).

---

## 8) Summary Table — Dialogue Patterns

| Use Case                | Core Tokens                                           | Deliverables                                |
|-------------------------|--------------------------------------------------------|---------------------------------------------|
| Creative writing        | 🎨, 🎭, 🗺️, ↪️, 🧠, 👥, 🤝                            | world_bible, character_sheet, narrative_beat |
| Research & debate       | 👁️, ❓, 🧠, 💬, ♊, 📝                                 | discourse_update, analogical_map            |
| Persistent task         | …, ⚡, 🚀, 👁️, 🧠                                    | decision_record, narrative_beat             |
| Analogy mapping         | 🧱, 🔀, ♊, 🧠                                         | analogical_map                              |
| Meta‑programming        | 🧠🧠, 🧪, 🧾, 🔬                                      | improved_query_stack, transformed_code      |
| Audio/visual composition| 🎼, 🎨, 🚀                                            | score_fragment                              |

---

## 9) Compliance Checklist (v3.7)

- ✅ Use **🧠 /intent** (not 🎓) for purpose declarations.  
- ✅ Use **👥 /collective** for team id; use **🤝 /mind** for participant lists.  
- ✅ Prefer **♊ /dialectic** instead of ad‑hoc tokens like `💭` or `/thesis` in protocol blocks.  
- ✅ Use **⚡ /trigger** for both declarations and fired events; avoid `/trigger_condition`.  
- ✅ Deliverables must be among spec’s sets (Secs. 4, 5.2, 6.5) or clearly labeled as extensions.  
- ✅ Advanced modes: `/channel, /query, … /ongoing, 🔀 /bridge, 🔬 /introspect, 🧠🧠 /meta` per Sec. 6.*.

---

### Ready to Play

1) Paste the NeuroGlyph Spec v3.7+.  
2) Paste this v3.7‑aligned User Guide.  
3) Start with a 🚀 **/act** followed by **🧭 /context** and **🤝 /mind**.
