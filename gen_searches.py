#!/usr/bin/env python3
"""
Rapid Google Maps scraper
Navigates to search pages, extracts all business data using JS
Then visits top 3 businesses per search for phone/address
"""
import json
import os
import time
from datetime import datetime
from collections import defaultdict

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

# Business types to search
TIPOS = [
    "salão de beleza", "restaurante", "lanchonete", "pizzaria",
    "padaria", "farmácia", "drogaria", "pet shop",
    "óptica", "loja de roupas", "material de construção", "distribuidora"
]

# Neighborhoods
BAIRROS = [
    "Independência Mansões", "Jardim Monte Sinai", "Jardim Riviera",
    "Bairro Independência", "Colina Azul", "St Fabricio",
    "Jardim Monte Líbano", "St dos Estados", "Cidade Livre",
    "Jardim Cristalino", "Setor Marista Sul", "Virgínia Parque",
    "St Andrade Reis", "Parque Itatiaia", "Jardim Ipiranga"
]

# Generate all search URLs
searches = []
for bairro in BAIRROS:
    for tipo in TIPOS:
        query = f"{tipo} em {bairro} Aparecida de Goiânia GO"
        url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
        searches.append({"url": url, "bairro": bairro, "tipo": tipo})

print(f"Total searches: {len(searches)}")
print(f"Business types: {len(TIPOS)}")
print(f"Neighborhoods: {len(BAIRROS)}")
print(f"Output: {arquivo}")

# Save search list
with open("/opt/projects/search_list.json", "w") as f:
    json.dump(searches, f, ensure_ascii=False, indent=2)
print("Search list saved to /opt/projects/search_list.json")
