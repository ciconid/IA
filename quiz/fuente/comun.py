# Banco de preguntas: Q(pregunta, correcta, [incorrectas], explicación, ctx=html)
# ctx: contexto (figura, tabla o programa) que se muestra entre la pregunta y las opciones, para no tener que
# salir del quiz a buscar el ejemplo al que se refiere la pregunta. Ver figuras.py.
# id_texto: si se reescribe el enunciado, el texto viejo, para que el id (y el progreso guardado) no cambie.
# practica: True si para responder hay que hacer algún cálculo (CF, derivaciones, árboles, trazas); si no, es teórica.
def Q(pregunta, correcta, incorrectas, explicacion, ctx=None, id_texto=None, practica=False):
    assert len(incorrectas) == 3, pregunta
    assert len({correcta, *incorrectas}) == 4, ('opciones repetidas', pregunta)
    d = dict(q=pregunta, c=correcta, w=list(incorrectas), e=explicacion)
    if ctx: d['x'] = ctx
    if id_texto: d['id'] = id_texto
    if practica: d['p'] = True
    return d


def sesgo(preguntas):
    """Estadísticas de sesgo de largo de un banco de preguntas (dicts de Q)."""
    n = len(preguntas)
    mas_larga = 0          # la correcta es estrictamente la más larga
    mas_corta = 0          # la correcta es estrictamente la más corta
    ratios = []            # largo de la correcta / largo promedio de las incorrectas
    for p in preguntas:
        lw = [len(w) for w in p['w']]
        if len(p['c']) > max(lw):
            mas_larga += 1
        if len(p['c']) < min(lw):
            mas_corta += 1
        ratios.append(len(p['c']) / (sum(lw) / 3))
    return dict(n=n, mas_larga=mas_larga, pct=100 * mas_larga / n if n else 0,
                pct_corta=100 * mas_corta / n if n else 0,
                ratio=sum(ratios) / n if n else 0, ratios=ratios)
