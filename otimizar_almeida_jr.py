#!/usr/bin/env python3
"""
Ormond Studio — Otimizador para case Almeida Jr
Copia e otimiza as imagens selecionadas de J:\\2023\\2023-almeida jr arquitetura
para images/cases/almeida-jr/ dentro do site.
"""
from PIL import Image
import os, shutil

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DEST = os.path.join(SITE_DIR, "images", "cases", "almeida-jr")
MAX_PX = 1600
MAX_KB = 500

IMAGENS = [
    # (origem, subpasta destino, nome_final)
    # NORTE
    (r"J:\2023\2023-almeida jr arquitetura\alm j norte\DJI_0686-Editar.jpg",           "norte", "DJI_0686.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j norte\_S3A3885-Aprimorado-NR-Editar.jpg", "norte", "_S3A3885.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j norte\_S3A4055-Aprimorado-NR-Editar.jpg", "norte", "_S3A4055.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j norte\_S3A3718-Aprimorado-NR-Editar.jpg", "norte", "_S3A3718.jpg"),
    # GARTEN
    (r"J:\2023\2023-almeida jr arquitetura\alm j garten jvlle\_S3A2687-Aprimorado-NR-2.jpg",    "garten", "_S3A2687.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j garten jvlle\_S3A3083-Aprimorado-NR-Editar.jpg","garten", "_S3A3083.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j garten jvlle\DSC01613-Aprimorado-NR-Editar.jpg","garten", "DSC01613.jpg"),
    # CONTINENTE
    (r"J:\2023\2023-almeida jr arquitetura\alm j continente\DJI_0025-Aprimorado-NR-Editar.jpg",    "continente", "DJI_0025.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j continente\_S3A7999-Aprimorado-NR-Editar.jpg",    "continente", "_S3A7999.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j continente\_S3A8591-Aprimorado-NR-Editar.jpg",    "continente", "_S3A8591.jpg"),
    # NAÇÕES
    (r"J:\2023\2023-almeida jr arquitetura\alm j nacoes crici\DSC03087-Aprimorado-NR-Editar.jpg",  "nacoes", "DSC03087.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j nacoes crici\_S3A7523-Aprimorado-NR-Editar.jpg",  "nacoes", "_S3A7523.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j nacoes crici\DSC03110-Aprimorado-NR-Editar.jpg",  "nacoes", "DSC03110.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j nacoes crici\_S3A7582-Aprimorado-NR-Editar.jpg",  "nacoes", "_S3A7582.jpg"),
    # NEUMARKT
    (r"J:\2023\2023-almeida jr arquitetura\alm j nmkt\_S3A5634-Aprimorado-NR-Editar.jpg",  "neumarkt", "_S3A5634.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j nmkt\_S3A5459-Aprimorado-NR-Editar.jpg",  "neumarkt", "_S3A5459.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j nmkt\_S3A4831-Aprimorado-NR-Editar.jpg",  "neumarkt", "_S3A4831.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\alm j nmkt\_S3A5172-Aprimorado-NR-Editar.jpg",  "neumarkt", "_S3A5172.jpg"),
    # BALNEÁRIO CAMBORIÚ
    (r"J:\2023\2023-almeida jr arquitetura\balneario camboriu\_S3A7220-Enhanced-NR-Editar.jpg", "bc", "_S3A7220.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\balneario camboriu\_S3A5821-Aprimorado-NR-Editar.jpg","bc", "_S3A5821.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\balneario camboriu\_S3A5974-Enhanced-NR.jpg",        "bc", "_S3A5974.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\balneario camboriu\_S3A6622-Enhanced-NR-Editar.jpg", "bc", "_S3A6622.jpg"),
    (r"J:\2023\2023-almeida jr arquitetura\balneario camboriu\_S3A6531-Editar.jpg",             "bc", "_S3A6531.jpg"),
]

print("=" * 55)
print("  Ormond Studio — Otimizando Almeida Jr")
print(f"  {len(IMAGENS)} imagens selecionadas")
print("=" * 55)

ok = 0
erros = []

for src, pasta, nome_dest in IMAGENS:
    dest_dir = os.path.join(BASE_DEST, pasta)
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, nome_dest)

    if not os.path.exists(src):
        print(f"  NAO ENCONTRADO: {src}")
        erros.append(src)
        continue

    try:
        img = Image.open(src).convert('RGB')
        w, h = img.size
        maior = max(w, h)
        if maior > MAX_PX:
            escala = MAX_PX / maior
            img = img.resize((int(w * escala), int(h * escala)), Image.LANCZOS)

        qualidade = 88
        while qualidade >= 50:
            img.save(dest, 'JPEG', quality=qualidade, optimize=True, progressive=True)
            if os.path.getsize(dest) / 1024 <= MAX_KB:
                break
            qualidade -= 5

        kb = os.path.getsize(dest) / 1024
        print(f"  OK {pasta}/{nome_dest}  {img.size[0]}x{img.size[1]}px  {kb:.0f}KB")
        ok += 1

    except Exception as e:
        print(f"  ERRO {nome_dest}: {e}")
        erros.append(src)

print()
print("=" * 55)
print(f"  {ok}/{len(IMAGENS)} imagens processadas → images/cases/almeida-jr/")
if erros:
    print(f"  {len(erros)} erros (verifique os caminhos acima)")
print()
print("  Agora abra o post no navegador para revisar,")
print("  e depois clique em publicar.bat para publicar.")
print("=" * 55)
input("\nEnter para fechar...")
