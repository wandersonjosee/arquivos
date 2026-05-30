#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processador de leads - converte dados coletados do browser em formato final.
"""
import json
import re
import os

# Raw data collected from Google Maps browser searches
# Format: {bairro: {tipo: [[name, phone, rating, address], ...]}}
RAW = {}

def add_raw(bairro, tipo, data):
    if bairro not in RAW:
        RAW[bairro] = {}
    RAW[bairro][tipo] = data

def process_leads():
    """Convert raw data to final lead format"""
    leads = []
    for bairro, tipos in RAW.items():
        for tipo, items in tipos.items():
            for item in items:
                name = item[0].strip() if item[0] else ""
                phone = item[1].strip() if len(item) > 1 and item[1] else ""
                rating = item[2].strip() if len(item) > 2 and item[2] else ""
                address = item[3].strip() if len(item) > 3 and item[3] else ""
                
                if not name:
                    continue
                
                # Clean rating
                rating_num = ""
                m = re.search(r'[\d,]+', rating)
                if m:
                    rating_num = m.group(0).replace(',', '.')
                
                # Build address
                if address and bairro not in address:
                    full_address = f"{address}, {bairro}, Aparecida de Goiânia - GO"
                else:
                    full_address = f"{bairro}, Aparecida de Goiânia - GO"
                
                leads.append({
                    "nome": name,
                    "telefone": phone,
                    "endereco": full_address,
                    "bairro": bairro,
                    "tipo": tipo,
                    "avaliacao": rating_num
                })
    return leads

# All collected data from browser searches
# Jardim Monte Sinai
add_raw("Jardim Monte Sinai", "salão de beleza", [
    ["Dina Cabeleireira", "(62) 99451-7993", "4,9 estrelas", ""],
    ["Studio divas", "", "5,0 estrelas", "Praca Jose Bonifácio"],
    ["Studio Sublime", "", "4,0 estrelas", "Rua Dona Getúlia, 15"],
    ["Selma cabeleireira", "", "5,0 estrelas", "R. 58"],
    ["Studio Espaço Mulher", "", "5,0 estrelas", "Av. Arão de Souza"],
])
add_raw("Jardim Monte Sinai", "lanchonete", [
    ["Mr.mixlanches", "", "5,0 estrelas", "R. Maitanga"],
    ["Lanchonety Cezar", "", "5,0 estrelas", "Av. 8, qd 87 - lt 04"],
    ["Cantinho da Tia Lu", "", "5,0 estrelas", "Av. Brasil"],
    ["Egami Cafetería Lanches", "", "4,3 estrelas", "Av. Independência"],
    ["Sanduicheria Payol", "", "4,8 estrelas", "Av. Milão, Qd 14 - Lt 09"],
])
add_raw("Jardim Monte Sinai", "pizzaria", [
    ["Pizzaria Maná", "(62) 98155-3742", "4,1 estrelas", "Rua tesouraria"],
    ["Dozzotro Pizzaria", "(62) 99404-1173", "4,8 estrelas", ""],
    ["Pizzaria Monte Sinai", "(62) 3258-6567", "4,2 estrelas", "Av. Center"],
    ["Pizzaria Bouganville Grill", "(62) 99371-5672", "4,4 estrelas", "Avenida Atlântida"],
    ["Pizza Nativa", "(62) 99490-3299", "4,3 estrelas", "Rua Atenas qd 90 lt 1"],
    ["Pizzaria Milhão", "(62) 99673-9654", "4,8 estrelas", "R. 69-A"],
    ["Chivas pizzaria pro", "(62) 99405-3812", "4,4 estrelas", "Av. Arão de Souza"],
])
add_raw("Jardim Monte Sinai", "padaria", [
    ["Panificadora e Confeitaria Mondale", "", "4,3 estrelas", "Av. Independência"],
    ["Nova Panificadora", "", "4,6 estrelas", ""],
    ["Delfina Quitandeira", "", "4,9 estrelas", "R. Transamazônica"],
    ["Canto do Gallo Panificadora", "", "4,6 estrelas", "Av. das Nações"],
    ["Oliver Pães - Sabor&Requinte", "", "4,8 estrelas", ""],
])
add_raw("Jardim Monte Sinai", "farmácia", [
    ["Alexfarma Novo Horizonte", "(62) 3221-6880", "4,3 estrelas", "Avenida César Lattes"],
    ["Drogaria Benfica", "(62) 3537-3400", "3,7 estrelas", "Av. Arão de Souza"],
    ["Farmácia Preço Baixo", "(62) 3097-3035", "4,6 estrelas", ""],
    ["Drogaiza", "(62) 98550-6777", "3,7 estrelas", "Av. Independência"],
    ["Drogaria Marttins", "(62) 99402-0192", "4,7 estrelas", "Av. Independência"],
    ["Droga Nunes", "(62) 3222-6489", "4,7 estrelas", "Av. Central"],
    ["Drogaria Farma vida", "(62) 3579-0667", "5,0 estrelas", "R. Verona"],
])
add_raw("Jardim Monte Sinai", "drogaria", [
    ["Alexfarma Novo Horizonte", "(62) 3221-6880", "4,3 estrelas", "Avenida César Lattes"],
    ["Drogaria Benfica", "(62) 3537-3400", "3,7 estrelas", "Av. Arão de Souza"],
    ["Drogaria Farma vida", "(62) 3579-0667", "5,0 estrelas", "R. Verona"],
    ["Farmácia Hiper Popular", "(62) 3537-0020", "4,2 estrelas", "Avenida C-4 QD 37 LT 13-E"],
    ["Droga Nunes", "(62) 3222-6489", "4,7 estrelas", "Av. Central"],
    ["Drogaiza", "(62) 98550-6777", "3,7 estrelas", "Av. Independência"],
    ["Farmácia Preço Baixo", "(62) 3097-3035", "4,6 estrelas", ""],
])
add_raw("Jardim Monte Sinai", "pet shop", [
    ["Au Au Salão de Beleza para Cães", "(62) 99147-5404", "5,0 estrelas", "Avenida 2ª Radial"],
    ["Clínica Veterinária Titiu", "(62) 3636-3136", "4,4 estrelas", "Avenida 4ª Radial"],
    ["Clínica e Pet Shop Mundo Dos Animais", "(62) 3248-0605", "4,6 estrelas", ""],
    ["Zeus Center Pet Atacarejo", "(62) 99222-5258", "5,0 estrelas", "Av. Argélia"],
    ["Clínica e Pet Shop Cães e Cia", "(62) 99131-4366", "4,9 estrelas", ""],
])
add_raw("Jardim Monte Sinai", "óptica", [
    ["Óticas Carol", "(62) 98193-2060", "3,9 estrelas", "Avenida Rio Verde"],
    ["Ótica Aparecida Dr Óculos", "(62) 99817-8624", "4,9 estrelas", "Av. Independência"],
    ["Otica loove", "(62) 99271-5452", "5,0 estrelas", "R. Albatroz"],
    ["Ótica Flay Premium", "(62) 98600-5368", "4,4 estrelas", "Av. Independência"],
    ["Óticas Camelo", "(62) 99232-1114", "4,9 estrelas", "Av. Independência"],
])
add_raw("Jardim Monte Sinai", "loja de roupas", [
    ["Bazar Emanuel modas", "(62) 98201-2242", "", "R. 66, Quadra 125"],
    ["GRINGO STORE GYN", "(62) 98117-7862", "5,0 estrelas", "Av. Arão de Souza, Qd 173 - Lt 1"],
])
add_raw("Jardim Monte Sinai", "material de construção", [
    ["Ferragista Bezerra", "(62) 99186-8265", "4,6 estrelas", "Rua 70 S/N Qd 196 Lt 44"],
])
add_raw("Jardim Monte Sinai", "distribuidora", [
    ["Santana Gás", "(62) 99329-6410", "5,0 estrelas", "Rua 58 Qd.147b, lt 01"],
])
add_raw("Jardim Monte Sinai", "restaurante", [
    ["Santana Gás", "(62) 99329-6410", "5,0 estrelas", "Rua 58 Qd.147b, lt 01"],
    ["AG Paisagismo e Floricultura", "(62) 99337-4923", "3,0 estrelas", "Rua Francisco Frota Soares Qd. 6 Lt. 4/5"],
])

# Jardim Riviera
add_raw("Jardim Riviera", "salão de beleza", [
    ["Studio Elizabeth Krause", "", "5,0 estrelas", "Av. Carlos Alberto Vanderlei"],
    ["CIDA CABELELEIROS", "", "4,8 estrelas", ""],
    ["Eli Clara Salão de Beleza", "", "", "Av. Juscelino Kubitscheck"],
    ["Ivailde moreira cabeleireira", "", "4,2 estrelas", "R. Olávo de Castro"],
    ["Studio Veras Beleza E Estética", "", "", "R. Marília Braga"],
])

if __name__ == "__main__":
    leads = process_leads()
    
    # Filter out invalid leads
    skip_keywords = ['barbearia', 'oficina', 'mecânica', 'posto de gasolina', 'auto center']
    filtered = []
    for lead in leads:
        combined = ' '.join(lead.values()).lower()
        skip = False
        for kw in skip_keywords:
            if kw in combined:
                skip = True
                break
        if not skip:
            filtered.append(lead)
    
    print(f"Total leads: {len(filtered)}")
    
    # Save
    output_file = "/opt/projects/leads_diarios/leads_brutos_2026-05-28.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)
    
    print(f"Saved to {output_file}")
    
    # Show summary by bairro
    from collections import defaultdict
    by_bairro = defaultdict(int)
    for lead in filtered:
        by_bairro[lead["bairro"]] += 1
    
    for bairro, count in sorted(by_bairro.items()):
        print(f"  {bairro}: {count} leads")
