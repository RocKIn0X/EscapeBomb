import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_SCALING = 0.5

class EscapeBombWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.player = arcade.Sprite('images/ship.png', SPRITE_SCALING)
        self.player.set_position(100, 100)


    def animate(self, delta):
        self.player.set_position(self.player.center_x, self.player.center_y + 5)

    def on_draw(self):
        arcade.start_render()

        self.player.draw()

if __name__ == '__main__':
    window = EscapeBombWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
