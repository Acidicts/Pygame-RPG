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


def load_player_sprites(image_path, grid_size):
    columns, rows = grid_size
    img = pygame.image.load(image_path).convert_alpha()  # Load the image

    tile_width = img.get_width() / columns
    tile_height = img.get_height() / rows

    sprites = []

    for y in range(rows):
        for x in range(columns):
            rect = pygame.Rect(int(x * tile_width), int(y * tile_height), int(tile_width), int(tile_height))
            sprite_surface = pygame.Surface((int(tile_width), int(tile_height)), pygame.SRCALPHA)
            sprite_surface.blit(img, (0, 0), rect)
            sprites.append(sprite_surface)

    return sprites
