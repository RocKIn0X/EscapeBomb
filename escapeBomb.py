import arcade

from models import Player

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_SCALING = 0.25

class EscapeBombWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.player = Player(100, 100)
        self.player_sprite = arcade.Sprite('images/boy.png', SPRITE_SCALING)


    def animate(self, delta):
        player = self.player

        player.animate(delta)
        self.player_sprite.set_position(player.x, player.y)

    def on_draw(self):
        arcade.start_render()

        self.player_sprite.draw()

if __name__ == '__main__':
    window = EscapeBombWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
