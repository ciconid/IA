"""Genera ../index.html a partir de template.html y los bancos de preguntas.
Uso: python3 -I build.py (desde esta carpeta)."""
import json, random, hashlib, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from u0_u1 import U0, U1
from u2_u3 import U2, U3
from u4_u5 import U4, U5
from u6_u7 import U6, U7

units = []
for U in (U0, U1, U2, U3, U4, U5, U6, U7):
    qs, vistos = [], set()
    for p in U['preguntas']:
        assert p['q'] not in vistos, ('repetida', p['q']); vistos.add(p['q'])
        assert p['c'] not in p['w'], p['q']
        opts = [p['c']] + p['w']
        seed = int(hashlib.md5(p['q'].encode()).hexdigest(), 16)
        random.Random(seed).shuffle(opts)
        qs.append(dict(q=p['q'], o=opts, a=opts.index(p['c']), e=p['e']))
    units.append(dict(id=U['id'], nombre=U['nombre'], tp=U['tp'], qs=qs))
    print(U['id'], U['nombre'], len(qs))

pos = [0]*4
for u in units:
    for q in u['qs']: pos[q['a']] += 1
print('total', sum(len(u['qs']) for u in units), 'posición de la correcta', pos)

aqui = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(aqui, 'template.html'), encoding='utf-8').read()
data = json.dumps(units, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
out = tpl.replace('/*__DATA__*/[]', data)
# Versión local: documento completo para abrir con doble clic.
local = ('<!doctype html>\n<html lang="es">\n<meta charset="utf-8">\n'
         '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n') + out
open(os.path.join(aqui, '..', 'index.html'), 'w', encoding='utf-8').write(local)
# Versión para publicar como artifact (el host agrega el esqueleto del documento).
if len(sys.argv) > 1:
    open(sys.argv[1], 'w', encoding='utf-8').write(out)
print('index.html', len(local)//1024, 'KB')
