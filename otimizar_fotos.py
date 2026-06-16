#!/usr/bin/env python3
"""
Ormond Studio — Otimizador de Fotos
- Redimensiona para max 1500px na maior aresta
- Comprime para max 450KB mantendo qualidade
- Copia para a pasta de destino no site
- Os 3 primeiros recebem prefixo index_ (aparecem no portfolio overview)

Uso:
  python otimizar_fotos.py

Edite as variáveis ORIGEM, DESTINO e CATEGORIA abaixo conforme necessário.
"""

from PIL import Image
import os, shutil

# ── CONFIGURAR AQUI ──────────────────────────────────────────────
ORIGEM    = r"F:\2021\2021-10-06-vitamedica\video ormond\produtos\jpg\portfolio"
CATEGORIA = "produtos"   # pasta dentro de images/
MAX_PX    = 1500         # pixels na maior aresta
MAX_KB    = 450          # tamanho máximo em KB
# ─────────────────────────────────────────────────────────────────

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
DESTINO  = os.path.join(SITE_DIR, "images", CATEGORIA)
EXTS     = {'.jpg', '.jpeg', '.png', '.webp', '.tiff', '.tif'}

os.makedirs(DESTINO, exist_ok=True)

# Listar arquivos de imagem na origem
arquivos = sorted([
    f for f in os.listdir(ORIGEM)
    if os.path.splitext(f)[1].lower() in EXTS
])

if not arquivos:
    print(f"Nenhuma imagem encontrada em:\n  {ORIGEM}")
    input("Enter para fechar...")
    exit()

print(f"{'='*55}")
print(f"  Otimizando {len(arquivos)} imagens → images/{CATEGORIA}/")
print(f"{'='*55}\n")

processados = []

for i, nome in enumerate(arquivos, 1):
    src = os.path.join(ORIGEM, nome)
    base, _ = os.path.splitext(nome)
    # Limpar nome do arquivo
    safe = base.replace(' ', '_').replace('(', '').replace(')', '')
    dest_nome = f"{safe}.jpg"

    # Prefixo index_ nos 3 primeiros
    if i <= 3:
        dest_nome = f"index_{CATEGORIA}_{i}_{safe}.jpg"

    dest = os.path.join(DESTINO, dest_nome)

    try:
        img = Image.open(src).convert('RGB')

        # Redimensionar mantendo proporção
        w, h = img.size
        maior = max(w, h)
        if maior > MAX_PX:
            escala = MAX_PX / maior
            img = img.resize((int(w * escala), int(h * escala)), Image.LANCZOS)

        # Salvar com qualidade ajustada para atingir MAX_KB
        qualidade = 88
        while qualidade >= 50:
            img.save(dest, 'JPEG', quality=qualidade, optimize=True, progressive=True)
            tamanho_kb = os.path.getsize(dest) / 1024
            if tamanho_kb <= MAX_KB:
                break
            qualidade -= 5

        tamanho_kb = os.path.getsize(dest) / 1024
        prefixo = "★ index_" if i <= 3 else "  "
        print(f"{prefixo}[{i:02d}/{len(arquivos)}] {dest_nome}")
        print(f"         {img.size[0]}×{img.size[1]}px — {tamanho_kb:.0f}KB (q={qualidade})")
        processados.append(dest_nome)

    except Exception as e:
        print(f"  ERRO [{i}] {nome}: {e}")

print(f"\n{'='*55}")
print(f"  {len(processados)} imagens salvas em:")
print(f"  {DESTINO}")
print(f"\n  Agora rode: python gerar_data_js.py")
print(f"{'='*55}")
input("\nEnter para fechar...")
