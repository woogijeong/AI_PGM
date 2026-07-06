import pygame
import sys
import random

# ---------------------------------------------------------
# 초기 설정
# ---------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기")
clock = pygame.time.Clock()
FPS = 60

# 색상
WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
GRAY = (60, 60, 60)
RED = (220, 60, 60)

BRICK_COLORS = [
    (231, 76, 60),
    (230, 126, 34),
    (241, 196, 15),
    (46, 204, 113),
    (52, 152, 219),
]

font_big = pygame.font.SysFont("malgungothic", 48)
font_mid = pygame.font.SysFont("malgungothic", 28)
font_small = pygame.font.SysFont("malgungothic", 20)

# ---------------------------------------------------------
# 패들
# ---------------------------------------------------------
PADDLE_WIDTH, PADDLE_HEIGHT = 110, 15
paddle_speed = 8


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - PADDLE_WIDTH // 2,
            HEIGHT - 40,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
        )

    def move(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

    def draw(self, surf):
        pygame.draw.rect(surf, WHITE, self.rect, border_radius=6)


# ---------------------------------------------------------
# 공
# ---------------------------------------------------------
BALL_RADIUS = 9


class Ball:
    def __init__(self, paddle):
        self.paddle = paddle
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top - 1
        self.speed_x = random.choice([-4, -3, 3, 4])
        self.speed_y = -5
        self.launched = False

    def launch(self):
        self.launched = True

    def update(self):
        if not self.launched:
            self.rect.centerx = self.paddle.rect.centerx
            self.rect.bottom = self.paddle.rect.top - 1
            return "ok"

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 좌우 벽
        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x *= -1
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.speed_x *= -1

        # 위쪽 벽
        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y *= -1

        # 바닥에 닿으면 실패
        if self.rect.top > HEIGHT:
            return "dead"

        # 패들과 충돌
        if self.rect.colliderect(self.paddle.rect) and self.speed_y > 0:
            self.rect.bottom = self.paddle.rect.top
            # 맞은 위치에 따라 반사각 조정
            offset = (self.rect.centerx - self.paddle.rect.centerx) / (
                self.paddle.rect.width / 2
            )
            self.speed_x = offset * 6
            self.speed_y = -abs(self.speed_y)

        return "ok"

    def draw(self, surf):
        pygame.draw.circle(surf, WHITE, self.rect.center, BALL_RADIUS)


# ---------------------------------------------------------
# 벽돌
# ---------------------------------------------------------
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = 70
BRICK_HEIGHT = 24
BRICK_PADDING = 6
BRICK_OFFSET_TOP = 60
BRICK_OFFSET_LEFT = (
    WIDTH - (BRICK_COLS * (BRICK_WIDTH + BRICK_PADDING) - BRICK_PADDING)
) // 2


def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING)
            y = BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
            rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append({"rect": rect, "color": BRICK_COLORS[row % len(BRICK_COLORS)]})
    return bricks


def draw_bricks(surf, bricks):
    for b in bricks:
        pygame.draw.rect(surf, b["color"], b["rect"], border_radius=4)
        pygame.draw.rect(surf, BLACK, b["rect"], width=1, border_radius=4)


# ---------------------------------------------------------
# 게임 상태
# ---------------------------------------------------------
def draw_text_center(surf, text, font, color, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, y))
    surf.blit(surface, rect)


def main():
    paddle = Paddle()
    ball = Ball(paddle)
    bricks = create_bricks()

    score = 0
    lives = 3
    game_state = "ready"  # ready, playing, gameover, clear

    while True:
        dt_events = pygame.event.get()
        for event in dt_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == "ready":
                        game_state = "playing"
                        ball.launch()
                    elif game_state in ("gameover", "clear"):
                        # 재시작
                        paddle = Paddle()
                        ball = Ball(paddle)
                        bricks = create_bricks()
                        score = 0
                        lives = 3
                        game_state = "ready"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        if game_state in ("ready", "playing"):
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                paddle.move(-paddle_speed)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                paddle.move(paddle_speed)

        if game_state == "playing":
            result = ball.update()
            if result == "dead":
                lives -= 1
                if lives <= 0:
                    game_state = "gameover"
                else:
                    ball.reset()
                    game_state = "ready"

            # 벽돌 충돌 체크
            hit_index = None
            for i, b in enumerate(bricks):
                if ball.rect.colliderect(b["rect"]):
                    hit_index = i
                    # 충돌 방향 판정 (간단 버전)
                    brick_rect = b["rect"]
                    overlap_x = min(ball.rect.right, brick_rect.right) - max(
                        ball.rect.left, brick_rect.left
                    )
                    overlap_y = min(ball.rect.bottom, brick_rect.bottom) - max(
                        ball.rect.top, brick_rect.top
                    )
                    if overlap_x < overlap_y:
                        ball.speed_x *= -1
                    else:
                        ball.speed_y *= -1
                    break

            if hit_index is not None:
                bricks.pop(hit_index)
                score += 10

            if not bricks:
                game_state = "clear"

        # ---------------- 그리기 ----------------
        screen.fill(BLACK)
        draw_bricks(screen, bricks)
        paddle.draw(screen)
        ball.draw(screen)

        # 상단 UI
        score_surf = font_small.render(f"점수: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))
        lives_surf = font_small.render(f"목숨: {lives}", True, WHITE)
        screen.blit(lives_surf, (WIDTH - 110, 10))

        if game_state == "ready":
            draw_text_center(screen, "스페이스바를 눌러 시작하세요", font_mid, WHITE, HEIGHT // 2 - 40)
            draw_text_center(screen, "← → 또는 A D 로 패들 이동", font_small, GRAY, HEIGHT // 2)
        elif game_state == "gameover":
            draw_text_center(screen, "게임 오버", font_big, RED, HEIGHT // 2 - 40)
            draw_text_center(screen, f"최종 점수: {score}", font_mid, WHITE, HEIGHT // 2 + 10)
            draw_text_center(screen, "스페이스바를 눌러 다시 시작", font_small, GRAY, HEIGHT // 2 + 50)
        elif game_state == "clear":
            draw_text_center(screen, "클리어!", font_big, (46, 204, 113), HEIGHT // 2 - 40)
            draw_text_center(screen, f"최종 점수: {score}", font_mid, WHITE, HEIGHT // 2 + 10)
            draw_text_center(screen, "스페이스바를 눌러 다시 시작", font_small, GRAY, HEIGHT // 2 + 50)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
