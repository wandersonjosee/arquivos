#!/usr/bin/env python3
"""
Master scraper - Uses hermes browser tools to scrape Google Maps.
Outputs JSON leads data.
"""
import json
import os
import re
import time
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%m")
DIR_LEADS = "/opt/projects/leads_diarios"
os.makedirs(DIR_LEADS, exist_ok=True)

BAIRROS = [
    "Independência Mansões", "Jardim Monte Sinai", "Jardim Riviera",
    "Bairro Independência", "Colina Azul", "St Fabricio",
    "Jardim Monte Líbano", "St dos Estados", "Cidade Livre",
    "Jardim Cristalino", "Setor Marista Sul", "Virgínia Parque",
    "St Andrade Reis", "Parque Itatiaia", "Jardim Ipiranga"
]

TIPOS = [
    "restaurante", "lanchonete", "pizzaria", "padaria",
    "salão de beleza", "farmácia", "pet shop", "loja de roupas",
    "material de construção", "distribuidora"
]

# Global leads list - will be populated by the orchestrator
ALL_LEADS = []

def make_url(tipo, bairro):
    t = tipo.replace(" ", "+")
    b = bairro.replace(" ", "+")
    return f"https://www.google.com/maps/search/{t}+em+{b}+Aparecida+de+Goiânia+GO"

def parse_snapshot_for_businesses(snapshot_text, bairro, tipo):
    """Extract business names and ratings from snapshot feed"""
    businesses = []
    lines = snapshot_text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Find article entries (business results in feed)
        m = re.search(r'article "([^"]+)" \[ref=(\w+)\]', line)
        if m:
            nome = m.group(1)
            ref = m.group(2)
            
            # Look ahead for rating
            avaliacao = ""
            for j in range(i+1, min(i+5, len(lines))):
                rm = re.search(r'image "(\d+[.,]\d+) estrelas"', lines[j])
                if rm:
                    avaliacao = rm.group(1).replace(',', '.')
                    break
            
            businesses.append({
                "nome": nome,
                "ref": ref,
                "avaliacao": avaliacao
            })
        
        i += 1
    
    return businesses

def parse_sidebar_data(snapshot_text):
    """Extract phone and address from open sidebar"""
    phone = ""
    address = ""
    
    m = re.search(r'Telefone: \((\d{2})\)\s*(\d{5})-?(\d{4})', snapshot_text)
    if m:
        phone = f"({m[1]}) {m[2]}-{m[3]}"
    
    m = re.search(r'Endereço: (.+?)(?:["\n]|Plus Code|$)', snapshot_text)
    if m:
        address = m.group(1).strip()
        if address.endswith('"'):
            address = address[:-1].strip()
    
    return phone, address

if __name__ == "__main__":
    # Generate search plan
    searches = []
    for bairro in BAIRROS:
        for tipo in TIPOS:
            searches.append({
                "bairro": bairro,
                "tipo": tipo,
                "url": make_url(tipo, bairro)
            })
    
    plan_file = f"/opt/projects/searches_{today.replace('m','d')}.json"
    os.makedirs("/opt/projects", exist_ok=True)
    with open(plan_file, "w", encoding="utf-8") as f:
        json.dump(searches, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(searches)} search tasks -> {plan_file}")
