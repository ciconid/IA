# Banco de preguntas: Q(pregunta, correcta, [incorrectas], explicación)
def Q(pregunta, correcta, incorrectas, explicacion):
    assert len(incorrectas) == 3, pregunta
    assert len({correcta, *incorrectas}) == 4, ('opciones repetidas', pregunta)
    return dict(q=pregunta, c=correcta, w=list(incorrectas), e=explicacion)


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
