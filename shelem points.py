def names():
    print('''Please enter the names of the players as follows:
Team 1: player no. 1 & player no. 2
Team 2: player no. 3 & player no. 4''')
    player_names = [input(f'player no. {i + 1}: ') for i in range(4)]
    return player_names


names_list = names()
team1 = names_list[0].lower(), names_list[1].lower(), '1', 'one'
team2 = names_list[2].lower(), names_list[3].lower(), '2', 'two'


print(f'''Team 1: {team1[:2]}
Team 2: {team2[:2]}''')


def goal_point():
    print("Goal of the game")
    while True:
        try:
            points = int(input('please enter maximum game points? (1200 is recommended)\n>>> '))
            if points % 5:
                print('It should be multiples of 5!')
            elif points < 330:
                print('It is too low for the Goal of the game! (330 at least)')
            else:
                break
        except ValueError:
            print('It should be a number!')
    return points


goal = goal_point()
print(f'The first team to reach {goal} wins.')


def declarer_bid():
    while True:
        declarer = input('Who is declarer? (please type declarer name or his/her team number)\n>>> ')
        if declarer.lower() in team2 or declarer.lower() in team1:
            break
        else:
            print(f'I don\'t know "{declarer}"!')
            pass
    while True:
        try:
            bid = int(input('the bid is '))
            if bid % 5 or bid <= 100 or bid > 165:
                print('bid is not acceptable')
            else:
                break
        except ValueError:
            print('bid should be a number!')
    return declarer.lower(), bid


def game():
    team1_points = 0
    team2_points = 0
    print('let\'s start the game!')
    n = 1
    while True:
        if team2_points < goal and team1_points < goal:
            print(f'game {n}')
            hakem, hokm = declarer_bid()
            while True:
                try:
                    hammal_point = int(input('The other team (not declarer) points: '))
                    if hammal_point % 5 or hammal_point < 0 or hammal_point > 165:
                        print('this score is not acceptable')
                    else:
                        break
                except ValueError:
                    print('It should be a number!')
            hakem_point = 0
            if hammal_point == 0:
                hakem_point = 2 * hokm
            elif hammal_point <= (165 - hokm):
                hakem_point = hokm
            elif hammal_point < 85:
                hakem_point = -hokm
            elif hammal_point >= 85:
                hakem_point = -2 * hokm

            if hakem in team1:
                team1_points += hakem_point
                team2_points += hammal_point
            elif hakem in team2:
                team2_points += hakem_point
                team1_points += hammal_point
            print(f'''Team 1 {team1[:2]} score = {team1_points}
Team 2 {team2[:2]} score = {team2_points}''')
            n += 1
        else:
            winner = team1 if team1_points > team2_points else team2
            print(f'{winner[0]} & {winner[1]} won the game!')
            break


game()
