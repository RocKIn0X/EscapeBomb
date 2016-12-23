import arcade

from models import World, Grid

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SPRITE_SCALING = 0.25

STATE_GAME = "ON GAME"
STATE_GAMEOVER = "GAME OVER"
#STATE_WINNING = "WIN"

class EscapeBombWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.setup(width, height)

    def setup(self, width, height):
        self.state = STATE_GAME

        arcade.set_background_color(arcade.color.GRAY)

        self.world = World(width, height)
        self.grid = Grid(self.world)
        self.total_time = 1
        self.score = 0
        self.bg_sound = arcade.load_sound("sounds/bg.ogg")
        #self.final_sound = arcade.load_sound("sounds/FLTFINAL.ogg")

        arcade.play_sound(self.bg_sound)

    def animate(self, delta_time):
        self.world.animate(delta_time)
        self.total_time = self.world.getTotalTime()

    def on_draw(self):
        arcade.start_render()

        if self.state == STATE_GAME:
            self.world.draw()
            if self.total_time <= 0:
                self.state = STATE_GAMEOVER

        else:
            arcade.set_background_color(arcade.color.YELLOW)
            self.score = self.world.getScore()
            arcade.draw_text("Your score: " + str(self.score), 500, 360, arcade.color.BLACK, 40)
            arcade.draw_text("Click for restart game", 560, 300, arcade.color.BLACK, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == STATE_GAME:
            self.world.on_mouse_press(x, y, button, modifiers)
        else:
            self.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


if __name__ == '__main__':
    window = EscapeBombWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
