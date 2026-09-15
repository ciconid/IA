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

---

**Fuentes consultadas:**

- **RN10:** Russell, S. y Norvig, P. *Artificial Intelligence: A Modern Approach*, 3ra ed., Pearson, 2010, capítulo 3 ("Solving Problems by Searching").
- **García:** García, A. J. *Inteligencia Artificial - Notas de Clase*, Episodio II: "Resolución automática de problemas utilizando búsqueda ciega y búsqueda informada", DCIC - Universidad Nacional del Sur, 08/09/2026.