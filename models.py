import arcade.key
from random import randint, random

WIDTH = 40
HEIGHT = 40

MARGIN = 10

class Player:
    def __init__(self, world, grid):
        self.world = world
        self.grid = grid
        self.playerPos = grid.grid

    def animate(self, delta):
        for i in range(10):
            for j in range(10):
                print(self.playerPos[i][j])

class Grid():
    def __init__(self, world):
        self.world = world
        self.grid = []
        self.score = 0;
        self.total_time = 0

        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)  # Append a cell

        self.assignBomb(self.grid)

    def assignBomb(self, grid):
        self.grid = grid

        for bomb in range(5):
            self.row = randint(0, 9)
            self.column = randint(0, 9)
            self.grid[self.row][self.column] = 2

    def animate(self, delta):
        self.total_time += delta
        self.second = self.total_time % 60

        if(self.total_time > 3):
            self.total_time = 0
            self.assignBomb(self.grid)

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
        if (row >= 0 and row < 10) and (column >= 0 and column < 10):
            if(self.grid[row][column] == 2):
                self.grid[row][column] = 1
                self.score += 1
                print(self.score)

            if(self.grid[row][column] == 0):
                self.score -= 1
                print(self.score)

        else:
            print("You click not correct")

        print("Click coordinates: ({}, {}). Grid coordinates: ({}, {})"
                 .format(x, y, row, column))
    def getScore(self):
        return self.score

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = Grid(self)
        self.score = self.grid.getScore()
        self.total_time = 0.0
        self.second = 0;
        self.player = Player(self, self.grid)

    def printScore(self):
        print(self.score)

    def animate(self, delta):
        self.grid.animate(delta)
        self.score = self.grid.getScore()
        print(self.score)

    def draw(self):
        self.grid.on_draw()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            print("hello")

        if key == arcade.key.D:
            print("world")

    def on_mouse_press(self, x, y, button, modifiers):
        self.grid.on_mouse_press(x, y, button, modifiers)
