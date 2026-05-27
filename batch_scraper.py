#!/usr/bin/env python3
"""
Batch Google Maps scraper - extracts data from a list of Google Maps URLs
Usage: python3 batch_scraper.py
"""
import json
import os
import subprocess
import time
from datetime import datetime

DIR_LEADS = "/opt/projects/leads_diarios"
data_str = datetime.now().strftime("%Y-%m-%d")
arquivo = f"{DIR_LEADS}/leads_brutos_{data_str}.json"

# All URLs to scrape with metadata
URLS = [
  # Pizzaria - Independência Mansões
  {"url": "https://www.google.com/maps/place/Pizzaria+Milh%C3%A3o/data=!4m7!3m6!1s0x935ef91449c7d7e5:0x718df750f6f452e3!8m2!3d-16.8179293!4d-49.3081018!16s%2Fg%2F11f3x5_twv!19sChIJ5dfHSRT5XpMR41L09lD3jXE?authuser=0&hl=pt-BR&rclk=1", "bairro": "Independência Mansões", "tipo": "pizzaria"},
  {"url": "https://www.google.com/maps/place/PIZZARELLA.62/data=!4m7!3m6!1s0x935ef9004ee97879:0xcababdd8d8d3295b!8m2!3d-16.8201478!4d-49.3114382!16s%2Fg%2F11x88m4zm_!19sChIJeXjpTgD5XpMRWynT2Ni9uso?authuser=0&hl=pt-BR&rclk=1", "bairro": "Independência Mansões", "tipo": "pizzaria"},
  {"url": "https://www.google.com/maps/place/Chivas+pizzaria+pro/data=!4m7!3m6!1s0x935ef96523a88eaf:0x252d9bc6e081ba97!8m2!3d-16.8205304!4d-49.3107343!16s%2Fg%2F11xlnb2smr!19sChIJr46oI2X5XpMRl7qB4MabLSU?authuser=0&hl=pt-BR&rclk=1", "bairro": "Independência Mansões", "tipo": "pizzaria"},
  {"url": "https://www.google.com/maps/place/Natally+Pizzaria+Hot+Dogs/data=!4m7!3m6!1s0x935efb9b091cad3d:0x18b602365c219a6f!8m2!3d-16.8279759!4d-49.3087513!16s%2Fg%2F11x341sybs!19sChIJPa0cCZv7XpMRb5ohXDYCthg?authuser=0&hl=pt-BR&rclk=1", "bairro": "Independência Mansões", "tipo": "pizzaria"},
  {"url": "https://www.google.com/maps/place/Casa+Azul/data=!4m7!3m6!1s0x935ef9c50e806537:0xc81236c574d48385!8m2!3d-16.822814!4d-49.3069609!16s%2Fg%2F11qxbbd6k8!19sChIJN2WADsX5XpMRhYPUdMU2Esg?authuser=0&hl=pt-BR&rclk=1", "bairro": "Independência Mansões", "tipo": "pizzaria"},
]

print(f"Total URLs to scrape: {len(URLS)}")
print(f"Output file: {arquivo}")
