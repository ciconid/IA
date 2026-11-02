def Q(pregunta, correcta, incorrectas, explicacion):
    assert len(incorrectas) == 3, pregunta
    return dict(q=pregunta, c=correcta, w=list(incorrectas), e=explicacion)
