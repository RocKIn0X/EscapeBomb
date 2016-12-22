import arcade.key
from random import randint, random

WIDTH = 40
HEIGHT = 40

MARGIN = 10

class Player:
    def __init__(self, world, grid):
        self.world = world
        self.grid = grid

    def animate(self, delta):
        if self.y > self.world.height:
            self.y = 0
        self.y += 5

class Grid():
    def __init__(self, world):
        self.world = world
        self.grid = []

        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)  # Append a cell

    def on_draw(self):
        # Draw the grid
        for row in range(10):
            for column in range(10):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2 + 385
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2 + 105

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = Grid(self)
        self.player = Player(self, self.grid)

    def animate(self, delta):
        self.player.animate(delta)

    def draw(self):
        self.grid.on_draw()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            print("hello")

        if key == arcade.key.D:
            print("world")
