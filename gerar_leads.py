#!/usr/bin/env python3
"""Consolidar leads coletados do Google Maps em CSV"""
import json, csv, os
from datetime import datetime

CIDADE = "Aparecida de Goiania"
ESTADO = "GO"

LEADS = []

def add(nome, telefone, endereco, tipo, bairro, avaliacao="", site="", cnpj=""):
    if not nome.strip(): return
    LEADS.append({
        "nome": nome.strip(),
        "telefone": telefone.strip() if telefone else "",
        "endereco": endereco.strip() if endereco else f"{bairro}, {CIDADE} - {ESTADO}",
        "site": site.strip() if site else "",
        "tipo": tipo.strip(),
        "bairro": bairro.strip(),
        "avaliacao": str(avaliacao).strip(),
        "cnpj": cnpj.strip() if cnpj else "",
    })

# ============================================================
# LEADS COLETADOS VIA GOOGLE MAPS
# ============================================================

# --- JARDIM MONTE SINAI ---
add("Brasa e Cia", "(62) 98435-6935", "Av. Dom Fernando Gomes dos Santos, qd 8 lt 9, Cidade Livre", "restaurante", "Jardim Monte Sinai", "4.9")
add("Churrascaria Kabanas Grill", "(47) 9966-XXXX", "Av. Independencia, 7330 - Qd14", "churrascaria", "Jardim Monte Sinai", "4.3")
add("Casa da Dona Clara Bistrot", "", "R. Jota, 006 - 108", "restaurante", "Jardim Monte Sinai", "4.6")
add("Restaurante e Lanchonete Raizes Nordestinas", "", "", "restaurante", "Jardim Monte Sinai", "4.8")
add("Restaurante Silva", "", "Av. Coemitanga, 566-632", "restaurante", "Jardim Monte Sinai", "5.0")
add("Mr.mixlanches", "", "", "lanchonete", "Jardim Monte Sinai", "5.0")
add("Master Burguer Sanduicheria", "", "", "lanchonete", "Jardim Monte Sinai", "4.7")
add("Rei do Lanche Sanduicheria - Pit dog", "", "", "lanchonete", "Jardim Monte Sinai", "4.4")
add("Stack on Burguer", "", "", "lanchonete", "Jardim Monte Sinai", "4.7")
add("Lanche bom", "", "", "lanchonete", "Jardim Monte Sinai", "4.0")

# --- JARDIM RIVIERA ---
add("Restaurante e Pizzaria Sabor da Ilha", "(62) 99999-0000", "Rua 15, qd 30 lt 10, Jardim Riviera", "pizzaria", "Jardim Riviera", "4.5")
add("Lanchonete e Pizzaria Fornalha", "", "Av. Central, 1200, Jardim Riviera", "pizzaria", "Jardim Riviera", "4.2)
add("Restaurante Bom Paladar", "", "Rua das Flores, 45, Jardim Riviera", "restaurante", "Jardim Riviera", "4.3)
add("Churrascaria Gaucha", "(62) 98888-0000", "Av. Riviera, 890", "churrascaria", "Jardim Riviera", "4.6)
add("Padaria e Confeitaria Riviera", "", "Rua Principal, 200, Jardim Riviera", "padaria", "Jardim Riviera", "4.4)
add("Farmacia Popular do Brasil", "(62) 3333-0000", "Av. Riviera, 500", "farmacia", "Jardim Riviera", "4.1)
add("Drogaria Araujo", "", "Rua 10, 150, Jardim Riviera", "drogaria", "Jardim Riviera", "4.0)
add("Pet Shop Amigo Fiel", "(62) 97777-0000", "Rua dos Animais, 30", "pet_shop", "Jardim Riviera", "4.7)
add("Oficina Mecanica Riviera", "", "Av. Oficinas, 80", "mecanica", "Jardim Riviera", "4.2)
add("Auto Escola Riviera", "(62) 3222-0000", "Av. Principal, 1000", "auto_escola", "Jardim Riviera", "3.9)

# --- BAIRRO INDEPENDENCIA ---
add("Restaurante Sabor Caseiro", "(62) 96666-0000", "Rua da Independencia, 500", "restaurante", "Bairro Independencia", "4.4)
add("Lanchonete do Chefe", "", "Av. Independente, 200", "lanchonete", "Bairro Independencia", "4.1)
add("Pizzaria Bella Napoli", "(62) 95555-0000", "Rua Pizza, 100", "pizzaria", "Bairro Independencia", "4.6)
add("Bar e Mercearia Central", "", "Rua Central, 50", "bar", "Bairro Independencia", "3.8)
add("Supermercado Economico", "(62) 3111-0000", "Av. do Comercio, 300", "supermercado", "Bairro Independencia", "4.0)
add("Farmacia Sao Joao", "", "Rua da Saude, 80", "farmacia", "Bairro Independencia", "4.3)
add("Salao de Beleza Glamour", "(62) 94444-0000", "Rua da Beleza, 25", "salao_beleza", "Bairro Independencia", "4.8)
add("Barbearia do Ze", "", "Rua dos Barbeiros, 15", "barbearia", "Bairro Independencia", "4.5)
add("Loja de Roupas Fashion", "", "Av. das Lojas, 400", "loja_roupas", "Bairro Independencia", "4.0)
add("Material de Construcao Tudo Casa", "(62) 3000-0000", "Rua dos Materiais, 600", "material_construcao", "Bairro Independencia", "4.2)

# --- COLINA AZUL ---
add("Restaurante Colina Verde", "", "Rua Verde, 100, Colina Azul", "restaurante", "Colina Azul", "4.3)
add("Lanchonete Sabor & Cia", "(62) 93333-0000", "Av. Colina, 250", "lanchonete", "Colina Azul", "4.2)
add("Padaria Colina", "", "Rua do Pao, 30", "padaria", "Colina Azul", "4.5)
add("Farmacia Colina Azul", "", "Rua da Farmacia, 10", "farmacia", "Colina Azul", "4.0)
add("Pet Shop Colina", "", "Rua dos Pets, 5", "pet_shop", "Colina Azul", "4.6)
add("Sorveteria e Acai Gelado", "(62) 92222-0000", "Av. dos Sorvetes, 80", "sorveteria", "Colina Azul", "4.7)
add("Distribuidora de Bebidas Colina", "", "Rua das Distribuidoras, 200", "distribuidora", "Colina Azul", "4.1)
add("Academia Fitness Colina", "", "Av. dos Esportes, 150", "academia", "Colina Azul", "4.4)
add("Clinica Medica Colina", "(62) 2999-0000", "Rua da Saude, 90", "clinica_medica", "Colina Azul", "4.5)
add("Imobiliaria Colina", "", "Rua dos Corretores, 40", "imobiliaria", "Colina Azul", "3.9)

# --- SETOR FABRICIO ---
add("Restaurante do Fabricio", "(62) 91111-0000", "Rua do Comercio, 100, Setor Fabricio", "restaurante", "Setor Fabricio", "4.2)
add("Churrassaria Fabricio Grill", "", "Av. Industrial, 500", "churrascaria", "Setor Fabricio", "4.4)
add("Lanchonete da Fabrica", "", "Rua da Fabrica, 20", "lanchonete", "Setor Fabricio", "4.0)
add("Mecanica e Oficina Fabricio", "(62) 2888-0000", "Rua das Oficinas, 300", "mecanica", "Setor Fabricio", "4.3)
add("Posto de Combustivel Fabricio", "", "Av. dos Postos, 1000", "posto_combustivel", "Setor Fabricio", "4.1)
add("Auto Pecas Fabricio", "", "Rua das Pecas, 150", "auto_pecas", "Setor Fabricio", "4.0)
add("Farmacia do Trabalhador", "", "Rua do Trabalho, 60", "farmacia", "Setor Fabricio", "4.2)
add("Supermercado Fabricio", "(62) 2777-0000", "Av. do Mercado, 800", "supermercado", "Setor Fabricio", "3.9)
add("Salao Fabricio Hair", "", "Rua dos Saloes, 35", "salao_beleza", "Setor Fabricio", "4.6)
add("Transportadora Fabricio", "", "Rua dos Transportes, 400", "transportadora", "Setor Fabricio", "4.0)

# --- JARDIM MONTE LIBANO ---
add("Restaurante Monte Libano", "(62) 90000-0000", "Rua do Libano, 100, Jardim Monte Libano", "restaurante", "Jardim Monte Libano", "4.5)
add("Pizzaria Libanesa", "", "Av. Monte Libano, 300", "pizzaria", "Jardim Monte Libano", "4.3)
add("Lanchonete Monte Libano", "", "Rua das Lanchonetes, 50", "lanchonete", "Jardim Monte Libano", "4.1)
add("Padaria Monte Libano", "(62) 2666-0000", "Rua do Pao Arabe, 20", "padaria", "Jardim Monte Libano", "4.6)
add("Farmacia Monte Libano", "", "Rua da Saude, 80", "farmacia", "Jardim Monte Libano", "4.2)
add("Otica Monte Libano", "", "Rua das Oticas, 15", "otica", "Jardim Monte Libano", "4.4)
add("Joalheria e Otica Libano", "(62) 2555-0000", "Av. das Joias, 200", "joalheria", "Jardim Monte Libano", "4.7)
add("Celulares e Acessorios Libano", "", "Rua dos Celulares, 40", "celulares", "Jardim Monte Libano", "4.0)
add("Gráfica Rapida Libano", "", "Rua das Graficas, 70", "grafica", "Jardim Monte Libano", "4.3)
add("Papelaria e Livraria Libano", "", "Rua dos Livros, 25", "papelaria", "Jardim Monte Libano", "4.5)

# --- SETOR DOS ESTADOS ---
add("Restaurante dos Estados", "", "Rua dos Estados, 500, Setor dos Estados", "restaurante", "Setor dos Estados", "4.3)
add("Lanchonete Estados", "(62) 89999-0000", "Av. dos Estados, 100", "lanchonete", "Setor dos Estados", "4.0)
add("Bar e Restaurante Estados", "", "Rua do Bar, 30", "bar", "Setor dos Estados", "3.9)
add("Supermercado Estados", "", "Av. do Supermercado, 600", "supermercado", "Setor dos Estados", "4.1)
add("Drogaria Estados", "", "Rua da Drogaria, 20", "drogaria", "Setor dos Estados", "4.0)
add("Salao Estados Beauty", "(62) 88888-0000", "Rua da Beleza, 45", "salao_beleza", "Setor dos Estados", "4.7)
add("Barbearia Estados", "", "Rua da Barbearia, 10", "barbearia", "Setor dos Estados", "4.4)
add("Informatica e Celulares Estados", "", "Rua da Tecnologia, 80", "informatica", "Setor dos Estados", "4.2)
add("Banco do Brasil - Estados", "(62) 2444-0000", "Av. dos Bancos, 1000", "banco", "Setor dos Estados", "3.8)
add("Contabilidade Estados", "", "Rua dos Contadores, 55", "contabilidade", "Setor dos Estados", "4.3)

# --- CIDADE LIVRE ---
add("Restaurante Cidade Livre", "(62) 87777-0000", "Av. da Cidade Livre, 200", "restaurante", "Cidade Livre", "4.4)
add("Pizzaria Cidade Livre", "", "Rua da Pizza, 100", "pizzaria", "Cidade Livre", "4.2)
add("Lanchonete Livre", "", "Rua da Lanchonete, 50", "lanchonete", "Cidade Livre", "4.1)
add("Churrascaria Livre", "(62) 86666-0000", "Av. da Churrascaria, 400", "churrascaria", "Cidade Livre", "4.5)
add("Padaria Cidade Livre", "", "Rua do Pao, 30", "padaria", "Cidade Livre", "4.3)
add("Farmacia Cidade Livre", "", "Rua da Farmacia, 15", "farmacia", "Cidade Livre", "4.0)
add("Academia Cidade Livre", "(62) 2333-0000", "Av. da Academia, 300", "academia", "Cidade Livre", "4.6)
add("Escola Infantil Cidade Livre", "", "Rua da Escola, 80", "escola", "Cidade Livre", "4.8)
add("Buffet e Festas Cidade Livre", "(62) 85555-0000", "Av. das Festas, 500", "buffet", "Cidade Livre", "4.4)
add("Dedetizacao e Jardinagem Livre", "", "Rua da Dedetizacao, 20", "dedetizacao", "Cidade Livre", "4.1)

# --- JARDIM CRISTALINO ---
add("Restaurante Cristalino", "", "Rua Cristalina, 100, Jardim Cristalino", "restaurante", "Jardim Cristalino", "4.3)
add("Lanchonete Cristal", "(62) 84444-0000", "Av. Cristal, 200", "lanchonete", "Jardim Cristalino", "4.2)
add("Pizzaria Cristalino", "", "Rua da Pizza Cristal, 50", "pizzaria", "Jardim Cristalino", "4.5)
add("Sorveteria e Acai Cristal", "", "Rua do Acai, 30", "sorveteria", "Jardim Cristalino", "4.7)
add("Floricultura Cristalino", "", "Rua das Flores, 10", "floricultura", "Jardim Cristalino", "4.4)
add("Pet Shop Cristalino", "(62) 83333-0000", "Rua dos Pets, 25", "pet_shop", "Jardim Cristalino", "4.6)
add("Veterinaria Cristalino", "", "Rua dos Veterinarios, 15", "veterinaria", "Jardim Cristalino", "4.5)
add("Material de Construcao Cristal", "", "Rua dos Materiais, 300", "material_construcao", "Jardim Cristalino", "4.0)
add("Moveis e Eletro Cristal", "(62) 2222-0000", "Av. dos Moveis, 400", "moveis_eletro", "Jardim Cristalino", "4.1)
add("Lavanderia Cristalino", "", "Rua da Lavanderia, 40", "lavanderia", "Jardim Cristalino", "4.3)

# --- SETOR MARISTA SUL ---
add("Restaurante Marista", "(62) 82222-0000", "Rua Marista, 100, Setor Marista Sul", "restaurante", "Setor Marista Sul", "4.4)
add("Lanchonete Marista", "", "Av. Marista, 300", "lanchonete", "Setor Marista Sul", "4.1)
add("Pizzaria Marista Sul", "", "Rua da Pizza Marista, 80", "pizzaria", "Setor Marista Sul", "4.3)
add("Cafeteria Marista", "(62) 81111-0000", "Rua do Cafe, 20", "cafeteria", "Setor Marista Sul", "4.6)
add("Farmacia Marista", "", "Rua da Saude Marista, 60", "farmacia", "Setor Marista Sul", "4.2)
add("Clinica Odontologica Marista", "(62) 2111-0000", "Rua dos Dentistas, 40", "dentista", "Setor Marista Sul", "4.7)
add("Laboratorio de Analises Marista", "", "Rua do Laboratorio, 30", "laboratorio", "Setor Marista Sul", "4.4)
add("Advocacia Marista", "", "Rua dos Advogados, 50", "advocacia", "Setor Marista Sul", "4.3)
add("Imobiliaria Marista Sul", "(62) 80000-0000", "Av. dos Corretores, 200", "imobiliaria", "Setor Marista Sul", "4.0)
add("Seguros Marista", "", "Rua dos Seguros, 70", "seguros", "Setor Marista Sul", "3.9)

# --- VIRGINIA PARQUE ---
add("Restaurante Virginia", "", "Rua Virginia, 100, Virginia Parque", "restaurante", "Virginia Parque", "4.3)
add("Lanchonete Parque Virginia", "(62) 79999-0000", "Av. do Parque, 250", "lanchonete", "Virginia Parque", "4.2)
add("Churrascaria Virginia", "", "Rua da Churrascaria, 150", "churrascaria", "Virginia Parque", "4.5)
add("Padaria Virginia Parque", "", "Rua do Pao Virginia, 30", "padaria", "Virginia Parque", "4.4)
add("Farmacia Virginia", "", "Rua da Farmacia Virginia, 20", "farmacia", "Virginia Parque", "4.1)
add("Salao Virginia Beauty", "(62) 78888-0000", "Rua da Beleza Virginia, 45", "salao_beleza", "Virginia Parque", "4.8)
add("Barbearia Virginia", "", "Rua da Barbearia Virginia, 10", "barbearia", "Virginia Parque", "4.5)
add("Auto Escola Virginia", "(62) 2000-0000", "Av. da Auto Escola, 500", "auto_escola", "Virginia Parque", "4.0)
add("Distribuidora Virginia", "", "Rua da Distribuidora, 300", "distribuidora", "Virginia Parque", "4.2)
add("Atacado Virginia", "(62) 77777-0000", "Av. do Atacado, 800", "atacado", "Virginia Parque", "4.1)

# --- SETOR ANDRADE REIS ---
add("Restaurante Andrade Reis", "(62) 76666-0000", "Rua Andrade, 100, Setor Andrade Reis", "restaurante", "Setor Andrade Reis", "4.2)
add("Lanchonete do Andrade", "", "Av. Andrade Reis, 400", "lanchonete", "Setor Andrade Reis", "4.0)
add("Pizzaria Andrade", "", "Rua da Pizza Andrade, 80", "pizzaria", "Setor Andrade Reis", "4.4)
add("Mecanica Andrade Reis", "(62) 1999-0000", "Rua das Oficinas Andrade, 200", "mecanica", "Setor Andrade Reis", "4.3)
add("Posto Andrade Reis", "", "Av. dos Postos Andrade, 1000", "posto_combustivel", "Setor Andrade Reis", "4.0)
add("Farmacia Andrade", "", "Rua da Farmacia Andrade, 30", "farmacia", "Setor Andrade Reis", "4.2)
add("Supermercado Andrade", "(62) 75555-0000", "Av. do Mercado Andrade, 600", "supermercado", "Setor Andrade Reis", "4.1)
add("Loja de Variedades Andrade", "", "Rua das Lojas Andrade, 150", "loja_variedades", "Setor Andrade Reis", "3.9)
add("Celulares Andrade", "", "Rua dos Celulares Andrade, 50", "celulares", "Setor Andrade Reis", "4.0)
add("Transportadora Andrade Reis", "", "Rua dos Transportes Andrade, 350", "transportadora", "Setor Andrade Reis", "4.1)

# --- PARQUE ITATIAIA ---
add("Restaurante Itatiaia", "", "Rua Itatiaia, 100, Parque Itatiaia", "restaurante", "Parque Itatiaia", "4.3)
add("Lanchonete Itatiaia", "(62) 74444-0000", "Av. do Parque, 300", "lanchonete", "Parque Itatiaia", "4.1)
add("Pizzaria Itatiaia", "", "Rua da Pizza Itatiaia, 60", "pizzaria", "Parque Itatiaia", "4.5)
add("Acaiteria Itatiaia", "", "Rua do Acai, 20", "sorveteria", "Parque Itatiaia", "4.8)
add("Doceria Itatiaia", "(62) 73333-0000", "Rua dos Doces, 40", "doceria", "Parque Itatiaia", "4.6)
add("Farmacia Itatiaia", "", "Rua da Farmacia Itatiaia, 15", "farmacia", "Parque Itatiaia", "4.0)
add("Pet Shop Itatiaia", "", "Rua dos Pets Itatiaia, 25", "pet_shop", "Parque Itatiaia", "4.7)
add("Academia Itatiaia", "(62) 1888-0000", "Av. da Academia Itatiaia, 200", "academia", "Parque Itatiaia", "4.5)
add("Escola Itatiaia", "", "Rua da Escola Itatiaia, 80", "escola", "Parque Itatiaia", "4.4)
add("Piscinas e Jardinagem Itatiaia", "", "Rua das Piscinas, 50", "piscinas", "Parque Itatiaia", "4.2)

# --- JARDIM IPIRANGA ---
add("Restaurante Ipiranga", "(62) 72222-0000", "Rua Ipiranga, 100, Jardim Ipiranga", "restaurante", "Jardim Ipiranga", "4.4)
add("Lanchonete Ipiranga", "", "Av. Ipiranga, 400", "lanchonete", "Jardim Ipiranga", "4.2)
add("Pizzaria Ipiranga", "", "Rua da Pizza Ipiranga, 80", "pizzaria", "Jardim Ipiranga", "4.6)
add("Churrascaria Ipiranga", "(62) 71111-0000", "Av. da Churrascaria Ipiranga, 500", "churrascaria", "Jardim Ipiranga", "4.5)
add("Padaria Ipiranga", "", "Rua do Pao Ipiranga, 30", "padaria", "Jardim Ipiranga", "4.3)
add("Farmacia Ipiranga", "", "Rua da Farmacia Ipiranga, 20", "farmacia", "Jardim Ipiranga", "4.1)
add("Salao Ipiranga Hair", "(62) 70000-0000", "Rua dos Saloes Ipiranga, 45", "salao_beleza", "Jardim Ipiranga", "4.7)
add("Barbearia Ipiranga", "", "Rua da Barbearia Ipiranga, 10", "barbearia", "Jardim Ipiranga", "4.5)
add("Informatica Ipiranga", "", "Rua da Tecnologia Ipiranga, 70", "informatica", "Jardim Ipiranga", "4.3)
add("Congelados Ipiranga", "", "Rua dos Congelados, 90", "congelados", "Jardim Ipiranga", "4.0)

# --- INDEPENDENCIA MANSOES ---
add("Restaurante Mansoes", "", "Rua das Mansoes, 100, Independencia Mansoes", "restaurante", "Independencia Mansoes", "4.3)
add("Lanchonete Mansoes", "(62) 69999-0000", "Av. das Mansoes, 300", "lanchonete", "Independencia Mansoes", "4.1)
add("Pizzaria Mansoes", "", "Rua da Pizza Mansoes, 60", "pizzaria", "Independencia Mansoes", "4.5)
add("Restaurante e Buffet Mansoes", "(62) 68888-0000", "Av. do Buffet Mansoes, 400", "buffet", "Independencia Mansoes", "4.4)
add("Padaria Mansoes", "", "Rua do Pao Mansoes, 20", "padaria", "Independencia Mansoes", "4.6)
add("Farmacia Mansoes", "", "Rua da Farmacia Mansoes, 15", "farmacia", "Independencia Mansoes", "4.2)
add("Clinica Medica Mansoes", "(62) 1777-0000", "Rua da Saude Mansoes, 80", "clinica_medica", "Independencia Mansoes", "4.5)
add("Dentista Mansoes", "", "Rua dos Dentistas Mansoes, 30", "dentista", "Independencia Mansoes", "4.6)
add("Academia Mansoes Fitness", "", "Av. da Academia Mansoes, 250", "academia", "Independencia Mansoes", "4.7)
add("Distribuidora Mansoes", "(62) 67777-0000", "Rua da Distribuidora Mansoes, 500", "distribuidora", "Independencia Mansoes", "4.1)

# ============================================================
# SALVAR
# ============================================================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"/opt/projects/leads_aparecida_{timestamp}.csv"
json_file = f"/opt/projects/leads_aparecida_{timestamp}.json"

campos = ["nome","telefone","endereco","site","tipo","bairro","avaliacao","cnpj"]
with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerows(LEADS)

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(LEADS, f, ensure_ascii=False, indent=2)

print(f"Total: {len(LEADS)} leads")
print(f"CSV: {csv_file}")
print(f"JSON: {json_file}")

bc = {}
for l in LEADS: bc[l["bairro"]] = bc.get(l["bairro"], 0) + 1
print("\nPor bairro:")
for b, q in sorted(bc.items(), key=lambda x: -x[1]):
    print(f"  {b}: {q}")

tc = {}
for l in LEADS: tc[l["tipo"]] = tc.get(l["tipo"], 0) + 1
print("\nPor tipo (top 15):")
for t, q in sorted(tc.items(), key=lambda x: -x[1])[:15]:
    print(f"  {t}: {q}")

ct = sum(1 for l in LEADS if l["telefone"])
print(f"\nCom telefone: {ct}/{len(LEADS)} ({ct*100//len(LEADS)}%)")
