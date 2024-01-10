import random
import os


class SnakeGame:
    def __init__(self):
        self.width = 10
        self.height = 10
        # Start snake in the middle facing up
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "UP"
        self.food = self.generate_food()

    def generate_food(self):
        """ Generate random coordinates for the food until a valid position is found"""
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def display(self):
        """ Display Grid by . and show the snake and food"""
        os.system("cls" if os.name == "nt" else "clear")
        for x in range(self.width):
            for y in range(self.height):
                if (y, x) in self.snake:
                    print("⬜️", end=" ")
                elif (y, x) == self.food:
                    print("F", end=" ")
                else:
                    print(".", end=" ")
            print()

    def move(self):
        """ Define movement of the snake """
        print(f"The snake is facing {self.direction}")
        while True:
            try:
                user_direction = input(
                    "Enter 'W' to move up, 'S' for down, 'A' for left and 'D' for right. Enter 'Q' to quit\n").upper()
                if user_direction not in ["W", "S", "A", "D", "Q"]:
                    raise ValueError("Invalid Entry")

                if user_direction == "Q":
                    print("Goodbye.....")
                    return False
                else:
                    self.direction = user_direction
                    # Get coordinates based on the direction chosen
                    snake_head = self.snake[0]
                    # Get user to input where to move the snake
                    if self.direction == "W":
                        new_location = (snake_head[0], snake_head[1] - 1)
                    elif self.direction == "S":
                        new_location = (snake_head[0], snake_head[1] + 1)
                    elif self.direction == "D":
                        new_location = (snake_head[0] + 1, snake_head[1])
                    elif self.direction == "A":
                        new_location = (snake_head[0] - 1, snake_head[1])

                    """Add new location to the snake, if the new location already has food, keep the new location
                    remove the old location if food is not present at the new location"""
                    self.snake.insert(0, new_location)

                    if new_location == self.food:
                        self.food = self.generate_food()
                    else:
                        self.snake.pop()

                    return True

                    break

            except ValueError:
                print("Invalid Entry Please try again")

    def game_over(self):
        """ Check if the snake collided with the edges or itself """
        snake_head = self.snake[0]
        if (
                # check x coordinate edges
                snake_head[0] < 0
                or snake_head[0] > self.width - 1
                # check y coordinate edges
                or snake_head[1] < 0
                or snake_head[1] > self.height - 1
                # check for collision
                or snake_head in self.snake[1:]
        ):
            return True

        return False
