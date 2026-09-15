:- encoding(utf8). %Determina el set de caracteres (para imprimir tildes).


%   Esquema del laberinto
%   ---------------------------------------------------------
%
%           C   I   J
%           A
%           B   D
%   H   G   E
%           F

%   ---------------------------------------------------------
%   ady(?CasillaX, ?CasillaY, ?Costo).
%   ---------------------------------------------------------
%   Determina la adyacencia entre dos casillas del laberinto,
%   y el Costo que implica pasar de CasillaX a CasillaY.
%
%   IMPORTANTE: El orden en el que son definidas las relaciones
%   de adyacencia no es aleatorio.
%   ¿Cuál le parece que es la razón?
%   ---------------------------------------------------------
ady('A','B', 1). ady('A','C', 1).
ady('B','E', 1). ady('B','D', 1). ady('B','A', 1). % ¿Qué pasa si intercambiamos de posición
ady('C','I', 1). ady('C','A', 1).				   % ady('B','E', 1) y ady('B','D', 1)?
ady('D','B', 1).
ady('E','G', 1). ady('E','F', 1). ady('E','B', 1).
ady('F','E', 1).
ady('G','H', 1).
ady('I','J', 1).


%   ---------------------------------------------------------
%   operador(?Op, +EstadoActual, -EstadoSiguiente, -Costo).
%   ---------------------------------------------------------
%   Relaciona un nodo del laberinto con sus nodos adyacentes
%
%   ---------------------------------------------------------
operador(moverse_a(CasillaY), EstadoActual, EstadoSiguiente, Costo):-
    EstadoActual = estado(CasillaX),
    ady(CasillaX,CasillaY,Costo),
    EstadoSiguiente = estado(CasillaY).


%   ---------------------------------------------------------
%   seleccionar(+Frontera, -Nodo, -FronteraSinNodo).
%   ---------------------------------------------------------
%   Estado es uno de los nodos de la lista Frontera.
%   FronteraSinNodo es la lista resultante de remover Nodo
%   de Frontera.
%
%   IMPORTANTE: La forma en la que es manipulada la frontera
%   a la hora de seleccionar y/o agregar estados determina la
%   estrategia de búsqueda
%   ---------------------------------------------------------
seleccionar([Nodo|FronteraSinNodo],Nodo,FronteraSinNodo).


%   ---------------------------------------------------------
%   vecinos(+Nodo, -Vecinos).
%   ---------------------------------------------------------
%   Vecinos son todos los nodos del árbol de búsqueda que
%   representan estados que son alcanzables desde el estado de
%   Nodo a partir de la aplicación un solo operador.
%   ---------------------------------------------------------
generarVecinos(Nodo,Vecinos):-
    Nodo = [Estado,CostoCamino,Camino],
    findall([EstadoSiguiente,NuevoCostoCamino,[E|Camino]],(
        operador(_Op,Estado,EstadoSiguiente,CostoOperador),
        EstadoSiguiente = estado(E),
        NuevoCostoCamino is CostoOperador+CostoCamino
    ),Vecinos).


%   ---------------------------------------------------------
%   agregar(+Vecinos, +Frontera, -FronteraNueva).
%   ---------------------------------------------------------
%   FronteraNueva es una lista generada a partir de agregar
%   los estados en la lista Vecinos a la lista Frontera.
%
%   IMPORTANTE: La forma en la que es manipulada la frontera
%   a la hora de seleccionar y/o agregar estados determina la
%   estrategia de búsqueda
%   ---------------------------------------------------------
agregar(Vecinos,Frontera,FronteraNueva):-
    append(Vecinos, Frontera, FronteraNueva).

%   ---------------------------------------------------------
%   esMeta(Estado).
%   ---------------------------------------------------------
%   Determina si un estado es un estado-meta.
%   ---------------------------------------------------------
esMeta(estado('H')).
esMeta(estado('J')).

%   ---------------------------------------------------------
%   buscarEn(+Frontera, -Solucion).
%   ---------------------------------------------------------
%   Aplica una estrategia de búsqueda a partir de los estados
%   que aparecen en la lista Frontera hasta encontrar un
%   estado-meta. Luego instancia Solución con la secuencia de
%   estados que se corresponden con la solución encontrada.
%   ---------------------------------------------------------
buscarEn(Frontera,Solucion):-
    seleccionar(Frontera,Nodo, _FronteraSinNodo),
    Nodo = [Estado,_Costo,Camino],
    esMeta(Estado),!,
    imprimirSeleccion(Frontera,Nodo,si),    
    reverse(Camino,Solucion). %Veniamos apilando los estado, hay que invertir la lista.

buscarEn(Frontera,Solucion):-
    seleccionar(Frontera,Nodo,FronteraSinNodo),
    imprimirSeleccion(Frontera,Nodo,no),
    generarVecinos(Nodo,Vecinos),
    agregar(Vecinos,FronteraSinNodo,NuevaFrontera),
    buscarEn(NuevaFrontera,Solucion).


%   ---------------------------------------------------------
%   iniciar.
%   ---------------------------------------------------------
%   Da arranque a la ejecución del método de búsqueda fijando
%   un estado inicial.
%   ---------------------------------------------------------
iniciar:-
    %La búsqueda empieza en el nodo A, con costo 0 y camino [].
    EstadoInicial = 'A',   
    NodoInicial = [estado(EstadoInicial),0,[EstadoInicial]],
    buscarEn([NodoInicial],Solucion),!,
    write("La solución es: "), write(Solucion), nl.

iniciar:-
    write("No hay solución."), nl, fail.


%   ---------------------------------------------------------
%   imprimirSeleccion(+Frontera,+Nodo,+EsMeta)
%   ---------------------------------------------------------
%   Imprime carteles indicando cuál es la frontera actual,
%   cuál fue el nodo seleccionado, y si este contiene (o no)
%   un estado-meta.
%   ---------------------------------------------------------
imprimirSeleccion(Frontera,Nodo,si):-
    !,write("Frontera:"),nl,
    write(Frontera),nl,
    write("-------------------------------"), nl,
    write("Seleccionado: "), write(Nodo), write(" ...es meta!"),nl,
    write("-------------------------------"), nl,nl,nl.

imprimirSeleccion(Frontera,Nodo,no):-
    write("Frontera:"),nl,
    write(Frontera),nl,
    write("-------------------------------"), nl,
    write("Seleccionado: "), write(Nodo), write(" ...no es meta, hay que seguir buscando!"),nl,
    write("-------------------------------"), nl,nl,nl.