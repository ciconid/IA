"""Genera ../index.html a partir de template.html y los bancos de preguntas.
Uso: python3 -I build.py [salida-artifact.html]   (desde cualquier carpeta)

Además del HTML, muestra estadísticas de calidad:
- en qué % de preguntas la correcta es la opción más larga / más corta (el azar daría ~25%);
- largo de la correcta / largo promedio de las incorrectas (ideal: ~1.0);
- las preguntas más sesgadas, para revisarlas a mano.
"""
import json, random, hashlib, sys, os, importlib
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, aqui)
from comun import sesgo

# Módulos con los bancos, en orden. Cada uno define U = dict(id, nombre, tp, preguntas).
MODULOS = ['u1_robotica', 'u2_aprendizaje', 'u3_sbc', 'u4_certeza', 'u5_informantes', 'u6_argumentos', 'u7_delp']

bancos = [importlib.import_module(m).U for m in MODULOS]

units, vistos = [], set()
for U in bancos:
    qs = []
    for p in U['preguntas']:
        assert p['q'] not in vistos, ('repetida', p['q']); vistos.add(p['q'])
        assert p['c'] not in p['w'], p['q']
        opts = [p['c']] + p['w']
        seed = int(hashlib.md5(p['q'].encode()).hexdigest(), 16)
        random.Random(seed).shuffle(opts)
        qs.append(dict(q=p['q'], o=opts, a=opts.index(p['c']), e=p['e']))
    units.append(dict(id=U['id'], nombre=U['nombre'], tp=U['tp'], qs=qs))
    s = sesgo(U['preguntas'])
    print(f"{U['id']:4} {U['nombre']:50} {len(qs):4} preguntas | más larga: {s['pct']:3.0f}% | más corta: {s['pct_corta']:3.0f}% | largo c/w: {s['ratio']:.2f}")

pos = [0] * 4
for u in units:
    for q in u['qs']: pos[q['a']] += 1
todas = [p for U in bancos for p in U['preguntas']]
s = sesgo(todas)
print(f"total {len(todas)} | posición de la correcta {pos} | más larga: {s['pct']:.0f}% | más corta: {s['pct_corta']:.0f}% | largo c/w: {s['ratio']:.2f}")
peores = sorted(zip(s['ratios'], todas), key=lambda t: -t[0])[:8]
print('más sesgadas (largo c/w):')
for r, p in peores:
    print(f"  {r:.2f}  {p['q'][:90]}")

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
print('index.html', len(local) // 1024, 'KB')
