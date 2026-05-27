#!/usr/bin/env python3
"""
Bot de Captacao de Leads - Google Maps Scraper
Extrai dados reais do Google Maps para Aparecida de Goiania-GO

Metodo: Busca via requests + extracao de dados JavaScript embutidos na pagina
"""
import requests
import re
import json
import csv
import time
import random
from datetime import datetime
from urllib.parse import quote_plus

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

TIPOS = [
    "restaurantes", "lanchonetes", "pizzarias", "bares",
    "padarias", "supermercados", "farmacias", "drogarias",
    "salao de beleza", "barbearias", "pet shop", "mecanica",
    "posto de gasolina", "lojas de roupas", "calcados",
    "otica", "joalheria", "floricultura", "sorvete acai",
    "material de construcao", "lavanderia", "imobiliaria",
    "academia", "escola", "clinica medica", "dentista",
    "distribuidora", "buffet", "grafica", "papelaria",
    "moveis", "celulares", "informatica", "auto escola",
    "veterinaria", "dedetizacao", "jardinagem",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Cache-Control": "max-age=0",
}

leads = []
vistos = set()

def extrair_leads_google_maps(html, tipo, bairro):
    """Extrai leads do HTML do Google Maps"""
    resultados = []
    
    # O Google Maps embute dados em formato JSON dentro de <script>
    # Padrao: window.APP_INITIALIZATION_STATE ou dados similares
    
    # Metodo 1: Extrair via regex os dados de lugares
    # O Google Maps pode retornar dados em formato JSON
    
    # Procurar por blocos de dados de lugares
    place_pattern = r'"(https://www\.google\.com/maps/place/[^"]+)"[^}]*"([^"]+)"'
    places = re.findall(place_pattern, html)
    
    # Metodo 2: Extrair via padroes conhecidos do HTML
    # Nome do estabelecimento
    nomes = re.findall(r'"name":"([^"]+)"', html)
    telefones = re.findall(r'"(phone|telephone)":"(\+?55\s*\(?\d{2}\)?[\s.]*\d{4,5}[-.\s]?\d{4})"', html)
    enderecos = re.findall(r'"(address|streetAddressFormatted|formattedAddress)":"([^"]+)"', html)
    avaliacoes = re.findall(r'"(rating|starRating)":(\d+\.?\d*)"', html)
    total_reviews = re.findall(r'"(totalRatings|userRatingsTotal)":(\d+)"', html)
    
    # Se encontrou dados estruturados
    if nomes:
        for i, nome in enumerate(nomes):
            if len(nome) < 3 or any(x in nome.lower() for x in ['google', 'maps', 'login', 'sign', 'play', 'store']):
                continue
            
            telefone = telefones[i][1] if i < len(telefones) else ""
            endereco = enderecos[i][1] if i < len(enderecos) else ""
            avaliacao = avaliacoes[i][1] if i < len(avaliacoes) else ""
            reviews = total_reviews[i][1] if i < len(total_reviews) else ""
            
            # Formatar telefone
            tel_limpo = re.sub(r'[^\d]', '', telefone)
            if len(tel_limpo) >= 10:
                telefone = f"({tel_limpo[:2]}) {tel_limpo[2:7]}-{tel_limpo[7:11]}"
            
            chave = nome.lower().strip()
            if chave not in vistos and nome.strip():
                vistos.add(chave)
                resultados.append({
                    "nome": nome.strip(),
                    "telefone": telefone,
                    "endereco": endereco.strip() if endereco else f"{bairro}, {CIDADE} - {ESTADO}",
                    "tipo": tipo,
                    "bairro": bairro,
                    "avaliacao": avaliacao,
                    "site": "",
                    "cnpj": "",
                })
    
    return resultados


def buscar_google_maps(query, max_tentativas=3):
    """Faz busca no Google Maps e retorna HTML"""
    url = f"https://www.google.com/maps/search/{quote_plus(query)}"
    
    for tentativa in range(max_tentativas):
        try:
            session = requests.Session()
            session.headers.update(HEADERS)
            
            resp = session.get(url, timeout=20, allow_redirects=True)
            
            if resp.status_code == 200:
                return resp.text
            elif resp.status_code == 429:
                print(f"    [RATE LIMIT] Aguardando 30s...")
                time.sleep(30)
            else:
                print(f"    [HTTP {resp.status_code}]")
                
        except requests.exceptions.Timeout:
            print(f"    [TIMEOUT] Tentativa {tentativa+1}")
        except Exception as e:
            print(f"    [ERRO] {e}")
        
        time.sleep(random.uniform(2, 5))
    
    return ""


def main():
    print("="*60)
    print("BOT DE CAPTACAO DE LEADS - GOOGLE MAPS")
    print(f"Cidade: {CIDADE} - {ESTADO}")
    print(f"Bairros: {len(BAIRROS)}")
    print(f"Tipos: {len(TIPOS)}")
    print(f"Total de buscas: {len(BAIRROS) * len(TIPOS)}")
    print("="*60)
    
    total_buscas = len(BAIRROS) * len(TIPOS)
    busca_atual = 0
    
    for bairro in BAIRROS:
        print(f"\n[BAIRRO] {bairro}")
        
        for tipo in TIPOS:
            busca_atual += 1
            progresso = busca_atual * 100 // total_buscas
            query = f"{tipo} em {bairro} {CIDADE} {ESTADO}"
            
            print(f"  [{progresso:3d}%] {tipo}...", end=" ", flush=True)
            
            html = buscar_google_maps(query)
            
            if html:
                novos = extrair_leads_google_maps(html, tipo, bairro)
                if novos:
                    print(f"-> {len(novos)} leads")
                    leads.extend(novos)
                else:
                    print("-> 0 (sem dados extrarios)")
            else:
                print("-> ERRO")
            
            # Pausa entre buscas
            time.sleep(random.uniform(1.5, 3.0))
    
    # Salvar
    if leads:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file = f"/opt/projects/leads_{CIDADE.replace(' ','_')}_{timestamp}.csv"
        
        campos = ["nome", "telefone", "endereco", "tipo", "bairro", "avaliacao", "site", "cnpj"]
        with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(leads)
        
        print(f"\n{'='*60}")
        print(f"FINALIZADO!")
        print(f"Total de leads: {len(leads)}")
        print(f"Arquivo: {csv_file}")
        
        # Resumo por bairro
        bc = {}
        for l in leads:
            b = l["bairro"]
            bc[b] = bc.get(b, 0) + 1
        print(f"\nPor bairro:")
        for b, q in sorted(bc.items(), key=lambda x: -x[1]):
            print(f"  {b}: {q}")
        
        # Com telefone
        ct = sum(1 for l in leads if l["telefone"])
        print(f"\nCom telefone: {ct}/{len(leads)} ({ct*100//len(leads)}%)")
    else:
        print("\nNenhum lead encontrado.")


if __name__ == "__main__":
    main()
