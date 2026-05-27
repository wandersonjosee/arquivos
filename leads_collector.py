#!/usr/bin/env python3
"""Batch leads collector - populate this with scraped data"""
import json
import os
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

os.makedirs(DIR_LEADS, exist_ok=True)

# Initialize leads list
leads = []

# ============================================
# LEADS FROM BROWSER SCRAPING - Add them below
# ============================================

def add_lead(nome, telefone, endereco, bairro, tipo, avaliacao):
    leads.append({
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco,
        "bairro": bairro,
        "tipo": tipo,
        "avaliacao": avaliacao
    })

# =============================================
# SCRAPED DATA WILL BE ADDED HERE DURING RUNTIME
# =============================================

# Example format:
# add_lead("Business Name", "(62) 99999-9999", "Full address", "Bairro", "tipo", "4.5")

# Save function
def save_leads():
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(leads)} leads to {arquivo}")

if __name__ == "__main__":
    # Print current state
    print(f"File: {arquivo}")
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            existing = json.load(f)
        print(f"Existing leads: {len(existing)}")
