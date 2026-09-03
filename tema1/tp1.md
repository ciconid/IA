# TP1

## 1
### Consulta al chatbot (LLM)

**Pregunta: ¿Qué es la inteligencia humana?**
La inteligencia humana es la capacidad cognitiva de comprender, razonar, aprender, adaptarse al entorno y resolver problemas. Incluye aspectos como razonamiento lógico y pensamiento abstracto, creatividad e imaginación, aprendizaje a partir de la experiencia, comprensión del lenguaje, inteligencia emocional y social, y adaptación a nuevas situaciones. Es un concepto amplio y multidimensional, estudiado desde la psicología, la neurociencia y la filosofía.

**Pregunta: ¿Qué es la inteligencia artificial?**
La inteligencia artificial (IA) es el campo de la computación que busca crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, como el aprendizaje a partir de datos, el razonamiento y la resolución de problemas, la percepción (visión, reconocimiento de voz), la comprensión del lenguaje natural y la toma de decisiones. Incluye subcampos como el aprendizaje automático (ML), las redes neuronales, el procesamiento de lenguaje natural (NLP) y la visión por computadora.

### Análisis de coincidencias y diferencias con lo desarrollado en clase

**Coincidencias:**
- Ambas definiciones coinciden en que la IA se ocupa de tareas que asociamos con la inteligencia humana: aprender, razonar, resolver problemas, percibir y comprender el lenguaje. Esto es consistente con la clase, donde la IA se presenta como "la Ciencia e Ingeniería de construir artefactos inteligentes, en especial programas inteligentes de computadora" (J. McCarthy) y centrada en el "comportamiento inteligente de entidades artificiales".
- En inteligencia humana, tanto el chatbot como la clase (notas de García) listan capacidades similares: resolución de problemas, conocimiento, lógica, aprendizaje, razonamiento, planificación y habilidades sociales.

**Diferencias:**
- La definición del chatbot es "operativa" y orientada a la tecnología (ML, redes neuronales, NLP). Asocia IA casi exclusivamente con el paradigma conexionista/aprendizaje automático, que es la visión más popularizada hoy.
- La definición de clase es más amplia y conceptual: introduce la IA como disciplina que estudia el comportamiento inteligente de entidades artificiales, y enmarca su núcleo en el concepto de agente — "una entidad computacional autónoma que percibe su entorno a través de sensores y actúa en él mediante efectores". También menciona expresamente que la IA "se relaciona con el uso de computadoras para entender la inteligencia humana", cosa que la definición del chatbot omite.
- El chatbot no menciona el ciclo percibir–actuar ni la autonomía del agente; presenta la IA como "campo de la computación con subcampos", sin un marco unificador.

**Reflexión sobre por qué ocurre la diferencia:**
La diferencia se debe principalmente a que la definición que circula públicamente (y que reflejan los chatbots, entrenados con contenido masivo de internet y marketing tecnológico) es la de la IA sub-simbólica / aprendizaje automático actual, dominada por las redes neuronales y la IA generativa. En cambio, el enfoque de la materia es el clásico de la IA como ciencia del comportamiento inteligente de agentes, que incluye también la representación de conocimiento, el razonamiento automático, la planificación y los sistemas multiagente (áreas presentes en el mapa de la clase y que el chatbot ignora). La definición popular es, entonces, una visión parcial producto del éxito reciente del aprendizaje profundo.

### Interpelación al chatbot con la definición dada en clase

**Interpelación:** "En mi clase de IA se define al agente como una entidad computacional autónoma que percibe su entorno a través de sensores y actúa en él mediante efectores, y a la IA como la ciencia e ingeniería de construir artefactos inteligentes, orientada también a entender la inteligencia humana. ¿Qué opinás? ¿Coincide con tu definición?"

**Respuesta (simulada/análisis) del LLM:** El chatbot suele reconocer que su definición es correcta pero incompleta: admite que la IA es más que aprendizaje automático, acepta el concepto de agente (perceptores/actuadores) y reconoce que su respuesta previa reflejaba el enfoque tecnológico actual. Sin embargo, tiende a justificar la omisión por "popularidad del término". Esto muestra la confusión actual: el uso mediático y comercial del término "IA" ha quedado asociado casi en exclusiva a los modelos generativos, desplazando la acepción académica original de agente inteligente que percibe y actúa.

### Reflexión sobre la confusión actual en torno al tema

Hoy existe una gran confusión porque el término "inteligencia artificial" se usa con significados distintos según el contexto:
- En el ámbito académico/clásico, IA es la ciencia del comportamiento inteligente de agentes (percibir, razonar, actuar), independiente del paradigma técnico.
- En el ámbito popular/tecnológico, por "IA" se entiende casi siempre el aprendizaje automático y los LLMs (ChatGPT y similares).

Esta ambigüedad alimenta expectativas exageradas, temores y malentendidos (por ejemplo, llamar "inteligente" a un chatbot que solo predice la siguiente palabra, o confundir la automatización estadística con comprensión genuina). La clase insiste en la responsabilidad del profesional en computación de "llevar luz donde hay oscuridad y conocimiento donde hay desinformación", justamente para aclarar esta confusión.

## 2
Según lo desarrollado en clase, un **agente** es una entidad computacional (programa o robot) **autónoma**, que puede **percibir su entorno** a través de **sensores** y **actuar en ese entorno** utilizando **efectores** (o actuadores/efectores). El término proviene del latín *agere* ("hacer"), es decir, algo "que obra o tiene capacidad de obrar".

La relación del agente con su entorno se da mediante un **ciclo continuo de percepción-acción**:
1. El agente **percibe** el estado del entorno a través de sus sensores.
2. Usando la información disponible, debe **decidir qué acción realizar** (toma de decisiones).
3. **Actúa** sobre el entorno mediante sus efectores.
4. Al actuar, produce **cambios en el entorno**; luego volverá a percibir esos cambios en un nuevo ciclo, y así durante todo su tiempo de vida.

Puntos importantes sobre esa relación:
- El agente no existe aislado: su comportamiento depende de la información que recibe del entorno y de los efectos que sus acciones producen sobre él.
- Si el entorno **no es completamente acotado**, la **percepción será parcial** y la **influencia del agente sobre el entorno también será parcial**; por más complejo que sea el agente, no podrá conocerlo ni controlarlo por completo.
- La **misma acción ejecutada dos veces puede tener efectos diferentes**, por lo que el agente debe estar preparado para que una acción falle o que sus efectos no sean los previstos.

## 3
Según lo consultado al LLM, un **agente de IA** es un sistema que recibe un objetivo y puede decidir qué acciones realizar para conseguirlo.

A diferencia de un chatbot que simplemente responde:

`LLM → pregunta → respuesta`

un agente puede hacer:

`Objetivo → analizar → decidir acción → usar herramientas → evaluar resultado → repetir → resultado`

Por ejemplo, "organizame un viaje" podría implicar buscar vuelos, comparar precios, buscar hoteles y armar un itinerario de forma autónoma.

### Contraste con la definición del punto 2 (clase)
La definición de clase describe al agente como una entidad computacional **autónoma** que **percibe su entorno** a través de sensores y **actúa** sobre él mediante efectores, en un ciclo continuo de percepción-acción. La respuesta del chatbot coincide en lo esencial: ambos plantean un agente que **recibe información del entorno (objetivo/estado)**, **decide una acción** en base a ella y **actúa**, repitiendo el ciclo hasta lograr un resultado. La definición del chatbot está más orientada a **agentes que usan herramientas** (buscar vuelos, comparar precios) y a la autonomía para alcanzar una meta, en línea con los agentes con metas/deliberativos de la clase.

### ¿ChatGPT es un agente?
Según la definición propia, ChatGPT **por sí solo no es un agente**: responde de forma directa a una pregunta (LLM → pregunta → respuesta), sin percibir un entorno dinámico, sin decidir secuencias de acciones y sin usar herramientas ni evaluar resultados. Sin embargo, **puede comportarse como parte de un agente** cuando se lo combina con un bucle que le da un objetivo, acceso a herramientas y capacidad de evaluar resultados (por ejemplo, un agente que usa un LLM como "cerebro" para organizar un viaje). La autonomía y el ciclo análisis-acción-evaluación son lo que distingue al agente del simple chatbot.

## 4
Esquema en Prolog de un agente reactivo que modela una puerta automática, siguiendo el patrón de los ejemplos de clase (bucle del agente → percibir → actuar → reglas condición-acción):

```prolog
% --- Agente reactivo: puerta automática ---

% Bucle principal del agente
puerta :- \+ fin,
          percibir(Entorno),
          actuar(Entorno),
          puerta.

% Percepción: se consulta el sensor de movimiento y el estado de la puerta
percibir(P) :- sensor_movimiento(Mov),
               estado_puerta(Estado),
               P = [mov(Mov), estado(Estado)].

% Acción: se decide qué hacer según lo percibido
actuar(P)    :- member(mov(Mov), P),
                member(estado(Estado), P),
                decidir(Estado, Mov).

% Reglas condición-acción
% Si la puerta está cerrada y hay movimiento, se abre
decidir(cerrada, si) :- abrir_puerta,
                        set_estado(abierta).
% Si la puerta está abierta y ya no hay movimiento, se cierra
decidir(abierta, no)  :- cerrar_puerta,
                        set_estado(cerrada).
% En cualquier otro caso no se hace nada
decidir(_, _).
```

Descripción del comportamiento:
- **puerta** es el ciclo del agente: mientras no haya fin, percibe, actúa y repite.
- **percibir/1** consulta los sensores (si hay movimiento y el estado actual de la puerta).
- **actuar/1** aplica una regla condición-acción según lo percibido.
- Si la puerta está **cerrada** y hay **movimiento**, se **abre** (y pasa a estado `abierta`).
- Si la puerta está **abierta** y ya **no hay movimiento**, se **cierra** (y pasa a estado `cerrada`).
- En cualquier otro caso no hace nada.

## 5
Programa Prolog del agente de seguridad de la galería de arte:

```prolog
llamar_bomberos :- fuego.
fuego :- humo.
fuego :- alarma_incendio_activada.
fuego :- calor_intenso, noche.
llamar_policia :- llamar_bomberos.
llamar_policia :- ladrones.
ladrones :- movimiento, cerrado.
movimiento :- sensor_mov_sala1.
movimiento :- sensor_mov_sala2.
cerrado :- lunes.
```

Para cada escenario, la respuesta que genera el intérprete es:

| Escenario (Hechos)                     | Consulta            | Respuesta |
|----------------------------------------|---------------------|-----------|
| `alarma_incendio_activada.`            | `?- fuego.`         | **true**  |
| `alarma_incendio_activada.`            | `?- llamar_bomberos.` | **true**  |
| `calor_intenso.`                       | `?- llamar_bomberos.` | **false** |
| `sensor_mov_sala2.`                    | `?- ladrones.`      | **false** |
| `sensor_mov_sala2.`  `cerrado.`        | `?- ladrones.`      | **true**  |
| `sensor_mov_sala1.`  `lunes.`          | `?- llamar_policia.` | **true**  |

Justificación:

1. `alarma_incendio_activada.` → `?- fuego.` → **true**: `fuego :- alarma_incendio_activada.`, y el hecho está presente.
2. `alarma_incendio_activada.` → `?- llamar_bomberos.` → **true**: `llamar_bomberos :- fuego.` y `fuego` se deriva de `alarma_incendio_activada`.
3. `calor_intenso.` → `?- llamar_bomberos.` → **false**: para derivar `fuego` por calor se necesita `calor_intenso, noche`, pero `noche` no puede probarse (no hay hecho ni regla), por lo que `fuego` cae y `llamar_bomberos` también.
4. `sensor_mov_sala2.` → `?- ladrones.` → **false**: `ladrones :- movimiento, cerrado.`; `movimiento` se deriva de `sensor_mov_sala2`, pero `cerrado` falla (no hay hecho `cerrado` ni `lunes`).
5. `sensor_mov_sala2. cerrado.` → `?- ladrones.` → **true**: `movimiento` (por `sensor_mov_sala2`) y `cerrado` son ambos verdaderos.
6. `sensor_mov_sala1. lunes.` → `?- llamar_policia.` → **true**: por `llamar_policia :- ladrones.`, con `movimiento` (por `sensor_mov_sala1`) y `cerrado :- lunes.` verdaderos.

