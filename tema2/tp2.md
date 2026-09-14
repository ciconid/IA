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

### 3.5. ¿Alguna Kᵢ es igual a K?

No. Ninguna de las bases obtenidas (K₁, K₂ ni K₃, en ninguna de sus variantes) coincide con la base original K = {c, b, c→b, d, d→a, d→e}.

- K₃⁽¹⁾ carece de `d` (tiene `a` en su lugar, agregado explícitamente).
- K₃⁽²⁾ carece de `d→a` (tiene `a` asertado, pero sin la regla que lo relacionaba con `d`).

**Conclusión:** el proceso de revisar por `¬a`, contraer por `¬a` y volver a expandir con `a` no recupera la base original. Esto ilustra que las operaciones de cambio de creencias (en particular la revisión) implican una pérdida irreversible de información: al revisar por `¬a` se tuvo que sacrificar `d` o `d→a` para evitar la inconsistencia, y esa información nunca se recupera aunque luego se vuelva a agregar `a`. Es decir, revisión + contracción + expansión no forman una operación identidad sobre la base original, a diferencia de lo que podría esperarse ingenuamente.

## 4. El tesoro

### 4.2. Regla deductiva vs. percepción reciente

Ante una inconsistencia entre una **regla deductiva** y una **percepción reciente**, la elección racional es descartar la **regla deductiva** y conservar la **percepción reciente**.

¿Por qué?
- La percepción reciente refleja el **estado actual** del entorno (información proveniente de los sentidos o de otros agentes en el momento presente). En un mundo dinámico, el estado del mundo puede cambiar y es la percepción más reciente la que mejor describe "cómo están las cosas ahora".
- La regla deductiva, en cambio, suele expresar conocimiento general o estático del dominio. Si bien sirve mientras sus condiciones se cumplen, no está garantizado que siga siendo aplicable en el contexto puntual, y en un conflicto puntual es más probable que la percepción tenga razón.
- Además, el hecho de que se produzca una inconsistencia indica que una de las dos ya no describe correctamente el mundo; dado que las percepciones son datos directos y los algoritmos asumen que son fiables, se prefiere la información nueva y se sacrifica la regla que la contradice.

En términos de dinámica de creencias, esto corresponde a una **revisión priorizada**: la información entrante (percepción) tiene mayor prioridad que las creencias previas (reglas), por lo que ante el conflicto se contrae la regla y se incorpora la percepción, manteniendo la base consistente.

## 5. Galería de arte

Reglas y hechos de conocimiento previo:

```
1. noche → cerrado
2. movimiento, cerrado → intruso
3. sensor_movimiento_activo → movimiento
4. noche → ¬día
```

### 5.2. Revisión priorizada vs. no priorizada en el escenario

En este escenario asumimos que el operador **no priorizado rechaza toda información inconsistente con la base actual**; en cambio, el **priorizado siempre incorpora la percepción nueva**, descartando (contrayendo) lo que la contradiga.

El punto donde ambas estrategias divergen es la percepción número 7: **noche**. Después de las percepciones 1–6, la base del agente contiene `día` (percibido en el paso 1) y la regla `noche → ¬día`. Por lo tanto:

- **Revisión priorizada:** `noche` tiene prioridad. Se contrae la base eliminando una de las creencias en conflicto (típicamente `día`), y `noche` queda incorporada. A partir de allí el agente deriva `cerrado` (regla 1, conjuntamente con `noche`) y, como ya percibió `sensor_movimiento_activo` → `movimiento`, deriva `intruso` (regla 2). El agente pasa a creer que es de noche y que hay un intruso, consistente con el mundo real del problema.

- **Revisión no priorizada:** al ser `noche` inconsistente con la base (porque `día` y `noche → ¬día` dan `¬noche`), el operador **rechaza** la percepción. La base conserva `día` y nunca incorpora `noche`: el agente sigue creyendo que es de día, no deriva `cerrado` ni `intruso`, y se pierde la información clave del cambio de contexto. Cuando en el paso 8 percibe `¬intruso`, como "intruso" nunca se derivó, la percepción es consistente y se incorpora sin problemas, manteniendo una base internamente consistente pero desconectada de la realidad.

**Conclusión:** la revisión priorizada mantiene ambas propiedades (consistencia *e* incorporación de la percepción), lo que en un entorno dinámico como el de la galería resulta correcto: los sensores son confiables y las percepciones recientes reflejan el estado actual del mundo. La revisión no priorizada, al rechazar el conflicto, preserva la consistencia pero renuncia a información nueva legítima (`noche`), dejando al agente con un modelo del mundo desactualizado y con decisiones de seguridad incorrectas. Solo convendría si las percepciones fueran poco confiables (por ejemplo, sensores defectuosos).

## 6. Comportamientos de agentes frente a las percepciones

### 6.1. Agente A1 (descarta todo, conserva solo la última percepción)

El comportamiento de A1 corresponde al operador de **reset (abandon)**, denotado `∘`, definido como:

```
K ∘ α = Cn({α})
```

Es decir, la base resultante contiene únicamente las consecuencias de la percepción más reciente y nada de lo anterior: se descarta por completo el conocimiento previo (incluso las creencias que no entraban en conflicto con `α`) y se conserva solo `α`. Es el operador de cambio más radical: a diferencia de la revisión (que intenta preservar todo lo posible), el reset no preserva nada. Se relaciona además con una contracción total de la base seguida de una expansión por `α`.

### 6.2. Agente A2 (acumula información del entorno)

El comportamiento de A2 corresponde al operador de **expansión** (`+`):

```
K + α = Cn( K ∪ {α} )
```

A2 incorpora cada nueva percepción al conjunto de creencias sin eliminar ninguna creencia previa, acumulando información de forma monótona. La expansión es el operador adecuado para modelar este comportamiento, siempre que no se generen contradicciones.

### 6.3. Efecto de no tener reglas de inferencia ni términos negados en A2

Dadas las condiciones de A2 (no tiene reglas explícitas para inferir nueva información y las percepciones no incluyen términos negados), **la expansión nunca produce inconsistencias**:

- Al no haber reglas, ninguna percepción nueva puede deducir una contradicción a partir de lo acumulado: solo se agregan los hechos directamente percibidos.
- Al no haber términos negados (`¬a`), una percepción nueva nunca puede ser la negación exacta de una creencia ya existente, por lo que no puede entrar en conflicto directo con la base.

Consecuentemente, la base **siempre se mantiene consistente** y A2 solo necesita el operador de **expansión**: nunca se requiere contracción ni revisión, porque nunca aparece una situación conflictiva que resolver. El proceso de revisión de la base de conocimiento queda reducido a una simple acumulación monótona de hechos.

## 7. Robot futbolista: revisión priorizada o no priorizada

En el contexto del robot futbolista (Ejercicio 9 del Práctico 1) convendría emplear **revisión priorizada**.

Justificación:
- El entorno del fútbol robótico es **altamente dinámico**: la posición de la pelota, de los compañeros y de los rivales cambia constantemente en segundos. Las percepciones (vía sensores de visión, distancia, etc.) capturan el *estado actual* del mundo, mientras que las creencias previas quedan desactualizadas rápidamente.
- Con revisión priorizada, cada nueva percepción desplaza a las creencias en conflicto, garantizando que la base siempre refleje la situación reciente del campo. Esto es fundamental para tomar decisiones correctas en tiempo real: saber dónde está realmente la pelota o un compañero para pasar, rematar o interponerse.
- Con revisión no priorizada (que puede rechazar lo recién percibido cuando entra en conflicto con creencias previas), el robot podría quedarse con información obsoleta (por ejemplo, creyendo que un compañero está en la posición de hace unos segundos), lo que lo llevaría a decisiones erróneas y pérdida de la pelota.
- Además, las percepciones del robot provienen de sensores directos y confiables del propio agente, no de fuentes dudosas, por lo que no hay motivo para desconfiar de la información nueva.

Por todo esto, la **revisión priorizada** de tipo kernel es la adecuada: mantiene la consistencia de la base y a la vez prioriza la percepción reciente, ajustando el modelo del mundo a la realidad cambiante del partido.

## 8. Revisión priorizada por conjuntos de sentencias

Base de creencias: **K = { a, b → ¬c, w }** y conjunto de sentencias a incorporar prioritariamente: **R = { a, b, c }**

### 8.1. Revisión secuencial con operador kernel

**Paso 1: revisión por `a`.** `a` ya está en K, no hay conflicto:

```
K₁ = K ∗ a = { a, b → ¬c, w }
```

**Paso 2: revisión por `b`.** Se agrega `b`; `b` junto con la regla `b → ¬c` deriva `¬c`, pero como aún no hay `c`, la base sigue siendo consistente:

```
K₂ = K₁ ∗ b = { a, b, b → ¬c, w }
```

**Paso 3: revisión por `c`.** Al agregar `c`, ahora se derivan `c` (recién agregada) y `¬c` (de `b` y `b → ¬c`). Para revisar por `c` se contrae por `¬c` (Identidad de Levi) y luego se expande.

Kernels de `¬c` en `K₂`:

```
K ⊥⊥ ¬c = { { b, b → ¬c } }        (único subconjunto ⊆-mínimo que implica ¬c)
```

La incisión debe eliminar al menos un elemento del kernel, es decir `b` **o** `b → ¬c`:

- **Alternativa 1** (elimina `b`):

  ```
  K₃⁽¹⁾ = { a, b → ¬c, c, w }   (consistente, contiene c)
  ```

- **Alternativa 2** (elimina `b → ¬c`):

  ```
  K₃⁽²⁾ = { a, b, c, w }        (consistente, contiene c)
  ```

**Si se revisa en otro orden**, p. ej. `c`, luego `b`, luego `a`:

- `K₁ = K ∗ c = { a, b → ¬c, c, w }` (consistente: todavía no hay `b`).
- `K₂ = K₁ ∗ b`: ahora `b` con `b → ¬c` deriva `¬c`, que contradice `c`. La base ya implica `¬b` (vía contraposición: `c` y `b → ¬c` implican `¬b`). Kernels de `¬b`:

  ```
  K ⊥⊥ ¬b = { { c, b → ¬c } }
  ```

  - Elimina `c` → contracción = `{ a, b → ¬c, w }`, expandida con `b`:

    ```
    K₂⁽¹⁾ = { a, b, b → ¬c, w }   (consistente, contiene b)
    ```

  - Elimina `b → ¬c` → contracción = `{ a, c, w }`, expandida con `b`:

    ```
    K₂⁽²⁾ = { a, b, c, w }        (consistente, contiene b)
    ```

- `K₃ = K₂ ∗ a`: `a` ya está, no cambia.

### 8.2. ¿El orden condiciona el resultado final?

**Sí.** El resultado final depende del orden en que se efectúan las revisiones. Por ejemplo:

- Orden `a, b, c` puede dar `{ a, b → ¬c, c, w }` (perdió `b`), y orden `c, b, a` puede dar `{ a, b, b → ¬c, w }` (perdió `c`). Ambos son resultados válidos de una revisión kernel secuencial pero son **bases distintas**.

Además, en la revisión secuencial **no se garantiza que R quede incluido por completo**: en `{ a, b → ¬c, c, w }` falta `b`, y en `{ a, b, b → ¬c, w }` falta `c`. La inclusión total de R depende del orden y de la incisión elegida en cada paso.

**¿Cómo garantizar que R esté incluido completamente?** Realizar una **revisión simultánea por el conjunto R** con un operador que trate a R como un todo de máxima prioridad: se incorporan todas las sentencias de R y se contrae de la base todo lo que entra en conflicto con el conjunto R (no con cada sentencia aislada). En este caso, el conflicto lo genera la regla `b → ¬c` frente a `{b, c}` de R, por lo que se elimina la regla y se obtiene:

```
K ⊛ R = { a, b, c, w }   (contiene íntegramente a R, consistente)
```

Es decir, la revisión por el conjunto de sentencias de R, tratándolo prioritariamente como una unidad, garantiza que todas las piezas de R sobrevivan a la revisión.