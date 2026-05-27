#!/usr/bin/env python3
"""
Bot de Captacao de Leads - Google Maps
Extrai nome, endereco, telefone e avaliacao de estabelecimentos
em bairros especificos de Aparecida de Goiania - GO

Como usar:
1. Este script gera um arquivo JSON com todas as buscas
2. O browser.py faz as buscas reais via Google Maps
3. Os dados sao consolidados em CSV final

Uso: python3 lead_bot_manual.py
"""

import json
import csv
import os
from datetime import datetime

CIDADE = "Aparecida de Goiania"
ESTADO = "GO"

# Dados coletados manualmente via Google Maps
# Formato: [nome, telefone, endereco, tipo, bairro, avaliacao, site, cnpj]

LEADS = []

def add(nome, telefone, endereco, tipo, bairro, avaliacao="", site="", cnpj=""):
    LEADS.append({
        "nome": nome.strip(),
        "telefone": telefone.strip() if telefone else "",
        "endereco": endereco.strip() if endereco else f"{bairro}, {CIDADE} - {ESTADO}",
        "site": site.strip() if site else "",
        "tipo": tipo.strip(),
        "bairro": bairro.strip(),
        "avaliacao": str(avaliacao).strip(),
        "cnpj": cnpj.strip() if cnpj else "",
    })

# ===================================================================
# JARDIM MONTE SINAI - Restaurantes
# ===================================================================
add("Brasa e Cia", "(62) 98435-6935", "Av. Dom Fernando Gomes dos Santos, qd 8 - lt 9 - Cidade Livre", "restaurante", "Jardim Monte Sinai", "4.9")
add("Churrascaria Kabanas Grill", "(47) 9966", "Av. Independencia, 7330 - Qd14", "churrascaria", "Jardim Monte Sinai", "4.3")
add("Casa da Dona Clara Bistrot", "", "R. Jota, 006 - 108", "restaurante", "Jardim Monte Sinai", "4.6")
add("Restaurante e Lanchonete Raizes Nordestinas", "", "", "restaurante", "Jardim Monte Sinai", "4.8")
add("Restaurante Silva", "", "Av. Coemitanga, 566-632", "restaurante", "Jardim Monte Sinai", "5.0")

# ===================================================================
# SALVAR ARQUIVOS
# ===================================================================

def salvar():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # CSV
    csv_file = f"/opt/projects/leads_aparecida_{timestamp}.csv"
    campos = ["nome", "telefone", "endereco", "site", "tipo", "bairro", "avaliacao", "cnpj"]
    with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(LEADS)
    
    # JSON
    json_file = f"/opt/projects/leads_aparecida_{timestamp}.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(LEADS, f, ensure_ascii=False, indent=2)
    
    # Resumo
    print(f"Total de leads: {len(LEADS)}")
    print(f"CSV: {csv_file}")
    print(f"JSON: {json_file}")
    print(f"\nPor bairro:")
    bc = {}
    for l in LEADS:
        b = l["bairro"]
        bc[b] = bc.get(b, 0) + 1
    for b, q in sorted(bc.items(), key=lambda x: -x[1]):
        print(f"  {b}: {q}")
    print(f"\nPor tipo:")
    tc = {}
    for l in LEADS:
        t = l["tipo"]
        tc[t] = tc.get(t, 0) + 1
    for t, q in sorted(tc.items(), key=lambda x: -x[1]):
        print(f"  {t}: {q}")
    ct = sum(1 for l in LEADS if l["telefone"])
    print(f"\nCom telefone: {ct}/{len(LEADS)}")

if __name__ == "__main__":
    salvar()
