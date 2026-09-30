# Trabajo Práctico 4 — Planificación automática

## 1. Conceptos básicos

### 1.a. ¿Cómo se define un problema de planificación?

Un problema de planificación se define indicando **tres componentes (I, G, A) en un lenguaje formal** [García, Episodio V, sec. "Problema de planificación"]:

- **(I) estado inicial:** una descripción del estado inicial del mundo.
- **(G) meta (goal):** una descripción de la meta del agente.
- **(A) acciones:** una descripción de las acciones que el agente puede ejecutar.

- "El planificador es el encargado de encontrar una solución" [García, Episodio V, sec. "Problema de planificación"]: recibe (I, G, A) y devuelve un plan.
- En AIMA el mismo problema se enuncia como un **problema de búsqueda** con sus cuatro piezas: estado inicial, función ACTIONS(s), función RESULT(s, a) y test de meta; "Now we have defined planning as a search problem" [RN10, sec. 10.1, p. 369]. La misma caracterización (I, G, A) puede encontrarse también en PMG.
- **Correspondencia con la búsqueda** vista en la materia [García, Episodio V, sec. "Sistema de Planeamiento"]:
  - estado inicial del problema de planificación ↔ nodo raíz de la búsqueda;
  - acciones (A) ↔ operadores/reglas que generan los sucesores de un nodo;
  - meta (G) ↔ test de meta;
  - plan ↔ solución (camino) de la búsqueda.
  - En PMG: "A plan is a path from the initial state to a state that satisfies the goal condition" [PMG, sec. 8.3, p. 299].
- **El dominio aporta A; el problema se completa con I y G** [García, Episodio V, sec. "Sistema de Planeamiento"]: "A set of action schemas serves as a definition of a planning domain. A specific problem within the domain is defined with the addition of an initial state and a goal" [RN10, sec. 10.1, pp. 368-369].

*Ejemplo (Mundo de Bloques):* I = E1 = {mesa(1), mesa(2), mesa(3), libre(1), libre(2), libre(3)} (bloques 1, 3 y 2 apilados), G = "el bloque 3 sobre el 1", A = {apilar(B1,B2), desapilar(B1,B2)} [García, Episodio V, secs. "Sistema de Planeamiento" y "Regression planning"].

### 1.b. ¿En qué consiste un dominio de planificación? ¿Qué características tiene un dominio "clásico"?

**Consiste en** [García, Episodio V, sec. "Dominio de planificación"]:

1. **Una caracterización del entorno** donde actúa el agente. En el Mundo de Bloques esa caracterización se hace indicando: qué bloques están en la mesa, cuáles están sobre otros y cuáles están libres (sin nada encima).
2. **Las acciones (operadores)** que el agente puede ejecutar en ese entorno.

- Con un mismo dominio se pueden formular **muchísimos problemas concretos**, basta variar I y G [García, ibidem]. La misma idea aparece en AIMA, donde el dominio queda fijado por los esquemas de acciones y cada problema se particulariza con su estado inicial y su meta [RN10, sec. 10.1, pp. 368-369].
- Los dominios varían mucho en tamaño y complejidad: "Los dominios de planificación pueden variar en tamaño y complejidad desde un vehículo autónomo en una autopista, hasta dominios de experimentación como el mundo de bloques" [García, Episodio V, sec. "Dominio de planificación"].

**Características de un dominio de planificación clásico** [García, Episodio V, sec. "Planificación clásica"]:

- **completamente observable** (el agente conoce el estado del mundo),
- **determinístico** (una acción tiene un único efecto conocido),
- **finito** (conjunto finito de estados, de objetos y de acciones instanciadas),
- **estático**: los cambios ocurren solamente cuando el agente actúa,
- **discreto**: en tiempo, acciones, objetos y efectos.

- La misma caracterización, resumida, se encuentra en AIMA: "This chapter covers fully observable, deterministic, static environments with single agents" (agente único) [RN10, cap. 10, p. 366]. Esta distinción entre planificación clásica y no clásica también aparece en PMG, que llama *classical planning* a la versión de STRIPS [PMG, sec. 8.2, p. 288].
- **Para qué sirve suponer "clásico":**
  - hace que PlanSAT (¿existe algún plan?) sea **decidible**, justamente porque el número de estados es finito; si se agregan símbolos de función, el espacio de estados es infinito y PlanSAT pasa a ser sólo *semidecidible* [RN10, sec. 10.1.4, p. 372].
  - habilita **heurísticas independientes del dominio** muy precisas: "That's the true advantage of the classical planning formalism: it has facilitated the development of very accurate domain-independent heuristics" [RN10, sec. 10.1.4, p. 372].
  - excluidos estos dominios, la planificación se vuelve probabilística/estocástica, con información parcial o dinámica, y con múltiples agentes, que se tratan en otros capítulos [RN10, cap. 10, p. 366].
- **Ejemplo:** el Mundo de Bloques, dominio de juguete creado por Terry Winograd para un sistema que interpretaba comandos de voz y resolvía la tarea moviendo bloques; en la versión usada en la materia: bloques todos del mismo tamaño e identificados unívocamente, un bloque no puede estar simultáneamente sobre dos bloques (ni dos sobre uno), y hay un único brazo robot que trabaja sin operación humana [García, Episodio V, sec. "Mundo de Bloques"]. En AIMA se describe en términos equivalentes: "a set of cube-shaped blocks sitting on a table. The blocks can be stacked, but only one block can fit directly on top of another. A robot arm can pick up a block and move it to another position... The arm can pick up only one block at a time" [RN10, sec. 10.1.3, pp. 370-371].

### 1.c. ¿Qué diferencia hay entre un operador y una acción? Brinde un ejemplo de cada uno

| | **Operador** (o esquema de acción) | **Acción** |
|---|---|---|
| Qué es |-plantilla genérica de una clase de acciones | una instancia concreta de un operador |
| Componentes | un **nombre**, una **lista de parámetros** (generalmente variables), las **precondiciones** y los **efectos** [García, Episodio V, sec. "Operadores y acciones"] | los mismos cuatro elementos, pero **sin variables**: todos los parámetros tienen valores fijos |
| Cómo se obtiene | es lo que se define en el dominio | se obtiene **instanciando** (completando las variables) un operador |

- En AIMA esta misma distinción aparece como *action schema* (representación "lifted") frente a *ground action*: "A set of ground (variable-free) actions can be represented by a single action schema. The schema is a lifted representation—it lifts the level of reasoning from propositional logic to a restricted subset of first-order logic" [RN10, sec. 10.1, p. 367].
- **Ejemplo de operador:** `apilar(X, Y)` — nombre y parámetros `apilar(X,Y)`; precondiciones = {mesa(X), libre(X), libre(Y)}; efectos: add-list = {sobre(X,Y)}, del-list = {libre(Y), mesa(X)} [García, Episodio V, secs. "Representación de acciones" y "Especificación de operadores"]. Escribió que `X ≠ Y` para evitar acciones espurias como `apilar(a,a)` [ibidem, sec. "Especificación en el lenguaje STRIPS"].
- **Ejemplo de acción:** `apilar(c, i)` (o `desapilar(b, c)`) — es el operador `apilar(X,Y)` con X = c e Y = i, ya sin variables. En el estado E1 = {mesa(i), mesa(c), libre(c), libre(i)} la acción `apilar(c,i)` es aplicable y produce E2 = {mesa(i), libre(c), sobre(c,i)}, mientras que `desapilar(c,i)` no es aplicable en E1 [García, Episodio V, sec. "Acciones aplicables en un estado"].
- **Cuántas acciones produce un operador:** "Con N bloques cada operador se puede instanciar en N×(N-1) acciones: para 3 bloques son 6 y para 7 bloques son 42" [García, Episodio V, sec. "Forward Planning"]. En general, si un esquema tiene *v* variables y el dominio tiene *k* objetos, hay *k^v* instanciaciones posibles [RN10, sec. 10.1, p. 368].
- **Relevancia para los planificadores:**
  - en **forward planning / STRIPS** el generador de sucesores expande operadores y prueba las acciones resultantes: un operador con muchas variables multiplica el factor de ramificación;
  - en **POP** cada paso que se agrega al plan es directamente una **acción** (no un esquema con variables), porque debe lograr una precondición concreta [García, Episodio VI, sec. "Partial Order Planning (POP)"].

### 1.d. ¿Qué es una solución a un problema de planificación?

- "Una solución para un problema de planificación es un **plan**" [García, Episodio V, sec. "Problema de planificación"].
- Un **plan** es una secuencia de acciones `P = [a1, a2, …, aN]` tal que [García, Episodio V, sec. "Sistema de Planeamiento"]:
  - cada `ai` es una **instancia de un elemento de A** (o sea, una acción obtainable de un operador de A);
  - se aplican **en el orden que impone la secuencia**: `a1` se aplica a I, `a2` al estado resultante, y así sucesivamente;
  - al llegar a `aN` se obtiene un **estado final F que satisface la meta G** (es decir, `G ⊆ F`).
- Equivalente a la noción de solución de búsqueda: el plan es el camino desde el estado inicial hasta un estado meta [García, ibidem; PMG, sec. 8.3, p. 299].
- *Ejemplo de solución:* I = E1, G = "el bloque 3 sobre el 1", A = {apilar, desapilar}; el plan `P = [desapilar 2 de 3, apilar 3 sobre 1]` es solución, porque la primera acción lleva E1 a E2 y la segunda lleva E2 a F, que satisface la meta [García, Episodio V, sec. "Sistema de Planeamiento"].
- **Características de una solución:**
  - **no tiene que ser única** ni **óptima**: en general encontrar *algún* plan es más fácil que encontrar el mejor; "For many domains..., Bounded PlanSAT is NP-complete while PlanSAT is in P; in other words, optimal planning is usually hard, but sub-optimal planning is sometimes easy" [RN10, sec. 10.1.4, p. 372]. Por eso un planificador completo ( breadth-first, A*, etc.) garantiza encontrar una solución si existe [García, Episodio V, sec. "Forward Planning"].
  - debe ser **ejecutable**: en un dominio clásico (determinista y estático), aplicando el plan tal como está desde I se llega efectivamente a F ⊨ G.
  - **contenido y corrección** se pueden comprobar mecánicamente con operaciones de conjuntos: estado final `F = I − Del(a1) ∪ Add(a1) − Del(a2) ∪ Add(a2) …` y luego verificar `G ⊆ F` [García, Episodio V, secs. "Especificación de operadores" y "Acciones aplicables en un estado"].
  - en **POP** la solución no es una secuencia sino un **plan parcial** `(As, Os, Ls, Goals)` que cumple dos condiciones: (1) no hay amenazas, y (2) para toda precondición P de un paso S incluido en As, existe en As un paso S1 que logra P y existe en Ls un vínculo causal que indica que S1 logra P para S [García, Episodio VI, sec. "Solución a un problema de planificación"]. De una misma solución se pueden derivar **varios planes totales** (esto se desarrolla en el punto 6).

### 1.e. ¿Por qué en un problema de planificación (I, G, A) es necesario representar en un lenguaje formal a I, G y a los elementos de A?

- **Porque el planificador es un programa y necesita verificar y aplicar las acciones mecánicamente.** Con A = (Pre, Add, Del) y estados como conjuntos de literales, todas las operaciones son aritmética de conjuntos: una acción es aplicable si `Pre ⊆ E`, y el estado siguiente es `E' = (E \ Del) ∪ Add` [García, Episodio V, secs. "Especificación de operadores" y "Acciones aplicables en un estado"]; en AIMA, `RESULT(s, a) = (s − DEL(a)) ∪ ADD(a)` [RN10, sec. 10.1, p. 368, ec. 10.1]. Sin una representación formal y no ambigua no se puede decidir nada de esto automáticamente.
- **Para que la representación sirva a la vez para razonar y para operar.** "The representation of states is carefully designed so that a state can be treated either as a conjunction of fluents, which can be manipulated by logical inference, or as a set of fluents, which can be manipulated with set operations" [RN10, sec. 10.1, p. 367]. En STRIPS cada estado es un conjunto finito de literales fijos positivos, y con la **Suposición del Mundo Cerrado** lo no mencionado se asume falso [García, Episodio V, sec. "Lenguaje STRIPS"]; junto con la suposición de nombres únicos [RN10, sec. 10.1, p. 367], esto hace que un estado denote un conjunto determinado y por lo tanto se pueda decidir si satisface la meta: "Un estado E satisface una meta G si G ⊆ E" [García, Episodio V, sec. "Ejemplos de estados y metas"].
- **Para poder abstraer el mundo real sin problemas (problema de marco).** Las acciones sólo declaran lo que cambia (add-list y del-list) y "todo lo demás queda igual": "PDDL does that by specifying the result of an action in terms of what changes; everything that stays the same is left unmentioned... A concise description of the action should mention only Δ; it shouldn't have to mention all the objects that stay in place" [RN10, sec. 10.1, p. 367]. En PMG esto es la *STRIPS assumption*: "All of the primitive relations not mentioned in the description of the action stay unchanged" [PMG, sec. 8.2, p. 288]. Si hubiera que nombrar todo lo que no cambia, la descripción dejaría de ser finita y manejable.
- **Para garantizar terminación y decidibilidad.** Si el lenguaje tiene un conjunto finito de constantes y de predicados y no usa símbolos de función, el número de estados es finito y ambos problemas de decisión son decidibles: "The first result is that both decision problems are decidable for classical planning. The proof follows from the fact that the number of states is finite. But if we add function symbols to the language, then the number of states becomes infinite, and PlanSAT becomes only semidecidable" [RN10, sec. 10.1.4, p. 372]. La forma del lenguaje es lo que le permite a un planificador saber cuándo terminar.
- **Para separar el dominio del problema y reutilizar el planificador.** El conjunto de esquemas de acciones define el **dominio**, y con I y G se define el **problema** [RN10, sec. 10.1, pp. 368-369]. Así un mismo planificador, independiente del dominio, resuelve problemas muy distintos sin reprogramarse; y la estructura de la representación permite derivar heurísticas automáticas muy precisas: "That's the true advantage of the classical planning formalism: it has facilitated the development of very accurate domain-independent heuristics" [RN10, sec. 10.1.4, p. 372]. Las restricciones del lenguaje también se explotan en los algoritmos: "the situation calculus is more expressive, but the restrictions imposed by the STRIPS representation can be exploited in the planning algorithms" [PMG, sec. 8.2, p. 288].
- **Para que la representación sea una abstracción útil del entorno.** El agente planifica sobre un modelo del mundo, no sobre el mundo real: "Were it not for the ability to construct useful abstractions, intelligent agents would be completely swamped by the real world" [RN10, sec. 3.1.2, pp. 68-69]. La misma necesidad de abstraer se descarta en el resto de la teoría de planificación.

---

## 2. Mundo de Bloques

### 2.a. Funcionamiento de los operadores `apilar(A,B)` y `desapilar(A,B)`

#### Cómo se ve el mundo

- Un **estado** es un conjunto finito de literales que dice qué es verdad en ese momento; lo que no se menciona se asume falso (Suposición del Mundo Cerrado) [García, Episodio V, sec. "Lenguaje STRIPS"]. Con las tres relaciones del enunciado:
  - `mesa(X)`: el bloque X está apoyado en la mesa;
  - `sobre(X,Y)`: el bloque X está apoyado sobre el bloque Y;
  - `libre(X)`: el bloque X no tiene ningún bloque encima.
- `libre(X)` hace falta porque en lógica de primer orden la condición "nada está sobre X" sería `¬∃Z sobre(Z,X)`, y el lenguaje usado no tiene cuantificadores; en su lugar se declara explícitamente un predicado `libre` que los operadores se encargan de mantener actualizado [RN10, sec. 10.1.3, p. 371]. Además así se respeta la restricción física del entorno: un bloque no puede estar sobre dos bloques, ni dos bloques sobre uno [García, Episodio V, sec. "Mundo de Bloques"].

#### Los dos operadores en una tabla

| Operador | Precondiciones | Add-list | Del-list |
|---|---|---|---|
| `apilar(X,Y)` | {`mesa(X)`, `libre(X)`, `libre(Y)`} | {`sobre(X,Y)`} | {`libre(Y)`, `mesa(X)`} |
| `desapilar(X,Y)` | {`libre(X)`, `sobre(X,Y)`} | {`libre(Y)`, `mesa(X)`} | {`sobre(X,Y)`} |

[ García, Episodio V, sec. "Especificación en el lenguaje STRIPS"]. A ambos se les puede agregar `X ≠ Y` para evitar acciones espurias como `apilar(a,a)` [ibidem].

#### `apilar(X,Y)`: tomar un bloque de la mesa y ponerlo sobre otro

- **Qué hace, intuitivamente:** "tomar un bloque B1 que se encuentra sobre la mesa y poner B1 sobre el bloque B2. Ninguno de los dos bloques debe tener otro encima" [García, Episodio V, sec. "Dominio de planificación: Mundo de Bloques"]. Es la acción del brazo robot: agarra el bloque de arriba y lo apoya encima del otro.
- **Condiciones que deben cumplirse (precondiciones):**
  - `mesa(X)`: **X debe estar en la mesa**. O sea, el bloque que se mueve tiene que ser un bloque "de abajo"; si X estuviera apoyado sobre otro bloque, primero habría que desapilarlo. Esto es coherente con el único brazo robot, que sólo manipula un bloque por vez.
  - `libre(X)`: **nada debe estar encima de X**, porque si no, al mover X se llevaría encima lo que tiene encima y el resultado ya no sería un solo bloque sobre Y.
  - `libre(Y)`: **nada debe estar encima de Y**, porque si no, Y ya no tiene lugar para recibir a X (violaría "un bloque no puede estar sobre dos bloques").
- **Resultado que produce (efectos):**
  - se agrega `sobre(X,Y)`: ahora X está sobre Y;
  - se borra `mesa(X)`: X ya no está en la mesa, porque fue levantado;
  - se borra `libre(Y)`: Y dejó de estar libre, porque tiene un bloque encima.
  - lo que **no** aparece en la lista es `libre(X)`: **X sigue estando libre** después de apilar, porque nada quedó encima de él. Y como no se menciona nada más, todo lo demás del estado queda igual (es la *STRIPS assumption*) [García, Episodio V, sec. "Representación de acciones"; PMG, sec. 8.2, p. 288].
- **Nota:** la precondición es `libre(Y)`, no `mesa(Y)`: Y puede estar en la mesa o sobre otro bloque, lo que se exige es que tenga espacio libre arriba.

#### `desapilar(X,Y)`: tomar el bloque de arriba y poner abajo el que estaba debajo

- **Qué hace, intuitivamente:** "tomar un bloque B1 que se encuentra sobre otro B2 y poner a B2 sobre la mesa. El bloque B1 no debe tener otro encima" [García, Episodio V, sec. "Dominio de planificación: Mundo de Bloques"]. O sea: se retira el bloque de arriba y se apoya en la mesa el que estaba abajo.
- **Condiciones que deben cumplirse (precondiciones):**
  - `sobre(X,Y)`: X tiene que estar efectivamente apoyado sobre Y; si no, no hay nada que desapilar entre esos dos bloques.
  - `libre(X)`: **X no debe tener nada encima**, porque el brazo tiene que poder sujetar a X para moverlo. Si X tuviera un bloque encima, primero habría que desapilar ese bloque.
  - No se exige `mesa(X)` justamente porque X está *sobre* Y, no en la mesa: es la condición opuesta a la de `apilar`.
- **Resultado que produce (efectos):**
  - se borra `sobre(X,Y)`: X ya no está sobre Y;
  - se agrega `libre(Y)`: Y quedó sin nada encima;
  - se agrega `mesa(Y)`: Y ahora está apoyado en la mesa.
  - `libre(X)` no se borra: **X sigue libre**, ya que no se le puso nada encima.
- **Simetría:** `apilar` y `desapilar` son operaciones inversas: si `apilar(X,Y)` lleva un estado E a E', entonces `desapilar(X,Y)` lleva E' de vuelta a E. Es por eso que el espacio de estados del Mundo de Bloques se puede recorrer en ambos sentidos.

#### Cómo se comprueba y se aplica un operador

- **Aplicabilidad:** una acción `A = (Pre, Add, Del)` es aplicable en el estado E si todas sus precondiciones se satisfacen en E, lo que se verifica simplemente comprobando la inclusión de conjuntos `Pre ⊆ E` [García, Episodio V, sec. "Acciones aplicables en un estado"]. Si no se cumple alguna, la acción no existe para ese estado: el planificador no la genera y sigue con otras.
- **Nuevo estado:** se obtiene con operaciones de conjuntos, `E' = (E \ Del) ∪ Add` [García, ibidem]; en AIMA, `RESULT(s, a) = (s − DEL(a)) ∪ ADD(a)` [RN10, sec. 10.1, p. 368, ec. 10.1]. O sea: primero se borra todo lo de la del-list, después se agrega todo lo de la add-list, y todo lo demás se arrastra sin cambios.

#### Ejemplo de aplicación paso a paso [García, Episodio V, sec. "Dominio de planificación: Mundo de Bloques"]

Sea `E1 = {mesa(a), mesa(d), libre(a), libre(b), sobre(c,d), sobre(b,c)}` (d y a en la mesa, c sobre d, b sobre c).

1. **¿Es aplicable `desapilar(b,c)`?** Pre = {`libre(b)`, `sobre(b,c)`}; los dos literales están en E1 → **sí**.
   `E2 = (E1 \ {sobre(b,c)}) ∪ {libre(c), mesa(b)} = {mesa(a), mesa(d), mesa(b), libre(a), libre(b), libre(c), sobre(c,d)}`.
   Ahora: a y d sueltos en la mesa, b encima de c, y c encima de d. Coherente: se despejó el bloque que estaba sobre c.
2. **¿Es aplicable `apilar(b,c)` en E2?** Pre = {`mesa(b)`, `libre(b)`, `libre(c)`}; los tres están en E2 → **sí**.
   `E1 = (E2 \ {libre(c), mesa(b)}) ∪ {sobre(b,c)}` → se recupera exactamente E1: los dos operadores son reversibles.
3. **Acciones que NO son aplicables en E1**, y por qué:
   - `apilar(c,d)`: falla `libre(d)`, porque `sobre(b,c)` implica que d tiene encima a c, o sea d no está libre;
   - `apilar(b,c)`: falla `mesa(b)`, porque b no está en la mesa sino sobre c;
   - `desapilar(c,d)`: falla `libre(c)`, porque c tiene a b encima;
   - `desapilar(a,d)`: falla `sobre(a,d)`, porque a no está sobre d.
   Obsérvese que el planificador no necesita "saber" estas reglas: simplemente no puede aplicarlas, porque sus precondiciones no están en el estado.

---

## 3. Planificadores

### 3.a. ¿Cuál es la tarea de un sistema de planeamiento (o planificador)?

- "La tarea de un Sistema de Planeamiento (planificador) es **buscar de forma automática una solución para un problema de planificación, esto es un plan (secuencia de acciones)**" [García, Episodio V, sec. "Plan que resuelve un problema"].
- En términos formales: dado un problema (A, I, G), el planificador devuelve un plan `P = [a1, a2, …, aN]` donde cada `ai` es una instancia de un elemento de A y, aplicadas en el orden de P desde el estado inicial I, llevan a un estado final F que satisface la meta G [García, Episodio V, sec. "Sistema de Planeamiento"].
- **Es exactamente la tarea de un método de búsqueda**, con la diferencia terminológica que muestran las notas: "sistema de planeamiento" ↔ "método de búsqueda", y "plan (secuencia)" ↔ "solución (camino)" [García, ibidem]. En PMG: "A plan is a path from the initial state to a state that satisfies the goal condition" [PMG, sec. 8.3, p. 299].
- En AIMA, una vez que la descripción del problema define un estado inicial, una función ACTIONS, una función RESULT y un test de meta, "we can solve planning problems with any of the heuristic search algorithms from Chapter 3 or a local search algorithm from Chapter 4 (provided we keep track of the actions used to reach the goal)" [RN10, sec. 10.2.1, pp. 372-373].
- Requisito práctico: el plan devuelto tiene que ser **ejecutable**; en un dominio clásico, al ejecutarlo se llega a un estado que satisface la meta (punto 1.d).

### 3.b. ¿Cómo modificaría los algoritmos de búsqueda para que retornen una solución? ¿Sería forward o backward planning?

**Modificaciones necesarias** sobre los algoritmos de búsqueda de la materia (BFS, UCS, A*, profundización iterativa):

1. **Generar los sucesores con acciones, no con arcos fijos.** Los operadores de A son esquemas con variables, así que hay que *instanciarlos* y conservar sólo las acciones **aplicables**: una acción `A = (Pre, Add, Del)` es aplicable si `Pre ⊆ E`, y produce `E' = (E \ Del) ∪ Add` [García, Episodio V, sec. "Acciones aplicables en un estado"]. El factor de ramificación no viene dado, sino que se calcula: en el Mundo de Bloques cada operador se instancia en N×(N-1) acciones (6 con 3 bloques, 42 con 7) [García, Episodio V, sec. "Forward Planning"], y en general el número de acciones aplicables en un estado puede ser enorme.
2. **Cada nodo debe guardar el estado y el plan que llevó a él.** La solución de planificación es el **plan**, no el nodo meta: si se usan métodos con grafo (A*, UCS) alcanza con guardar el padre y la acción aplicada, pero con un método que no guarda historia hay que llevar explícitamente la lista de acciones ejecutadas: "provided we keep track of the actions used to reach the goal" [RN10, sec. 10.2.1, pp. 372-373]. Es exactamente lo que hace FF con su hill climbing: "hill-climbing search (modified to keep track of the plan)" [RN10, sec. 10.2.3, p. 378].
3. **Test de meta:** un estado es meta si satisface la meta, es decir `G ⊆ E` (la meta es un estado parcialmente especificado) [García, Episodio V, sec. "Ejemplos de estados y metas"].
4. **Función de costo:** con costo 1 por acción, `g(n)` es la cantidad de acciones aplicadas, de modo que BFS o A* con heurística admisible devuelven el plan más corto (óptimo) [RN10, sec. 10.1.4, p. 372].
5. **Control de visitados:** imprescindible, porque muchas acciones distintas llevan al mismo estado (por ejemplo, desapilar y volver a apilar el mismo bloque); sin él la búsqueda recorre indefinidamente el mismo subespacio.
6. **Heurística:** `h` no necesita conocimiento del dominio, porque se puede derivar de la estructura de la representación (heurísticas *ignore delete lists*, `h_max`/`h_add`/`h_FF`, grafos de planificación) [RN10, secs. 10.2.3 y 10.3]. No es un detalle menor: sin heurística el espacio explota, por ejemplo en el problema de transporte de carga con 10 aeropuertos, 50 aviones y 200 paquetes hay ~2000 acciones por estado, y el grafo hasta la profundidad de la solución obvia tiene ~2000⁴¹ nodos: "Clearly, even this relatively small problem instance is hopeless without an accurate heuristic" [RN10, sec. 10.2.1, p. 373].
7. **Algoritmo resultante (esquema):** `frontera ← {I}`; extraer nodo E con el plan π asociado; si `G ⊆ E` devolver π; si no, instanciar todos los operadores, filtrar los aplicables en E, calcular `E' = (E \ Del) ∪ Add` y agregar `(E', π·a)` a la frontera, ordenando según la estrategia elegida (BFS, UCS, A* con h). Es el mismo esqueleto de la búsqueda, con la generación de sucesores y el test de meta reemplazados por la semántica de STRIPS.

**¿Forward o backward?** Sería un planificador **hacia adelante (forward planning / progresión)**:

- "Se denomina **Forward Planning** (o planificación hacia adelante) a las técnicas que **comienzan en el estado inicial y realizan una búsqueda en el espacio de estados**, hasta encontrar un estado que satisface la meta. Esta forma de hallar planes es una de las más simples. La mayoría de los métodos de búsqueda estudiados previamente pueden ser utilizados para tratar de encontrar un plan. La solución de la búsqueda es una secuencia de acciones que corresponde a un plan. Por ejemplo, Primero a lo Ancho, Profundización Iterativa o A* garantizan encontrar un plan" [García, Episodio V, sec. "Forward Planning"].
- Es decir, los algoritmos de búsqueda de la materia, tal como están, dan un planificador hacia adelante: el nodo inicial de la búsqueda es I y se progresa hacia la meta. En AIMA esto es "Forward (progression) state-space search" [RN10, sec. 10.2.1, p. 372].
- **¿Por qué no backward?** El enfoque alternativo (regression planning) "comienza de una lista de metas G, luego busca una acción A que tenga como efecto (add list) lograr algún literal de G, se retira de G ese literal y las precondiciones de A son agregadas a G como nuevas metas, luego hace regresión nuevamente. Así hasta llegar al estado inicial" [García, Episodio V, sec. "Regression planning"], con `g' = (g − ADD(a)) ∪ PRECOND(a)` [RN10, sec. 10.2.2, p. 374]. Su ventaja es que "en dominios donde hay muchos operadores aplicables en cada estado, entonces la búsqueda puede enfocarse en acciones relevantes para las metas buscadas" [García, ibidem]. Pero es más difícil de implementar con los algoritmos que ya vimos: se busca sobre *conjuntos* de estados y no sobre estados, lo que dificulta obtener heurísticas buenas: "Backward search keeps the branching factor lower than forward search, for most problem domains. However, the fact that backward search uses state sets rather than individual states makes it harder to come up with good heuristics. That is the main reason why the majority of current systems favor forward search" [RN10, sec. 10.2.2, p. 376]. Con los métodos de la materia, entonces, el camino natural es forward.
- *Ejemplo de la clase:* I = {libre(1), mesa(1), libre(2), mesa(2), libre(3), mesa(3)}, G = {sobre(1,2), sobre(2,3), mesa(3), libre(1)} → `PLAN = [apilar(2,3), apilar(1,2)]` [García, Episodio V, sec. "Regression planning"]; y ese mismo plan se obtiene también buscando hacia adelante desde I.

### 3.c. ¿Para implementar un planificador podría usar un método de búsqueda sin frontera?

**Sí se puede, aunque con pérdida de garantías.** Ejemplos: hill climbing, simulated annealing, búsqueda genética, hill climbing con reinicios aleatorios.

- **Es factible:** "we can solve planning problems with any of the heuristic search algorithms from Chapter 3 **or a local search algorithm from Chapter 4** (provided we keep track of the actions used to reach the goal)" [RN10, sec. 10.2.1, pp. 372-373]; en PMG: "In a forward planner, you search the state-space graph from the initial state looking for a state that satisfies a goal description. You can use any of the search strategies described in Chapter 4" [PMG, sec. 8.3, p. 299]. De hecho, un planificador-forward muy usado, FF, "uses hill-climbing search (modified to keep track of the plan) with the heuristic to find a solution" [RN10, sec. 10.2.3, p. 378].
- **Pero hay que modificarlo y aceptar las siguientes condiciones:**
  - **Hay que registrar el plan explícitamente:** "La solución de este método es un nodo meta. No almacena, ni retorna el camino recorrido desde el nodo inicial al nodo meta" [García, Episodio III, sec. "Hill Climbing (Escalador o Trepada)"], y en planificación la salida debe ser el plan, no el nodo. De ahí el "modified to keep track of the plan" de FF [RN10, sec. 10.2.3, p. 378].
  - **Se pierde la completitud:** el método "no garantiza ser completo" [García, Episodio III, sec. "Hill Climbing (Escalador o Trepada)"]; puede quedar atrapado en un máximo local o en una meseta, y no puede afirmar que "no hay solución" (algo que un planificador debe poder asegurar). FF lo resuelve con un parche: "When it hits a plateau or local maximum—when no action leads to a state with better heuristic score—then FF uses iterative deepening search until it finds a state that is better, or it gives up and restarts hill-climbing" [RN10, sec. 10.2.3, p. 378].
  - **Se pierde la optimalidad:** el plan obtenido puede no ser el más corto [RN10, sec. 10.2.3, p. 377].
  - **Hace falta una heurística muy buena, obtenida de la representación:** "This complexity may be reduced by finding good heuristics (see Exercise 8.4), but the heuristics have to be very good to overcome the combinatorial explosion" [PMG, sec. 8.3, p. 299]. Con la heurística relajada *ignore delete lists* el paisaje es favorable: "In both these problems, there is a wide path to the goal. There are no dead ends, so no need for backtracking; a simple hill-climbing search will easily find a solution to these problems (although it may not be an optimal solution)" [RN10, sec. 10.2.3, p. 377].
  - **Ventaja a su favor:** memoria constante, sin frontera ni lista de visitados, lo que lo hace apto cuando almacenar la frontera es prohibitivo [García, Episodio III, sec. "Hill Climbing (Escalador o Trepada)"].
- **Conclusión:** si sólo se busca *algún* plan (no el óptimo) y se dispone de una buena heurística derivada de la representación, un método sin frontera es una opción válida y ahorra memoria; si se necesita garantiza de encontrar la solución cuando existe y de optimalidad, corresponde un método con frontera: "Primero a lo Ancho, Profundización Iterativa o A* garantizan encontrar un plan" [García, Episodio V, sec. "Forward Planning"].

---

## 4. Lenguaje de representación y planificador STRIPS

### 4.a. ¿En qué consiste el lenguaje de representación de STRIPS?

- **Qué significa la sigla:** STRIPS = **ST**anford **R**esearch **I**nstitute **P**roblem **S**olver [García, Episodio V, sec. "Lenguaje de representación STRIPS"]. Históricamente fue el solucionador de problemas del robot Shakey, uno de los primeros robots construidos con técnicas de IA [PMG, sec. 8.2, p. 288].
- **Sobre qué se define:** "El lenguaje de representación STRIPS se define sobre tres conjuntos disjuntos y finitos de símbolos: un conjunto de variables V, un conjunto de constantes C y un conjunto de predicados P. Una convención habitual para distinguir los elementos del lenguaje consiste en denotar las variables con una letra mayúscula inicial" [García, ibidem]. Para el Mundo de Bloques: `C = {a, b, c, d}` y `P = {libre, mesa, sobre}` [ibidem].
- **Qué permite expresar:** es un lenguaje para describir *qué es verdad en cada estado* y *qué cambia cuando se ejecuta cada acción*. "The representation is used for specifying the following problem: Given a state and an action, determine whether the action can be carried out in that state and, if it can, determine what is true in the state resulting from carrying out the action" [PMG, sec. 8.2, p. 288].
- **Elementos que define** (los tres del enunciado):
  - **Estados:** un conjunto finito de literales fijos positivos, que representa todo lo que es verdadero en ese estado, más la **Suposición del Mundo Cerrado** [García, Episodio V, sec. "Lenguaje STRIPS: estados, metas y estados que satisfacen metas"].
  - **Metas:** un estado parcialmente especificado, es decir una conjunción de literales fijos positivos [ibidem].
  - **Operadores (esquemas de acción):** nombre, lista de parámetros (variables), precondiciones y efectos; los efectos se separan en **add-list** y **del-list** [García, Episodio V, sec. "Especificación de operadores"].
- **Restricciones del lenguaje (lo que lo hace simple y computable):**
  - Un **literal** es *fijo* si no contiene variables, y *positivo* si no está precedido por negación [García, ibidem]. En los estados y metas no aparecen literales negativos.
  - **Las precondiciones y las metas no pueden contener literales negativos**: "PDDL was derived from the original STRIPS planning language (Fikes and Nilsson, 1971), which is slightly more restricted than PDDL: STRIPS preconditions and goals cannot contain negative literals" [RN10, sec. 10.1, p. 368]. Si un problema necesita "¬P", se reemplaza por un predicado nuevo positivo P' [RN10, sec. 10.2.3, p. 377, nota 3].
  - **Toda variable que aparece en los efectos debe aparecer también en las precondiciones**, para que al instanciar la acción queden todos los valores determinados [RN10, sec. 10.1, p. 368].
  - Lo que **no** cambia no se menciona: es la *STRIPS assumption*, "All of the primitive relations not mentioned in the description of the action stay unchanged" [PMG, sec. 8.2, p. 288], que resuelve el problema de marco permitiendo descripciones acotadas [RN10, sec. 10.1, p. 367].
- **Importante: el lenguaje y el planificador son cosas distintas.** "You can use the STRIPS representation with other planners, and you can use the STRIPS planner with other representations" [PMG, sec. 8.2, p. 288]. Es decir, el STRIPS *Planner* (4.d) es un algoritmo que usa (o puede no usar) esta representación.

### 4.b. ¿Cómo se representan los estados, las metas y los operadores?

**Estados** — conjuntos finitos de literales fijos positivos [García, Episodio V, sec. "Lenguaje STRIPS: estados, metas y estados que satisfacen metas"]:

- Mundo de Bloques, usando las relaciones `libre(X)`, `mesa(X)` y `sobre(X,Y)`:
  - `E1 = {mesa(a), mesa(d), libre(a), libre(b), sobre(c,d), sobre(b,c)}` (a y d en la mesa, c sobre d, b sobre c);
  - `E2 = {mesa(a), libre(c), sobre(b,a), sobre(c,b)}` (b sobre a, c sobre b) [García, Episodio V, secs. "Ejemplos de estados y metas" y "Especificación de operadores"].
- Con la Suposición del Mundo Cerrado, todo literal que no aparece en el conjunto se considera **falso**; por eso no hace falta decir que `libre(c)` es falsa en E2 [García, ibidem]. En AIMA esto es la semántica de base de datos: "the closed-world assumption means that any fluents that are not mentioned are false, and the unique names assumption means that Truck 1 and Truck 2 are distinct" [RN10, sec. 10.1, p. 367].

**Metas** — estados parcialmente especificados, escritos como conjunciones de literales fijos positivos [García, Episodio V, sec. "Lenguaje STRIPS: estados, metas y estados que satisfacen metas"]:

- `G1 = {mesa(a)}`, `G2 = {libre(a), mesa(a)}`, `G3 = {sobre(c,b), sobre(b,a)}` [García, Episodio V, sec. "Ejemplos de estados y metas"].
- La meta **no describe el estado final completo**, sólo lo que debe ser cierto: no importa qué pase con los bloques que no se mencionan.

**Operadores** — nombre, parámetros, precondiciones y efectos separados en add-list y del-list [García, Episodio V, sec. "Especificación de operadores"]:

| Operador | Precondiciones | Add-list | Del-list |
|---|---|---|---|
| `apilar(X,Y)` | {`mesa(X)`, `libre(X)`, `libre(Y)`} | {`sobre(X,Y)`} | {`libre(Y)`, `mesa(X)`} |
| `desapilar(X,Y)` | {`libre(X)`, `sobre(X,Y)`} | {`libre(Y)`, `mesa(X)`} | {`sobre(X,Y)`} |

[García, Episodio V, sec. "Especificación en el lenguaje STRIPS"].

- **Verificación y aplicación** (todo con operaciones de conjuntos):
  - una acción es **aplicable** en E si `Pre ⊆ E`; en caso contrario no existe como sucesora de E;
  - el **nuevo estado** es `E' = (E \ Del) ∪ Add` [García, Episodio V, sec. "Acciones aplicables en un estado"], que en AIMA es `RESULT(s, a) = (s − DEL(a)) ∪ ADD(a)` [RN10, sec. 10.1, p. 368, ec. 10.1].
  - Ejemplo: `apilar(c,i)` es aplicable en `E1 = {mesa(i), mesa(c), libre(c), libre(i)}` y produce `E2 = {mesa(i), libre(c), sobre(c,i)}`; `desapilar(c,i)` no es aplicable en E1 [García, Episodio V, sec. "Acciones aplicables en un estado"].

### 4.c. ¿Bajo qué condición se dice que un estado satisface una meta?

- **Condición:** "Un estado E satisface una meta G si **G ⊆ E**" [García, Episodio V, sec. "Lenguaje STRIPS: estados, metas y estados que satisfacen metas"]. Es decir, **todos** los literales de la meta deben estar presentes en la descripción del estado; gracias a la Suposición del Mundo Cerrado, alcanza con verificar la inclusión (lo que no está en G no se exige nada) [ibidem].
- Ejemplos con los estados del punto anterior [García, Episodio V, sec. "Ejemplos de estados y metas"]:
  - `E1 = {mesa(c), mesa(b), mesa(a), libre(c), libre(a), libre(b)}` satisface `G1 = {mesa(a)}` y `G2 = {libre(a), mesa(a)}`, pero **no** satisface `G3 = {sobre(c,b), sobre(b,a)}` (le falta `sobre(c,b)` y `sobre(b,a)`);
  - `E2 = {mesa(a), libre(c), sobre(b,a), sobre(c,b)}` satisface `G1` y `G3`, pero **no** satisface `G2` (le falta `libre(a)`);
  - con el otro juego de ejemplos, `E1 = {mesa(a), mesa(d), libre(a), libre(b), sobre(c,d), sobre(b,c)}` satisface `G1 = {mesa(a), libre(a)}` pero no `G2 = {libre(c), sobre(c,d)}` (le falta `libre(c)`) [García, Episodio V, sec. "Lenguaje STRIPS: estados, metas y estados que satisfacen metas"].
- **Interpretación:** la meta define un **conjunto de estados meta**; un estado pertenece a ese conjunto si y sólo si contiene todos sus literales. Por eso el test de meta de un planificador es una simple prueba de inclusión `G ⊆ E` [García, ibidem; RN10, sec. 10.1, p. 369].
- En AIMA la condición equivalente es que el estado **implicue** la meta: "The problem is solved when we can find a sequence of actions that end in a state s that entails the goal" [RN10, sec. 10.1, p. 369].

### 4.d. Algoritmo de planificación "STRIPS Planner"

**Idea general (divide and conquer sobre las metas):** "The basic idea behind the STRIPS planner is divide and conquer: to create a plan to achieve a conjunction of goals, create a plan to achieve one goal, and then create a plan to achieve the rest of the goals" [PMG, sec. 8.3, p. 301]. En palabras: "To achieve a list of goals choose one of them to achieve. If it is not already achieved, choose an action that makes the goal true, achieve the preconditions of the action, carry out the action, and then achieve the rest of the goals" [PMG, ibidem].

**Algoritmo** (especificación de la Figura 8.2 de PMG, que usa la representación STRIPS) [PMG, sec. 8.3, pp. 301-302]:

```
% achieve_all(Gs, W0, Wf):  Wf es el mundo resultante luego de lograr cada meta de la lista Gs desde W0
achieve_all([],     W0, W0)
achieve_all(Goals, W0, W2)  :-  remove(G, Goals, RestGoals),
                                achieve(G, W0, W1),
                                achieve_all(RestGoals, W1, W2)

% achieve(G, W0, Wf):  Wf es el mundo resultante luego de lograr la meta G desde el mundo W0
achieve(G, W, W)                  :- holds(G, W).                      % (1) la meta ya es cierta
achieve(G, W0, Wj)                :- clause(G, B),
                                    achieve_all(B, W0, Wi).             % (2) G es relación derivada
achieve(G, W0, do(Action, Wi))    :- achieves(Action, G),
                                    preconditions(Action, Pre),
                                    achieve_all(Pre, W0, Wi).           % (3) G es relación primitiva
```

- **Cómo se lee:**
  - `achieve_all` toma una lista de metas y las va resolviendo **de a una**, en el orden en que aparecen en la lista, **sobre el mismo mundo** que va actualizando: si la lista de metas está vacía, el problema está resuelto sin ejecutar nada más.
  - `achieve` para una meta G tiene tres casos: (1) si G ya es verdadera en W, no hay nada que hacer; (2) si G es una **relación derivada** (tiene una cláusula que la define), se lograrán todos los átomos del cuerpo de esa cláusula; (3) si G es una **relación primitiva** y no es verdadera, se elige una acción A cuyo *add-list* contiene G, se `achieve` primero todas sus **precondiciones** y recién entonces se ejecuta A, produciendo `do(Action, Wi)`.
  - Los predicados auxiliares: `holds(G, W)` indica que G es cierta en W; `achieves(A, G)` indica que G está en el add-list de A; `preconditions(A, Pre)` devuelve la lista de precondiciones de A [PMG, sec. 8.3, p. 303].
  - El plan que devuelve es la concatenación de las acciones **en el orden en que se van aplicando**, y el mundo final se va construyendo con `do(Action, W')`, es decir aplicando add-list y del-list [PMG, sec. 8.3, pp. 302-303].
- **Ejemplo (delivery robot de PMG):** ante las metas `[carrying(rob, parcel), sitting_at(rob, lab2)]`, el algoritmo elige lograr primero `carrying(rob, parcel)`, que no es cierta inicialmente; busca la acción que la logra, `pickup(rob, parcel)`, y tiene que lograr sus precondiciones `[autonomous(rob), sitting_at(parcel, Pos), at(rob, Pos)]`; entre ellas `at(rob, storage)`, que se logra con `move(rob, Pos1, storage)`, y así siguiendo recursivamente hasta que todas las precondiciones valen [PMG, sec. 8.3, p. 303].
- **Características y limitaciones:**
  - Es un **planificador hacia atrás en su razonamiento pero hacia adelante en su ejecución**: elige acciones por lo que agregan (add-list) y luego las ejecuta, acumulando el mundo [PMG, sec. 8.3, pp. 301-302].
  - Es **sencillo y de divide y conquer**, pero **no es completo**: no contempla backtracking cuando hay varias acciones candidatas ni verifica al final que las metas ya logradas sigan siendo ciertas. Si al lograr una meta posterior una acción borra (del-list) un literal de una meta anterior, el plan devuelto no soluciona el problema. De hecho, elegir un mal orden de resolución de las metas puede hacer que la versión más simple no retorne solución, como se estudia en los puntos 5.b y 5.c del enunciado.
  - "El algoritmo STRIPS Planner no debe confundirse con el lenguaje STRIPS: se puede usar la representación STRIPS con otros planificadores, y el planificador STRIPS con otras representaciones" [PMG, sec. 8.2, p. 288].
  - Para dominios más grandes, AIMA muestra que se le pueden aplicar las heurísticas y estructuras de la sección 10.2/10.3 (FF usa búsqueda hacia adelante con *hill climbing* modificado sobre esta representación) [RN10, sec. 10.2.3, p. 378].

## 6. Planificador de Orden Parcial

### 6.a. ¿Qué es un plan parcial? ¿Qué elementos lo forman? ¿En qué se diferencia de un plan total? ¿Cuál es su ventaja?

- **Plan parcial:** cada nodo del espacio de búsqueda de POP es un plan parcial, formado por **cuatro elementos** `(As, Os, Ls, Goals)` [García, VI, PDF p. 11]:
  - `As`: conjunto de acciones (o pasos) del plan;
  - `Os`: conjunto de restricciones de orden (orden parcial) sobre los pasos; se escribe `A < B` cuando el paso `A` debe preceder al `B`. **Todo vínculo causal es una restricción de orden** [ibidem];
  - `Ls`: conjunto de vínculos (*links*) causales entre pasos;
  - `Goals` ("agenda"): lista de (pre)condiciones pendientes o sub-metas que el planificador aún debe resolver por regresión [ibidem].
- **Plan inicial:** dado un problema `(I, G, A)`, es `As = {start, finish}`, `Os = {start < finish}`, `Ls = {}`, `Goals = G`, donde `start` tiene como efecto el estado inicial `I` y `finish` tiene como precondiciones la meta `G` [García, VI, PDF pp. 12-13].
- **Diferencia con el plan total:** los planificadores vistos mantienen un **orden total** en los planes que generan, y "al ir formando la secuencia de acciones... el planificador se compromete al orden total de las acciones que ya están en esta secuencia". "El orden total es impuesto por el algoritmo, **aún cuando ese orden no sea realmente necesario**" [García, VI, PDF p. 3].
- **Ventaja:** no hace falta decidir el orden de acciones que no se relacionan. En el problema de cambiar los cartuchos de una impresora hay **6 planes totalmente ordenados** posibles, pero alcanza con indicar las **2 restricciones de orden** que impone el vínculo causal: `sacar(negro,viejo)` antes de `poner(negro,nuevo)`, y `sacar(color,viejo)` antes de `poner(color,nuevo)` [García, VI, PDF pp. 7-8]. En general, la solución de POP es un conjunto de pasos `As` más un conjunto de restricciones `Os`: puede haber **más de una secuencia** de elementos de `As` que cumpla las restricciones de `Os`, y cada una de esas secuencias es un plan (totalmente ordenado) [García, VI, PDF p. 33].

#### EXTRAS

- **Definición formal:** "A partial-order plan is a set of actions together with a partial ordering, representing a 'before' relation on actions, such that any total ordering of the actions, consistent with the partial ordering, will solve the goal from the initial state" [PMG, sec. 8.3, p. 309]. La idea equivalente también se encuentra en RN10 [sec. 10.4.4, p. 390].
- **Formalización en PMG:** un plan parcial es `plan(As, Os, Ls)`; un plan completo es un plan parcial seguro con la agenda vacía, y corresponde a un plan de orden parcial [PMG, sec. 8.3, pp. 310-311]. También se lo llama *nonlinear planner*, "but this is a misnomer as such planners often produce a linear plan" [ibidem].
- **Costo del orden total:** el planificador debe probar cada permutación de las acciones, "when it may be possible to show that all orderings don't succeed" [PMG, sec. 8.3, p. 308].
- **Least commitment:** el refinamiento agrega a cada paso la mínima cantidad de restricciones necesarias: "At every step, we make the least commitment possible to fix the flaw" [RN10, sec. 10.4.4, p. 391].
- **Búsqueda en el espacio de planes:** POP no busca en el espacio de estados sino en el espacio de planes, partiendo del plan vacío (sólo estado inicial y meta, sin acciones) y reparando *flaws*: "A flaw is anything that keeps the partial plan from being a solution" [RN10, sec. 10.4.4, pp. 390-391].
- **Ganancia por descomposición:** si el problema es totalmente descomponible en subproblemas independientes, se obtiene una aceleración exponencial frente a la búsqueda en el espacio de estados: "the identification of independent subproblems can be a powerful weapon. In the best case—full decomposability of the problem—we get an exponential speedup" [RN10, sec. 10.5, p. 392].
- **Contras:** no tiene representación explícita de estados, lo que vuelve incómodos algunos cálculos: "it has the disadvantage of not having an explicit representation of states in the state-transition model" [RN10, sec. 10.4.4, p. 391]. Por eso hoy no es competitivo en planificación clásica completamente automatizada, aunque se sigue usando en planificación de operaciones y en dominios donde es importante que **humanos entiendan los planes** [ibidem].

---

**Fuentes consultadas:**

- **RN10:** Russell, S. y Norvig, P. *Artificial Intelligence: A Modern Approach*, 3ra ed., Pearson, 2010. Capítulo 3 ("Solving Problems by Searching", sec. 3.1.2) y capítulo 10 ("Classical Planning", secs. 10.1, 10.1.3, 10.1.4, 10.4.4 y 10.5).
- **García:** García, A. J. *Inteligencia Artificial - Notas de Clase*, DCIC - Universidad Nacional del Sur: Episodio V: "Agentes BDI. Representación de acciones y planificación automática", 15/09/2026 (`tema4/ale-2026-IA-06-Agentes-BDI-Acciones-y-planes.pdf`); Episodio VI: "Planificación de Orden Parcial (POP)", 22/09/2026 (`tema4/ale-2026-IA-07-Planificación-Orden-Parcial (POP).pdf`).
- **PMG:** Poole, D.; Mackworth, A. y Goebel, R. *Computational Intelligence: A Logical Approach*, Oxford University Press, 1998, capítulo 8 ("Actions and Planning", secs. 8.2 y 8.3).
