# NeuroGlyph Cognitive Virtual Machine (NG-CVM) — Operational Specification v1.1

---

### 🧠 Purpose
The Cognitive Virtual Machine for NeuroGlyph (NG-CVM) is a conceptual and operational architecture that maps expressions in NeuroGlyph language (NG) into cognitive states, agent actions, and computable relational structures. It enables interaction between humans and agents in conversational, project-based, and epistemic environments.

---

### 🧾 1. Logical Structure of an NG Act

Each NeuroGlyph sentence is interpreted as a **relational cognitive act**:

```python
NG_ACT := {
  "act": <action_type>,         # e.g., "reflect", "compare", "seed"
  "focus": <conceptual_object>,
  "participants": [<mind_spec>],
  "intent": <cognitive_intention>,
  "context": <temporal/situational anchors>,
  "output": [<deliverable>],
  "network": <cognitive_network>,
  "gliph": <evocative_symbol>
}
```

---

### 🌐 2. Gliph Semantics

| Gliph         | Semantic Effect         | Description                         |
|---------------|--------------------------|-------------------------------------|
| `/act:`       | cognitive act type       | generates action plan               |
| `/focus:`     | semantic node            | directs agent attention             |
| `/mind:`      | actor relation topology  | defines interaction topology        |
| `/intent:`    | dialogic purpose         | drives planning and memory          |
| `/context:`   | temporal/spatial anchor  | enables memory binding              |
| `/gliph:`     | symbolic invocation      | triggers evocative modules          |
| `/deliverable:` | expected output        | generates artifacts                 |
| `/chain:`     | semantic branching       | creates subtasks or derivations     |
| `/network:`   | semantic linkage         | connects threads and sessions       |

---

### 🤖 3. Agent Operational Cycle

```python
def interpret_ng_act(ng_act):
    agent_state.update_context(ng_act["context"])
    goal = planner.generate_goal(ng_act["intent"], ng_act["focus"])
    plan = planner.plan(goal, ng_act["act"])
    result = executor.execute(plan)
    if "deliverable" in ng_act:
        result = formatter.format(result, ng_act["output"])
    return result
```

---

### 🧠 4. Agent Cognitive State Structure

```python
AgentState := {
  "role": "relational philosopher",
  "active_focus": "origin of reciprocity",
  "context_buffer": [...],
  "intent_buffer": [...],
  "deliverable_log": [...],
  "dialogue_memory": [...],
  "cognitive_graph": ConceptGraph(...)
}
```

---

### 🔁 5. Relational Routing via `/mind:`

| Form               | Relation Type | Operational Effect        |
|--------------------|---------------|----------------------------|
| `human ↔ agent`     | dialogic      | co-generation              |
| `agent_A ↔ agent_B` | inter-agent   | autonomous dialogue        |
| `human ⊕ agent`     | cooperation   | shared task                |
| `agent ← human`     | instruction   | learning phase             |
| `human ← agent`     | tutoring      | explanation                |

---

### ⚙️ 6. Composition and Persistence

- `/chain:` spawns **semantic branches** within current scene
- `/network:` links acts, dialogues, and projects into a **cognitive thread**
- `/context:` allows **memory recall or anchoring to prior episodes**

---

### 🔄 7. Output and Artifact Generation

Deliverables include:
- `symbolic_map`: visual conceptual networks
- `annotated_dialogue`: semantically tagged logs
- `gliph_extension`: symbolic generation
- `concept_thread`: traceable argument lines

---

### 🧠 8. Modal Extension (NG-MODEX)

> Extension of NG-CVM for representing beliefs, intentions, desires, duties, and knowledge

#### 🧾 New Modal Gliphs

| Gliph             | Logical Semantics       | Meaning                         |
|------------------|--------------------------|----------------------------------|
| `/modal:believe` | `□_A φ`                  | agent believes φ                |
| `/modal:know`    | `K_A φ`                  | agent knows φ                   |
| `/modal:intend`  | `I_A φ`                  | agent intends to do φ           |
| `/modal:desire`  | `D_A φ`                  | agent desires φ                 |
| `/modal:ought`   | `O_A φ`                  | φ is an obligation for agent A  |

#### 🧬 Extended NG_ACT Structure with Modal Context

```python
NG_ACT := {
  ...
  "modal_context": [
    { "agent": "agent_philo", "type": "believe", "content": "ritual encodes logic" },
    { "agent": "human_sofia", "type": "intend", "content": "map myth epistemics" }
  ]
}
```

#### 🧠 Modal States in Agent

```python
AgentState := {
  ...
  "modal_beliefs": Set[φ],
  "modal_intentions": Queue[Goal],
  "modal_desires": WeightedSet[φ],
  ...
}
```

#### 🔁 Modal Processing Functions

```python
def update_beliefs(agent, φ):
    agent.modal_beliefs.add(φ)

def plan_from_intention(agent):
    goal = agent.modal_intentions.dequeue()
    return planner.plan(goal)
```

---

### 🧪 Example with Modal Gliphs

```ng
🚀 /act:compare
👁️ /focus:"concept of soul in Plato and shamanic traditions"
🤝 /mind:human_sofia ↔ agent_ethno
/modal:believe:agent_ethno:"soul implies non-dual topologies"
/modal:intend:human_sofia:"create comparative map"
📦 /deliverable:symbolic_map
/network:archeo_threads
```

---

### 🧱 9. Execution Stack (Layered)

1. **NG Parser → AST**
2. **AST → NG_ACT structure**
3. **Planner + Execution Engine**
4. **State Tracker + Dialogue Memory**
5. **Renderer for /gliph, /map, /thread**

---

### 🌱 10. Future Extensions

- 🖖 Modal logic for beliefs and obligations
- ⏰ Multi-threaded temporal tracking
- ⚛️ Integration with LLM agent frameworks (LangChain, CREW, etc.)
- ♻️ Self-organizing dynamic ontologies

---

**End of Specification v1.1**
