import arcade
import TownWindow
FRAME_HEIGHT = 0
FRAME_WIDTH = 50

def main():
    window: TownWindow.TownWindow = TownWindow.TownWindow()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()

