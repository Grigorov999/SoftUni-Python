tournament_days = int(input())

money = 0
daily_money = 0
total_money = 0
final_money = 0
win_count = 0
lose_count = 0
win_rate = 0
lose_rate = 0


for i in range(1, tournament_days+1):
    while i in range(tournament_days):
        sport = input()
        result = input()
        if result == 'win':
            money += 20
            win_count += 1
        elif result == 'lose':
            money += 0
            lose_count += 1

        money += money
        win_rate += win_count
        lose_rate += lose_count

        if win_rate > lose_rate:
            daily_money = money + ( money * 0.1)
        else:
            daily_money = money

        total_money += daily_money
        if sport == 'Finish':
            break

    sport = input()

if win_rate > lose_rate:
    final_money = total_money + (total_money * 0.2)
    print(f'You won the tournament! Total raised money: {final_money:.2f}')
elif win_count < lose_count:
    print(f'You lost the tournament! Total raised money: {total_money}')
