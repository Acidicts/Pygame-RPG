import pygame
import Game.utils.utils as utils
from Game.utils.settings import TILE_SIZE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RPG Game")
        utils.init("Game/Assets/")

        self.width, self.height = 800, 600
        self.win = pygame.display.set_mode((self.width, self.height))

        self.assets = {
            "grass": utils.load_image("Tiles/Grass_Middle.png"),
            "water": utils.load_image("Tiles/Water_Middle.png"),
            "path": utils.load_image("Tiles/Path_Middle.png"),
            "farmland_tiles": utils.load_tiles((6, 3), "Tiles/FarmLand_Tile.png"),
            "path_tiles": utils.load_tiles((3, 3), "Tiles/Path_Tile.png"),
        }

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.win.fill((0, 0, 0))

            pos = 0
            for index in range(len(self.assets["path_tiles"])):
                self.win.blit(self.assets["path_tiles"][index], (pos, 400))
                pos += TILE_SIZE

            pygame.display.update()
