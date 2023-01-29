import pygame
from puzzle import Puzzle

pygame.init()
pygame.display.set_caption("15PuzzleSolver")

class Application:
    def __init__(self):
        """Initializes the components for the application, like fonts etc.
        """
        pixels = 720
        self.puzzle = Puzzle()
        self.puzzle.set_numbers()
        self.puzzle.shuffle_board(999)
        self.rectSize = pixels / self.puzzle.size
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((pixels, pixels))
        self.screen.fill((0, 0, 0))
        self.font = pygame.font.SysFont("", 68)
        self.border_color = (35, 35, 35)
        self.tile_color = (70, 70, 70)
        self.font_color = (255, 255, 255)

    def game_loop(self):
        """The main loop of the application."""
        while True:
            self.draw_puzzle()
            pygame.display.flip()
            self.clock.tick(120)

    def draw_puzzle(self):
        """Draws a puzzle to the screen, forms rectangles for the numbers etc.
        """
        for x in range(self.puzzle.size):
            for y in range(self.puzzle.size):
                text = str(self.puzzle.get_number(x, y))
                rectangle = pygame.Rect(x * self.rectSize,
                                        y * self.rectSize,
                                        self.rectSize, self.rectSize)
                if not text:
                    pygame.draw.rect(self.screen, self.border_color, rectangle)
                else:
                    pygame.draw.rect(self.screen, self.tile_color, rectangle)
                pygame.draw.rect(self.screen, self.border_color, rectangle, 1)
                number = self.font.render(text, 1, self.font_color)
                centered_width = self.rectSize / 2 - number.get_width() / 2
                centered_height = (self.rectSize / 2) - number.get_height() / 2
                self.screen.blit(number,
                                 ((x * self.rectSize + centered_width), 
                                 y * self.rectSize + centered_height))
