import itertools

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget


class Root(AnchorLayout):
    pass

class Tile(Widget):
    def left(self):
        print("left")

    def right(self):
        print("right")

class TileGrid(RelativeLayout):
    def update_grid(self, rows=3, cols=3):

        tileSize = 200, 200

        for i, j in itertools.product(range(cols), range(rows)):
            tile = Tile()
            tile.size = tileSize
            tile.pos = (i*tile.width, j*tile.height)
            self.add_widget(tile)

        self.size = tileSize[0] * cols, tileSize[1] * rows

        print(self.size)



class TileMixer(App):
    def build(self):
        root_widget = Root()

        tile_grid = TileGrid()
        tile_grid.update_grid()

        root_widget.add_widget(tile_grid)

        return root_widget


if __name__ == '__main__':
    TileMixer().run();