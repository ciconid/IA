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

**Fuentes consultadas:**

- **RN10:** Russell, S. y Norvig, P. *Artificial Intelligence: A Modern Approach*, 3ra ed., Pearson, 2010. Capítulo 3 ("Solving Problems by Searching", sec. 3.1.2) y capítulo 10 ("Classical Planning", secs. 10.1, 10.1.3, 10.1.4).
- **García:** García, A. J. *Inteligencia Artificial - Notas de Clase*, DCIC - Universidad Nacional del Sur: Episodio V: "Agentes BDI. Representación de acciones y planificación automática", 15/09/2026; Episodio VI: "Planificación de Orden Parcial (POP)", 22/09/2026.
- **PMG:** Poole, D.; Mackworth, A. y Goebel, R. *Computational Intelligence: A Logical Approach*, Oxford University Press, 1998, capítulo 8 ("Actions and Planning", secs. 8.2 y 8.3).
