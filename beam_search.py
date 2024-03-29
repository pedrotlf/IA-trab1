import aux_problema_mochila as mochila
import functools
from time import time


def beam_search(m, s, pes, val, pes_max):
    inicio = time()

    expansao = mochila.vizinhos_mais_proximos(s, pes, pes_max)
    fila = []

    while expansao and time() - inicio < 120:
        fila = list(expansao)
        fila = sorted(fila, key=functools.partial(mochila.valor_total, val=val), reverse=True)
        fila = fila[:m]
        expansao = mochila.expandir_estados(fila, pes, pes_max)

    return fila[0]


# v_pesos = [3, 2, 2, 4]
# v_valores = [4, 3, 3, 5]
# ss = beam_search(30, mochila.estado_inicial_aleatorio(v_pesos, 25), v_pesos, v_valores, 25)
# valor = mochila.valor_total(ss, v_valores)
# peso = mochila.peso_total(ss, v_pesos)
# print(ss, peso, valor)
