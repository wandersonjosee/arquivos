#!/usr/bin/env python3
"""
Bot Prospeccao - Busca leads no Google Maps e envia via Telegram
Roda diariamente via cron job as 08:00

Uso:
  python3 bot_prospeccao.py --run-now    # Executa busca agora
  python3 bot_prospeccao.py --test       # Modo teste (1 bairro only)
"""

import subprocess
import json
import csv
import os
import sys
import argparse
from datetime import datetime
from collections import defaultdict

CIDADE = "Aparecida de Goiânia"
ESTADO = "GO"

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
    "Jardim Ipiranga",
]

TIPOS_NEGOCIO = [
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
    "distribuidora",
]

ARQUIVO_HISTORICO = "/opt/projects/leads_historico.json"
DIR_LEADS = "/opt/projects/leads_diarios"


def carregar_historico():
    """Carrega histórico de leads já enviados para evitar duplicatas"""
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def salvar_historico(chaves):
    """Salva histórico de leads enviados"""
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(list(chaves), f, ensure_ascii=False, indent=2)


def formatar_mensagem(leads_por_bairro, data_str):
    """Formata mensagem do Telegram agrupando por bairro, máx 10 por grupo"""
    msg = f"🔍 *BOT PROSPEÇÃO - {data_str}*\n"
    msg += f"📍 {CIDADE} - {ESTADO}\n"
    msg += f"📋 Total: *{sum(len(v) for v in leads_por_bairro.values())}* leads novos\n"

    total_telefones = sum(
        1 for leads in leads_por_bairro.values() for l in leads if l.get("telefone")
    )
    msg += f"📱 Com telefone: *{total_telefones}*\n"
    msg += "━" * 30 + "\n\n"

    for bairro, leads in sorted(leads_por_bairro.items()):
        # Máximo de 10 leads por bairro na mensagem
        leads_msg = leads[:10]
        restantes = len(leads) - 10

        msg += f"🏘️ *{bairro}* ({len(leads)} leads)\n"

        if restantes > 0:
            msg += f"   _...e mais {restantes} leads_\n"

        msg += "\n"

        for i, lead in enumerate(leads_msg, 1):
            nome = lead.get("nome", "N/A")
            telefone = lead.get("telefone", "Não disponível")
            endereco = lead.get("endereco", "")
            avaliacao = lead.get("avaliacao", "")
            tipo = lead.get("tipo", "")

            msg += f"  {i}. *{nome}*\n"
            if tipo:
                msg += f"     📂 {tipo}\n"
            msg += f"     📱 {telefone}\n"
            if endereco:
                # Encurtar endereço se muito longo
                end_curto = endereco[:60] + "..." if len(endereco) > 60 else endereco
                msg += f"     📍 {end_curto}\n"
            if avaliacao:
                estrelas = "⭐" * int(float(avaliacao.split()[0])) if avaliacao.split() else ""
                msg += f"     ⭐ {avaliacao} {estrelas}\n"
            msg += "\n"

        if restantes > 0:
            msg += f"  _+{restantes} leads salvos no CSV_\n"

        msg += "\n"

    msg += "━" * 30 + "\n"
    msg += "💡 _CNPJ: consulte manualmente em casadosdados.com.br_\n"
    msg += "_ou pesquise \"Nome + CNPJ\" no Google_"

    return msg


def salvar_csv(leads, data_str):
    """Salva leads em CSV"""
    os.makedirs(DIR_LEADS, exist_ok=True)
    arquivo = f"{DIR_LEADS}/leads_{data_str.replace('/', '-')}.csv"

    campos = ["nome", "telefone", "endereco", "bairro", "tipo", "avaliacao"]
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(leads)

    return arquivo


def enviar_telegram(mensagem):
    """Envia mensagem via Telegram usando o CLI do Hermes"""
    try:
        # Usar o send_message do hermes via subprocess
        result = subprocess.run(
            ["hermes", "telegram", "send", "--message", mensagem],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            print("[OK] Mensagem enviada via Telegram")
            return True
        else:
            print(f"[ERRO] Telegram: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERRO] Telegram: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Bot Prospeccao")
    parser.add_argument("--run-now", action="store_true", help="Executa busca agora")
    parser.add_argument("--test", action="store_true", help="Modo teste (1 bairro)")
    parser.add_argument(
        "--format-only", type=str, help="Formata e envia leads de CSV existente"
    )
    args = parser.parse_args()

    data_str = datetime.now().strftime("%d/%m/%Y")
    print(f"{'='*60}")
    print(f"BOT PROSPECAO - {data_str}")
    print(f"{'='*60}")

    # Se for apenas formatar CSV existente
    if args.format_only:
        leads = []
        with open(args.format_only, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                leads.append(row)
        leads_por_bairro = defaultdict(list)
        for l in leads:
            leads_por_bairro[l["bairro"]].append(l)
        msg = formatar_mensagem(leads_por_bairro, data_str)
        print(msg)
        return

    print(f"\n[INFO] Este script gera o comando para o Hermes executar.")
    print(f"[INFO] O scraping real e feito pelo agente Hermes via browser.")
    print(f"[INFO] Bairros configurados: {len(BAIRROS)}")
    print(f"[INFO] Tipos de negocio: {len(TIPOS_NEGOCIO)}")
    print(f"[INFO] Total de buscas: {len(BAIRROS) * len(TIPOS_NEGOCIO)}")

    # Gerar relatorio de execucao
    relatorio = {
        "data": data_str,
        "bairros": BAIRROS,
        "tipos": TIPOS_NEGOCIO,
        "total_buscas": len(BAIRROS) * len(TIPOS_NEGOCIO),
        "arquivo_historico": ARQUIVO_HISTORICO,
        "diretorio_leads": DIR_LEADS,
    }

    relatorio_file = "/opt/projects/bot_prospeccao_config.json"
    with open(relatorio_file, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=2)

    print(f"\n[OK] Configuracao salva em {relatorio_file}")
    print(f"\n[INFO] Para busca automatica, o cron job do Hermes executa:")
    print(f"  1. Browser busca no Google Maps por bairro + tipo")
    print(f"  2. Extrai nome, telefone, endereco, avaliacao")
    print(f"  3. Agrupa por bairro (max 10 leads por grupo)")
    print(f"  4. Envia formatado no Telegram")
    print(f"\n[INFO] Execute 'hermes cron list' para ver o agendamento")


if __name__ == "__main__":
    main()
