#!/usr/bin/env python3
"""
Lead scraper - extracts all data from Google Maps via browser JavaScript injection.
"""
import json
import re
import subprocess
import sys

# This script formats data extracted via browser JS into the leads format.
# The browser JS extraction is done via hermes browser console tool.

def parse_raw_extraction(raw_data, bairro, tipo):
    """Parse raw extraction data into structured leads."""
    leads = []
    for item in raw_data:
        name = item.get('name', '').strip()
        phone = item.get('phone', '').strip()
        rating = item.get('rating', '').strip()
        address = item.get('address', '').strip()
        raw = item.get('raw', '')
        
        if not name:
            continue
        
        # Skip if name matches neighborhood or city
        if name.lower() == bairro.lower() or name.lower() == 'aparecida de goiânia':
            continue
        
        # Clean up address - extract from raw if needed
        if not address:
            addr_match = re.search(r'(R\.|Av\.|Rua|Avenida|Est\.)[^<\n]*', raw)
            if addr_match:
                address = addr_match.group(0).strip()
        
        # Clean address
        address = re.sub(r'\s+', ' ', address).strip()
        address = re.sub(r'^(Salão|Brechó|Floricultura|Companhia|Loja|Ferragista)\s+.*$', '', address).strip()
        
        # Extract rating number
        rating_num = ''
        if rating:
            num_match = re.search(r'[\d,]+', rating)
            if num_match:
                rating_num = num_match.group(0).replace(',', '.')
        
        # Extract phone from raw if not found
        if not phone:
            phone_match = re.search(r'\(62\)\s*\d{4,5}-\d{4}', raw)
            if phone_match:
                phone = phone_match.group(0)
        
        lead = {
            'nome': name,
            'telefone': phone,
            'endereco': address if address else f"{bairro}, Aparecida de Goiânia - GO",
            'bairro': bairro,
            'tipo': tipo,
            'avaliacao': rating_num
        }
        leads.append(lead)
    
    return leads


if __name__ == "__main__":
    # Read raw data from stdin
    raw_json = sys.stdin.read()
    data = json.loads(raw_json)
    
    all_leads = []
    for entry in data:
        bairro = entry['bairro']
        tipo = entry['tipo']
        items = entry['items']
        
        leads = parse_raw_extraction(items, bairro, tipo)
        
        # Filter out non-relevant businesses
        filtered = []
        skip_types = ['barbearia', 'oficina', 'mecânica', 'posto', 'gasolina']
        for lead in leads:
            raw_text = ' '.join(lead.values()).lower()
            skip = False
            for st in skip_types:
                if st in raw_text:
                    skip = True
                    break
            if not skip:
                filtered.append(lead)
        
        all_leads.extend(filtered)
    
    print(json.dumps(all_leads, ensure_ascii=False, indent=2))
