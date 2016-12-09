import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class EscapeBombWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

if __name__ == '__main__':
    window = EscapeBombWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
