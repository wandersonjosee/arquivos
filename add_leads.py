#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coletor de leads - armazena dados extraídos do Google Maps.
Cada execução adiciona dados de uma busca.
"""
import json
import os
import sys
from datetime import datetime

DATA_FILE = "/opt/projects/leads_diarios/leads_brutos_2026-05-28.json"

def load_existing():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_leads(leads):
    existing = load_existing()
    existing.extend(leads)
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"Total leads saved: {len(existing)}")

def add_search_results(bairro, tipo, raw_results):
    """Convert raw browser extraction to lead format.
    raw_results: list of [name, phone, rating, address]
    """
    leads = []
    for item in raw_results:
        name = item[0].strip() if item[0] else ""
        phone = item[1].strip() if len(item) > 1 and item[1] else ""
        rating = item[2].strip() if len(item) > 2 and item[2] else ""
        address = item[3].strip() if len(item) > 3 and item[3] else ""
        
        if not name:
            continue
        
        # Clean rating - extract number
        rating_num = ""
        import re
        m = re.search(r'[\d,]+', rating)
        if m:
            rating_num = m.group(0).replace(',', '.')
        
        # Build full address
        if address and bairro not in address:
            full_address = f"{address}, {bairro}, Aparecida de Goiânia - GO"
        else:
            full_address = f"{bairro}, Aparecida de Goiânia - GO"
        
        lead = {
            "nome": name,
            "telefone": phone,
            "endereco": full_address,
            "bairro": bairro,
            "tipo": tipo,
            "avaliacao": rating_num
        }
        leads.append(lead)
    
    save_leads(leads)
    print(f"Added {len(leads)} leads for {bairro} / {tipo}")
    return leads

if __name__ == "__main__":
    # Test
    print(f"Data file: {DATA_FILE}")
    existing = load_existing()
    print(f"Existing leads: {len(existing)}")
