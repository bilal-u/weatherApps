from mysql.connector import connect

host = 'localhost'
user = 'root'
password = 'password'


def get_rows(query):
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            mysql_cursor.execute(query)
            column_names = mysql_cursor.column_names
            rows = mysql_cursor.fetchall()
            return column_names, rows


def get_player_info(player_id):
    """
    returns player name and age as a tuple for any given player_id
    :param player_id: id of the player
    :return: (name, age)
    """
    # Use the get_rows() function
    query = f"SELECT * FROM fantastic_games.players WHERE player_id = {player_id}"
    col_names, rows = get_rows(query)
    # print(rows)
    # print(rows[0])
    name = rows[0][1]
    age = rows[0][2]
    return name, age


def get_game_info(game_id):
    q2 = f'SElECT game_name, price, year FROM fantastic_games.game WHERE game_id = {game_id}'
    info = get_rows(q2)[1]
    name, price, year = info[0]
    return name, price, year


def add_new_player(player_name: str, player_age: int):
    """
    Adds a new row in the players table
    """
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Create a query and execute
            add_player_sql = f"INSERT INTO fantastic_games.players (player_name, player_age) VALUES ('{player_name}', {player_age})"
            mysql_cursor.execute(add_player_sql)
            # Step 4: Commit changes
            mysql_connection_object.commit()


if __name__ == '__main__':
    # add_new_player('Matt', 20)
    pass