# Quiz de Inteligencia Artificial (UNS, 2026)

Quiz interactivo de opción múltiple sobre los temas 5, 6 y 8 de la materia: 247 preguntas en 7 unidades.

| Unidad | Tema | TP | Preguntas | Fuentes |
|---|---|---|---|---|
| U1 | Robótica, roboética y legislación | TP5 | 53 | Robótica y roboética, `resolucion-tp5` |
| U2 | Aprendizaje automático | TP6 | 51 | Episodio VII (partes 1–3), `resolucion-tp6` |
| U3 | SBC: arquitectura, Prolog y explicaciones | TP7 | 41 | Episodio VIII, `resolucion-tp7` (ej. 1–6) |
| U4 | Información contradictoria y valores de certeza | TP7 | 29 | Episodio IX (valores de certeza), Ejemplo SBC, ej. 7 |
| U5 | Informantes | TP7 | 22 | Episodio IX (informantes), Ejemplo SBC, ej. 8 |
| U6 | Razonamiento basado en argumentos | TP7 | 13 | Episodio X, parte 1 |
| U7 | DeLP | TP8 | 38 | Episodio X, parte 2, Resolución con DeLP, enunciado del TP8 |

Cada pregunta trae una explicación que dice por qué la correcta es correcta y, cuando hace falta, por qué falla el
distractor más tentador. Termina con la fuente: episodio y título de la diapositiva, o ejercicio del TP.

## Cómo usarlo

- Abrir `index.html` con el navegador (doble clic, o `xdg-open quiz/index.html`). Es un único archivo sin
  dependencias. Sin conexión cambia la tipografía, pero funciona igual.
- Atajos: A–D o 1–4 para responder, ← → para moverse.
- El progreso se guarda en el navegador (`localStorage`, clave `ia-uns-2026-quiz-v1`). Si se borran los datos del
  sitio, se pierde.
- Sugerencia: hacer cada unidad después de repasar sus diapositivas, y al final usar «Reintentar las incorrectas».

## Cómo están armadas las opciones

El formato sale del quiz de ejemplo de otra materia (`ejemplos/examen/quiz/`). En ese quiz la correcta solía delatarse
por ser la más larga: lo era en el 66% de las preguntas, y en promedio medía 1,93 veces lo que miden las incorrectas.
Acá se evita eso:

- las cuatro opciones tienen un largo y un nivel de detalle parecidos;
- los distractores son errores plausibles:
  - conceptos vecinos;
  - la fuente equivocada (UNESCO, Parlamento Europeo o Argentina);
  - relaciones invertidas;
  - resultados de un cálculo con un error típico, como multiplicar en vez de tomar el mínimo;
- no hay frases idénticas con una palabra cambiada, ni «todas las anteriores»;
- si las incorrectas traen una justificación, la correcta también («laser, porque…»), para que no se distinga por ser
  la única sin ella.

`build.py` lo controla al generar el HTML. Valores del quiz completo:

- la correcta es la opción más larga en el 22% de las preguntas y la más corta en el 17% (por azar, cerca del 25%);
- su largo promedio respecto de las incorrectas es 1,00;
- aparece en la posición A, B, C o D 55, 66, 59 y 67 veces.

## Cómo regenerar

```sh
python3 -I quiz/fuente/build.py                 # regenera quiz/index.html
python3 -I quiz/fuente/build.py salida.html     # además, una versión sin <html> para publicar como artifact
```

`build.py` muestra, por unidad, los porcentajes de sesgo y las preguntas más sesgadas. Al agregar o editar preguntas,
conviene mirar los dos porcentajes (más larga y más corta): corregir solo uno tiende a pasarse al otro extremo.

## Estructura

```
quiz/
  index.html              quiz generado (no editar a mano)
  plan.md                 plan por etapas con el que se armó
  fuente/
    template.html         interfaz (HTML + CSS + JS); los datos se insertan en /*__DATA__*/
    comun.py              Q(pregunta, correcta, [3 incorrectas], explicación) y estadísticas de sesgo
    build.py              arma index.html; el orden de las opciones se baraja con una semilla fija por pregunta
    u1_robotica.py … u7_delp.py   un banco por unidad
  ejemplos/               quiz de otra materia que se usó como modelo (solo referencia)
```

Para agregar una unidad: crear `uN_tema.py` con `U = dict(id=..., nombre=..., tp=..., preguntas=[Q(...), ...])` y
sumarla a `MODULOS` en `build.py`.

## Pendiente

- **DeLP (U7):** el TP8 todavía no tiene resolución. Cuando la tenga, conviene agregar preguntas sobre líneas de
  argumentación aceptables y sobre los programas P2 y P5, que las diapositivas no cubren.
- **Robótica:** la diapositiva de la palabra «robot» la atribuye a Josef Čapek, y el texto del Parlamento Europeo, a
  Karel. Por eso no hay pregunta sobre quién la inventó.
