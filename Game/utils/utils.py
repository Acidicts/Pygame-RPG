import pygame
from Game.utils.settings import TILE_SIZE

base_dir = "Game/Assets/"


def load_image(name):
    img = pygame.image.load(base_dir + name).convert()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img.set_colorkey((0, 0, 0))

    return img


def load_tiles(grid, name):
    columns, rows = grid
    img = pygame.image.load(base_dir + name).convert_alpha()

    tile_width = img.get_width() // columns
    tile_height = img.get_height() // rows  # Corrected to use get_height for tile height calculation

    tiles = []

    for y in range(rows):
        for x in range(columns):
            rect = pygame.Rect(int(x * tile_width), int(y * tile_height), tile_width, tile_height)

            tile_surface = pygame.Surface((tile_width, tile_height), pygame.SRCALPHA)

            tile_surface.blit(img, (0, 0), rect)
            tile_surface = pygame.transform.scale(tile_surface, (TILE_SIZE, TILE_SIZE))
            tiles.append(tile_surface)

    return tiles


class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

    def get_images(self, scale):
        images = []
        for y in range(self.sprite_sheet.get_height() // 32):
            for x in range(self.sprite_sheet.get_width() // 32):

                images.append(pygame.transform.scale(self.get_image(x * 32, y * 32, 32, 32), (scale, scale)))
        return images


class Animation:
    def __init__(self, game, images, img_dur=1, loop=True, flipped=False):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0
        self.flipped = flipped

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images))
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return pygame.transform.flip(self.images[int(self.frame / self.img_duration)], self.flipped, False)
