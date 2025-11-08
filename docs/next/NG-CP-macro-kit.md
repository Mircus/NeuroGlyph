# NG‑CP Macro Kit (Reusable Flows)

> Drop‑in macros for common studio actions. Use with NG 4.0 `/macro` + `/use`.

---

## 1) Dailies Session

```text
/macro(
  /name:"dailies_session",
  /params:["target","moderator"],
  /body:(
    /review.session(/target:@target, /stage:"dailies", /moderator:@moderator)
    /deliverable:dailies_report
  )
)
```

## 2) VFX Turnover

```text
/macro(
  /name:"vfx_turnover",
  /params:["shot","vendor"],
  /body:(
    /vfx.task(/shot:@shot, /vendor:@vendor, /stage:"comp")
    /event(/topic:"shot/assigned", /data:{ "shot":@shot, "vendor":@vendor })
    /deliverable:turnover_package
  )
)
```

## 3) Shot Review → Signoff

```text
/macro(
  /name:"shot_review",
  /params:["shot","stage"],
  /body:(
    /review.session(/target:@shot, /stage:@stage)
    /review.collect_notes
    /review.signoff(/scope:"shot:@shot", /stage:@stage, /by:["Director","Producer"])
    /deliverable:approval_record
  )
)
```

## 4) Edit Lock

```text
/macro(
  /name:"edit_lock",
  /params:["cut_id"],
  /body:(
    /film.edit.timeline(/id:@cut_id, /rate:"24", /aspect:"2.39")
    /event(/topic:"edit/locked", /data:{ "cut":@cut_id })
    /deliverable:edit_sequence
  )
)
```
