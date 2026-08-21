#!/usr/bin/env python3
"""FanX JP proposal builder: concat src/*.html, inline {{IMG:name}} as data URIs."""
import re, base64, glob, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
IMG = os.path.join(ROOT, 'img-src')

MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp'}

parts = sorted(glob.glob(os.path.join(SRC, '*.html')))
html = ''.join(open(p, encoding='utf-8').read() for p in parts)

def repl(m):
    name = m.group(1)
    for ext, mime in MIME.items():
        p = os.path.join(IMG, name + ext)
        if os.path.exists(p):
            b64 = base64.b64encode(open(p, 'rb').read()).decode()
            return f'data:{mime};base64,{b64}'
    sys.exit(f'MISSING IMAGE: {name}')

html = re.sub(r'\{\{IMG:([A-Za-z0-9_\-]+)\}\}', repl, html)
out = os.path.join(ROOT, 'index.html')
open(out, 'w', encoding='utf-8').write(html)
print(f'OK index.html {os.path.getsize(out)//1024}KB from {len(parts)} parts')
