import pygame

pygame.init()

# タイトルの描画
def draw_title():
    title_img = font.render(title, True, BLACK, GREEN)
    screen.blit(title_img, (150, 50))

# トータルの描画
def draw_total():
    total_count_img = font.render(str(total_count), True, BLACK)
    screen.blit(total_count_img, (270, 150))

# ボックスの描画
def draw_box():
    if total_count < 29: # 合計が30未満の時
        for i in range(0, 3):
            pygame.draw.line(screen, BLACK, (175 * i + 75, 300), (175 * i + 75, 500), 5)
            pygame.draw.line(screen, BLACK, (175 * i + 175, 300), (175 * i + 175, 500), 5)
            pygame.draw.line(screen, BLACK, (175 * i + 75, 300), (175 * i + 175, 300), 5)
            pygame.draw.line(screen, BLACK, (175 * i + 75, 500), (175 * i + 175, 500), 5)
    elif total_count == 29: # 合計が29の時
        for i in range(0, 2):
            pygame.draw.line(screen, BLACK, (175 * i + 150, 300), (175 * i + 150, 500), 5)
            pygame.draw.line(screen, BLACK, (175 * i + 250, 300), (175 * i + 250, 500), 5)
            pygame.draw.line(screen, BLACK, (175 * i + 150, 300), (175 * i + 250, 300), 5)
            pygame.draw.line(screen, BLACK, (175 * i + 150, 500), (175 * i + 250, 500), 5)
    elif total_count == 30: # 合計が30の時
        pygame.draw.line(screen, BLACK, (250, 300), (250, 500), 5)
        pygame.draw.line(screen, BLACK, (350, 300), (350, 500), 5)
        pygame.draw.line(screen, BLACK, (250, 300), (350, 300), 5)
        pygame.draw.line(screen, BLACK, (250, 500), (350, 500), 5)

# 追加する数値の描画
def draw_select():
    if total_count < 29: # 合計が30未満の時
        for i in range(0, 3):
            plus_img = font.render('+' + str(plus[i]), True, BLACK)
            screen.blit(plus_img, (175 * i + 85, 310))
            count_img = font.render(str(count[i]), True, RED)
            screen.blit(count_img, (175 * i + 85, 400))
    elif total_count == 29: # 合計が29の時
        for i in range(0, 2):
            plus_img = font.render('+' + str(plus[i]), True, BLACK)
            screen.blit(plus_img, (175 * i + 160, 310))
            count_img = font.render(str(count[i]), True, RED)
            screen.blit(count_img, (175 * i + 160, 400))
    elif total_count == 30: # 合計が30の時
        plus_img = font.render('+' + str(plus[0]), True, BLACK)
        screen.blit(plus_img, (260, 310))
        count_img = font.render(str(count[0]), True, RED)
        screen.blit(count_img, (260, 400))

# スタートの文字を描画
def draw_start():
    start_text_img = font.render('click to start', True, BLACK, BLUE)
    screen.blit(start_text_img, (100, 300))

# 勝者の確認
def check_winner():
    game_over = False
    if total_count >= 31:
        game_over = True
    if game_over:
        finish_text_img = font.render('You Lose', True, BLACK, BLUE)
        screen.blit(finish_text_img, (150, 220))
        reset_text_img = font.render('click to reset', True, BLACK, BLUE)
        screen.blit(reset_text_img, (100, 300))

    return game_over

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
plus = [1, 2, 3]
count = [1, 2, 3]

# AIの手を選択
def ai_move():
    global total_count
    
    if total_count % 4 == 0:
        total_count += 2
        for i in range(0, 3):
            count[i] += 2
    elif total_count % 4 == 1:
        total_count += 1
        for i in range(0, 3):
            count[i] += 1
    elif total_count % 4 == 3:
        total_count += 3
        for i in range(0, 3):
            count[i] += 3

    # AIの手を選択した後に遅延を追加
    pygame.time.delay(500)  # 1000ミリ秒（1秒）の遅延

# メインループ#####################################################
run = True
start_check = False
player_turn = False # プレイヤーのターンかどうかを管理

while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)
    
    # タイトルの描画
    draw_title()

    if start_check:
        # トータルの描画
        draw_total()

        # ボックスの描画
        draw_box()

        # ボックスの描画
        draw_select()
    else:
        # スタートの文字を描画
        draw_start()

    # マウスの位置を取得
    mx, my = pygame.mouse.get_pos()

    # 勝者の確認
    game_over = check_winner()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if start_check and not game_over and player_turn:
            if total_count < 29:
                for i in range(0,3):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (mx > 175 * i + 75 and mx < 175 * i + 175) and (my > 300 and my < 500):
                            total_count += plus[i]
                            for index, n in enumerate(count):
                                count[index] += plus[i]
                            player_turn = False
            elif total_count == 29: # 合計が29の時
                for i in range(0,2):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (mx > 175 * i + 150 and mx < 175 * i + 250) and (my > 300 and my < 500):
                            total_count += plus[i]
                            for index, n in enumerate(count):
                                count[index] += plus[i]
            elif total_count == 30: # 合計が30の時
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (mx > 250 and mx < 350) and (my > 300 and my < 500):
                        total_count += plus[0]

        elif start_check and not game_over and not player_turn:
            ai_move()
            player_turn = True

        if game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                total_count = 0
                count = [1, 2, 3]
        
        if not start_check:
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_check = True

    # 更新
    pygame.display.update()

##################################################################

pygame.quit()
