#!/usr/bin/env python3
"""
Google Maps Lead Scraper - Coleta dados de negócios em Aparecida de Goiânia
Executa via browser: navega, clica, extrai dados do sidebar, e salva em JSON.
"""
import json
import os
import re
import time
import subprocess
import sys
from datetime import datetime
from collections import defaultdict

today = datetime.now().strftime("%Y-%m-%m")
DIR_LEADS = "/opt/projects/leads_diarios"

# Bairros e tipos
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

# Prioridades - tipos de negócio que mais compram máquina de cartão
TIPOS_PRIORITARIOS = [
    "restaurante", "lanchonete", "pizzaria", "padaria", "farmácia",
    "salão de beleza", "pet shop", "loja de roupas", "material de construção",
    "distribuidora", "drogaria", "óptica"
]

os.makedirs(DIR_LEADS, exist_ok=True)
