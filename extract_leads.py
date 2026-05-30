#!/usr/bin/env python3
"""
Google Maps Scraper - Automated browser scraping for business leads.
This script outputs lead data as JSON to stdout.
"""
import json
import sys
import re

# This script will be called by the main orchestrator
# It takes a search URL and extracts business data from the snapshot

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_leads.py <snapshot_file>")
        sys.exit(1)
    
    # Parse snapshot data and extract leads
    snapshot_file = sys.argv[1]
    with open(snapshot_file, 'r') as f:
        snapshot = f.read()
    
    # Extract business articles from snapshot
    articles = []
    current = {}
    
    lines = snapshot.split('\n')
    for i, line in enumerate(lines):
        # Look for article entries
        m = re.search(r'article "([^"]+)"', line)
        if m:
            if current:
                articles.append(current)
            current = {"nome": m.group(1)}
        
        # Look for ratings
        m = re.search(r'image "(\d+[.,]\d+) estrelas"', line)
        if m and current:
            current["avaliacao"] = m.group(1).replace(',', '.')
        
        # Look for phone in sidebar
        m = re.search(r'Telefone: \((\d{2})\)\s*(\d{5})-?(\d{4})', line)
        if m and current:
            current["telefone"] = f"({m[1]}) {m[2]}-{m[3]}"
        
        # Look for address
        m = re.search(r'Endereço: (.+?)(?:"]|$)', line)
        if m and current:
            current["endereco"] = m.group(1).strip()
    
    if current:
        articles.append(current)
    
    print(json.dumps(articles, ensure_ascii=False, indent=2))
