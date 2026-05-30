#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script para agregar todos os leads coletados"""
import json
import re

# JS extraction template - use with browser_console expression
JS_EXTRACT = """
(function() { 
  var r=[]; 
  var arts=document.querySelectorAll('[role="article"]'); 
  arts.forEach(function(a) { 
    var lk=a.querySelector('a[aria-label]'); 
    var n=lk?lk.getAttribute('aria-label'):''; 
    var t=a.innerText||''; 
    var p=t.match(/\\(62\\)\\s*\\d{4,5}-\\d{4}/); 
    var s=a.querySelector('[aria-label*="estrela"]'); 
    var rt=s?s.getAttribute('aria-label'):''; 
    var ad=t.match(/(R\\.|Av\\.|Rua|Avenida|Travessa)[^,\\n]{5,100}/); 
    if(n)r.push([n, p?p[0]:'', rt, ad?ad[0].trim():'']); 
  }); 
  return JSON.stringify(r); 
})()
"""

# Data collected from Google Maps searches
# Each entry: [name, phone, rating, address]
RAW_DATA = {}

if __name__ == "__main__":
    print("Use this JS in browser_console:")
    print(JS_EXTRACT)
