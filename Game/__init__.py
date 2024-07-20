import sys

import pygame
import Game.utils.utils as utils
from Game.Scripts.tilemap import TileMap
from Game.utils.settings import TILE_SIZE
from Game.Scripts.player import Player


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RPG Game")

        self.width, self.height = 800, 640
        self.win = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        self.running = True

        self.assets = {
            "tiles": {"grass": utils.load_image("Tiles/Grass_Middle.png"),
                      "water": utils.load_image("Tiles/Water_Middle.png"),
                      "path": utils.load_image("Tiles/Path_Middle.png"),
                      "farmland_tile": utils.load_tiles((6, 3), "Tiles/FarmLand_Tile.png"),
                      "path_tile": utils.load_tiles((3, 3), "Tiles/Path_Tile.png")},
            "player": {"player": utils.SpriteSheet("Game/Assets/Player/Player.png").get_images(64),
                       "player_actions": utils.load_tiles((2, 12), "Player/Player_Actions.png")},
        }

        self.tile_map = TileMap(self)
        self.tile_map.create_map()

        self.player = Player(0, 0, self)

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(24)

            self.win.fill((0, 0, 0))

            self.tile_map.draw(self.win)
            self.player.update()

            pygame.display.update()
