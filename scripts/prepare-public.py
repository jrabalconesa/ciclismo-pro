"""Render the public adapter from an already authorized private Site checkout.
Only code/assets are copied. Documents, personal text and Library identifiers stay private.
Usage: python scripts/prepare-public.py /absolute/path/to/site-checkout
"""
from pathlib import Path
import json,shutil,sys
source=Path(sys.argv[1]).resolve()/'dist';target=Path(__file__).resolve().parents[1]/'dist'
target.mkdir(exist_ok=True)
for item in source.iterdir():
 if item.name in ['docs','resources.json']:continue
 if item.is_dir():shutil.copytree(item,target/item.name,dirs_exist_ok=True)
 else:shutil.copy2(item,target/item.name)
rows=json.loads((source/'resources.json').read_text());out=[]
for row in rows:
 record={k:row[k] for k in ['id','title','type','version','section','pages'] if k in row}
 record.update(private=True,text='',url='https://ciclismo-pro.joserabalconesa.chatgpt.site/#biblioteca',notes='Documento conservado en la edición privada de ChatGPT Sites. '+row.get('notes',''))
 out.append(record)
(target/'resources.json').write_text(json.dumps(out,ensure_ascii=False))
p=target/'app.js';text=p.read_text().replace('El sitio tiene acceso privado del propietario.','Esta es la edición pública de la aplicación. Los documentos del proyecto permanecen en la edición privada de ChatGPT Sites.').replace('La factura y las instrucciones personales se abren en su archivo privado original.','La biblioteca enlaza a la edición privada de Sites, que requiere iniciar sesión.');p.write_text(text)
p=target/'index.html';text=p.read_text().replace('</body>','<p style="padding:12px 24px;margin-bottom:80px;font:14px system-ui">Edición GitHub Pages · Los documentos del proyecto se consultan en <a href="https://ciclismo-pro.joserabalconesa.chatgpt.site/#biblioteca" target="_blank" rel="noreferrer">ChatGPT Sites privado</a>.</p></body>');p.write_text(text)
assert not (target/'docs').exists(),'Do not stage private documents for this public edition.'
