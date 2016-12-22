import arcade

from models import World, Grid

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_SCALING = 0.25

class EscapeBombWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GRAY)

        self.world = World(width, height)
        self.grid = Grid(self.world)

    def animate(self, delta_time):
        self.world.animate(delta_time)

    def on_draw(self):
        arcade.start_render()

        self.world.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)


if __name__ == '__main__':
    window = EscapeBombWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
