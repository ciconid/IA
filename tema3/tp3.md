# Trabajo Práctico 3

## 1. Importancia de los métodos de búsqueda para el desarrollo de agentes inteligentes

La resolución automática de problemas mediante búsqueda es central en IA [García, Episodio II]: el capítulo 3 de *Artificial Intelligence: A Modern Approach* se abre señalando que permite encontrar "una secuencia de acciones que alcanza sus metas cuando ninguna acción individual es suficiente" [RN10, cap. 3, p. 64]. Por ello, la búsqueda es de gran interés para el desarrollo de agentes inteligentes, ya que:

- **Satisface la racionalidad:** los agentes buscan maximizar su *performance measure* [RN10, sec. 3.1, p. 64]; la búsqueda traduce ese criterio en acciones: encuentra la secuencia que lleva del estado inicial a uno meta y, con la estrategia adecuada, la de menor costo (óptima) [RN10, sec. 3.1.1, p. 68].

- **Las metas organizan el comportamiento:** "las metas ayudan a organizar el comportamiento limitando los objetivos que el agente intenta alcanzar y, por lo tanto, las acciones que necesita considerar" [RN10, sec. 3.1, p. 65]. La búsqueda convierte el objetivo en un plan concreto, integrada en el ciclo *formular objetivo → formular problema → buscar → ejecutar* [RN10, sec. 3.1, Fig. 3.1, p. 66].

- **Supera a los agentes reactivos:** el mapeo directo estado→acción "sería demasiado grande para almacenar y tomaría demasiado tiempo de aprender" [RN10, p. 64]. La búsqueda da **deliberación**: permite anticiparse y resolver problemas no previstos en el diseño, examinando "las acciones futuras que conducen a estados de valor conocido" [RN10, sec. 3.1, p. 65].

- **Es general e independiente del dominio:** "para una gran variedad de situaciones, la resolución de un problema se puede transformar en la tarea de encontrar un camino en un grafo", permitiendo "un método de resolución genérico e independiente del dominio" [García, Episodio II]. Los mismos algoritmos (BFS, DFS, UCS, A*, etc.) se aplican a laberintos, rutas, juegos, planificación, logística o robótica [RN10, sec. 3.2, p. 69].

- **Ofrece garantías formales:** según la estrategia, se garantiza **completitud** (si existe solución, se encuentra) y **optimalidad** (la solución es la de menor costo) [RN10, sec. 3.7, p. 108], a diferencia de un agente que simplemente adivina.

- **Explota la abstracción:** el agente busca sobre un modelo abstraído del mundo (formulación del problema); "si no fuera por la capacidad de construir abstracciones útiles, los agentes inteligentes se verían completamente desbordados por el mundo real" [RN10, sec. 3.1.2, pp. 68-69].

- **Admite conocimiento del dominio:** las estrategias informadas (A*) orientan la exploración hacia estados promisorios, reduciendo el esfuerzo computacional sin perder optimalidad (con heurística admisible).

- **Sustenta otras capacidades de la IA:** juegos (cap. 5), satisfacción de restricciones (cap. 6), planificación (cap. 10) y robótica (cap. 25) se construyen sobre estos métodos [RN10].

En síntesis, la búsqueda es cómo el agente "piensa" para pasar de su estado actual a la meta: sin ella depende de respuestas programadas; con ella resuelve problemas nuevos de forma autónoma y con garantías.

---

**Fuentes consultadas:**

- **RN10:** Russell, S. y Norvig, P. *Artificial Intelligence: A Modern Approach*, 3ra ed., Pearson, 2010, capítulo 3 ("Solving Problems by Searching").
- **García:** García, A. J. *Inteligencia Artificial - Notas de Clase*, Episodio II: "Resolución automática de problemas utilizando búsqueda ciega y búsqueda informada", DCIC - Universidad Nacional del Sur, 08/09/2026.