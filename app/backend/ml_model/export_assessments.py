# ml-model/export_assessments.py
import os
import django
import json
import pandas as pd

# setup django environment (project-root me run karo)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from assessments.models import Assessment

rows = []
for a in Assessment.objects.all():
    # responses stored as list or JSONField
    responses = a.responses if isinstance(a.responses, list) else json.loads(a.responses)
    rows.append({
        **{f"q{i+1}": int(responses[i]) for i in range(len(responses))},
        "score": a.score,
        "risk_level": a.risk_level,
    })

df = pd.DataFrame(rows)
if df.empty:
    print("No assessments found in DB. Take some tests first.")
else:
    df.to_csv("ml-model/assessments_dataset.csv", index=False)
    print("Exported", len(df), "rows to ml-model/assessments_dataset.csv")
