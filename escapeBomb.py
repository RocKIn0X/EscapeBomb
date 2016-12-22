import arcade

from models import World, Player

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_SCALING = 0.25

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, SPRITE_SCALING, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class EscapeBombWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GRAY)

        self.world = World(width, height)
        self.player_sprite = ModelSprite('images/boy.png', model=self.world.player)

    def animate(self, delta):
        self.world.animate(delta)

    def on_draw(self):
        arcade.start_render()

        self.player_sprite.draw()

if __name__ == '__main__':
    window = EscapeBombWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
