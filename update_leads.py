#!/usr/bin/env python3
"""
Complete leads data collector for 2026-05-27
All data collected from Google Maps browser scraping
"""
import json
import os
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

os.makedirs(DIR_LEADS, exist_ok=True)

# Start with existing data if file exists
existing = []
if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        existing = json.load(f)

# New leads to add
new_leads = [
  # === Pizzaria - Independência Mansões ===
  {"nome": "Pizzaria Milhão", "telefone": "(62) 99673-9654", "endereco": "R. 69-A, qd 180 - lt 20 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-327", "bairro": "Independência Mansões", "tipo": "pizzaria", "avaliacao": "4,8"},
  {"nome": "PIZZARELLA.62", "telefone": "(62) 99138-9120", "endereco": "Av. Arão de Souza - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-275", "bairro": "Independência Mansões", "tipo": "pizzaria", "avaliacao": "5,0"},
]

# Combine and deduplicate
all_leads = existing + new_leads
seen = set()
unique_leads = []
for l in all_leads:
    key = f"{l['nome'].lower().strip()}|{l['bairro'].lower().strip()}"
    if key not in seen:
        seen.add(key)
        unique_leads.append(l)

with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(unique_leads, f, ensure_ascii=False, indent=2)

print(f"Total unique leads: {len(unique_leads)}")
print(f"Saved to: {arquivo}")
