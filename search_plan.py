#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script que automatiza o processo completo de coleta.
Navega para cada URL do Google Maps e extrai dados via JS.
"""
import json
import time
import subprocess

# Todas as buscas organizadas por bairro
BAIRROS_TIPOS = {
    "Jardim Monte Sinai": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Jardim Riviera": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Bairro Independência": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Colina Azul": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "St Fabricio": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Jardim Monte Líbano": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "St dos Estados": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Cidade Livre": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Jardim Cristalino": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Setor Marista Sul": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Virgínia Parque": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "St Andrade Reis": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Parque Itatiaia": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Jardim Ipiranga": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
    "Independência Mansões": [
        "salão de beleza", "restaurante", "lanchonete", "pizzaria",
        "padaria", "farmácia", "drogaria", "pet shop",
        "óptica", "loja de roupas", "material de construção", "distribuidora"
    ],
}

if __name__ == "__main__":
    # Save the search organization
    with open("/opt/projects/search_plan.json", "w") as f:
        json.dump(BAIRROS_TIPOS, f, ensure_ascii=False, indent=2)
    total = sum(len(v) for v in BAIRROS_TIPOS.values())
    print(f"Search plan: {total} total searches across {len(BAIRROS_TIPOS)} neighborhoods")
