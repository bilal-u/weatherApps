from controller import *


def display_options():
    print('1. Get Player Info By PlayerID')
    print('2. Display All Players')
    print('3. Get Game Info')
    print('4. Display All Games')
    print('5. Add NEW PLAYER')
    print('6. Add NEW GAME!')
    print('7. DELETE A PLAYER!')
    print('8. UPDATE A PLAYER\'S AGE!')
    print('0. Exit')


def main():
    while True:
        display_options()
        choice = int(input('Enter Choice: '))
        if choice == 1:
            player_id = int(input('Enter Player ID: '))
            player_name, player_age = get_player_info(player_id)
            print(f'Player Name = {player_name}\tPlayer Age: {player_age}')
        elif choice == 2:
            query_all_players = 'SELECT * FROM fantastic_games.players'
            col_names, rows = get_rows(query_all_players)
            print(col_names)
            for row in rows:
                print(row)
        elif choice == 3:
            game_id = int(input('Enter Game ID: '))
            game_name, price, year = get_game_info(game_id)
            print(f'Game Name = {game_name}\tGame Price = {price}\t Release Year ={year} ')
        elif choice == 4:
            query_all_games = 'SELECT * FROM fantastic_games.game'
            col_names, rows = get_rows(query_all_games)
            print(col_names)
            for row in rows:
                print(f'{row[0]}\t{row[1]}\t{float(row[2])}\t{row[3]}\t')
        elif choice == 5:
            name = input('Enter Player Name: ')
            age = int(input('Enter Player Age: '))
            add_new_player(name, age)
        elif choice == 6:
            game_name = input('Enter Game Name: ')
            price = float(input('Enter Game Price: '))
            year = int(input('Enter Game Release Year: '))
            add_new_game(game_name,price,year)
        elif choice == 7:
            '''
            delete player name by player_id
            '''
            player_id = int(input('Enter Player ID to be deleted: '))
            delete_player(player_id)
        elif choice == 8:
            '''
            update plaers age in the player table 
            '''
            player_age = int(input('Enter Player Correct Age: '))
            player_id = int(input('Enter Player ID: '))
            update_player_age(player_age,player_id)

        input('Hit enter to continue\t')


if __name__ == "__main__":
    main()