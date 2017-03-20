import itertools
import kivy
# kivy.require("")


from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Root(Widget):
    pass

class TileGrid(Widget):
    def update_grid(self, rows=3, cols=3):
        for i, j in itertools.product(range(rows), range(cols)):
            img = Image(source="txt.jpg")
            img.pos = (i*img.width, j*img.height)
            self.add_widget(img)



class TileMixer(App):

    def build(self):
        tile_grid = TileGrid()
        tile_grid.update_grid()

        root_widget = Root()
        root_widget.add_widget(tile_grid)

        return root_widget


if __name__ == '__main__':
    TileMixer().run();