class Soldier:
    def __init__(self, soldier_type, soldier_id, x, y):
        self.soldier_type = soldier_type
        self.soldier_id = soldier_id
        self.health = 100
        self.x = x
        self.y = y

class Archer(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("archer", soldier_id, x, y)

class Melee(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("melee", soldier_id, x, y)

class Game:
    def __init__(self, n):
        self.n = n
        self.board = [[None] * n for _ in range(n)]
        self.players = {0: [], 1: []}
        self.current_turn = 0

    def create_soldier(self, soldier_type, soldier_id, x, y):
        if self.board[x][y] is not None:
            print("duplicate tag")
            return

        if soldier_type == "archer":
            soldier = Archer(soldier_id, x, y)
        elif soldier_type == "melee":
            soldier = Melee(soldier_id, x, y)
        else:
            print("invalid soldier type")
            return

        self.board[x][y] = soldier
        self.players[self.current_turn].append(soldier)

    def move_soldier(self, soldier_id, direction):
        soldier = self.find_soldier(soldier_id)
        if soldier is None:
            return

        new_x, new_y = self.calculate_new_position(soldier.x, soldier.y, direction)

        if not (0 <= new_x < self.n and 0 <= new_y < self.n):
            print("out of bounds")
            return

        if self.board[new_x][new_y] is not None:
            print("duplicate tag")
            return

        self.board[soldier.x][soldier.y] = None
        self.board[new_x][new_y] = soldier
        soldier.x, soldier.y = new_x, new_y

    def attack(self, attacker_id, target_id):
        attacker = self.find_soldier(attacker_id)
        target = self.find_soldier(target_id)

        if attacker is None or target is None:
            return

        if self.calculate_distance(attacker.x, attacker.y, target.x, target.y) > 1:
            print("the target is too far")
            return

        if isinstance(attacker, Archer):
            target.health -= 10
        elif isinstance(attacker, Melee):
            target.health -= 20

        print("target eliminated" if target.health <= 0 else f"target health: {target.health}")

    def get_info(self, soldier_id):
        soldier = self.find_soldier(soldier_id)
        if soldier is None:
            return

        print(f"health: {soldier.health}")
        print(f"location: {soldier.x} {soldier.y}")

    def who_is_in_lead(self):
        score = {0: 0, 1: 0}
        for player, soldiers in self.players.items():
            for soldier in soldiers:
                score[player] += soldier.health

        if score[0] > score[1]:
            print("Player 0 is in the lead")
        elif score[0] < score[1]:
            print("Player 1 is in the lead")
        else:
            print("draw")

    def find_soldier(self, soldier_id):
        for row in self.board:
            for soldier in row:
                if soldier is not None and soldier.soldier_id == soldier_id:
                    return soldier
        print("soldier does not exist")
        return None

    def calculate_new_position(self, x, y, direction):
        if direction == "up":
            return x - 1, y
        elif direction == "down":
            return x + 1, y
        elif direction == "left":
            return x, y - 1
        elif direction == "right":
            return x, y + 1

    def calculate_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

# Main program
n = int(input())
game = Game(n)

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "new":
        game.create_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
    elif command[0] == "move":
        game.move_soldier(int(command[1]), command[2])
    elif command[0] == "attack":
        game.attack(int(command[1]), int(command[2]))
    elif command[0] == "info":
        game.get_info(int(command[1]))
    elif command[0] == "who" and command[1] == "is" and command[2] == "in" and command[3] == "lead":
        game.who_is_in_lead()
