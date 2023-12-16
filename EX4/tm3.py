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

        self.health -= max(damage1, damage2)

    def calculate_damage(self, card1, card2):
        return card1[card2]

def main():
    try:
        player_names = input().split()
        int1,int2=input().split()
        player1 = Player(player_names[0], int(int1))
        player2 = Player(player_names[1], int(int2))

        card_damage = {}
        
        A,B,C = input().split()
        card_damage['A'] = int(A)
        card_damage['B'] = int(B)
        card_damage['C'] = int(C)

        for _ in range(3):
            card1, card2 = input().split()
            player1.play_round(card_damage[card1], card_damage[card2])
            player2.play_round(card_damage[card2], card_damage[card1])

        print(f"{player1.name} -> Score: {player1.score}, Health: {player1.health}")
        print(f"{player2.name} -> Score: {player2.score}, Health: {player2.health}")

    except ValueError:
        print("Invalid Command.")

if __name__ == "__main__":
    main()
