#!/usr/bin/env python3
"""
Orquestrador de scraping - inicia o browser e coleta dados.
Vai navegar para cada busca e extrair dados via JS.
"""
import json
import sys
import re

# Template da funcao JS para extracao
JS_EXTRACT = r"""
(function() { 
  var results = []; 
  var articles = document.querySelectorAll('[role="article"]'); 
  for (var i = 0; i < articles.length; i++) { 
    var a = articles[i]; 
    var text = a.innerText || ''; 
    var links = a.querySelectorAll('a'); 
    var name = ''; 
    for (var j = 0; j < links.length; j++) { 
      if (links[j].href && links[j].href.indexOf('maps/place') >= 0) { 
        name = links[j].textContent.trim(); 
        break; 
      } 
    } 
    if (!name && links.length > 0) name = links[0].textContent.trim(); 
    var phoneMatch = text.match(/\(62\)\s*\d{4,5}-\d{4}/g); 
    var phone = phoneMatch ? phoneMatch[0] : ''; 
    var allAria = a.querySelectorAll('[aria-label]'); 
    var rating = ''; 
    for (var k = 0; k < allAria.length; k++) { 
      var lbl = allAria[k].getAttribute('aria-label'); 
      if (lbl && lbl.indexOf('estrela') >= 0) { rating = lbl; break; } 
    }
    var addrMatch = text.match(/(R\.|Av\.|Rua|Avenida|Travessa|Est\.|Rod\.)[^,\n]{5,80}/); 
    var address = addrMatch ? addrMatch[0].trim() : '';
    var lines = text.split('\n');
    var cat = '';
    for (var l = 0; l < lines.length; l++) {
      if (lines[l].match(/Salão|Restaurante|Lanchonete|Pizzaria|Padaria|Farmácia|Drogaria|Pet|Óptica|Loja|Distribuidora|Material|Construção|Bazar|Mercado|Supermercado|Lavanderia|Gráfica|Papelaria|Presentes|Calçados|Fantasias|Floricultura|Ferragens|Ferragista|Auto|Elétrica|Informática|Celulares|Variedades|Bebidas|Café|Sorvetes|Açai|Doces|Confeitaria|Churrascaria|Padaria|Panificadora/i)) {
        cat = lines[l].trim(); break;
      }
    }
    results.push({name: name, phone: phone, rating: rating, address: address, category: cat}); 
  } 
  return JSON.stringify(results); 
})()
"""

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
    "Jardim Ipiranga"
]

TIPOS = [
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
    "distribuidora"
]

def build_url(tipo, bairro):
    from urllib.parse import quote
    query = f"{tipo} em {bairro} Aparecida de Goiânia GO"
    return f"https://www.google.com/maps/search/{quote(query)}"

if __name__ == "__main__":
    searches = []
    for bairro in BAIRROS:
        for tipo in TIPOS:
            searches.append({
                "bairro": bairro,
                "tipo": tipo,
                "url": build_url(tipo, bairro)
            })
    
    # Output as JSON
    output = {
        "js_template": JS_EXTRACT,
        "searches": searches,
        "total_searches": len(searches),
        "total_bairros": len(BAIRROS),
        "total_tipos": len(TIPOS)
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
