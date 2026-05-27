#!/usr/bin/env python3
"""
Final comprehensive leads data for 2026-05-27
All data collected from Google Maps browser scraping
"""
import json
import os
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

os.makedirs(DIR_LEADS, exist_ok=True)

leads = [
  # =============================================
  # INDEPENDÊNCIA MANSÕES
  # =============================================
  # Salão de beleza
  {"nome": "Dina Cabeleireira", "telefone": "(62) 99451-7993", "endereco": "Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,9"},
  {"nome": "Studio divas", "telefone": "(62) 99387-1166", "endereco": "Praca Jose Bonifácio - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "5,0"},
  {"nome": "Selma cabeleireira", "telefone": "(62) 99250-9905", "endereco": "R. 58 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "5,0"},
  {"nome": "Studio Sublime", "telefone": "(62) 99570-1675", "endereco": "Rua Dona Getúlia, 15 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,0"},
  {"nome": "Salão Da Jô", "telefone": "", "endereco": "R. 59 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "salão de beleza", "avaliacao": "4,9"},
  
  # Restaurante
  {"nome": "Restaurante e jantinha Bom Gosto", "telefone": "(62) 99240-3909", "endereco": "Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "restaurante", "avaliacao": "4,1"},
  {"nome": "Restaurante Fogaça", "telefone": "(62) 99164-4131", "endereco": "Av. 21 de Abril - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "restaurante", "avaliacao": "4,2"},
  {"nome": "FRANGO DA MISS LÚCIA", "telefone": "(62) 99305-0028", "endereco": "R. Manoel J. Coelho - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "restaurante", "avaliacao": "5,0"},
  
  # Pizzaria
  {"nome": "Pizzaria Milhão", "telefone": "(62) 99673-9654", "endereco": "R. 69-A, qd 180 - lt 20 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "pizzaria", "avaliacao": "4,8"},
  {"nome": "PIZZARELLA.62", "telefone": "(62) 99138-9120", "endereco": "Av. Arão de Souza - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "pizzaria", "avaliacao": "5,0"},
  
  # Padaria
  {"nome": "Kello's padaria", "telefone": "", "endereco": "R. Umbelina Alves, 1-167 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "padaria", "avaliacao": "5,0"},
  {"nome": "Panificadora Cia dos Pães e Salgados", "telefone": "(62) 98147-5395", "endereco": "Av. Benedito Silvestre de Tolêdo, Qd 172 - Lote 01 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "padaria", "avaliacao": "5,0"},
  
  # Pet shop
  {"nome": "Pet Love Pet Shop", "telefone": "(62) 99259-9979", "endereco": "R. 62 - Bairro Independência Mansões, Aparecida de Goiânia - GO", "bairro": "Independência Mansões", "tipo": "pet shop", "avaliacao": "4,1"},
  
  # =============================================
  # JARDIM MONTE SINAÍ
  # =============================================
  # Farmácia
  {"nome": "Drogaria São Gabriel", "telefone": "(62) 3277-5454", "endereco": "Av. Pedro Luís Ribeiro - Conjunto Residencial Storil, Aparecida de Goiânia - GO", "bairro": "Jardim Monte Sinai", "tipo": "farmácia", "avaliacao": "4,6"},
  {"nome": "Drogaria Marttins", "telefone": "", "endereco": "Jardim Monte Sinai, Aparecida de Goiânia - GO", "bairro": "Jardim Monte Sinai", "tipo": "drogaria", "avaliacao": "4,7"},
  {"nome": "Droga Mega", "telefone": "", "endereco": "Jardim Monte Sinai, Aparecida de Goiânia - GO", "bairro": "Jardim Monte Sinai", "tipo": "drogaria", "avaliacao": "4,8"},
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
