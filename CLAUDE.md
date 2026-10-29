# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## Qué es este repo

No es un proyecto de software: es material de estudio de la materia **Inteligencia Artificial** (UNS, Dr. Alejandro J. García, 2026). El trabajo típico es responder las consignas de los Trabajos Prácticos en Markdown siguiendo las reglas de `AGENTS.md`.

## Estructura

- `temaN/` — un directorio por unidad, con:
  - `ale-2026-IA-NN-*.pdf`: diapositivas de la cátedra (fuente primaria). Cada una se titula "Episodio <romano>", que es como se citan.
  - `2026 - IA - TP N - *.pdf`: enunciado del TP.
  - Otros PDFs (`Traza ...`, `Ejemplo ...`): ejemplos resueltos de la cátedra.
  - `tpN.md`: respuestas al TP (se crean/editan aquí).
- La numeración de directorios no coincide siempre con la de los TPs: `tema8/` contiene TP 7 (SBC) y TP 8 (DeLP); no hay `tema7/`.
- `libros/` — bibliografía para la sección "EXTRAS": AIMA 3ª ed. (Russell & Norvig) y Computational Intelligence (Poole, Mackworth, Goebel).

## Leer los PDFs

Usar `pdftotext` (instalado), p. ej. `pdftotext -layout archivo.pdf -` o `pdftotext -f 60 -l 70 libro.pdf -` para un rango de páginas de los libros (son grandes; no extraerlos completos).

## Convenciones de las respuestas (ver `tema3/tp3.md`, `tema4/tp4.md`)

- Encabezados: `# Trabajo Práctico N — <tema>`, `## <n>. <sección>`, `### <n>.<letra>. <consigna textual>`, y `#### EXTRAS` dentro de cada consigna.
- Formato de citas:
  - Cátedra: `[García, Episodio V, sec. "<título de diapositiva>"]`
  - AIMA: `[RN10, sec. 10.1, p. 369]`
  - Poole et al.: `[PMG, sec. 8.3, p. 299]`
- Al usar una fuente redundante: "La misma definición se encuentra en AIMA [RN10, ...]" sin repetir el contenido.

## Otros archivos

- `tema3/busqueda.pl`: código Prolog provisto por la cátedra (búsqueda en un laberinto). Se ejecuta con SWI-Prolog (`swipl tema3/busqueda.pl`), que no está instalado en este entorno.
