#!/usr/bin/env python3
"""
Script otimizado de scraping do Google Maps via browser automation.
Usa subprocess para chamar hermes browser tools via CLI.
"""
import json
import time
import subprocess
import sys
import os

BAIRROS = [
    "Independência Mansões",
    "Jardim Monte Sinai", 
    "Jardim Riviera",
    "Bairro Independência",
    "Colina Azul",
    "St Fabricio",
    "Jardim Monte Líbano",
    "St dos Estados",
    "Cidade Livre",
    "Jardim Cristalino",
    "Setor Marista Sul",
    "Virgínia Parque",
    "St Andrade Reis",
    "Parque Itatiaia",
    "Jardim Ipiranga"
]

TIPOS = [
    "salão de beleza",
    "restaurante",
    "lanchonete",
    "pizzaria",
    "padaria",
    "farmácia",
    "drogaria",
    "pet shop",
    "óptica",
    "loja de roupas",
    "material de construção",
    "distribuidora"
]

def build_search_url(tipo, bairro):
    query = f"{tipo} em {bairro} Aparecida de Goiânia GO"
    from urllib.parse import quote
    return f"https://www.google.com/maps/search/{quote(query)}"

if __name__ == "__main__":
    # Just output the URLs to scrape
    urls = []
    for bairro in BAIRROS:
        for tipo in TIPOS:
            url = build_search_url(tipo, bairro)
            urls.append({"bairro": bairro, "tipo": tipo, "url": url})
    
    print(json.dumps(urls, ensure_ascii=False, indent=2))
