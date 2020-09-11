number_of_transactions = int(input())

counter = 0
acc_balance = 0
while counter < number_of_transactions:
    transaction_value = float(input())
    if transaction_value < 0:
        print('Invalid operation!')
        break

    acc_balance += transaction_value
    counter += 1
    print(f'Increase: {transaction_value:.2f}')

print(f'Total: {acc_balance:.2f}')
