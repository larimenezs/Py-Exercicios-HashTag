#O objetivo é identificar quem são os clientes inadimplentes e enviar essa lista de clientes para o setor de cobrança. Sua função deve então receber uma lista de clientes, analisar quais clientes estão inadimplentes e retorná-los em uma lista (como cpf).

#A inadimplência nessa empresa é calculada da seguinte forma:
#Se o cliente estiver devendo mais de R$1000 por mais de 20 dias ele é inamdimplente, caso contrário não.


def clientes_inadimplentes(lista_devedores):
    lista_inadimplentes = []
    for cliente in lista_devedores:
        cpf, valor, dias = cliente
        if valor > 1000 and dias > 20:
            lista_inadimplentes.append(cpf)
    return lista_inadimplentes


lista_devedores = [
    ("123.456.789-00", 1500, 30),
    ("987.654.321-00", 500, 10),
    ("111.222.333-44", 1200, 25),
    ("555.666.777-88", 800, 40)
]


# Chamar a função e armazenar o resultado
inadimplentes = clientes_inadimplentes(lista_devedores)


print(inadimplentes)

