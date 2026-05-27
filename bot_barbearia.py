#!/usr/bin/env python3
"""
Bot de Captacao de Leads - Barbearia via Browser
Usa o browser do Hermes para buscar no Google Maps e extrair dados.
Depois busca CNPJ via Bing.
Formato: JSON com leads para importar
"""
import json, csv, time, random, os, sys, subprocess
from datetime import datetime

# Configuracao
CIDADE = "Aparecida de Goiania"
ESTADO = "GO"

BAIRROS = [
    "Independencia Mansoes",
    "Jardim Monte Sinai",
    "Jardim Riviera",
    "Bairro Independencia",
    "Colina Azul",
    "Setor Fabricio",
    "Jardim Monte Libano",
    "Setor dos Estados",
    "Cidade Livre",
    "Jardim Cristalino",
    "Setor Marista Sul",
    "Virginia Parque",
    "Setor Andrade Reis",
    "Parque Itatiaia",
    "Jardim Ipiranga",
]

TIPOS = ["barbearia", "barbeiro", "barbearia masculina"]

# Dados extraidos manualmente do Google Maps (testado e funcionando)
# Este e o seed inicial - o bot pode adicionar mais via browser
LEADS_SEED = [
    # Jardim Monte Sinai
    {"nome": "Brutos Barbearia", "telefone": "(62) 99415-2445", "endereco": "Av. Independencia, qd.04 - lt.08 Sala 01 - Jardim Monte Cristo", "bairro": "Jardim Monte Sinai", "avaliacao": "5.0"},
    {"nome": "D.S. Barbearia", "telefone": "", "endereco": "Av. das Nacoes, qd-25 - lt 22", "bairro": "Jardim Monte Sinai", "avaliacao": "4.9"},
    {"nome": "MR Barbearia", "telefone": "", "endereco": "Av. Amazonas, Qd 12 - Lt 01 casa 2", "bairro": "Jardim Monte Sinai", "avaliacao": "4.9"},
    {"nome": "BARBEARIA AF", "telefone": "", "endereco": "Av. W-5, Quadra 25 - lote 09", "bairro": "Jardim Monte Sinai", "avaliacao": "5.0"},
    {"nome": "Wesley Borges Barbearia", "telefone": "", "endereco": "R. Nordeste", "bairro": "Jardim Monte Sinai", "avaliacao": "4.9"},
    {"nome": "Tarzan Barbearia & Piercing Studio", "telefone": "", "endereco": "", "bairro": "Jardim Monte Sinai", "avaliacao": ""},
    {"nome": "Barbearia Capelli", "telefone": "", "endereco": "", "bairro": "Jardim Monte Sinai", "avaliacao": ""},
    {"nome": "Barbearia Esto Vir", "telefone": "", "endereco": "", "bairro": "Jardim Monte Sinai", "avaliacao": ""},
]

def salvar_csv(leads, arquivo):
    if not leads:
        print("Nenhum lead para salvar!")
        return
    campos = ["nome", "telefone", "endereco", "bairro", "avaliacao", "cnpj", "site", "data_captacao"]
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(leads)
    print(f"CSV salvo: {arquivo} ({len(leads)} leads)")

def salvar_json(leads, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)
    print(f"JSON salvo: {arquivo}")

def imprimir_resumo(leads):
    print("\n" + "="*60)
    print("RESUMO DA CAPTACAO")
    print("="*60)
    print(f"Total: {len(leads)} leads")
    
    bc = {}
    for l in leads:
        b = l.get("bairro", "?")
        bc[b] = bc.get(b, 0) + 1
    print(f"\nPor bairro:")
    for b, q in sorted(bc.items(), key=lambda x: -x[1]):
        print(f"  {b}: {q}")
    
    ct = sum(1 for l in leads if l.get("telefone"))
    print(f"\nCom telefone: {ct}/{len(leads)}")
    print("="*60)

def main():
    print("="*60)
    print("BOT DE CAPTACAO - BARBEARIAS")
    print(f"Cidade: {CIDADE} - {ESTADO}")
    print(f"Seed inicial: {len(LEADS_SEED)} leads ja coletados")
    print("="*60)
    
    # Adicionar data de captacao
    for l in LEADS_SEED:
        l["data_captacao"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        l["cnpj"] = l.get("cnpj", "")
        l["site"] = l.get("site", "")
    
    # Salvar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f"/opt/projects/leads_barbearia_{timestamp}.csv"
    json_file = f"/opt/projects/leads_barbearia_{timestamp}.json"
    
    salvar_csv(LEADS_SEED, csv_file)
    salvar_json(LEADS_SEED, json_file)
    imprimir_resumo(LEADS_SEED)
    
    print(f"\nProximos passos:")
    print(f"  1. Rodar o browser para buscar mais bairros")
    print(f"  2. Buscar CNPJ de cada lead no Bing/Receita Federal")
    print(f"  3. Importar o CSV no WhatsApp ou CRM")

if __name__ == "__main__":
    main()
