#!/usr/bin/env python3
"""Quick lead collector - saves leads from browser scraping session"""
import json
import os
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

os.makedirs(DIR_LEADS, exist_ok=True)

# Load existing leads if any
existing = []
if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        existing = json.load(f)

print(f"Current leads count: {len(existing)}")
print(f"File: {arquivo}")
