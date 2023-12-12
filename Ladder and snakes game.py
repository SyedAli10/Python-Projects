import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
PLAYER_SIZE = 30
FPS = 10

WHITE = (255, 255, 255)

class Player:
    def __init__(self, name, image_path):
        self.name = name
        self.position = 1
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))

class SnakeAndLadderGame:
    def __init__(self, size=100):
        self.size = size
        self.players = []
        self.snakes_and_ladders = {
            2: 23, 6: 45, 20: 59, 52: 72, 57: 96,
            71: 92, 43: 17, 50: 5, 56: 8, 74: 16,
            84: 58, 87: 49, 98: 40
        }

    def add_player(self, player):
        self.players.append(player)

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        new_position = player.position + steps
        if new_position in self.snakes_and_ladders:
            new_position = self.snakes_and_ladders[new_position]
        if new_position <= self.size:
            player.position = new_position
        if new_position == self.size:
            print(f"Player {player.name} has reached the final position and won!")

def draw_board(game, last_positions):
    screen.fill(WHITE)
    background_resized = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background_resized, (0, 0))

    for player, last_pos in zip(game.players, last_positions):
        row, col = divmod(player.position - 1, 10)

        x = col * (WIDTH // 10) + (WIDTH // 20)
        y = (9 - row) * (HEIGHT // 10) + (HEIGHT // 20)  

        screen.blit(player.image, (x - PLAYER_SIZE // 2, y - PLAYER_SIZE // 2))

    pygame.display.flip()


def main():
    game = SnakeAndLadderGame()
    player1 = Player("Player 1", "images//Blue.png")
    player2 = Player("Player 2", "images//Green.png")
    game.add_player(player1)
    game.add_player(player2)

    clock = pygame.time.Clock()

    print("Welcome to Snake and Ladder Game!")
    print("Rules:")
    print("1. Each player starts at position 1.")
    print("2. Roll a dice to move forward.")
    print("3. Land on a ladder to climb up.")
    print("4. Land on a snake to slide down.")
    print("5. The first player to reach or exceed position 100 wins.")

    input("Press Enter to start the game...")

    last_positions = [player.position for player in game.players]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for player, last_pos in zip(game.players, last_positions):
            print(f"{player.name}, Press Enter to roll the dice...")
            input()
            dice_roll = game.roll_dice()
            print(f"{player.name} rolled a {dice_roll}")
            last_positions[game.players.index(player)] = player.position
            game.move_player(player, dice_roll)

        draw_board(game, last_positions)
        clock.tick(FPS)

if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake and Ladder Game")
    background = pygame.image.load("images//Snake and Ladder Board.png")

    main()




