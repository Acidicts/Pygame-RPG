import pygame
from pygame.math import Vector2
from Game.utils.settings import TILE_SIZE
from Game.utils.utils import Animation


class Player:
    def __init__(self, x, y, game):
        self.img_num = 0
        self.img = game.assets["player"]["player"][self.img_num].convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE_SIZE, TILE_SIZE))

        self.rect = self.img.get_rect()
        self.collided = False

        self.rect.x = x
        self.rect.y = y
        self.vector = Vector2(self.rect.center)

        self.game = game
        self.action = {
            "idle": ([0, 1, 2, 3, 4, 5], False),
            "left": ([6, 7, 8, 9, 10, 11], True),
            "right": ([6, 7, 8, 9, 10, 11], False),
            "up": ([30, 31, 32, 33, 34, 35], False),
            "down": ([18, 19, 20, 21, 22, 23], False),
            "down_right": ([24, 25, 26, 27, 28, 29], False),
            "down_left": ([24, 25, 26, 27, 28, 29], True),
            "up_left": ([30, 31, 32, 33, 34, 35], True),
            "up_right": ([30, 31, 32, 33, 34, 35], False),
        }

        self.animation = None
        self.frames = None

        self.mode = "idle"
        self.change_mode(self.mode)

    def update(self):
        self.control()
        self.draw()
        self.animation.update()

        self.rect = pygame.rect.Rect(self.vector.x, self.vector.y, TILE_SIZE, TILE_SIZE)
        self.collided = self.game.tile_map.collide(self.rect)

    def draw(self):
        self.img = self.animation.img()
        self.game.win.blit(self.img, self.vector)

    def control(self):
        keys = pygame.key.get_pressed()

        movement = Vector2(0, 0)
        if keys[pygame.K_w]:
            movement.y -= 1
        if keys[pygame.K_s]:
            movement.y += 1
        if keys[pygame.K_a]:
            movement.x -= 1
        if keys[pygame.K_d]:
            movement.x += 1

        if movement.length() > 0:
            movement = movement.normalize() * (5 if not self.collided else -5)
            predicted_position = self.rect.move(movement.x, movement.y)
            if not self.game.tile_map.collide(predicted_position):
                self.vector += movement
                self.rect.x, self.rect.y = self.vector.x, self.vector.y
                self.change_mode_based_on_movement(movement)
            else:
                if self.mode != "idle":
                    self.change_mode("idle")
        else:
            if self.mode != "idle":
                self.change_mode("idle")

    def change_mode_based_on_movement(self, movement):
        if movement.x > 0 and movement.y == 0:
            if self.mode != "right":
                self.change_mode("right")
        elif movement.x < 0 and movement.y == 0:
            if self.mode != "left":
                self.change_mode("left")
        elif movement.y > 0 and movement.x == 0:
            if self.mode != "down":
                self.change_mode("down")
        elif movement.y < 0 and movement.x == 0:
            if self.mode != "up":
                self.change_mode("up")
        elif movement.x > 0 and movement.y > 0:
            if self.mode != "down_right":
                self.change_mode("down_right")
        elif movement.x < 0 and movement.y < 0:
            if self.mode != "up_left":
                self.change_mode("up_left")
        elif movement.x > 0 > movement.y:
            if self.mode != "up_right":
                self.change_mode("up_right")
        elif movement.x < 0 < movement.y:
            if self.mode != "down_left":
                self.change_mode("down_left")

    def change_mode(self, mode):
        mode = str(mode)
        mode = mode.lower()
        self.mode = mode

        self.frames = [self.game.assets["player"]["player"][i] for i in self.action[mode][0]]
        self.animation = Animation(self.game, self.frames, 3, True, self.action[mode][1])
