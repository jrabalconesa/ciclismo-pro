# Ciclismo PRO

El código compartido se registra en pro-sync.json. La biblioteca privada, facturas y textos personales quedan fuera del repositorio público. resources.json e index.html son adaptadores de la publicación pública y no se sobrescriben desde Sites.

`platform_files` registra por separado las huellas de la fuente privada y de su adaptador público. Si cambia una de ellas, usa `python scripts/prepare-public.py /ruta/al/checkout-sites` para regenerar la copia pública y valida el resultado. Nunca copies los originales privados como sustitución directa.
