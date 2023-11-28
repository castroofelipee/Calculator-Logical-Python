class Despesa:
    def __init__(self, categoria, valor):
        self.categoria = categoria
        self.valor = valor

class CalculadoraDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, categoria, valor):
        despesa = Despesa(categoria, valor)
        self.despesas.append(despesa)
        print(f'Despesa de {categoria} no valor de R${valor:.2f} adicionada com sucesso.')

    def calcular_total(self):
        total = sum(despesa.valor for despesa in self.despesas)
        print(f'Total de despesas: R${total:.2f}')

    def exibir_despesas(self):
        print("Lista de despesas:")
        for despesa in self.despesas:
            print(f'{despesa.categoria}: R${despesa.valor:.2f}')



calculadora = CalculadoraDespesas()

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar despesa")
    print("2 - Calcular total de despesas")
    print("3 - Exibir despesas")
    print("0 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        categoria = input("Digite a categoria da despesa: ")
        valor = float(input("Digite o valor da despesa: "))
        calculadora.adicionar_despesa(categoria, valor)

    elif opcao == "2":
        calculadora.calcular_total()

    elif opcao == "3":
        calculadora.exibir_despesas()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
