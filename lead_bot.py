#!/usr/bin/env python3
"""
Bot de Captacao de Leads - Google Maps via Browser
Cidade: Aparecida de Goiania - GO
Usa o browser para buscar no Google Maps e extrair dados completos.
"""

import json
import time
import csv
import os
import random
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

TIPOS_BUSCA = [
    "restaurantes",
    "lanchonetes",
    "pizzarias",
    "bares e pub",
    "cafeterias",
    "padarias",
    "supermercados",
    "lojas de roupas",
    "calcados",
    "farmacias",
    "drogarias",
    "salao de beleza",
    "barbearias",
    "pet shop",
    "mecanica automotiva",
    "oficina mecanica",
    "informatica",
    "celulares",
    "otica",
    "joalheria",
    "floricultura",
    "sorvete acai",
    "material de construcao",
    "lavanderia",
    "imobiliaria",
    "advocacia",
    "contabilidade",
    "clinica medica",
    "dentista laboratorio",
    "auto escola",
    "posto de combustivel",
    "distribuidora",
    "buffet",
    "grafica",
    "papelaria",
    "moveis eletro",
    "lanchonete acai",
    "escola infantil",
    "academia esportes",
]

# Lista para armazenar todos os leads
LEADS = []
LEADS_VISTOS = set()  # Para deduplicacao

def adicionar_lead(nome, endereco, telefone, tipo, bairro, avaliacao="", site=""):
    """Adiciona um lead se nao for duplicado"""
    chave = nome.lower().strip()
    if chave not in LEADS_VISTOS and nome.strip():
        LEADS_VISTOS.add(chave)
        LEADS.append({
            "nome": nome.strip(),
            "endereco": endereco.strip() if endereco else f"{bairro}, {CIDADE} - {ESTADO}",
            "telefone": telefone.strip() if telefone else "",
            "site": site.strip() if site else "",
            "tipo": tipo,
            "bairro": bairro,
            "avaliacao": avaliacao,
            "cnpj": "",
        })

def salvar_csv(arquivo="/opt/projects/leads_aparecida.csv"):
    """Salva leads em CSV"""
    if not LEADS:
        print("Nenhum lead para salvar!")
        return
    
    campos = ["nome", "endereco", "telefone", "site", "tipo", "bairro", "avaliacao", "cnpj"]
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(LEADS)
    print(f"[CSV] {len(LEADS)} leads salvos em {arquivo}")

def salvar_json(arquivo="/opt/projects/leads_aparecida.json"):
    """Salva leads em JSON"""
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(LEADS, f, ensure_ascii=False, indent=2)
    print(f"[JSON] {len(LEADS)} leads salvos em {arquivo}")

def imprimir_resumo():
    """Imprime resumo dos leads"""
    print("\n" + "="*60)
    print("RESUMO DA CAPTACAO DE LEADS")
    print("="*60)
    print(f"Total de leads: {len(LEADS)}")
    
    # Por bairro
    bairros = {}
    for l in LEADS:
        b = l["bairro"]
        bairros[b] = bairros.get(b, 0) + 1
    
    print(f"\nLeads por bairro:")
    for b, q in sorted(bairros.items(), key=lambda x: -x[1]):
        print(f"  {b}: {q}")
    
    # Por tipo
    tipos = {}
    for l in LEADS:
        t = l["tipo"]
        tipos[t] = tipos.get(t, 0) + 1
    
    print(f"\nLeads por tipo:")
    for t, q in sorted(tipos.items(), key=lambda x: -x[1])[:10]:
        print(f"  {t}: {q}")
    
    # Com telefone
    ct = sum(1 for l in LEADS if l["telefone"])
    print(f"\nCom telefone: {ct} ({ct*100//len(LEADS) if LEADS else 0}%)")
    print("="*60)


# ==== FUNCOES DE BUSCA VIA BROWSER (para uso com browser_automation) ====

def buscar_bairro_tipo(bairro, tipo):
    """
    Busca estabelecimentos de um tipo em um bairro.
    Retorna lista de dicionarios com os dados.
    Esta funcao deve ser chamada com o browser ja no Google Maps.
    """
    query = f"{tipo} em {bairro} {CIDADE} {ESTADO}"
    url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
    return url

def extrair_leads_da_pagina(resultados_brutos):
    """
    Extrai leads dos resultados da pagina do Google Maps.
    Recebe uma lista de artigos/nomes encontrados.
    """
    leads = []
    for r in resultados_brutos:
        if r.get("nome"):
            leads.append({
                "nome": r["nome"],
                "endereco": r.get("endereco", ""),
                "telefone": r.get("telefone", ""),
                "site": r.get("site", ""),
                "tipo": r.get("tipo", ""),
                "bairro": r.get("bairro", ""),
                "avaliacao": r.get("avaliacao", ""),
                "cnpj": "",
            })
    return leads
