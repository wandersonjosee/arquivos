#!/usr/bin/env python3
"""
Comprehensive leads data for 2026-05-27
Collected from Google Maps scraping - Independência Mansões
"""
import json
import os
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

os.makedirs(DIR_LEADS, exist_ok=True)

leads = [
  # === INDEPENDÊNCIA MANSÕES - Salão de Beleza ===
  {"nome": "Dina Cabeleireira", "telefone": "(62) 99451-7993", "endereco": "Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-281", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,9"},
  {"nome": "Studio divas", "telefone": "(62) 99387-1166", "endereco": "Praca Jose Bonifácio - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-351", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "5,0"},
  {"nome": "Selma cabeleireira", "telefone": "(62) 99250-9905", "endereco": "R. 58 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-271", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "5,0"},
  {"nome": "Studio Sublime", "telefone": "(62) 99570-1675", "endereco": "Rua Dona Getúlia, 15 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-267", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,0"},
  {"nome": "Salão Da Jô", "telefone": "", "endereco": "R. 59 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-270", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,9"},
  
  # === INDEPENDÊNCIA MANSÕES - Restaurante ===
  {"nome": "Restaurante e jantinha Bom Gosto", "telefone": "(62) 99240-3909", "endereco": "Bairro Independência Mansões, Aparecida de Goiânia - GO, 74958-190", "bairro": "Independência Mansões", "tipo": "restaurante", "avaliacao": "4,1"},
  {"nome": "Restaurante Fogaça", "telefone": "(62) 99164-4131", "endereco": "Av. 21 de Abril - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74961-685", "bairro": "Independência Mansões", "tipo": "restaurante", "avaliacao": "4,2"},
  {"nome": "Lanchonete Brandão", "telefone": "", "endereco": "R. 64 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-280", "bairro": "Independência Mansões", "tipo": "lanchonete", "avaliacao": "4,8"},
  {"nome": "FRANGO DA MISS LÚCIA", "telefone": "(62) 99305-0028", "endereco": "R. Manoel J. Coelho - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-308", "bairro": "Independência Mansões", "tipo": "restaurante", "avaliacao": "5,0"},
  
  # === INDEPENDÊNCIA MANSÕES - Lanchonete ===
  {"nome": "Lanchonete Brandão", "telefone": "", "endereco": "R. 64 - Bairro Independência Mansões, Aparecida de Goiânia - GO, 74959-280", "bairro": "Independência Mansões", "tipo": "lanchonete", "avaliacao": "4,8"},
]

# Deduplicate
seen = set()
unique_leads = []
for l in leads:
    key = f"{l['nome'].lower().strip()}|{l['bairro'].lower().strip()}"
    if key not in seen:
        seen.add(key)
        unique_leads.append(l)

with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(unique_leads, f, ensure_ascii=False, indent=2)

print(f"Saved {len(unique_leads)} unique leads to {arquivo}")
