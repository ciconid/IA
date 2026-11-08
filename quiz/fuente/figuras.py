# Figuras de contexto para las preguntas que se apoyan en un ejemplo de las diapositivas o del TP.
# Devuelven HTML (tablas o SVG inline) que el template muestra entre el enunciado y las opciones.
# Los colores salen de las variables CSS del template, así que funcionan en modo claro y oscuro.

# --- Asistente de impresión (Ep. VII, parte 2) -------------------------------------------------
IMPRESORA = [
    ('e1', 'L-V', 'mañana', 'pocas', 'pdf', 'grande', 'inkjet'),
    ('e2', 'L-V', 'tarde', 'muchas', 'doc', 'mediano', 'laser'),
    ('e3', 'L-V', 'tarde', 'muchas', 'xls', 'chico', 'laser'),
    ('e4', 'L-V', 'noche', 'muchas', 'doc', 'mediano', 'inkjet'),
    ('e5', 'L-V', 'mañana', 'muchas', 'pdf', 'grande', 'laser'),
    ('e6', 'L-V', 'tarde', 'pocas', 'xls', 'chico', 'inkjet'),
    ('e7', 'L-V', 'noche', 'muchas', 'xls', 'chico', 'inkjet'),
    ('e8', 'L-V', 'tarde', 'muchas', 'doc', 'chico', 'laser'),
    ('e9', 'L-V', 'tarde', 'pocas', 'doc', 'chico', 'inkjet'),
    ('e10', 'L-V', 'noche', 'muchas', 'pdf', 'grande', 'inkjet'),
    ('e11', 'L-V', 'mañana', 'muchas', 'xls', 'chico', 'laser'),
    ('e12', 'Finde', 'mañana', 'muchas', 'pdf', 'grande', 'inkjet'),
    ('e13', 'Finde', 'tarde', 'muchas', 'doc', 'chico', 'inkjet'),
    ('e14', 'Finde', 'mañana', 'pocas', 'doc', 'grande', 'inkjet'),
]


def tabla_impresora():
    cab = ''.join(f'<th>{c}</th>' for c in ('', 'día', 'hora', 'páginas', 'tipo', 'tamaño', 'decisión'))
    filas = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in f) + '</tr>' for f in IMPRESORA)
    return (f'<div class="ctx-tit">Conjunto de entrenamiento del asistente de impresión</div>'
            f'<div class="ctx-scroll"><table class="ctx-tabla"><thead><tr>{cab}</tr></thead><tbody>{filas}</tbody></table></div>')


def arbol_impresora():
    # nodos: (x, y, texto, es_hoja)
    N = {
        'pag': (200, 22, 'páginas', False),
        'ink0': (80, 92, 'inkjet', True),
        'hora': (330, 92, 'hora', False),
        'dia1': (200, 162, 'día', False),
        'dia2': (380, 162, 'día', False),
        'ink1': (500, 162, 'inkjet', True),
        'las1': (150, 232, 'laser', True),
        'ink2': (250, 232, 'inkjet', True),
        'las2': (330, 232, 'laser', True),
        'ink3': (430, 232, 'inkjet', True),
    }
    E = [('pag', 'ink0', 'pocas'), ('pag', 'hora', 'muchas'),
         ('hora', 'dia1', 'mañana'), ('hora', 'dia2', 'tarde'), ('hora', 'ink1', 'noche'),
         ('dia1', 'las1', 'L-V'), ('dia1', 'ink2', 'Finde'), ('dia2', 'las2', 'L-V'), ('dia2', 'ink3', 'Finde')]
    s = []
    for a, b, et in E:
        (x1, y1, *_), (x2, y2, *_) = N[a], N[b]
        s.append(f'<line x1="{x1}" y1="{y1 + 13}" x2="{x2}" y2="{y2 - 13}" class="ar"/>')
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        s.append(f'<text x="{mx}" y="{my + 4}" class="et">{et}</text>')
    for x, y, t, hoja in N.values():
        w = 64 if hoja else 74
        s.append(f'<rect x="{x - w / 2}" y="{y - 13}" width="{w}" height="26" rx="{4 if hoja else 13}" class="{"hoja" if hoja else "nodo"}"/>')
        s.append(f'<text x="{x}" y="{y + 5}" class="{"th" if hoja else "tn"}">{t}</text>')
    return ('<div class="ctx-tit">Árbol de decisión aprendido para la impresora</div>'
            '<svg class="ctx-svg" viewBox="36 0 508 252" role="img" aria-label="Árbol de decisión de la impresora: '
            'páginas pocas: inkjet; páginas muchas: hora; hora noche: inkjet; hora mañana o tarde: día; '
            'día L-V: laser; día Finde: inkjet">' + ''.join(s) + '</svg>')


# --- Programas y bases de conocimiento -----------------------------------------------------------
def _esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def programa(titulo, texto):
    """Bloque con un programa o KB, una cláusula por línea."""
    return f'<div class="ctx-tit">{titulo}</div><pre>{_esc(texto.strip())}</pre>'


def nota(titulo, texto):
    """Descripción breve del ejemplo (sin adelantar la respuesta)."""
    return f'<div class="ctx-tit">{titulo}</div><p>{texto}</p>'


OKAERI = nota('El agente Okaeri (Ep. VIII)',
              'Agente de compañía con un SBC: le sugiere a su usuario qué llevar según el clima '
              '(«No te olvides de llevar un paraguas», «A la noche refrescará. Llevá abrigo»).')

MERVAL_DESC = nota('El agente Mer-val (Ep. VIII)',
                   'Agente de recomendación para el mercado bursátil: responde consultas sobre la compra de acciones '
                   'de una empresa, con un SBC que usa Prolog como máquina de inferencia y el top-level como interface.')

MERVAL_ORIG = programa('Mer-val original, sin negación fuerte (Ep. VIII)', '''
comprar_acciones(X) :- buen_precio(X).
buen_precio(X) :- buen_precio_web(X).
no_comprar_acciones(X) :- riesgosa(X).
riesgosa(X) :- en_fusion(X,Y).
en_fusion(X,Y) :- listado_fusiones_web(X,Y).
riesgosa(X) :- rumores_deuda_web(X).
no_riesgosa(X) :- en_fusion(X,Y), fuerte(Y).
no_riesgosa(X) :- fuerte(X).
fuerte(X) :- listado_fuertes_web(X).
buen_precio_web(skynet).
buen_precio_web(acme).
listado_fusiones_web(acme, strong).
rumores_deuda_web(acme).
rumores_deuda_web(usrobotics).
listado_fuertes_web(strong).''')

MERVAL_NEG = programa('KB de Mer-val con negación fuerte', '''
comprar_acciones(X) :- buen_precio(X).
buen_precio(X) :- buen_precio_web(X).
buen_precio_web(skynet).
buen_precio_web(acme).
~comprar_acciones(X) :- riesgosa(X).
riesgosa(X) :- en_fusion(X,Y).
riesgosa(X) :- rumores_deuda_web(X).
en_fusion(X,Y) :- listado_fusiones_web(X,Y).
listado_fusiones_web(acme,strong).
rumores_deuda_web(acme).
rumores_deuda_web(usrobotics).''')

CF_EJEMPLO = programa('KB del ejemplo de la cátedra, con valores de certeza (Ep. IX)', '''
 0.7  a ← b.
 0.9  a ← c.
 0.7 ~a ← d.
 0.8 ~a ← e.
 0.7 ~a ← p, f.
 0.6  b ← p, g.
 1    b ← h.
 0.8  d ← k.
 0.9  f ← m.
 1    p.
 0.4  e.
 0.9  g.
 0.9  h.
-0.5  k.
 0.8  m.''')

CF_LAGO = programa('KB del TP7, ej. 7 (valores de certeza)', '''
h1   1    gallina(turuleca).
h2  -0.3  gallina(petete).
h3  -1    gallina(donald).
h4   1    pato(donald).
h5   0.5  ave(petete).
r1   1    ave(X) ← pato(X).
r2   1    ave(X) ← gallina(X).
r3   0.8  anida_suelo(X) ← gallina(X).
r4   0.9  anida_suelo(X) ← pato(X).
r5   0.7  ~vuela(X) ← anida_suelo(X), ave(X).
r6   0.8  ~cruza_lago(X) ← ~vuela(X), ave(X).
r7   0.9  cruza_lago(X) ← vuela(X).
r8   0.7  vuela(X) ← ave(X).''')

INF_EJEMPLO = programa('KB del ejemplo de la cátedra, con informantes (Ep. IX)', '''
[e1]  a ← b.        [e2]  b ← p, g.
[e3]  a ← c.        [e1]  b ← h.
[e2] ~a ← d.        [e2]  d ← k.
[e1] ~a ← e.        [e3]  f ← m.
[e1] ~a ← p, f.     [w3]  p.
                    [w1]  e.
                    [w1]  g.
                    [w3]  h.
                    [w2]  k.
                    [w2]  m.''')

INF_VIAJE = programa('KB del TP7, ej. 8 (informantes)', '''
[At] ~camino_abierto ← nieve.
[Av] ~viaje ← ~camino_abierto.
[Av] viaje ← camino_abierto.
[Ar] camino_abierto.
[Ap] camino_abierto.
[Ai] camino_abierto ← ~nieve.
[Ai] ~nieve.
[Ap] ~nieve.
[Ai] nieve.''')

DELP_RES = programa('Programa de la «Resolución con DeLP»', '''
Π = { h1.  h2.  h3.  h4. }

Δ = { a -< h1.     b -< h2.     c -< h2.
      a -< b.      b -< h5.    ~c -< d.
     ~a -< c.     ~b -< h4.     d -< h3.
                               ~d -< h4. }

Orden entre reglas:
  (~a -< c)  > (a -< h1)
  (b -< h2)  > (~b -< h4)
  (~c -< d)  > (c -< h2)''')

DELP_NN = programa('Programa (Πn, Δn)', '''
Πn = { ~en_casa ← en_supermercado.
       en_supermercado.
       de_noche.
       festejo. }

Δn = { en_casa -< de_noche.
       preparo_cena -< de_noche.
       ~preparo_cena -< festejo.
       acuesto_tarde -< festejo.
       en_oficina -< trabajando. }''')

ACME_KB = programa('KB de Mer-val usada en el Ep. X (c = comprar_acciones, r = riesgosa, a = acme)', '''
comprar_acciones(X) :- buen_precio(X).
buen_precio(X) :- buen_precio_web(X).
~comprar_acciones(X) :- riesgosa(X).
riesgosa(X) :- en_fusion(X,Y).
en_fusion(X,Y) :- listado_fusiones_web(X,Y).
riesgosa(X) :- rumores_deuda_web(X).
~riesgosa(X) :- en_fusion(X,Y), fuerte(Y).
~riesgosa(X) :- fuerte(X).
fuerte(X) :- listado_fuertes_web(X).
buen_precio_web(acme).
listado_fusiones_web(acme, strong).
rumores_deuda_web(acme).
listado_fuertes_web(strong).''')


def derivaciones_acme():
    """Las cuatro derivaciones del ejemplo de acme como triángulos (conclusión arriba), sin las flechas de ataque."""
    D = [  # (x, nombre, conclusión, punto interno, reglas usadas)
        (95, 'd1', 'c(a)', None, ['c(a) ← buen_precio(a)', 'buen_precio(a) ← web']),
        (265, 'd2', '~c(a)', 'r(a)', ['~c(a) ← r(a)', 'r(a) ← en_fusion(a,s)', 'en_fusion ← web']),
        (435, 'd3', '~r(a)', None, ['~r(a) ← en_fusion(a,s),', 'fuerte(s)', 'en_fusion, fuerte ← web']),
        (605, 'd4', 'r(a)', None, ['r(a) ← rumores_deuda', '_web(a)']),
    ]
    s = []
    for x, n, c, interno, reglas in D:
        s.append(f'<polygon points="{x},34 {x - 52},128 {x + 52},128" class="tri"/>')
        s.append(f'<text x="{x}" y="24" class="tn">{_esc(c)}</text>')
        if interno:
            s.append(f'<polygon points="{x},74 {x - 22},114 {x + 22},114" class="tri2"/>')
            s.append(f'<text x="{x}" y="70" class="et2">{_esc(interno)}</text>')
        s.append(f'<text x="{x}" y="148" class="tn">{n}</text>')
        for i, r in enumerate(reglas):
            s.append(f'<text x="{x}" y="{170 + 15 * i}" class="et2">{_esc(r)}</text>')
    return ('<div class="ctx-tit">Derivaciones del ejemplo de acme (Ep. X, parte 1; s = strong)</div>'
            '<div class="ctx-scroll"><svg class="ctx-svg ctx-ancho" viewBox="0 0 700 220" role="img" aria-label="d1 concluye c(a); '
            'd2 concluye ~c(a) pasando por r(a); d3 concluye ~r(a); d4 concluye r(a)">' + ''.join(s) + '</svg></div>')


ACME = ACME_KB + derivaciones_acme()

OKAERI_KB = programa('KB de Okaeri en Prolog (Ep. VIII)', '''
recomendar(paraguas) :- chance(lluvia,X), X > 50.
recomendar(abrigo) :- minima(T), T < 10.
recomendar(sombrero) :- verano.
chance(lluvia,80).
minima(8).
% con los hechos de hemisferio y mes que tiene la KB, verano no se cumple''')


# --- Redes neuronales (Ep. VII, parte 3) -----------------------------------------------------------
def red_neuronal(capas, titulo):
    """Red feed-forward completamente conectada. capas: [(nombre, cantidad, nodos a dibujar)].
    Si la capa tiene más neuronas que las dibujadas, se ponen puntos suspensivos en el medio."""
    W, H, top, bot = 520, 250, 38, 212
    xs = [90 + i * (W - 180) / (len(capas) - 1) for i in range(len(capas))]
    cols = []
    for (nombre, n, k), x in zip(capas, xs):
        ys = [top + j * (bot - top) / (k - 1) for j in range(k)] if k > 1 else [(top + bot) / 2]
        if n > k:   # hueco central para los puntos suspensivos
            m = k // 2
            paso = (bot - top) / k
            ys = [top + j * paso for j in range(m)] + [bot - (k - m - 1 - j) * paso for j in range(k - m)]
        cols.append((x, ys, nombre, n, k))
    s = []
    for (x1, ys1, *_), (x2, ys2, *_) in zip(cols, cols[1:]):
        for y1 in ys1:
            for y2 in ys2:
                s.append(f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" class="arco"/>')
    for x, ys, nombre, n, k in cols:
        for y in ys:
            s.append(f'<circle cx="{x}" cy="{y:.1f}" r="7" class="neu"/>')
        if n > k:
            yc = (top + bot) / 2
            s.append(f'<text x="{x}" y="{yc + 5:.1f}" class="tn">⋮</text>')
        s.append(f'<text x="{x}" y="18" class="tn">{nombre}</text>')
        s.append(f'<text x="{x}" y="{H - 8}" class="et2">{n} neuronas</text>')
    return (f'<div class="ctx-tit">{titulo}</div>'
            f'<svg class="ctx-svg" viewBox="0 0 {W} {H}" role="img" aria-label="Red con capas de ' +
            ', '.join(f'{n} ({nombre})' for nombre, n, _ in capas) + ', cada neurona conectada con todas las de la capa siguiente">' +
            ''.join(s) + '</svg>')


def perceptron(entradas, b, titulo):
    """Perceptrón: entradas [(nombre, valor o None, peso)], sesgo b. No muestra la salida (es lo que se pregunta)."""
    s = ['<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" class="punta"/></marker></defs>']
    cx, cy = 300, 100
    n = len(entradas)
    for i, (nombre, valor, w) in enumerate(entradas):
        y = cy + (i - (n - 1) / 2) * 90
        etiqueta = f'{nombre} = {valor}' if valor is not None else nombre
        s.append(f'<rect x="40" y="{y - 16}" width="96" height="32" rx="16" class="nodo"/>')
        s.append(f'<text x="88" y="{y + 5}" class="tn">{_esc(etiqueta)}</text>')
        s.append(f'<line x1="136" y1="{y}" x2="{cx - 44}" y2="{cy + (y - cy) * 0.25}" class="ar" marker-end="url(#fl)"/>')
        mx, my = (136 + cx - 44) / 2, (y + cy + (y - cy) * 0.25) / 2
        s.append(f'<text x="{mx}" y="{my - 7}" class="et">{_esc(w)}</text>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="42" class="neu"/>')
    s.append(f'<text x="{cx}" y="{cy - 4}" class="tn">perceptrón</text>')
    s.append(f'<text x="{cx}" y="{cy + 15}" class="et2">b = {_esc(b)}</text>')
    s.append(f'<line x1="{cx + 42}" y1="{cy}" x2="{cx + 128}" y2="{cy}" class="ar" marker-end="url(#fl)"/>')
    s.append(f'<text x="{cx + 138}" y="{cy + 5}" class="tn" style="text-anchor:start">salida</text>')
    return (f'<div class="ctx-tit">{titulo}</div>'
            f'<svg class="ctx-svg" viewBox="20 0 480 200" role="img" aria-label="Perceptrón con entradas ' +
            ', '.join(f'{_esc(e[0])} de peso {_esc(e[2])}' for e in entradas) + f' y sesgo b = {_esc(b)}">' +
            ''.join(s) + '</svg>')
