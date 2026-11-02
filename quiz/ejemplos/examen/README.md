# Material para el examen teórico de APS (7502), 27/10/2026

Todo lo necesario para estudiar el examen teórico, en un solo lugar. El contenido se limita a lo que dio la
cátedra: diapositivas, enunciados de los TPs y resoluciones publicadas. La única excepción son los temas que el
TP6 pregunta y no tienen diapositivas (métricas de Fenton y auditoría de sistemas). Esos salen de la
bibliografía y están marcados en el resumen.

## Qué hay

| Archivo | Para qué sirve |
|---|---|
| `resumen/resumen-final.pdf` | Resumen autocontenido de todo el programa (37 págs.). Es lo único que hay que leer. |
| `practica/ejercicios-examen.pdf` | Guía de ejercicios por bloque, con las plantillas y fórmulas que traería el enunciado. |
| `practica/respuestas-ejercicios.pdf` | Respuestas desarrolladas de la guía, para comparar después de hacerla. |
| `quiz/index.html` | Quiz interactivo de 477 preguntas de opción múltiple, en 8 unidades. |

Los `.tex` son las fuentes de los PDFs. `quiz/fuente/` tiene las preguntas y el generador del quiz.

## Cómo estudiar (sugerencia)

1. Leer el resumen por sección. Cada una termina con un recuadro "En resumen".
2. Después de cada sección, hacer la unidad correspondiente del quiz.
3. Hacer la guía de ejercicios sin mirar y recién después comparar con las respuestas. Priorizar los tipos que
   según el docente son "muy similares a los de los TPs": red PDM con planificación temprana y tardía, Puntos de
   Función, matriz persona/perfil, selección por velocity, comparación de soluciones, y requerimientos y
   riesgos a partir de un enunciado largo.
4. Al final, repasar la hoja de fórmulas y las preguntas de repaso del resumen (§12 y §13). Las fórmulas vienen
   en el enunciado, así que alcanza con saber qué significa cada término y cómo interpretar el resultado.

## Cómo usar el quiz

- **Online:** https://claude.ai/artifact/CS2AC9E3NM52cMzLLpiLXc (cualquiera con el link puede verlo).
- **Sin internet / sin el artifact:** abrir `quiz/index.html` con el navegador (doble clic, o
  `xdg-open quiz/index.html` en Linux). Es un único archivo sin dependencias. Sin conexión cambia la
  tipografía, pero funciona igual. Se puede copiar o mandar el archivo solo.
- El progreso se guarda en el navegador (`localStorage`), por separado para el archivo local y para el link.
  Si se borran los datos del sitio, se pierde.

## Cómo regenerar

Desde esta carpeta:

```sh
python3 -I quiz/fuente/build.py                    # regenera quiz/index.html
(cd resumen  && latexmk -pdf resumen-final.tex         && latexmk -c resumen-final.tex)
(cd practica && latexmk -pdf ejercicios-examen.tex     && latexmk -c ejercicios-examen.tex)
(cd practica && latexmk -pdf respuestas-ejercicios.tex && latexmk -c respuestas-ejercicios.tex)
```

Para compartir con compañeros alcanza con comprimir la carpeta `examen/`.

## Pendiente

- **Auditoría (TP6):** la sección del resumen sale del libro de Weber porque la cátedra todavía no subió las
  diapositivas. Cuando estén, hay que reemplazarla y revisar las preguntas de auditoría del quiz.
