"""Segundo borrão das evidências publicáveis (dados pessoais ilegíveis).

As capturas já saem com o texto borrado por CSS (sigaa_coleta.py). Este passo aplica
um desfoque gaussiano uniforme em toda a imagem, proporcional à largura, para que
nenhum texto, número ou rosto seja legível, preservando a estrutura da página
(tabelas, menus, larguras e sobreposições), que é o que as evidências comprovam.

Uso: python coleta/borrar.py dados/brutos/flexibilidade/evidencias
"""
import sys
from pathlib import Path

from PIL import Image, ImageFilter

for arq in sorted(Path(sys.argv[1]).rglob("*.jpg")):
    img = Image.open(arq)
    raio = max(4, img.width / 280)
    img.convert("RGB").filter(ImageFilter.GaussianBlur(raio)).save(arq, quality=60, optimize=True)
    print(arq, f"raio={raio:.1f}")
