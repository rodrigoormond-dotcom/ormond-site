#!/usr/bin/env python3
"""
Ormond Studio — Gerador de data.js
Lê as imagens já baixadas nas pastas images/* e gera js/data.js automaticamente.
Execute DEPOIS de baixar as imagens com baixar_imagens.py.

Uso: python gerar_data_js.py
"""
import os, json

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

CATEGORIAS = {
    'publicidade': ('Publicidade',         'Fotografia comercial e publicitária para marcas, agências e campanhas.'),
    'moda':        ('Moda',                'Fotografias de moda, lookbooks e catálogos para as melhores marcas.'),
    'produtos':    ('Produtos & E-commerce','Fotografia de produto e e-commerce com foco em conversão e qualidade.'),
    'arquitetura': ('Arquitetura & Design', 'Fotografia arquitetônica, interiores e design.'),
    'retratos':    ('Retratos',            'Retratos corporativos, editoriais e artísticos com identidade única.'),
    'alimentos':   ('Alimentos',           'Food photography para restaurantes, marcas e campanhas gastronômicas.')
}

EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

results = {}
for cat in CATEGORIAS:
    folder = os.path.join(SITE_DIR, 'images', cat)
    if not os.path.isdir(folder):
        results[cat] = []
        print(f'  {cat}: pasta não encontrada')
        continue
    files = sorted([f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in EXTS])
    results[cat] = files
    print(f'  {cat}: {len(files)} imagens')

# Hero: primeira imagem de 3 categorias
hero_imgs = []
for cat in ['publicidade', 'moda', 'retratos', 'alimentos', 'arquitetura', 'produtos']:
    if results.get(cat):
        hero_imgs.append({'src': f'images/{cat}/{results[cat][0]}', 'label': cat.capitalize()})
    if len(hero_imgs) == 4:
        break

# Montar data.js
lines = ['/* ORMOND STUDIO — data.js (gerado por gerar_data_js.py) */\n']
lines.append('const ORMOND_DATA = {\n')
lines.append('\n  hero: [\n')
for h in hero_imgs:
    lines.append(f"    {{ src: '{h['src']}', label: '{h['label']}' }},\n")
lines.append('  ],\n')

lines.append('\n  videos: [\n')
lines.append('    // Adicione vídeos do Vimeo:\n')
lines.append('    // { categoria: "publicidade", titulo: "Nome", src: "https://player.vimeo.com/video/ID?color=c8a96e&title=0&byline=0", fonte: "Vimeo", descricao: "" },\n')
lines.append('  ],\n')

lines.append('\n  portfolio: {\n')
for cat, (titulo, desc) in CATEGORIAS.items():
    imgs = results.get(cat, [])
    lines.append(f"\n    {cat}: {{\n")
    lines.append(f"      titulo: '{titulo}',\n")
    lines.append(f"      descricao: '{desc}',\n")
    lines.append(f"      imagens: [\n")
    for img in imgs:
        lines.append(f"        '{img}',\n")
    lines.append(f"      ]\n")
    lines.append(f"    }},\n")
lines.append('  }\n')
lines.append('};\n')

lines.append("""
function renderGallery(categoriaKey) {
  const container = document.getElementById('gallery-container');
  if (!container) return;
  const cat = ORMOND_DATA.portfolio[categoriaKey];
  if (!cat || !cat.imagens.length) {
    container.innerHTML = '<div style="padding:80px;text-align:center;color:var(--grey)"><p>Imagens em breve.</p></div>';
    return;
  }
  container.innerHTML = cat.imagens.map((img, i) => `
    <div class="masonry-item" data-index="${i}" data-caption="${img.replace(/\\.[^/.]+$/, '').replace(/[-_]/g, ' ')}">
      <img src="../../images/${categoriaKey}/${img}" alt="${img}" loading="lazy">
      <div class="masonry-overlay">&#x26F6;</div>
    </div>
  `).join('');
  if (typeof initMasonryLightbox === 'function') initMasonryLightbox();
}

function renderVideos(categoriaKey) {
  const container = document.getElementById('videos-container');
  if (!container) return;
  const vids = categoriaKey ? ORMOND_DATA.videos.filter(v => v.categoria === categoriaKey) : ORMOND_DATA.videos;
  if (!vids.length) { container.innerHTML = '<p style="color:var(--grey)">Adicione vídeos em js/data.js</p>'; return; }
  container.innerHTML = vids.map(v => `<div class="vcard fade-in"><iframe class="vcard-embed" src="${v.src}" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe><div class="vcard-body"><div class="vcard-title">${v.titulo}</div><span class="vcard-source">${v.fonte}</span></div></div>`).join('');
}

function renderHero() {
  const slidesEl = document.getElementById('hero-slides');
  const dotsEl = document.getElementById('hero-dots');
  if (!slidesEl) return;
  const slides = ORMOND_DATA.hero;
  if (!slides.length) return;
  slidesEl.innerHTML = slides.map((s,i) => `<div class="hero-slide${i===0?' active':''}" style="background-image:url('${s.src}')"></div>`).join('');
  if (dotsEl) dotsEl.innerHTML = slides.map((_,i) => `<div class="hero-dot${i===0?' active':''}"></div>`).join('');
}
document.addEventListener('DOMContentLoaded', renderHero);
""")

out_path = os.path.join(SITE_DIR, 'js', 'data.js')
os.makedirs(os.path.join(SITE_DIR, 'js'), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

total = sum(len(v) for v in results.values())
print(f'\ndata.js gerado com {total} imagens em {out_path}')
print('Pronto! Faça commit e push para o GitHub.')
