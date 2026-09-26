# Trabajo Práctico 3

## 1. Importancia de los métodos de búsqueda para el desarrollo de agentes inteligentes

La resolución automática de problemas mediante búsqueda es central en IA [García, Episodio II]: el capítulo 3 de *Artificial Intelligence: A Modern Approach* se abre señalando cómo "an agent can find a sequence of actions that achieves its goals when no single action will do" [RN10, cap. 3, p. 64]. Por ello, la búsqueda es de gran interés para el desarrollo de agentes inteligentes, ya que:

- **Satisface la racionalidad:** los agentes buscan maximizar su *performance measure* [RN10, sec. 3.1, p. 64]; la búsqueda traduce ese criterio en acciones: encuentra la secuencia que lleva del estado inicial a uno meta y, con la estrategia adecuada, la de menor costo (óptima) [RN10, sec. 3.1.1, p. 68].

- **Las metas organizan el comportamiento:** "Goals help organize behavior by limiting the objectives that the agent is trying to achieve and hence the actions it needs to consider" [RN10, sec. 3.1, p. 65]. La búsqueda convierte el objetivo en un plan concreto, integrada en el ciclo *formular objetivo → formular problema → buscar → ejecutar* [RN10, sec. 3.1, Fig. 3.1, p. 66].

- **Supera a los agentes reactivos:** el mapeo directo estado→acción "would be too large to store and would take too long to learn" [RN10, p. 64]. La búsqueda da **deliberación**: permite anticiparse y resolver problemas no previstos en el diseño, examinando "future actions that eventually lead to states of known value" [RN10, sec. 3.1, p. 65].

- **Es general e independiente del dominio:** "para una gran variedad de situaciones, la resolución de un problema se puede transformar en la tarea de encontrar un camino en un grafo", permitiendo "un método de resolución genérico e independiente del dominio" [García, Episodio II]. Los mismos algoritmos (BFS, DFS, UCS, A*, etc.) se aplican a laberintos, rutas, juegos, planificación, logística o robótica [RN10, sec. 3.2, p. 69].

- **Ofrece garantías formales:** según la estrategia, se garantiza **completitud** (si existe solución, se encuentra) y **optimalidad** (la solución es la de menor costo) [RN10, sec. 3.7, p. 108], a diferencia de un agente que simplemente adivina.

- **Explota la abstracción:** el agente busca sobre un modelo abstraído del mundo (formulación del problema); "Were it not for the ability to construct useful abstractions, intelligent agents would be completely swamped by the real world" [RN10, sec. 3.1.2, pp. 68-69].

- **Admite conocimiento del dominio:** las estrategias informadas (A*) orientan la exploración hacia estados promisorios, reduciendo el esfuerzo computacional sin perder optimalidad (con heurística admisible).

- **Sustenta otras capacidades de la IA:** juegos (cap. 5), satisfacción de restricciones (cap. 6), planificación (cap. 10) y robótica (cap. 25) se construyen sobre estos métodos [RN10].

En síntesis, la búsqueda es cómo el agente "piensa" para pasar de su estado actual a la meta: sin ella depende de respuestas programadas; con ella resuelve problemas nuevos de forma autónoma y con garantías.

---

## 2. Definición de problema de búsqueda y conceptos asociados

**Problema de búsqueda:** se define indicando: 
- (1) la descripción del **estado inicial** desde donde se comienza la búsqueda; 
- (2) la descripción de los **operadores** disponibles con los cuales el agente puede transformar un estado en otro; 
- (3) un **test de meta** que determina si un estado es una meta; 
- (4) una **función de costo de camino** *g(n)* que determina el costo para llegar del estado inicial a un estado "n" [García, Episodio II, sec. Terminología]. La misma definición se encuentra en AIMA [RN10, sec. 3.1.1, p. 67].

**Solución:** un camino desde el estado inicial hasta un estado meta; puede no ser única [García, Episodio II]. La misma definición se encuentra en AIMA [RN10, sec. 3.1.1, p. 68].

**Solución óptima:** aquella que tiene el menor costo de camino entre todas las soluciones del problema [García, Episodio II, sec. Terminología]. La misma definición se encuentra en AIMA [RN10, sec. 3.1.1, p. 68].

**Espacio de estados (o espacio de búsqueda):** el conjunto de todos los estados alcanzables desde el estado inicial mediante los operadores disponibles [García, Episodio II, sec. Terminología]. La misma definición se encuentra en AIMA [RN10, sec. 3.1.1, p. 67].

**Operador:** función que, si puede aplicarse en un estado, lo transforma en otro estado; también se lo suele llamar regla, transición, función sucesor, producción o acción [García, Episodio II, sec. Terminología]. La misma noción se denomina *action* en AIMA [RN10, sec. 3.1.1, p. 67].

**Estado alcanzable:** un estado al cual se puede llegar desde el estado inicial aplicando una secuencia de operadores [García, Episodio II, sec. Terminología].

**Grafo de búsqueda:** el grafo que representa el espacio de estados, donde cada nodo representa un estado y cada arco la aplicación de un operador del problema; al representar el espacio de estados también se lo llama "espacio de búsqueda" o "grafo de búsqueda", y puede generarse dinámicamente a medida que la búsqueda avanza [García, Episodio II, sec. Terminología]. Cuando la representación se expande como un árbol con raíz en el estado inicial se denomina "árbol de búsqueda" [García, Episodio II, sec. Terminología]. La misma idea se encuentra en AIMA [RN10, sec. 3.1.1, p. 67].

## 4. El ta-te-ti (tic-tac-toe) como problema de búsqueda

Siguiendo la definición de problema de búsqueda del punto 2 [García, Episodio II, sec. Terminología], el ta-te-ti se define de la siguiente manera:

- **Estado inicial:** tablero de 3x3 completamente vacío, con el turno del jugador X.
- **Operadores:** colocar la ficha del jugador en turno (X u O) en una casilla vacía del tablero. Dado un estado, hay tantos operadores aplicables como casillas vacías (como máximo 9).
- **Test de meta:** un estado es meta si uno de los jugadores completó una fila, una columna o una diagonal (ganó), o si el tablero quedó completo sin que ninguno formara una línea (empate).
- **Función de costo de camino:** se asume costo 1 por cada operador aplicado, por lo que *g(n)* = profundidad del nodo (cantidad de fichas colocadas).

Una solución es entonces una secuencia de movimientos que, partiendo del tablero vacío, lleva a un estado meta. Dado que el ta-te-ti es un juego de dos jugadores con turnos alternados, una modelización más realista debe considerar las jugadas del oponente; esto se aborda con la búsqueda adversarial (juegos) [RN10, cap. 5].

## 5. Estrategias para recorrer un espacio de búsqueda

Tener un método o una estrategia de búsqueda implica establecer un **orden determinado para seleccionar y expandir los nodos de la frontera**: decidir cuál de los nodos que aún no fueron explorados es el próximo a expandir. Todos los algoritmos de búsqueda comparten la misma estructura básica y se diferencian "primarily according to how they choose which state to expand next—the so-called search strategy" [RN10, sec. 3.3, p. 75]. El nodo elegido define qué caminos se exploran primero, y por lo tanto las propiedades del algoritmo, que se evalúan según cuatro criterios: 
- **completitud** (¿garantiza hallar una solución cuando existe?), 
- **optimalidad** (¿encuentra la solución óptima?), 
- **complejidad temporal** y 
- **complejidad espacial** [RN10, sec. 3.3.2, p. 80].

Un buen método garantiza que la exploración sea *sistemática* y no desperdicie recursos. En cambio, visitar estados en cualquier momento, sin ningún orden o criterio definido, puede generar problemas graves:

- **Ciclos (caminos con lazos):** si no se controlan, se pueden volver a generar estados ya visitados. Al poder recorrer un ciclo una cantidad ilimitada de veces, el árbol de búsqueda se vuelve infinito incluso cuando el espacio de estados es finito ("the complete search tree for Romania is infinite because there is no limit to how often one can traverse a loop"), y "loops can cause certain algorithms to fail, making otherwise solvable problems unsolvable" [RN10, sec. 3.3, pp. 75-76].

- **Caminos redundantes y explosión combinatoria:** seguir caminos redundantes (que vuelven a un mismo estado) multiplica innecesariamente los nodos y puede convertir un problema tratable en intratable. En una grilla rectangular, un árbol de búsqueda de profundidad *d* que incluye estados repetidos tiene 4\^d hojas, pero solo hay ~2*d*\^2 estados distintos; para *d* = 20, cerca de un trillón de nodos frente a unos 800 estados [RN10, sec. 3.3, p. 77].

- **Falta de garantías de terminación o de completitud:** una exploración sin estrategia puede quedarse infinitamente en una rama que no contiene la meta, o no llegar nunca a la solución aunque exista, además de consumir memoria y tiempo sin control.

Estos problemas se evitan de dos maneras complementarias: 
- (1) aplicando **control de visitados** (explored set o closed list); y 
- (2) eligiendo una **estrategia concreta** cuyas propiedades (completitud, optimalidad, complejidad) sean adecuadas al problema, en lugar de seleccionar nodos arbitrariamente.

El control de visitados convierte la búsqueda de *tree search* en *graph search*: no se vuelven a considerar caminos redundantes ni ciclos ("algorithms that forget their history are doomed to repeat it" [RN10, sec. 3.3, p. 77]). El algoritmo sigue construyendo un árbol de búsqueda, pero al descartar estados repetidos ese árbol crece directamente sobre el grafo del espacio de estados ("the search tree constructed by the GRAPH-SEARCH algorithm contains at most one copy of each state, so we can think of it as growing a tree directly on the state-space graph" [RN10, sec. 3.3, p. 77]). La diferencia entre ambos es que el *tree search* considera todos los caminos posibles, mientras que el *graph search* evita caminos redundantes [RN10, sec. 3.7, p. 108].

## 6. Qué significa que una estrategia de búsqueda sea ciega

Que una estrategia sea **ciega** (también llamada *blind search* o *no informada*, *uninformed search*) significa que, para decidir qué nodo expandir de la frontera, no utiliza ninguna información del problema más allá de su definición: no sabe cuáles nodos son "más promisorios" que otros. Los métodos ciegos "recorren el espacio de búsqueda hasta que se 'tropiezan' con la solución" y "exploran el espacio de búsqueda 'a ciegas' sin usar ningún tipo de información que 'dirija' la búsqueda hacia nodos sin explorar que sean 'más promisorios'" [García, Episodio II, sec. Búsqueda a ciegas]. La misma definición se encuentra en AIMA [RN10, sec. 3.4, p. 81]. Por eso la exploración se define solo por el *orden* en que se seleccionan y expanden los nodos (DFS expande el nodo más profundo, BFS el menos profundo, UCS el de menor costo), sin ninguna guía heurística. Como contrapartida, las estrategias **informadas** (heurísticas) sí usan información específica del problema para orientar la búsqueda.

## 7. Descripción de DFS y BFS

**Depth First Search (DFS):** *búsqueda en profundidad*. La estrategia consiste en expandir siempre el nodo más profundo de la frontera: se retira el primero de la lista de la frontera y los nuevos nodos generados se agregan al principio (comportamiento de **pila**, *stack*, LIFO) [García, Episodio II, sec. Búsqueda en profundidad - DFS]. La búsqueda desciende inmediatamente hasta el nivel más profundo del árbol y, cuando los nodos no tienen sucesores, "back up" al siguiente nodo más profundo que aún tenga sucesores sin explorar; en AIMA: "Depth-ﬁrst search always expands the deepest node in the current frontier of the search tree" y usa "a LIFO queue" [RN10, sec. 3.4.3, p. 85]. Como resultado, la frontera crece de manera *lineal* (contiene los nodos "hermanos" de la rama que se está explorando), por lo que su uso de memoria es reducido; a cambio, no garantiza optimalidad y, en espacios con caminos infinitos, la versión *tree search* puede no ser completa [RN10, sec. 3.4.3, pp. 86-87].

**Breadth First Search (BFS):** *búsqueda a lo ancho*. La estrategia consiste en expandir siempre el nodo menos profundo de la frontera: se retira el primero de la lista de la frontera y los nuevos nodos generados se agregan al final (comportamiento de **cola**, *queue*, FIFO) [García, Episodio II, sec. Búsqueda a lo ancho - BFS]. Por lo tanto, se expanden todos los nodos de una profundidad del árbol antes de pasar al siguiente nivel; en AIMA: "Breadth-ﬁrst search is a simple strategy in which the root node is expanded ﬁrst, then all the successors of the root node are expanded next, then their successors, and so on" [RN10, sec. 3.4.1, p. 81]. La frontera queda formada por los "hijos" del último nivel explorado, por lo que crece *exponencialmente*: requiere O(b\^d) nodos en memoria [García, Episodio II; RN10, sec. 3.4.1, pp. 81-82]. A cambio, es completa y, cuando todos los costos de paso son iguales (como en este TP, donde cada movimiento tiene costo 1), es **óptima**, ya que siempre encuentra la meta menos profunda [RN10, sec. 3.4.1, p. 82].

## 8. Dónde se determina la estrategia en el algoritmo genérico de búsqueda

En el algoritmo genérico dado, la estrategia de búsqueda se determina en los predicados **`seleccionar/3`** y **`agregar/3`**:

- **`seleccionar(Nodo, Frontera, FronteraReducida)`:** decide cuál nodo de la frontera se elige para expandir en cada paso (p. ej., el primero, el de menor costo, el más promisorio según una heurística).
- **`agregar(FronteraReducida, Vecinos, NuevaFrontera)`:** decide en qué posición de la frontera se colocan los vecinos recién generados.

Como señalan las notas de clase, "la forma de seleccionar el nodo a expandir y la forma como agregar un nodo a la frontera permite definir diferentes estrategias de búsqueda" [García, Episodio II, sec. Estrategia de búsqueda]. Por ejemplo, con `seleccionar` = primero de la frontera: si `agregar` coloca los vecinos al principio de la frontera se obtiene búsqueda en profundidad (DFS, comportamiento de pila), y si los coloca al final se obtiene búsqueda a lo ancho (BFS, comportamiento de cola) [García, Episodio II, sec. Estrategia de búsqueda]. La misma idea se encuentra en AIMA: la estrategia se define por cómo se elige qué nodo expandir ("they vary primarily according to how they choose which state to expand next—the so-called search strategy" [RN10, sec. 3.3, p. 75]).

## 9. Estrategia de búsqueda en `busqueda.pl`

### 9-a. ¿Qué estrategia usa `busqueda.pl`?

La estrategia implementada es **búsqueda en profundidad (DFS)**. Se determina por la manipulación de la frontera en **`seleccionar/3`** y **`agregar/3`**:

- **`seleccionar/3`:** siempre toma el **primer** elemento de la frontera (`seleccionar([Nodo|FronteraSinNodo],Nodo,FronteraSinNodo)`).
- **`agregar/3`:** los vecinos recién generados se colocan **al principio** de la frontera (`append(Vecinos, Frontera, FronteraNueva)`).

Con `seleccionar` = primero de la frontera, si `agregar` pone los vecinos al **principio** se obtiene búsqueda en profundidad (DFS, comportamiento de **pila/LIFO**); si los pusiera al **final** se obtendría BFS (cola/FIFO) [García, Episodio II, sec. Estrategia de búsqueda; ver punto 8 de este TP]. Al expandirse siempre el nodo más recientemente generado, la frontera desciende en profundidad hasta encontrar una meta. En la traza del programa la solución hallada es `A → B → E → G → H` (costo 4).

### 9-b. ¿Por qué importa el orden de las relaciones `ady/3`?

Los sucesores de un nodo se generan con `findall/3` en `generarVecinos/2`, que enumera los vecinos **en el orden en que están escritas las cláusulas `ady/3`**. Como `seleccionar/3` toma el primer nodo de la frontera y `agregar/3` pone los vecinos nuevos al principio, el vecino que aparece primero en `findall` es el que DFS explora primero. El orden de las cláusulas decide, entonces, **por qué rama se desciende primero** y, en consecuencia, **qué solución se encuentra** (y si se encuentra).

**¿Qué pasa si cambiamos el orden?** Intercambiar `ady('B','E',1)` y `ady('B','D',1)` hace que desde `B` los vecinos se generen como `D`, `E`, `A` (en lugar de `E`, `D`, `A`). La búsqueda desciende entonces por `D`; como `D` solo es adyacente a `B` (ciclo `B ↔ D`), los vecinos de `D` vuelven a incluir a `B`, que a su vez regenera `D`, y así indefinidamente. Como `busqueda.pl` implementa *tree search* sin control de visitados, DFS queda atrapada en el ciclo `B ↔ D`, nunca explora la rama de `E` (que lleva a la meta `H`) ni la de `C` (que lleva a `J`), y **no termina**. Es la debilidad conocida del *tree search* DFS: en espacios con ciclos o caminos infinitos puede no ser completa [RN10, sec. 3.4.3, pp. 86-87]. El hecho de que la versión original "funcione" se debe a que el orden de las cláusulas hace que DFS primero descienda por la rama afortunada.

**¿Cómo solucionarlo?** Aplicando **control de visitados** (*explored set* / *closed list*), es decir, pasando de *tree search* a *graph search* (ver punto 8): los estados ya generados no se vuelven a expandir ni a re-agregar a la frontera. Con eso, desde `D` el vecino `B` es descartado por ya estar visitado, la búsqueda continúa con el siguiente nodo de la frontera (`E`) y alcanza una meta; así el resultado deja de depender de ciclos y de la suerte del orden de las cláusulas. Reordenar las cláusulas de a mano para cada problema solo funciona para ese caso puntual, por lo que no es una solución general.

### 9-c. Modificaciones para convertir la búsqueda en BFS

La única modificación necesaria es en **`agregar/3`** (y el comentario que la acompaña), para que los vecinos nuevos se coloquen **al final** de la frontera en lugar del principio:

```prolog
agregar(Vecinos,Frontera,FronteraNueva):-
    append(Frontera, Vecinos, FronteraNueva).
```

`seleccionar/3` queda igual (sigue tomando el primer nodo). Con `seleccionar` = primero y `agregar` que encola al final, la frontera se comporta como una **cola (FIFO)**: se expanden todos los nodos de una profundidad antes de pasar a la siguiente, es decir, BFS.

**¿En qué momento se diferencian DFS y BFS?** En la forma de manipular la frontera, que es donde se determina la estrategia (punto 8): ambos usan el **mismo `seleccionar`** (primero de la frontera) y solo cambia **`agregar/3`** — DFS antepone los vecinos (pila), BFS los pospone (cola). En este esquema, DFS y BFS son intercambiables con una única línea de código.

### 9-d. Comparación del DFS original contra BFS

Ninguna de las dos es *mejor* en abstracto: la elección depende del problema y de qué se priorice. Sus propiedades se describen en el punto 7 de este TP [RN10, secs. 3.4.1–3.4.3; García, Episodio II]:

- **Completitud:** BFS es completa (con costos iguales, siempre encuentra la meta más superficial). El *tree search* DFS aquí no es completo, como se vio en 9-b (puede entrar en un ciclo infinito).
- **Optimalidad:** BFS es **óptima** cuando todos los costos son iguales, como en `busqueda.pl` (cada movimiento cuesta 1). DFS **no garantiza** optimalidad: en este laberinto encontró `A → B → E → G → H` (costo 4), que coincide con el mínimo porque `H` está a profundidad 4, pero en general puede hallar caminos más largos.
- **Memoria:** DFS necesita memoria **lineal** O(b·m) (la frontera son los "hermanos" de la rama actual); BFS necesita **exponencial** O(b^d) (todos los nodos de un nivel). En este laberinto pequeño la diferencia no se nota, pero en espacios grandes BFS se vuelve inviable en memoria.
- **Tiempo:** ambos son exponenciales en el peor caso; BFS expande todos los nodos hasta la profundidad de la meta, mientras que DFS puede "acertar" la rama correcta rápido o perderse en una rama sin salida.

**Escenarios convenientes:**

- **DFS** conviene cuando la solución está **profunda** y/o el espacio de estados es **grande** y se dispone de **poca memoria**, y no se exige optimalidad (p. ej., verificar la existencia de una solución, laberintos con solución cerca del final).
- **BFS** conviene cuando se necesita **la solución de mínimo costo** (optimalidad) y la meta está a poca profundidad desde el estado inicial, a costa de memoria (p. ej., caminos cortos en mapas, puzles con solución cercana).

## 10. Consecuencias para BFS de considerar costos de operadores diferentes

**Consecuencia principal:** BFS expande los nodos en **orden de profundidad**, no de costo. Su optimalidad depende de que el costo de camino sea una función no decreciente de la profundidad, lo cual se cumple cuando "all actions have the same cost" [RN10, sec. 3.4.1, p. 82]: la meta menos profunda también es la de menor costo. Si los costos son **distintos entre sí**, eso deja de valer: BFS sigue encontrando la meta **menos profunda** (no la óptima), porque al aplicar el test de meta apenas se **genera** el nodo ("the shallowest goal node is not necessarily the optimal one" [RN10, sec. 3.4.1, p. 82]). En términos de las notas de clase, BFS no es apropiado cuando "el costo de los operadores no es 1" [García, Episodio II, sec. ¿Alguna conclusión?]. Además, el costo de las soluciones encontradas **deja de ser un reflejo** del número de pasos, por lo que BFS no aporta ninguna garantía sobre la calidad de la solución.

**Espacio de búsqueda que ilustra el problema:**

```
              ┌────(1)──── X ────(1)──── M2  (meta)
S (inicial) ──┤
              └────(100)─── M1  (meta)
```

Con BFS (cola FIFO) se expande `S` y se **generan** sus dos vecinos `M1` y `X` (profundidad 1). Como el test de meta se aplica al generar, `M1` (que es meta y está a profundidad 1) es detectada de inmediato y la búsqueda retorna la solución `S → M1`, de **costo 100**. Sin embargo, la solución óptima es `S → X → M2`, de **costo 2** (costo total *g* = 1 + 1), aunque la meta esté a mayor profundidad. BFS nunca la considera porque ya se detuvo en la meta más superficial.

**Estrategia que resuelve el problema:** **Uniform-Cost Search (UCS)**, también llamada *Lowest-Cost-First Search* (LCFS) [García, Episodio II, sec. "Lowest-cost-first Search (LCFS)"]. Se obtiene como una "simple extension" de BFS [RN10, sec. 3.4.2, p. 84]:

- **Selección por costo, no por profundidad:** "Instead of expanding the shallowest node, uniform-cost search expands the node *n* with the lowest path cost *g*(n)", manteniendo la frontera como una **cola con prioridad** ordenada por *g*(n) [RN10, sec. 3.4.2, p. 84]. En el esquema de `busqueda.pl` debe modificarse `agregar/3` para que quede primero el nodo con menor `g(n)` [García, Episodio II, sec. LCFS].

- **Test de meta al seleccionar, no al generar:** un nodo meta generado puede no ser aún el de menor costo; por eso UCS recién termina cuando el nodo meta es **seleccionado para expandir** ("the first goal node selected for expansion must be the optimal solution" [RN10, sec. 3.4.2, p. 85]).

- **Garantías:** es **completa** y **óptima**, siempre que cada paso tenga un costo positivo mínimo *ε* > 0. A cambio, su complejidad se mide en función del costo óptimo *C*\* y puede ser elevada: *O(b^⌊1+C\*/ε⌋)*, mucho mayor que *b^d* cuando hay pasos muy baratos [RN10, sec. 3.4.2, pp. 84-85].

En el ejemplo anterior, UCS expande `S`, luego `X` (g=1) antes que `M1` (g=100), después `M2` (g=2) y recién entonces selecciona la meta de menor costo, devolviendo la solución óptima `S → X → M2` (costo 2).

## 13. Diferencia entre costo de camino y heurística

Ambas son funciones que asignan un valor numérico no negativo a un nodo, pero miden cosas distintas:

- **Costo de camino *g*(n):** es el costo **acumulado real** del camino que va desde el estado inicial hasta el nodo *n* [RN10, sec. 3.4, p. 78, Fig. 3.7]. Es parte de la **definición del problema** (función de costo de camino, punto 2 de este TP) y se **conoce con exactitud** a medida que se construye el camino, sumando los costos de los operadores aplicados. Depende del camino recorrido: dos nodos con el mismo estado pueden tener distinto *g*(n) según por dónde se llegó.

- **Heurística *h*(n):** es una **estimación** del costo del camino menos costoso entre el nodo *n* y una meta alcanzable desde *n* [García, Episodio II, sec. Función heurística]. En AIMA: "h(n) = estimated cost of the cheapest path from the state at node n to a goal state", y a diferencia de *g*(n), "it depends only on the state at that node" [RN10, sec. 3.5, p. 92]. No proviene de la definición del problema: es información **particular del dominio** ("in general, each problem has its own h(N) and for each problem several h(N) can be defined" [García, Episodio II, sec. Función heurística]), por lo que puede **subestimar o sobrestimar** el costo real restante. Vale además que *h*(n)=0 cuando *n* es un estado meta [RN10, sec. 3.5, p. 92].

**Diferencias fundamentales:**

- *g*(n) es **real y exacto** (lo ya recorrido); *h*(n) es una **estimación** (lo que falta).
- *g*(n) surge de la **definición del problema** y se puede calcular; *h*(n) es un **conocimiento adicional del dominio**, no computable a partir de la definición del problema [RN10, sec. 3.5, p. 92].
- *g*(n) depende del **camino** hasta *n*; *h*(n) depende **solo del estado** de *n* [RN10, sec. 3.5, p. 92].
- Son las dos componentes que los métodos informados combinan para evaluar un nodo, siendo la **función de evaluación** típica *f*(n) = *g*(n) + *h*(n), usada por A* (punto 16 de este TP).

## 14. Descripción de Best First Search (BestFS) y Heuristic Depth First Search (HDFS)

Ambos son métodos de **búsqueda informada (heurística)**: usan la función h(N) —estimación del costo del camino menos costoso entre el nodo N y una meta alcanzable desde N— para decidir qué nodo explorar [García, Episodio III; RN10, sec. 3.5, p. 92].

### Best First Search (BestFS) — "el mejor primero"

- **Estrategia:** elegir de la frontera el nodo con **menor valor de h(N)**, el que "parece estar más cerca de la meta". La frontera se trata como una **cola con prioridad ordenada por h(N)** [García, Episodio III, sec. El mejor primero]. En AIMA se denomina *greedy best-first search*: "Greedy best-first search tries to expand the node that is closest to the goal, on the grounds that this is likely to lead to a solution quickly. Thus, it evaluates nodes by using just the heuristic function; that is, f(n) = h(n)" [RN10, sec. 3.5.1, p. 93]. La misma estrategia se encuentra en PMG [PMG, sec. 4.5, p. 133].
- **Implementación** en el esquema de `busqueda.pl`: `seleccionar/3` toma el primero de la frontera y `agregar/3` reordena **la frontera completa** por h(N) [García, Episodio III, sec. El mejor primero; PMG, sec. 4.5, p. 133].
- **Garantías:** no garantiza **optimalidad** ni **completitud**: "Greedy best-first tree search is also incomplete even in a finite state space, much like depth-first search" [RN10, sec. 3.5.1, p. 93]. Lo mismo en PMG: "unlike breadth-first search, it isn't guaranteed to find a solution even if one exists. It doesn't necessarily find the shortest path first" [PMG, sec. 4.5, p. 133].
- **Complejidad:** peor caso O(b^m) en tiempo **y espacio**; "La complejidad espacial puede ser un grave problema ya que en el peor caso es exponencial" [García, Episodio III, sec. El mejor primero]. Con una buena heurística, el espacio efectivamente explorado se reduce sustancialmente [RN10, sec. 3.5.1, p. 93].

### Heuristic Depth First Search (HDFS) — "profundidad heurístico"

- **Estrategia:** como DFS, expande siempre el **nodo más profundo de la frontera** (comportamiento de pila), pero **ordena los vecinos del nodo recién expandido por h(N)** antes de agregarlos al principio de la frontera: "elije de los primeros vecinos del nodo elegido el de menor valor de h(N)" [García, Episodio III, sec. Heuristic Depth-First Search]. Otras palabras: "Heuristic depth-first is a way to use heuristic knowledge in depth-first search. It retains the space advantages of depth-first search, while using problem-specific information to guide the search. The idea is to make the locally best choice according to the heuristic function by ordering the neighbors before adding them to the front of the frontier" [PMG, sec. 4.5, p. 134].
- **Diferencia clave con BestFS:** la elección es **local** y no global. BestFS considera toda la frontera; HDFS, en cambio, "locally chooses which subtree to develop. It chooses a neighbor of the current node to pursue, and it only considers other neighbors if all paths from the chosen node end without finding a solution" [PMG, sec. 4.5, p. 134].
- **Garantías:** no es **completa** ni **óptima**; puede ser "llevado por el camino del jardín": "it pursues all paths from that choice before trying another path. Thus, it can be 'led up the garden path.' If there is an infinite path from the first neighbor chosen, it would never choose the second neighbor. This may preclude finding a solution" [PMG, sec. 4.5, p. 134].
- **Complejidad espacial:** **lineal** en la profundidad (hereda la ventaja de memoria de DFS): "Esta estrategia tiene un mejor manejo de memoria que BestFS" [García, Episodio III, sec. Heuristic Depth-First Search].

### Ventajas y desventajas frente a DFS y BFS

| Propiedad | BFS | DFS | BestFS | HDFS |
|---|---|---|---|---|
| Completa (¿encuentra solución si existe?) | Sí (espacios finitos) | No (puede encerrarse en ciclos, punto 9-b de este TP) | No | No |
| Óptima | Sí (si los costos de arco son iguales) | No | No | No |
| Espacio | Exponencial O(b^d) | Lineal | Exponencial (peor caso) | Lineal |
| Información usada | Ninguna (ciega) | Ninguna (ciega) | Heurística (global: toda la frontera) | Heurística (local: vecinos del nodo expandido) |

Ningún método es *mejor* en abstracto; la tabla resume el compromiso (misma idea en [PMG, sec. 4.5, Fig. 4.6, p. 138]):

- **Frente a BFS:** BFS garantiza **completitud y optimalidad** (con costos de arco uniformes, punto 7 de este TP) a costa de memoria y tiempo exponenciales [RN10, sec. 3.4.1]. BestFS, con una buena heurística, suele alcanzar una meta explorando mucho menos espacio —"the amount of the reduction depends on the particular problem and on the quality of the heuristic" [RN10, sec. 3.5.1, p. 94]— pero **pierde garantías**: puede no encontrar solución, no encuentra necesariamente la óptima, y su frontera puede seguir creciendo exponencialmente. HDFS combina el guiado heurístico con el **uso lineal de memoria**, pero tampoco garantiza optimalidad ni completitud [PMG, sec. 4.5, pp. 133-135].

- **Frente a DFS:** DFS desciende a ciegas por la primera rama que encuentra; HDFS mantiene las propiedades de memoria y "profundidad" de DFS pero **orienta el descenso** hacia los vecinos más promisorios según h(N) [PMG, sec. 4.5, p. 134]. Comparten, sin embargo, las mismas debilidades: pueden no terminar (ramas infinitas o ciclos) y no garantizan la solución óptima; HDFS agrega el riesgo de que la heurística **engañe** a la búsqueda (como se expresó recién), llevándola por un subárbol promisorio pero sin salida [PMG, sec. 4.5, pp. 134-135].

- **Caso extremo:** con heurísticas perfectas, BestFS y HDFS van directo a una meta; sin heurística (h(N)=0 para todo N), HDFS **degenera en DFS** y BestFS en una elección casi aleatoria de la frontera ("with no heuristics they degenerate to depth-first search, random search (any node on the frontier could be chosen), …") [PMG, sec. 4.5, p. 138]. En síntesis, estas estrategias informadas intercambian **garantías formales** (de BFS) por **menor esfuerzo de exploración** cuando se dispone de un buen conocimiento heurístico del dominio.

## 15. Espacio de búsqueda donde BestFS y HDFS llegan a metas diferentes

La diferencia es que BestFS elige **globalmente** (mínimo h(N) de toda la frontera) mientras que HDFS elige **localmente** (mínimo h(N) entre los vecinos del nodo recién expandido) y se compromete con esa rama [PMG, sec. 4.5, p. 134] (la misma distinción está en [RN10, sec. 3.5.1, p. 93]). Basta un espacio donde, tras expandir un nodo, un nodo **viejo** de la frontera tenga menor h(N) que el mejor hijo:

```
                 A (h=2)
                /       \
           B (h=1)     C (h=2)
           /     \        \
      D (h=4)  E (h=3)   F (h=1)
       |         |         |
     D1 (h=3)  E1 (h=2)  G2 (meta)
       |         |
     D2 (h=2)  E2 (h=1)
       |         |
     D3 (h=1)  G1 (meta)
       |
     G3 (meta)
```

- Estado inicial **A**; metas **G1**, **G2** y **G3**; todos los arcos tienen costo 1.
- Los valores de h(N) son **admisibles** (incluso consistentes: h(N) ≤ 1 + h(N') en todo arco), de modo que la diferencia entre ambos métodos no se debe a una heurística mala, sino a las estrategias mismas. No hace falta control de visitados: el grafo es un árbol.

**Traza de BestFS** (frontera = cola con prioridad por h(N)):

| Paso | Nodo expandido | Frontera resultante (h) | ¿Meta? |
|---|---|---|---|
| 1 | A (h=2) | B (1), C (2) | No |
| 2 | B (h=1) — mínimo global | C (2), E (3), D (4) | No |
| 3 | **C (h=2)** — mínimo global | E (3), D (4), F (1) | No |
| 4 | F (h=1) | E (3), D (4), G2 (0) | No |
| 5 | G2 (h=0) | — | **Sí** |

- **Solución: A → C → F → G2**, costo **3**.

**Traza de HDFS** (pila; al expandir, los vecinos se ordenan por h(N) y se agregan al frente):

| Paso | Nodo expandido | Vecinos agregados (ordenados por h) | ¿Meta? |
|---|---|---|---|
| 1 | A (h=2) | B (1), C (2) | No |
| 2 | B (h=1) | E (3), D (4) | No |
| 3 | **E (h=3)** — mejor hijo de B | E1 (2) | No |
| 4 | E1 (h=2) | E2 (1) | No |
| 5 | E2 (h=1) | G1 (0) | No |
| 6 | G1 (h=0) | — | **Sí** |

- **Solución: A → B → E → E1 → E2 → G1**, costo **5**.

(En ambos casos el test de meta se aplica al **seleccionar** el nodo, como en `busqueda.pl` [García, Episodio III, sec. El mejor primero]. Si se aplicara al generarlo, las soluciones obtenidas son las mismas.)

**Conclusión:**

- Ambos llegan a **metas distintas**: BestFS a `G2`, HDFS a `G1`.
- El punto de divergencia es el paso 2→3: al expandir `B`, HDFS se compromete con `E` (h=3) aunque en la frontera sigue `C` (h=2), que **nunca vuelve a evaluar** porque su elección es local. BestFS, en cambio, reordena la frontera completa y salta a `C`.
- La rama `D → … → G3` no es explorada por ninguno de los dos: `D` tiene h=4, el peor valor de la frontera, así que nunca llega a ser seleccionado.
- BestFS encontró la solución óptima (costo 3) y HDFS una de costo 5, pero esto es **casual**: ninguno de los dos garantiza optimalidad ni completitud (punto 14).

## 16. Estrategia A* y condiciones para que halle la mejor solución

**Descripción.** A* es una estrategia de **búsqueda informada**: es idéntica a UCS (LCFS) salvo que, en lugar de ordenar la frontera por *g*(n), la ordena por la **función de evaluación** *f*(n) = *g*(n) + *h*(n), expandiendo siempre el nodo con menor *f* [RN10, sec. 3.5.2, p. 93]: "*f*(n) = estimated cost of the cheapest solution through *n*". Combina "*lowest-cost-first*" con "*best-first*" [García, Episodio III, sec. Método de búsqueda A*]; en el esquema de `busqueda.pl`, `seleccionar/3` toma el primero de la frontera y `agregar/3` ordena la frontera **completa** por *f*(n).

- Se expande en **orden no decreciente de *f*(n)** y no expande ningún nodo con *f*(n) > C\* (C\* = costo de la solución óptima).
- El **test de meta se aplica al seleccionar** el nodo, no al generarlo: en una meta *h* = 0, así que *f* = costo real de la solución.
- Al depender de *h*, hereda de BestFS la dependencia del conocimiento del dominio y la frontera potencialmente exponencial (puntos 14 y 19).

**Condiciones para que halle la mejor solución, y por qué cada una:**

- **(1) *h* es admisible:** *h*(n) nunca sobrestima el costo real de llegar de *n* a una meta, es decir, *h*(n) ≤ *h*\*(*n*), donde *h*\* es el costo del camino más barato real hasta una meta [RN10, sec. 3.5.2, p. 94]. Como *g*(n) es el costo real ya recorrido, se sigue que *f*(n) **nunca sobrestima** el costo de una solución que pasa por *n*: todo nodo del camino óptimo tiene *f*(n) ≤ C\*, mientras que una meta no óptima tiene *f* = su costo real > C\*. Por eso, mientras quede en la frontera un nodo del camino óptimo, A* no puede seleccionar la meta subóptima [RN10, sec. 3.5.2, pp. 94-95]. Es la condición suficiente para ***tree search***.
- **(2) *h* es consistente (o monótona):** *h*(n) ≤ *c*(n, a, n′) + *h*(n′) para todo sucesor *n′* [RN10, sec. 3.5.2, p. 95]. Implica que *f* es **no decreciente a lo largo de todo camino**: *f*(n′) = *g*(n) + *c*(n, a, n′) + *h*(n′) ≥ *g*(n) + *h*(n) = *f*(n). Gracias a eso, cuando A* selecciona un nodo *n*, **el camino óptimo hasta *n* ya fue encontrado** (si faltara un tramo, el nodo siguiente de ese camino tendría *f* menor y se habría seleccionado antes). Hace falta para ***graph search***, donde un mismo estado puede alcanzarse por caminos distintos y reinsertarse en la frontera al aparecer un camino más barato que el ya expandido [RN10, sec. 3.5.2, pp. 95-96]. Nótese que toda heurística consistente es admisible, por lo que (2) implica (1) [RN10, sec. 3.5.2, p. 95].
- **(3) Factor de ramificación finito y costos de arco acotados inferiormente** (∃ ε > 0 tal que todo costo de arco > ε) [García, Episodio III, sec. Admisibilidad del Algoritmo A*]. Es lo que garantiza la **completitud** (que A* halle una solución si existe, aun con espacio de estados infinito): de este modo hay solo **finitos nodos con *f*(n) ≤ C\***, así que la búsqueda necesariamente alcanza la frontera óptima; sin esta condición podría haber infinitos nodos por debajo de C\* y la búsqueda no terminaría [RN10, sec. 3.5.2, p. 97]. La misma formulación se encuentra en PMG: "*the branching factor is finite (each node has only a finite number of neighbors)*", "*arc costs are bounded above zero (there is some ε > 0 such that all of the arc costs are greater than ε)*" y "*h(n) is a lower bound on the actual minimum cost of the shortest path from n to a goal node*" [PMG, sec. 4.5, Prop. 4.1, pp. 136-137].

**Detalles de terminología y propiedades:**

- En las notas, **admisibilidad** es la propiedad del **algoritmo**: "Si la solución existe, y se cumplen las siguientes tres condiciones, la primera solución encontrada por A* será la óptima" [García, Episodio III, sec. Admisibilidad del Algoritmo A*]. No debe confundirse con ***h* admisible**, que es la condición (1) sobre la heurística [RN10, sec. 3.5.2, p. 94].
- **Poda:** al no expandir nodos con *f* > C\*, A* elimina ramas enteras; en la búsqueda de Bucarest con *h*<sub>SLD</sub>, Timisoara (*f* = 447) nunca se expande al ser C\* = 418 [RN10, sec. 3.5.2, pp. 97-98].
- **Eficiencia óptima:** entre los algoritmos que extienden caminos desde la raíz usando la misma heurística, "no other optimal algorithm is guaranteed to expand fewer nodes than A\*" [RN10, sec. 3.5.2, p. 98]. La misma idea se encuentra en PMG [PMG, sec. 4.5, pp. 135-136].
- Si *h* **no** es admisible, A* sigue siendo completo (bajo la condición (3)) pero puede devolver una solución **subóptima** (punto 18 de este TP).

## 17. A* con h(n) = 0 para todo nodo

**Resultado: A* se reduce a UCS (Lowest-Cost-First Search).**

- *f*(n) = *g*(n) + *h*(n) = *g*(n) + 0 = *g*(n). Ordenar la frontera por *f* es entonces **exactamente lo mismo** que ordenarla por *g*, que es la estrategia de UCS: "uniform-cost search expands the node *n* with the lowest path cost *g*(n)" [RN10, sec. 3.4.2, p. 84]. Es lo esperable, ya que A* está definido como una extensión de UCS: "The algorithm is identical to U NIFORM -C OST-S EARCH except that A∗ uses *g* + *h* instead of *g*" [RN10, sec. 3.5.2, p. 93].
- En la tabla resumen de estrategias, la fila de A* indica "Minimal *f*(n*) — *h*(*n*) + *g*(*n*)"; con *h* ≡ 0 esa fila se reduce a la de *Lowest-cost-first*, "Minimal *g*(*n*)" [PMG, sec. 4.5, Fig. 4.6, p. 138].
- **Qué se pierde y qué se conserva:**
  - Se conserva la **completitud y la optimalidad**: *h* ≡ 0 es admisible y consistente trivialmente (0 ≤ *c*(*n*, *n*′) + 0), y cumple la condición (3) del punto 16 [RN10, sec. 3.5.2, pp. 94-97].
  - Se pierde toda **guía heurística**: el método pasa a ser **ciego** (punto 6), porque ya no usa información del dominio; sólo se guía por el costo recorrido. Por eso las bandas de expansión se vuelven "circular" alrededor del estado inicial, en lugar de estirarse hacia la meta [RN10, sec. 3.5.2, p. 97].
  - El costo computacional es el de UCS: exponencial, O(*b*<sup>⌈1+C*/ε⌉</sup>), y la frontera puede seguir creciendo exponencialmente [RN10, sec. 3.4.2, pp. 84-85].
- **Contraste con el otro extremo:** si *h* fuera **perfecta** (*h*(*n*) = *h*\*(*n*), el costo real hasta la meta), entonces *f*(*n*) sería el costo real de la solución que pasa por *n* y A* iría **directo a la meta** sin ramificar [PMG, sec. 4.5, p. 138]. Entre ambos extremos, *h* = 0 es el caso degenerado: "*with no heuristics they degenerate to depth-first search, random search…, and lowest-cost-first search, respectively*" [PMG, sec. 4.5, p. 138].

---

**Fuentes consultadas:**

- **RN10:** Russell, S. y Norvig, P. *Artificial Intelligence: A Modern Approach*, 3ra ed., Pearson, 2010, capítulo 3 ("Solving Problems by Searching").
- **García:** García, A. J. *Inteligencia Artificial - Notas de Clase*, DCIC - Universidad Nacional del Sur: Episodio II: "Resolución automática de problemas utilizando búsqueda ciega", 08/09/2026; Episodio III: "Búsqueda informada", 10/09/2026.
- **PMG:** Poole, D.; Mackworth, A. y Goebel, R. *Computational Intelligence: A Logical Approach*, Oxford University Press, 1998, capítulo 4 ("Searching").