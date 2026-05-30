#!/usr/bin/env python3
"""
Comprehensive Google Maps Lead Scraper for Aparecida de Goiânia
Uses hermes_tools browser to navigate and extract business data.
"""
import json
import os
import re
import time
from datetime import datetime
from hermes_tools import terminal

today = datetime.now().strftime("%Y-%m-%d")
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
    "salão de beleza", "restaurante", "lanchonete", "pizzaria",
    "padaria", "farmácia", "drogaria", "pet shop", "óptica",
    "loja de roupas", "material de construção", "distribuidora"
]

ALL_LEADS = []

def make_url(tipo, bairro):
    t = tipo.replace(" ", "+")
    b = bairro.replace(" ", "+")
    return f"https://www.google.com/maps/search/{t}+em+{b}+Aparecida+de+Goiânia+GO"

def parse_feed_for_names(snapshot_text):
    """Extract business names, refs and ratings from feed"""
    businesses = []
    lines = snapshot_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.search(r'article "([^"]+)" \[ref=(\w+)\]', line)
        if m:
            nome = m.group(1)
            ref = m.group(2)
            avaliacao = ""
            for j in range(i+1, min(i+6, len(lines))):
                rm = re.search(r'image "(\d+[.,]\d+) estrelas"', lines[j])
                if rm:
                    avaliacao = rm.group(1).replace(',', '.')
                    break
            businesses.append({"nome": nome, "ref": ref, "avaliacao": avaliacao})
        i += 1
    return businesses

def parse_sidebar(snapshot_text):
    """Extract phone and address from sidebar"""
    phone = ""
    address = ""
    m = re.search(r'Telefone: \((\d{2})\)\s*(\d{5})-?(\d{4})', snapshot_text)
    if m:
        phone = f"({m[1]}) {m[2]}-{m[3]}"
    m = re.search(r'Endereço: ([^"]+?)(?:\s*"|\s*Plus Code|\s*$)', snapshot_text)
    if m:
        address = m.group(1).strip().rstrip('"').strip()
    return phone, address

if __name__ == "__main__":
    print(f"Scraper ready. Date: {today}")
    print(f"Neighborhoods: {len(BAIRROS)}, Business types: {len(TIPOS)}")
    print(f"Total searches: {len(BAIRROS) * len(TIPOS)}")
