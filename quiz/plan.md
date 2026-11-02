# Plan: quiz de IA (temas 5, 6 y 8)

Quiz interactivo de opción múltiple, con el mismo formato que `ejemplos/examen/quiz/`:
- un único `index.html` sin dependencias, generado con Python a partir de bancos de preguntas;
- unidades como pestañas, tablero con el estado de cada pregunta y progreso guardado en `localStorage`.

## Estructura de archivos

```
quiz/
  plan.md                 este archivo
  README.md               cómo usar y regenerar (etapa final)
  index.html              quiz generado (no se edita a mano)
  fuente/
    template.html         copia del ejemplo, adaptada (título, clave de localStorage)
    comun.py              Q(pregunta, correcta, [incorrectas], explicación) + chequeos
    build.py              arma index.html y muestra estadísticas de calidad
    u1_robotica.py
    u2_aprendizaje.py
    u3_sbc.py
    u4_certeza.py
    u5_informantes.py
    u6_argumentos.py
    u7_delp.py
```

Regenerar: `python3 -I quiz/fuente/build.py`.

## Unidades

| Unidad | Tema | Fuentes | Preguntas aprox. |
|---|---|---|---|
| U1 · TP5 | Robótica, roboética y legislación | ep. 08, `resolucion-tp5` | 40 |
| U2 · TP6 | Aprendizaje automático | ep. 09, 10 y 11, `resolucion-tp6` | 45 |
| U3 · TP7 | SBC: arquitectura, Prolog, explicaciones | ep. 12 (Episodio VIII), ej. 1–6 de `resolucion-tp7` | 35 |
| U4 · TP7 | Información contradictoria y valores de certeza (MYCIN) | ep. 13, Ejemplo SBC, ej. 7 | 30 |
| U5 · TP7 | Informantes (eslabón más débil) | ep. 14, Ejemplo SBC, ej. 8 | 30 |
| U6 · TP7 | Razonamiento basado en argumentos | ep. 15 | 20 |
| U7 · TP8 | DeLP | ep. 16, `Resolución con DeLP`, enunciado del TP8 | 40 |

Si al leer el material una unidad queda muy cargada (por ejemplo, la U2), se divide en dos.

## Contenido de las preguntas

- **Fuente**: las diapositivas de la cátedra; las resoluciones de los TPs, para lo que el TP pregunta y las diapositivas no cubren. Nada que no esté en ese material.
- **Mezcla de tipos**:
  - conceptuales (definiciones, diferencias, para qué sirve cada cosa);
  - "¿cuál de estas NO…?", con moderación;
  - de aplicación, con KBs chicas en el enunciado. Por ejemplo, calcular un $vc$ con MYCIN, el informante de una derivación o la respuesta de DeLP a una consulta. Estas son las que más se parecen a los TPs.
- **Explicación**: 1–2 oraciones que digan por qué la correcta es correcta y, si hace falta, por qué falla el distractor más tentador. Al final, la fuente corta, por ejemplo `(Ep. IX, informantes)`.
- Sin preguntas de memoria pura sobre datos anecdóticos (fechas de un video, nombres de un aeropuerto). Sí entran fechas o nombres que la cátedra remarca, como Čapek/RUR o la ley europea de 2024.

## Criterios para las opciones (lo que se refina respecto del ejemplo)

Problema del ejemplo: la correcta suele ser la más larga y detallada. Para evitarlo:

1. **Largo parejo**: las cuatro opciones tienen aproximadamente el mismo largo y nivel de detalle. Si la correcta necesita un matiz, los distractores también llevan uno (falso).
2. **Distractores plausibles, no triviales**: cada incorrecta es un error que un alumno podría cometer de verdad:
   - confundir dos conceptos vecinos (mínimo/máximo, regla estricta/rebatible, ética/moral, supervisado/no supervisado);
   - atribuir algo a la fuente equivocada (UNESCO vs. Parlamento Europeo vs. Argentina);
   - invertir una relación causa-efecto o la dirección de una comparación;
   - un resultado numérico al que se llega con un error típico (multiplicar en vez de tomar el mínimo, olvidar que un CF negativo da 0).
3. **Tampoco trampas de redacción**: los distractores no son la misma frase con una palabra o un artículo cambiado. Cada opción debe distinguirse por una idea, no por un detalle gramatical. No hay preguntas innecesariamente difíciles.
4. **Sin pistas formales**:
   - nada de "todas las anteriores" ni "ninguna";
   - nada de absolutos ("siempre", "nunca") solo en los distractores;
   - la correcta no repite palabras del enunciado más que las otras.
5. **Chequeo automático en `build.py`**:
   - porcentaje de preguntas en que la correcta es la opción más larga, y en que es la más corta (objetivo: cerca del 25%, que es lo que daría el azar);
   - largo promedio de la correcta contra el de las incorrectas;
   - distribución de la posición de la correcta (ya existe en el ejemplo);
   - listado de las preguntas más sesgadas, para revisarlas a mano.

## Etapas

Cada etapa termina con `build.py` corriendo sin errores y con sus estadísticas revisadas. Cuando lo pidas, se hace commit.

- [x] **Etapa 0, infraestructura**. Referencia medida en el ejemplo: la correcta es la más larga en el 66% de las preguntas, con un largo c/w de 1,93:
  - copiar `template.html`, `build.py` y `comun.py`;
  - adaptar el título ("Quiz de IA · UNS 2026"), la clave de `localStorage` y la etiqueta de las pestañas;
  - agregar los chequeos de sesgo de largo;
  - medir el sesgo del ejemplo como referencia.
- [x] **Etapa 1**: U1, robótica y roboética. Quedó en 53 preguntas: la correcta es la más larga en el 17% y la más corta en el 25%, con un largo c/w de 0,99.
- [x] **Etapa 2**: U2, aprendizaje automático. No se dividió: quedó en 51 preguntas, con la correcta como más larga en el 22% y como más corta en el 20%, y un largo c/w de 1,02. Corregir el sesgo de largo puede pasarse al otro extremo (en un momento la correcta fue la más larga solo en el 2%), así que hay que mirar los dos porcentajes.
- [x] **Etapa 3**: U3, SBC. Quedó en 41 preguntas: la correcta es la más larga en el 20% y la más corta en el 12%, con un largo c/w de 1,05.
- [x] **Etapa 4**: U4, valores de certeza. Quedó en 29 preguntas: la correcta es la más larga en el 28% y la más corta en el 24%, con un largo c/w de 0,93. Ojo con las respuestas numéricas: hay tres que dan 0, así que el 0 también aparece como distractor.
- [x] **Etapa 5**: U5, informantes. Quedó en 22 preguntas, menos de las 30 previstas porque el material es más acotado: la correcta es la más larga en el 23% y la más corta en el 14%, con un largo c/w de 0,97. El ejemplo de Punta Tombo quedó afuera: depende de mes(septiembre), que no está en la KB, y las diapositivas no son consistentes.
- [x] **Etapa 6**: U6 y U7, argumentación y DeLP.
  - U6: 13 preguntas; la correcta es la más larga en el 23% y la más corta en el 8%. El grafo de derrotas de la diapositiva no se usó, porque el sentido de algunas flechas es ambiguo; en su lugar hay cadenas de derrota descriptas en el texto.
  - U7: 38 preguntas; la correcta es la más larga en el 24% y la más corta en el 11%. Salen de las diapositivas y de la «Resolución con DeLP», porque el TP8 todavía no tiene resolución.
  - Total del quiz: 247 preguntas; la correcta es la más larga en el 21% y la más corta en el 17%, con un largo c/w de 1,00.
- [x] **Etapa 7, cierre**:
  - revisión de duplicados: se compararon todos los pares de enunciados y de respuestas. Dos pares se superponían en contenido y se reemplazó una pregunta de cada uno: en la U6, «la derivación es una razón» se cambió por por qué d1 y d2 están en conflicto; en la U5, «indeciso» se cambió por la definición de min(I). Los demás pares parecidos solo comparten la plantilla del enunciado;
  - `README.md` escrito;
  - revisión visual en Chrome headless: pestañas, pregunta respondida con su devolución, y símbolos de DeLP;
  - publicación como artifact: pendiente de que decidas.

Después de cada etapa conviene que hagas la unidad en el navegador: si alguna pregunta se responde sin saber el tema, o es ambigua, se ajusta antes de seguir.
