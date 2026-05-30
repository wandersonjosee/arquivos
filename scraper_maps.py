#!/usr/bin/env python3
"""
Google Maps scraper - extracts business data from Google Maps search results.
Uses the browser tool via subprocess to navigate and collect snapshot data.
This script outputs JSON leads data.
"""
import json
import sys
import time
import os
import re
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

BAIRROS = [
    "Independência Mansões", "Jardim Monte Sinai", "Jardim Riviera",
    "Bairro Independência", "Colina Azul", "St Fabricio",
    "Jardim Monte Líbano", "St dos Estados", "Cidade Livre",
    "Jardim Cristalino", "Setor Marista Sul", "Virgínia Parque",
    "St Andrade Reis", "Parque Itatiaia", "Jardim Ipiranga"
]

TIPOS = [
    "salão de beleza", "restaurante", "lanchonete", "pizzaria",
    "padaria", "farmácia", "drogaria", "pet shop", "óptica",
    "loja de roupas", "material de construção", "distribuidora"
]

def normalize_rating(rating_str):
    """Convert rating string like '4,0 estrelas' to '4.0'"""
    if not rating_str:
        return ""
    m = re.search(r'(\d+[.,]\d+)', rating_str.replace(',', '.'))
    return m.group(1) if m else ""

def normalize_phone(phone_str):
    """Extract phone from string like 'Telefone: (62) 99570-1675'"""
    if not phone_str:
        return ""
    m = re.search(r'\((\d{2})\)\s*(\d{5})-?(\d{4})', phone_str)
    return f"({m[1]}) {m[2]}-{m[3]}" if m else ""

def normalize_address(addr_str):
    """Clean address string"""
    if not addr_str:
        return ""
    return addr_str.replace("Endereço: ", "").strip()

if __name__ == "__main__":
    # This script is called with --collect to output search URLs
    if "--collect" in sys.argv:
        searches = []
        for bairro in BAIRROS:
            for tipo in TIPOS:
                url = f"https://www.google.com/maps/search/{tipo.replace(' ', '+')}+em+{bairro.replace(' ', '+')}+Aparecida+de+Goiânia+GO"
                searches.append({"bairro": bairro, "tipo": tipo, "url": url})
        
        out_file = f"/opt/projects/pendentes_busca_{today}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(searches, f, ensure_ascii=False, indent=2)
        print(f"Generated {len(searches)} search URLs -> {out_file}")
    
    elif "--merge" in sys.argv:
        # Merge partial results
        import glob
        all_leads = []
        for f in sorted(glob.glob(f"/opt/projects/leads_parciais_*.json")):
            with open(f) as fp:
                data = json.load(fp)
                all_leads.extend(data)
            os.remove(f)
        
        out_file = f"/opt/projects/leads_diarios/leads_brutos_{today}.json"
        os.makedirs("/opt/projects/leads_diarios", exist_ok=True)
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(all_leads, f, ensure_ascii=False, indent=2)
        print(f"Merged {len(all_leads)} leads -> {out_file}")
    
    else:
        print("Usage: scraper_maps.py --collect | --merge")
