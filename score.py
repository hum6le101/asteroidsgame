import pygame
from constants import *
# create a Scorebox-textfield
class Score(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(self.containers)
        self.score_value = 0
        self.font = pygame.font.Font(SCORE_FONT, SCORE_FONT_SIZE)

    def draw(self, screen):
        score = self.font.render(f"Score: {self.score_value}", True, SCORE_FONT_COLOR)
        textbox = score.get_rect()
        textbox.topleft = (SCORE_POSITION_X, SCORE_POSITION_Y)
        screen.blit(score, textbox)

    def score_increment(self):
        self.score_value += 1