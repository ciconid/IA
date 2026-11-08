# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

No es un proyecto de software: es material de estudio de la materia **Inteligencia Artificial** (UNS, Dr. Alejandro J. García, 2026). El trabajo típico es resolver los Trabajos Prácticos de a un ejercicio por vez, generando un PDF con LaTeX (ver "Formato de las resoluciones").

## Reglas para las respuestas

- **Respuesta**: lo mínimo y suficiente para contestar la consigna. Tomarlo preferentemente de las diapositivas de la cátedra; si a la cátedra le falta algo esencial para contestar, completarlo con los libros (la nota al pie deja ver qué parte no es de la cátedra).
- **EXTRAS**: todo lo que profundiza o amplía la respuesta sin ser necesario para contestar, venga de la cátedra o de los libros. Lo que solo está en la cátedra pero no hace falta para contestar también va acá.
- No repetir información. EXTRAS solo puede tener información **nueva** respecto de la respuesta: si algo ya está arriba (aunque sea en otro idioma, con otras palabras o como cita textual), no va en EXTRAS; a lo sumo se agrega la otra fuente a la nota al pie de la respuesta ("Misma idea en AIMA, §2.1, p. 34"). Antes de compilar, revisar cada viñeta de EXTRAS contra la respuesta y contra las demás viñetas de EXTRAS.
- Citar siempre las fuentes (cátedra y libros), en notas al pie.
- Escribir respuestas sin mucha verbosidad innecesaria
- En caso de citar fuentes en inglés, no traducir al español. Poner el texto original.
- Si varias fuentes expresan la misma idea o definición, citar solo una de ellas. En todo caso, agregar la otra fuente en la misma nota al pie, sin agregar su contenido.
- Siempre priorizar mostrar listas con bullet-points en lugar de usar prosa.
- **Tablas y pictogramas siempre que se pueda** (comparaciones, clasificaciones, ciclos, procesos, arquitecturas): sirven como referencia visual de los conceptos. Van **además** del texto, aunque muestren exactamente lo mismo. No deben agregar información que no esté en el texto. Dibujarlos con TikZ (hay íconos reutilizables en el preámbulo).
- **Figuras en el lugar donde se usan, aunque se repitan**: en resoluciones de TPs y resúmenes, si un ejercicio o sección necesita una figura, pictograma o gráfico que ya apareció antes, se vuelve a poner ahí completo, en vez de remitir con "ver figura del ejercicio 2". Esto aplica solo a figuras, pictogramas y gráficos; párrafos y texto **no** se repiten (para eso sí vale remitir a donde ya está). Estas dos (figura junto al texto y figura repetida donde se necesita) son las únicas repeticiones permitidas.

## Reporte al terminar

- Después de resolver ejercicios a pedido del usuario, **no** resumir lo que se hizo. Reportar solo lo que salió mal: errores, problemas del enunciado (p. ej. datos faltantes), supuestos que hubo que tomar, cosas que no se pudieron verificar.
- Si no hubo ningún inconveniente, una sola línea avisando que terminó con éxito.

## Estructura

- `temaN/` — un directorio por unidad, con:
  - `ale-2026-IA-NN-*.pdf`: diapositivas de la cátedra (fuente primaria). La mayoría se titula "Episodio <romano>"; las de robótica (tema5) no tienen número.
  - `2026 - IA - TP N - *.pdf`: enunciado del TP.
  - Otros PDFs (`Traza ...`, `Ejemplo ...`): ejemplos resueltos de la cátedra.
  - `resolucion-tpN.tex` + `.pdf`: resolución (desde el TP5). `tp1.md`–`tp4.md` son resoluciones viejas en Markdown con otro formato; no se migran.
- La numeración de directorios no coincide siempre con la de los TPs: `tema8/` contiene TP 7 (SBC) y TP 8 (DeLP); no hay `tema7/`.
- `libros/` — bibliografía complementaria: AIMA 3.ª ed. (Russell & Norvig) y Computational Intelligence (Poole, Mackworth, Goebel).
- `plantilla/preambulo.tex` — preámbulo LaTeX común a todas las resoluciones.

## Leer los PDFs

- Usar `pdftotext` (instalado), p. ej. `pdftotext -layout archivo.pdf -` o `pdftotext -f 60 -l 70 libro.pdf -` para un rango de páginas de los libros (son grandes; no extraerlos completos). Extraer a la carpeta scratchpad, nunca dentro del repo.
- AIMA: página del libro = página del PDF − 19. Algunos capítulos (p. ej. el 25, Robotics) salen con la fuente mal codificada en `pdftotext`; en ese caso leer la página como imagen (Read con `pages`, o `pdftoppm -r 110 -png`).
- Si una diapositiva tiene diagramas o tablas relevantes, leerla también como imagen.

## Formato de las resoluciones (LaTeX)

- Un archivo por TP: `temaN/resolucion-tpM.tex`, que hace `\input{../plantilla/preambulo}`. Tomar `tema5/resolucion-tp5.tex` como modelo.
- **Índice obligatorio**: después de `\maketitle` y `\notafuentes` va `\indice` (macro del preámbulo: índice con hipervínculos).
- Por cada ejercicio: `\section{Ejercicio N}` y, para los incisos, `\subsection{a)}`, **sin asterisco** (no se numeran, pero así entran al índice). Cada `\section` empieza en página nueva automáticamente (`\sectionbreak` del preámbulo); los incisos de un mismo ejercicio van seguidos.
- Dentro de cada ejercicio o inciso: caja `enunciado` con la consigna textual, la respuesta (mínima, en viñetas) y después una caja `extras` con la ampliación. Caja `aviso` para ambigüedades del enunciado o erratas.
- Citas: **nunca en el cuerpo del texto**, siempre en nota al pie con los macros del preámbulo: `\catedra{Episodio I}{<título de diapositiva>}`, `\aima{25.1}{973}`, `\pmg{12.1}{443}` y `\fuentes{...}` para varias en una nota. Si varias viñetas seguidas salen de la misma fuente, una sola nota en la viñeta que las agrupa.
- Citas textuales en inglés con `\cita{...}`, sin traducir.
- Compilar dentro de `temaN/`: `latexmk -pdf -interaction=nonstopmode resolucion-tpM.tex`, corregir errores y warnings relevantes, y limpiar con `latexmk -c resolucion-tpM.tex` (dejar solo `.tex` y `.pdf`).
- Revisar visualmente el PDF (`pdftoppm -r 70 -png` al scratchpad y mirar las páginas).
- Trampas de babel español: `es-noshorthands` + `\usetikzlibrary{babel}` ya están en el preámbulo; en matemática escribir `$35\%$`, no `$35\,\%$`; decimales `0{,}65`.

## Otros archivos

- `quiz/`: quiz interactivo generado con `python3 -I quiz/fuente/build.py`. Antes de agregar o editar preguntas, leer
  `quiz/README.md`: tiene las reglas de las preguntas (cada una se responde sola, sin ir a buscar el TP o la
  diapositiva; KB una cláusula por línea; sesgo de largo de las opciones).

- `tema3/busqueda.pl`: código Prolog provisto por la cátedra (búsqueda en un laberinto). Se ejecuta con SWI-Prolog (`swipl tema3/busqueda.pl`), que no está instalado en este entorno.

## Git

- Repo de estudio: los commits son siempre `git add .` + commit directo en `main` (sin ramas). No hace falta pedir confirmación para commitear cuando el usuario lo pide.
