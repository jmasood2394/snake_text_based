from game_logic import SnakeGame

game = SnakeGame()
game.display()


while game.move():
    if game.game_over():
        print(" Game Over! ")
        break
    game.display()
