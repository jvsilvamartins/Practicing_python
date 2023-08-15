import random

print(">>>>>>>>>> CALCULADORA FINANCEIRA <<<<<<<<<<")


def executar():
    while True:
        try:
            salario_input = float(input("Favor informe seu salário : R$ "))
            print("Digite a palavra 'FIM' para FINALIZAR O PROGRAMA")
            break
        except:
            print('Favor digitar apenas números inteiros e/ou reais')
            try:
                salario_input = float(input("Favor informe seu salário : R$ "))
                print("Digite a palavra 'FIM' para FINALIZAR O PROGRAMA")
            except:
                print("O valor informado do salário é invalido, portando ele será igual a R$0,00")
                salario_input = 0.00
                break


    gastos = []
    somatoria_gastos = 0

    while True:
        descricao_gastos = input("Descreva o no nome do seu gasto : (Ex.: aluguel, compras) - ")
        descricao_gastos = descricao_gastos.upper()
        if descricao_gastos == 'FIM' or descricao_gastos == '':
            break
        valor_gastos = float(input(f"Digite o valor referente ao gasto {descricao_gastos} - R$ "))
        gastos += descricao_gastos, valor_gastos
        somatoria_gastos += valor_gastos
        print("\n")
        for i in range(0, len(gastos), 2) :
            print(f' ● {gastos[i]} - R${gastos[i + 1]}')
        print("\n")

    resultado_final = (salario_input - somatoria_gastos)

    print("Segue seus gastos informados: ")
    print("\n")
    for j in range(0, len(gastos), 2) :
        print(f' ● {gastos[j]} - R${gastos[j + 1]}')
    print("\n")
    try:
        print(f'O total dos seus gastos são R${somatoria_gastos}')
        print(f"Você terá R${resultado_final} após seus gastos.")
    except:
        print("PROGRAMA FINALIZADO")

executar()