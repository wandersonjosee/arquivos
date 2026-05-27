#!/usr/bin/env python3
"""
Compilador de Leads - Formata e envia via Telegram
Apos o scraping via browser, salve os dados em /opt/projects/leads_diarios/leads_brutos_{data}.json
e execute este script para formatar e enviar.

Uso:
  python3 compilador_leads.py --arquivo leads_brutos_2026-05-26.json
  python3 compilador_leads.py --teste  # Envia mensagem de teste
"""

import json
import csv
import os
import sys
import argparse
from datetime import datetime
from collections import defaultdict

CIDADE = "Aparecida de Goiânia"
DIR_LEADS = "/opt/projects/leads_diarios"
ARQUIVO_HISTORICO = "/opt/projects/leads_historico.json"


def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def salvar_historico(chaves):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(list(chaves), f, ensure_ascii=False, indent=2)


def formatar_mensagem(leads_por_bairro, data_str, total_geral, total_tel):
    """Formata mensagem Telegram - max ~4000 chars (limite Telegram)"""
    linhas = []
    linhas.append(f"🔍 *BOT PROSPEÇÃO - {data_str}*")
    linhas.append(f"📍 {CIDADE} - GO")
    linhas.append(f"📋 Total: *{total_geral}* leads novos")
    linhas.append(f"📱 Com telefone: *{total_tel}*")
    linhas.append("━" * 25)
    linhas.append("")

    for bairro, leads in sorted(leads_por_bairro.items()):
        leads_msg = leads[:10]  # Max 10 por bairro
        restantes = len(leads) - 10

        linhas.append(f"🏘️ *{bairro}* ({len(leads)} leads)")
        if restantes > 0:
            linhas.append(f"   _...e mais {restantes}_")
        linhas.append("")

        for i, lead in enumerate(leads_msg, 1):
            nome = lead.get("nome", "N/A")
            telefone = lead.get("telefone", "")
            endereco = lead.get("endereco", "")
            avaliacao = lead.get("avaliacao", "")
            tipo = lead.get("tipo", "")

            linhas.append(f"  {i}. *{nome}*")
            if tipo:
                linhas.append(f"     📂 {tipo}")
            if telefone:
                linhas.append(f"     📱 {telefone}")
            else:
                linhas.append(f"     📱 _sem telefone_")
            if endereco:
                end_curto = endereco[:55] + "…" if len(endereco) > 55 else endereco
                linhas.append(f"     📍 {end_curto}")
            if avaliacao:
                try:
                    n_estrelas = int(float(str(avaliacao).split()[0]))
                    estrelas = "⭐" * n_estrelas
                except:
                    estrelas = ""
                linhas.append(f"     ⭐ {avaliacao} {estrelas}")
            linhas.append("")

        linhas.append("")

    linhas.append("━" * 25)
    linhas.append("💡 _CNPJ: casadosdados.com.br_")

    msg = "\n".join(linhas)

    # Telegram tem limite de 4096 chars
    if len(msg) > 4000:
        msg = msg[:4000] + "\n\n_... (mensagem truncada - ver CSV completo)_"

    return msg


def processa_leads(arquivo_json, enviar=True):
    """Processa arquivo JSON de leads, deduplica, formata e envia"""

    with open(arquivo_json, "r", encoding="utf-8") as f:
        leads = json.load(f)

    historico = carregar_historico()
    novos = []
    duplicados = 0

    for lead in leads:
        chave = f"{lead.get('nome', '').lower().strip()}|{lead.get('bairro', '').lower().strip()}"
        if chave not in historico:
            historico.add(chave)
            novos.append(lead)
        else:
            duplicados += 1

    print(f"Total no arquivo: {len(leads)}")
    print(f"Novos: {len(novos)}")
    print(f"Duplicados: {duplicados}")

    if not novos:
        print("Nenhum lead novo encontrado.")
        return None

    # Agrupar por bairro
    leads_por_bairro = defaultdict(list)
    for l in novos:
        leads_por_bairro[l.get("bairro", "Outros")].append(l)

    # Salvar CSV
    os.makedirs(DIR_LEADS, exist_ok=True)
    data_str = datetime.now().strftime("%Y-%m-%d")
    csv_file = f"{DIR_LEADS}/leads_{data_str}.csv"

    campos = ["nome", "telefone", "endereco", "bairro", "tipo", "avaliacao"]
    with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(novos)

    print(f"CSV salvo: {csv_file}")

    # Salvar historico atualizado
    salvar_historico(historico)

    # Formatar mensagem
    total_tel = sum(1 for l in novos if l.get("telefone"))
    data_fmt = datetime.now().strftime("%d/%m/%Y")
    msg = formatar_mensagem(leads_por_bairro, data_fmt, len(novos), total_tel)

    print(f"\nMensagem ({len(msg)} chars):")
    print("=" * 40)
    print(msg)
    print("=" * 40)

    return msg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arquivo", type=str, help="Arquivo JSON de leads brutos")
    parser.add_argument("--teste", action="store_true", help="Envia mensagem de teste")
    args = parser.parse_args()

    if args.teste:
        # Mensagem de teste
        leads_teste = [
            {
                "nome": "Barbearia Teste",
                "telefone": "(62) 99999-9999",
                "endereco": "Rua Teste, 123",
                "bairro": "Jardim Monte Sinai",
                "tipo": "barbearia",
                "avaliacao": "5.0",
            }
        ]
        leads_por_bairro = {"Jardim Monte Sinai": leads_teste}
        msg = formatar_mensagem(leads_por_bairro, datetime.now().strftime("%d/%m/%Y"), 1, 1)
        print(msg)
        return

    if not args.arquivo:
        print("Uso: python3 compilador_leads.py --arquivo <arquivo.json>")
        print("     python3 compilador_leads.py --teste")
        sys.exit(1)

    processa_leads(args.arquivo)


if __name__ == "__main__":
    main()
