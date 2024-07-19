import pygame
from Game.utils.settings import TILE_SIZE

global base_dir


def init(directory):
    global base_dir
    base_dir = directory


def load_image(name):
    global base_dir

    img = pygame.image.load(base_dir + name).convert()
    img.set_colorkey((0, 0, 0))
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))

    return img


def load_tiles(grid, name):
    columns, rows = grid
    img = pygame.image.load(base_dir + name).convert_alpha()  # Load the full image containing all tiles

    tile_width = img.get_width() // columns
    tile_height = img.get_width() // rows

    tiles = []

    for y in range(rows):
        for x in range(columns):
            # Calculate the position of the tile in the image
            rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)
            # Create a new surface for the tile
            tile_surface = pygame.Surface((tile_width, tile_height), pygame.SRCALPHA)
            # Blit the corresponding section of the image onto the surface
            tile_surface.blit(img, (0, 0), rect)
            tiles.append(tile_surface)

    return tiles
