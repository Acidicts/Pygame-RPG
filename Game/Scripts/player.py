import pygame
from Game.utils.settings import TILE_SIZE

class Player:
    def __init__(self, x, y, game):
        self.img_num = 0
        self.img = game.assets["player"]["player"][self.img_num].convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE_SIZE, TILE_SIZE))

        self.rect = self.img.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.game = game

    def update(self):
        self.control()
        self.draw()

    def draw(self):
        self.game.win.blit(self.img, (self.rect.x, self.rect.y))

    def control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5

    def change_img(self, event):
        if event.key == pygame.K_SPACE:
            if self.img_num < 47:
                self.img_num += 1
            else:
                self.img_num = 0
            self.img = self.game.assets["player"]["player"][self.img_num].convert_alpha()
