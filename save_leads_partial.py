#!/usr/bin/env python3
"""
Comprehensive leads data for 2026-05-27
Collected from Google Maps scraping
"""
import json
import os
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

os.makedirs(DIR_LEADS, exist_ok=True)

leads = [
  # === INDEPENDÊNCIA MANSÕES ===
  {"nome": "Dina Cabeleireira", "telefone": "(62) 99451-7993", "endereco": "Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-281", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,9"},
  {"nome": "Studio divas", "telefone": "(62) 99387-1166", "endereco": "Praca Jose Bonifácio - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-351", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "5,0"},
  {"nome": "Selma cabeleireira", "telefone": "(62) 99250-9905", "endereco": "R. 58 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-271", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "5,0"},
  {"nome": "Studio Sublime", "telefone": "(62) 99570-1675", "endereco": "Rua Dona Getúlia, 15 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-267", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,0"},
  {"nome": "Salão Da Jô", "telefone": "", "endereco": "R. 59 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-270", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,9"},
]

with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(leads, f, ensure_ascii=False, indent=2)

print(f"Saved {len(leads)} leads to {arquivo}")
