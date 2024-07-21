import pygame
from Game.utils.settings import TILE_SIZE


class TileMap:
    def __init__(self, game):
        self.game = game
        self.columns, self.row = 25, 20

        self.tiles = []

    def create_map(self):
        for y in range(self.row):
            for x in range(self.columns):
                self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, self.game.assets["tiles"]["grass"], False))

        for x in range(self.game.width // 48):
            self.tiles.append(Tile(x * TILE_SIZE, 0 * TILE_SIZE, self.game.assets["tiles"]["cliff_1"], True))
            self.tiles.append(Tile(x * TILE_SIZE, 18 * TILE_SIZE, self.game.assets["tiles"]["cliff_1"], True))

    def draw(self, win):
        for tile in self.tiles:
            tile.draw(win)

    def collide(self, rect):
        for tile in self.tiles:
            if tile.collides and rect.colliderect(tile.rect):
                return True
        return False


class Tile:
    def __init__(self, x, y, img, collides):
        self.img = img

        self.rect = img.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.collides = collides

    def draw(self, win):
        win.blit(self.img, (self.rect.x, self.rect.y))
