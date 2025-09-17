print("Seja bem vindo à Calculadora de despesas!")
name = input("Primeiro, como você se chama? ")

def welcome():
    print(f'Que ótimo que você está aqui conosco, {name}!')

def sum_expenses(expense_list):
    return sum(expense_list)

def average_expenses(expense_list):
    if len(expense_list) == 0:
        return 0
    return sum(expense_list) / len(expense_list)

def percentage_part(total, part):
    if total == 0:
        return 0
    return (part / total) * 100

def main():
    welcome()

    expenses = []

    while True:
        value = input("Digite o valor da sua despesa ('sair' para finalizar): ").lower()
        if value.lower() == 'sair':
            break
        try:
            expenses.append(float(value))
        except:
            print('Insira um número válido.')
    total = sum_expenses(expenses)
    media = average_expenses(expenses)

    print(f'\nTotal de despesas: R${total:.2f}')
    print(f'Média das despesas: R${media:.2f}')

    for i, value in enumerate(expenses):
        perc = percentage_part(total, value)
        print(f'Despesa {i+1}: R${value:.2f} -> {perc:.2f}% do total')

if __name__ == "__main__":
    main()