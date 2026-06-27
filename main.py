valor = int(input('Qual valor você quer sacar? R$ '))

cedulas = [50, 20, 10, 1]
restante = valor

for cedula in cedulas:
    qtd = restante // cedula
    restante %= cedula

    if qtd > 0:
        print(f'{qtd} cédula(s) de R$ {cedula}')

print('Saque finalizado!')
