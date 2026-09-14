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

## 1.3. Operadores de cambio y la Identidad de Levi

**Expansión (K + α):** incorpora la nueva creencia α a la base conservando todo lo anterior. El resultado es `Cn(K ∪ {α})`: ninguna creencia previa se pierde, el operador es monótono. Su desventaja es que no resuelve conflictos: si α contradice a K, la base resultante es inconsistente (y por lo tanto trivial).

**Contracción (K − α):** elimina la creencia α (y todo lo que la implica) de la base, reteniendo el resto lo más intacto posible. Se usa típicamente para eliminar una creencia no deseada o para reparar una inconsistencia, quitando alguna de las sentencias en conflicto. Es no monótona: al eliminar una creencia pueden perderse consecuencias que antes se derivaban.

**Revisión (K ∗ α):** incorpora la nueva información α garantizando dos condiciones: la base resultante es consistente **y** contiene a α. Es decir, cuando α contradice a K, primero se elimina lo que entra en conflicto con α y luego se agrega α.

**Identidad de Levi:** expresa la revisión en términos de contracción y expansión:

```
K ∗ α = (K − ¬α) + α
```

Es decir, revisar por α equivale a: primero contraer la base eliminando la negación de la nueva información (¬α), y luego expandir agregando α. De esta forma, la contradicción se resuelve al contraer antes de expandir, garantizando consistencia e incorporación de α.

## 1.4. Revisión priorizada vs. no priorizada

**Revisión priorizada:** la nueva información percibida tiene siempre mayor prioridad que las creencias previas. Cuando la nueva percepción entra en conflicto con la base, se elimina (contrae) todo lo que se oponga a la nueva información, que siempre termina incorporada. Es la postura de "la percepción más reciente es la más confiable": modela agentes en entornos dinámicos, donde el conocimiento anterior queda desactualizado rápidamente.

*Escenario conveniente:* un robot o agente que se mueve por un entorno cambiante y percibe el mundo con sensores confiables. Por ejemplo, un agente de seguridad que registra que se activa un sensor de movimiento: aunque antes creyera que nadie estaba en la sala, la percepción nueva de "movimiento" es más reciente y fiable, por lo que debe revisar su base y creer lo recién percibido.

**Revisión no priorizada:** la nueva información **no** tiene garantizada la incorporación: si contradice creencias previas, puede ser rechazada cuando estas se consideran más confiables o mejor justificadas que la percepción nueva. La decisión de aceptar o no la nueva información depende de su confiabilidad y no simplemente de ser la más reciente.

*Escenario conveniente:* ambientes con fuentes de distinta confiabilidad. Por ejemplo, un agente que recibe información de otros agentes o de fuentes no verificadas (rumores, sensores defectuosos, noticias dudosas). Si un agente confiable le comunica "el tesoro no está en la posición A" pero un sensor poco fiable reporta lo contrario, conviene no priorizar la percepción nueva y conservar la creencia que se considera más sólida.

## 1.5. ¿Puede una base consistente volverse inconsistente tras un cambio?

Supongamos que B es consistente y queremos analizar cada operador aplicado por la sentencia `a`.

**Expansión (B + a): Sí, puede resultar inconsistente.**
La expansión agrega `a` sin eliminar ninguna creencia previa. Si B ya implicaba `¬a`, entonces al incorporar `a` se deriva tanto `a` como `¬a`.

Ejemplo:
```
B = { ¬a }          (consistente)
B + a = Cn({ ¬a, a })   (inconsistente, ya que se derivan a y ¬a)
```
La expansión no ofrece garantía de consistencia: solo asegura que la nueva creencia queda incluida.

**Contracción (B − a): No puede resultar inconsistente.**
La contracción solo elimina creencias de B (y sus consecuencias), nunca agrega información nueva. Como B es consistente, todo subconjunto de `Cn(B)` (y en particular el resultado de la contracción) también lo es. Por lo tanto, `B − a` es siempre consistente.

**Revisión (B ∗ a): No puede resultar inconsistente.**
Por definición, la revisión impone que la base resultante sea consistente **y** contenga a `a`. Siguiendo la Identidad de Levi, `B ∗ a = (B − ¬a) + a`: la contracción elimina primero lo que entra en conflicto con `a`, dejando una base que ya no deriva `¬a`; entonces la expansión por `a` ya no produce contradicción. El resultado es, por construcción, consistente.

## 1.6. Mismo análisis cuando B es de antemano inconsistente

Ahora supongamos que B es inconsistente desde el inicio. En ese caso `Cn(B) = L`: de una base inconsistente se deduce cualquier sentencia del lenguaje.

**Expansión (B + a): Necesariamente inconsistente.**
Como B ya es inconsistente, su conjunto de consecuencias es todo el lenguaje. Agregar `a` no elimina nada, por lo que `B + a = Cn(B ∪ {a}) = L` sigue siendo inconsistente. La expansión no puede reparar una base ya contradictoria.

**Contracción (B − a): Puede ser consistente o inconsistente.**
La contracción solo elimina creencias, nunca agrega, por lo que no puede *introducir* nuevas contradicciones. Pero tampoco garantiza eliminarlas: si las sentencias removidas no tocan la fuente del conflicto, la base permanece inconsistente; si logran eliminar la fuente de la contradicción, la base se restaura a un estado consistente.

Ejemplo: `B = { a, ¬a }` (inconsistente).
- Si la contracción elimina `¬a`, queda `{ a }`: **consistente** (se reparó la base).
- Si, en cambio, la contracción solo retirara otras creencias dejando `a` y `¬a` juntas, el resultado seguiría siendo **inconsistente**.

**Revisión (B ∗ a): Siempre consistente (si `a` es consistente).**
La revisión es el único operador que por definición garantiza la consistencia del resultado: al revisar, se contrae lo necesario (vía Levi: `B ∗ a = (B − ¬a) + a`, o vía kernels) para que ningún conflicto persista y luego se incorpora `a`. De hecho, revisar es el operador adecuado justamente para *sanear* una base inconsistente mientras se incorpora nueva información del entorno.

## 3. Kernel, caso de estudio

Base de creencias:

```
K = { c, b, c → b, d, d → a, d → e }
```

### 3.1. Expansión de K con ¬a

Si se expande K con `¬a`, la base resultante es **inconsistente**.

Es decir: `K` ya contiene las creencias `d` y `d → a`. Aplicando modus ponens se deduce:

```
d, d → a  ⟹  a
```

Por lo tanto `K ⊢ a`. Al expandir agregamos `¬a`, conservando todo lo anterior (la expansión no elimina creencias):

```
K + ¬a = Cn( K ∪ {¬a} )
```

Ahora de la base se derivan tanto `a` como `¬a`. Por el principio de explosión lógica (*ex falso quodlibet*), de `K + ¬a` se sigue cualquier sentencia del lenguaje, por lo que la base queda trivializada e inconsistente. La expansión es monótona y no protege contra contradicciones: falla justamente cuando la nueva creencia contradice alguna consecuencia ya presente en la base.