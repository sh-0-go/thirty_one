import pygame

pygame.init()

# タイトルの描画
def draw_title():
    title_img = font.render(title, True, BLACK, GREEN)
    screen.blit(title_img, (150, 50))

# グリッド線の描画
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * 50, i * 200), (screen_width, i * 200), 5)
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), 5)

# ウィンドウの作成
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("31 ゲーム")

# 他の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 

# フォントの設定
font = pygame.font.SysFont(None, 100)

title = "31 game!"
total_count = 0

# メインループ#####################################################
run = True

while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)
    
    # タイトルの描画
    draw_title()

    total_count_img = font.render(str(total_count), True, BLACK)
    screen.blit(total_count_img, (280, 200))

    # マウスの位置を取得
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    


    # 更新
    pygame.display.update()

##################################################################

pygame.quit()
