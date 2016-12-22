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

        self.assignBomb(self.grid)

    def assignBomb(self, grid):
        self.grid = grid

        for bomb in range(10):
            self.row = randint(0, 9)
            self.column = randint(0, 9)
            self.grid[self.row][self.column] = 2

        for i in range(10):
            for j in range(10):
                print(i, j, self.grid[i][j])


    def on_draw(self):
        # Draw the grid
        for row in range(10):
            for column in range(10):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                elif self.grid[row][column] == 2:
                    color = arcade.color.RED
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2 + 385
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2 + 105

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = (x - 385) // (WIDTH + MARGIN)
        row = (y - 105) // (HEIGHT + MARGIN)

        # Set that location to one
        self.grid[row][column] = 1
        print("Click coordinates: ({}, {}). Grid coordinates: ({}, {})"
                 .format(x, y, row, column))

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

    def on_mouse_press(self, x, y, button, modifiers):
        self.grid.on_mouse_press(x, y, button, modifiers)
