#!/usr/bin/env python3
"""Gerar leads consolidados das barbearias"""
import json, csv
from datetime import datetime

CIDADE = "Aparecida de Goiania"
ESTADO = "GO"

leads = [
    # Jardim Monte Sinai (coletados via Google Maps)
    {"nome": "Brutos Barbearia", "telefone": "(62) 99415-2445", "endereco": "Av. Independencia, qd.04 - lt.08 Sala 01 - Jardim Monte Cristo", "bairro": "Jardim Monte Sinai", "avaliacao": "5.0", "cnpj": ""},
    {"nome": "D.S. Barbearia", "telefone": "", "endereco": "Av. das Nacoes, qd-25 - lt 22", "bairro": "Jardim Monte Sinai", "avaliacao": "4.9", "cnpj": ""},
    {"nome": "MR Barbearia", "telefone": "", "endereco": "Av. Amazonas, Qd 12 - Lt 01 casa 2", "bairro": "Jardim Monte Sinai", "avaliacao": "4.9", "cnpj": ""},
    {"nome": "BARBEARIA AF", "telefone": "", "endereco": "Av. W-5, Quadra 25 - lote 09", "bairro": "Jardim Monte Sinai", "avaliacao": "5.0", "cnpj": ""},
    {"nome": "Wesley Borges Barbearia", "telefone": "", "endereco": "R. Nordeste", "bairro": "Jardim Monte Sinai", "avaliacao": "4.9", "cnpj": ""},
    {"nome": "Tarzan Barbearia & Piercing Studio", "telefone": "", "endereco": "", "bairro": "Jardim Monte Sinai", "avaliacao": "", "cnpj": ""},
    {"nome": "Barbearia Capelli", "telefone": "", "endereco": "", "bairro": "Jardim Monte Sinai", "avaliacao": "", "cnpj": ""},
    {"nome": "Barbearia Esto Vir", "telefone": "", "endereco": "", "bairro": "Jardim Monte Sinai", "avaliacao": "", "cnpj": ""},

    # Jardim Riviera (coletados via Google Maps)
    {"nome": "Metropoles barbearia", "telefone": "(62) 99434-1381", "endereco": "Av. Benedito Silvestre de Toledo, QD 01 - LT 21", "bairro": "Jardim Riviera", "avaliacao": "5.0", "cnpj": ""},
    {"nome": "K3 Barbearia", "telefone": "", "endereco": "R. Sabia, 1356-1440", "bairro": "Jardim Riviera", "avaliacao": "5.0", "cnpj": ""},
    {"nome": "BARBEARIA METROPOLES", "telefone": "", "endereco": "Av. Dr. Pedro L. Teixeira, 246", "bairro": "Jardim Riviera", "avaliacao": "5.0", "cnpj": ""},
    {"nome": "Wesley Borges Barbearia", "telefone": "", "endereco": "R. Nordeste", "bairro": "Jardim Riviera", "avaliacao": "4.9", "cnpj": ""},
    {"nome": "Messyas Barbearia", "telefone": "", "endereco": "", "bairro": "Jardim Riviera", "avaliacao": "5.0", "cnpj": ""},

    # Geral Aparecida de Goiania
    {"nome": "Barbearia stilus", "telefone": "", "endereco": "Av. Flamingo, 547", "bairro": "Outros", "avaliacao": "4.6", "cnpj": ""},
    {"nome": "Barbearia Detroit", "telefone": "", "endereco": "Av. Dom Fernando Gomes dos Santos, 336", "bairro": "Outros", "avaliacao": "4.9", "cnpj": ""},
    {"nome": "Barbearia Martins", "telefone": "", "endereco": "Rua das Gaivotas, R. Quirua, lt 05", "bairro": "Outros", "avaliacao": "4.9", "cnpj": ""},
    {"nome": "FVM Barbearia", "telefone": "", "endereco": "R. das Gaivotas, QD24 lt03", "bairro": "Outros", "avaliacao": "", "cnpj": ""},
]

# Deduplicar
vistos = set()
unicos = []
for l in leads:
    chave = l["nome"].lower().strip() + "|" + l["bairro"].lower().strip()
    if chave not in vistos:
        vistos.add(chave)
        l["data_captacao"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        unicos.append(l)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"/opt/projects/leads_barbearia_{timestamp}.csv"
json_file = f"/opt/projects/leads_barbearia_{timestamp}.json"

campos = ["nome", "telefone", "endereco", "bairro", "avaliacao", "cnpj", "data_captacao"]
with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerows(unicos)

print(f"Total: {len(unicos)} leads unicos")
print(f"CSV: {csv_file}")

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(unicos, f, ensure_ascii=False, indent=2)
print(f"JSON: {json_file}")

print("\nPor bairro:")
bc = {}
for l in unicos:
    b = l["bairro"]
    bc[b] = bc.get(b, 0) + 1
for b, q in sorted(bc.items(), key=lambda x: -x[1]):
    print(f"  {b}: {q}")

print(f"\nCom telefone: {sum(1 for l in unicos if l['telefone'])}/{len(unicos)}")
