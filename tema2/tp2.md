# Trabajo Práctico 2

## 1.1. Definición de conceptos

**Dato:** conjunto de símbolos o representaciones sin interpretar, que por sí solos no tienen significado ni utilidad. Son la unidad mínima de información (números, palabras, caracteres, etc.).

**Creencia:** disposición o estado mental que se acepta como verdadero, sin que necesariamente exista una justificación completa o una verificación empírica. Una creencia puede ser verdadera o falsa y no siempre se sostiene sobre evidencia suficiente.

**Información:** dato procesado y dotado de significado dentro de un contexto, que reduce la incertidumbre y es útil para quien la interpreta. Surge cuando los datos se organizan, contextualizan e interpretan.

**Conocimiento:** información integrada y contextualizada con la experiencia, justificación o comprensión, que permite tomar decisiones, resolver problemas o actuar. Puede verse como la relación entre el agente y la información que este dispone de manera justificada; suele implicar una creencia verdadera y justificada.

## 1.2. Importancia de la consistencia en las bases de creencias

En la teoría de Cambio de Creencias, mantener la consistencia resulta de vital importancia porque una base de creencias inconsistente hace que cualquier sentencia del lenguaje sea consecuencia lógica de ella (principio de explosión lógica: *ex falso quodlibet*). Si dentro de una misma base se pueden derivar tanto una sentencia `a` como su negación `¬a`, el operador de consecuencia lógica `Cn` devuelve el lenguaje completo, es decir, toda sentencia es "creída". Esto vuelve a la base inútil para el agente, ya que no puede distinguir qué información es verdadera y qué es falsa, y pierde todo poder discriminatorio.

**Ejemplo de base consistente:**

K = { llueve, llueve → calle_mojada }

De esta base se deriva que la calle está mojada, pero no se genera ninguna contradicción.

**Extensión que la vuelve inconsistente:**

Extendemos la base con `¬calle_mojada`:

K' = { llueve, llueve → calle_mojada, ¬calle_mojada }

Ahora de K' se pueden derivar tanto `calle_mojada` como `¬calle_mojada`, y por explosión lógica se deriva cualquier sentencia (por ejemplo `2 + 2 = 5`, o cualquier otra proposición del lenguaje).

**Problema que surge:** al ser inconsistente, la base trivializa el conocimiento: toda sentencia y su negación son consecuencias lógicas, por lo que la base deja de informar sobre el mundo real. Ningún agente racional, regla de inferencia o sistema de razonamiento automático puede confiar en ella para tomar decisiones, y cualquier tarea de deducción o de elección de cursos de acción pierde sentido.