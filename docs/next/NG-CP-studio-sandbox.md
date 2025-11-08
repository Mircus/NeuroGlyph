# Studio Sandbox — Sample Transcript (NG 4.0 + NG‑CP v0.1)

> 2025-11-08 · Minimal end‑to‑end example


```text
/version:"4.0"
/thread(/id:"film/ep1", /enter:true)
/group(/id:"ProdCrew", /members:["Director","DP","Editor","VFX-Sup","Composer","LineProd"])

/film.story(/title:"Furnace of Stars", /logline:"A cartographer maps a dying sun.")

/film.scene(/id:"SC_024", /slug:"Observatory Rooftop – Night", /pages:1.5, /location:"Backlot A", /cast:["Kaelen","Mira"])
/film.shot(/id:"SC_024_SH_010", /type:"MS", /cam:"A", /lens:"50mm", /fps:24, /tc:"01:02:13:12", /description:"Kaelen lifts the sextant; neon reflection.")

/asset.register(/urn:"urn:ng:asset:prop/sextant@v3", /kind:"prop", /hash:"sha256:abc...", /src:"ModelingDept")

/policy(/safety:"strict", /guard:["union:meal_breaks_6h","color:ACEScg → Rec.709"], /enforce_budgets:true)
/budget(/time:"2m", /tokens:4000)

# Dailies
/macro(/name:"dailies_session", /params:["target","moderator"], /body:(/review.session(/target:@target, /stage:"dailies", /moderator:@moderator) /deliverable:dailies_report))
/use("dailies_session","SC_024","Director")
/review.pin(/target:"SC_024_SH_010", /tc:"01:02:15:08", /note:"Flare harsh", /by:"Director")

# VFX turnover
/macro(/name:"vfx_turnover", /params:["shot","vendor"], /body:(/vfx.task(/shot:@shot, /vendor:@vendor, /stage:"comp") /event(/topic:"shot/assigned", /data:{ "shot":@shot, "vendor":@vendor }) /deliverable:turnover_package))
/use("vfx_turnover","SC_024_SH_010","StudioX")

# Editorial clips
/film.edit.timeline(/id:"CUT_A1", /rate:"24", /aspect:"2.39", /working_color:"ACEScg", /display_color:"Rec.709", /tracks:[{ /v:"V1" }, { /a:"A1_DIA" }])
/film.edit.clip(/track:"V1", /src:"SC_024_SH_010.mov", /in:"01:02:13:12", /out:"01:02:18:00", /pos:"00:12:34:00")

# Music cue
/music.cue(/id:"CUE_17", /scene:"SC_024", /mood:"lonely awe", /tempo:72, /palette:"felt piano + glock", /stem:["pno","glock","pad"])

# Review & signoff
/macro(/name:"shot_review", /params:["shot","stage"], /body:(/review.session(/target:@shot, /stage:@stage) /review.collect_notes /review.signoff(/scope:"shot:@shot", /stage:@stage, /by:["Director","Producer"]) /deliverable:approval_record))
/use("shot_review","SC_024_SH_010","client_preview")

# Rights & scheduling
/rights.license(/asset:"CUE_17", /terms:{ "territory":"world", "media":"all", "term":"perpetual" }, /owner:"Composer-X", /proof:"url:signed.pdf")
/sched.call(/day:"2025-12-10", /unit:"Main", /scene:["SC_024"], /calltime:"06:00", /wrap:"18:30", /dept:["Camera","Lighting","Art","Sound"])

# Edit lock
/macro(/name:"edit_lock", /params:["cut_id"], /body:(/film.edit.timeline(/id:@cut_id, /rate:"24", /aspect:"2.39") /event(/topic:"edit/locked", /data:{ "cut":@cut_id }) /deliverable:edit_sequence))
/use("edit_lock","CUT_A1")
```
