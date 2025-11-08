import pygame.font


class ScopeBoard:
    """Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройка шрифта для вывода счета.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)

        # Подготовка исходного изображения счета.
        self.prep_scope()

    def prep_scope(self):
        """Преобразует текущий счет в графическое изображение."""
        scope_str = str(self.stats.scope)
        self.score_image = self.font.render(scope_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_scope(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)
