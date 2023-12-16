def read_game_iteration(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # If the file is not found, create it with gameiter=0
        with open(file_path, 'w') as file:
            file.write('gameiter=0\n')
        return 0, []

    game_iterations = []
    current_game_iteration = None

    for line in lines:
        if line.startswith('gameiter='):
            current_game_iteration = int(line.split('=')[1].strip())
            game_iterations.append(current_game_iteration)

    if current_game_iteration is None:
        # If 'gameiter=' is not found in the file, add it with a starting value of zero
        lines.insert(0, 'gameiter=0\n')
        game_iterations.append(0)

    return game_iterations[-1], lines

def write_data_with_iteration(file_path, data, game_iteration):
    with open(file_path, 'a') as file:
        file.write(f'\ngameiter={game_iteration + 1}\n')
        for line in data:
            file.write(line)
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.score = 0

    def play_round(self, card1, card2):
        damage1 = self.calculate_damage(card1, card2)
        damage2 = self.calculate_damage(card2, card1)

        if damage1 > damage2:
            self.score += 1

    def calculate_damage(self, card1, card2):
        return card1-card2
    def emotional_damage(self,dam):
        self.health-=dam

def main():
    input_file_paths = ['input1.txt', 'input2.txt', 'input3.txt', 'input4.txt', 'input5.txt', 'input6.txt',
                        'input7.txt', 'input8.txt', 'input9.txt', 'input10.txt','input11.txt']

    for input_file_path in input_file_paths:
        try:
            with open(input_file_path, 'r') as file:
                player_names = file.readline().strip().split()
                if len(player_names) != 2:
                    raise ValueError

                int1, int2 = file.readline().strip().split()
                player1 = Player(player_names[0], int(int1))
                player2 = Player(player_names[1], int(int2))

                card_damage = {}
                A, B, C = file.readline().strip().split()
                card_damage['A'] = int(A)
                card_damage['B'] = int(B)
                card_damage['C'] = int(C)

                player1plays = []
                player2plays = []

                for _ in range(3):
                    card1, card2 = file.readline().strip().split()
                    player1plays.append(f"{card1}:{card_damage[card1]}")
                    player2plays.append(f"{card2}:{card_damage[card2]}")
                    player1.play_round(card_damage[card1], card_damage[card2])
                    player1.emotional_damage(card_damage[card2])
                    player2.play_round(card_damage[card2], card_damage[card1])
                    player2.emotional_damage(card_damage[card1])

                if player1.score > player2.score:
                    result = "winner:player1"
                elif player1.score < player2.score:
                    result = "winner:player2"
                else:
                    result = "Draw"

                message1 = f"{player1.name} -> Score: {player1.score}, Health: {player1.health}"
                message2 = f"{player2.name} -> Score: {player2.score}, Health: {player2.health}"
                message3 = f"{message1}\n{message2}\nplayer1 plays: {', '.join(player1plays)} \nplayer2 plays: {', '.join(player2plays)} \n{result}\n------------------------------------------"

                print(message1)
                print(message2)

                result_file_path = 'result.txt'  # Replace with the actual path to your result file
                current_game_iteration, existing_lines = read_game_iteration(result_file_path)

                # Write the new data with the incremented game iteration
                write_data_with_iteration(result_file_path, message3, current_game_iteration)

                # Check the updated game iteration
                current_game_iteration, _ = read_game_iteration(result_file_path)
                print(f'Current game iteration: {current_game_iteration}')

        except ValueError as e:
            print(f"Invalid Command. {e}")
if __name__ == "__main__":
    main()
