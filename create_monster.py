import pygame
from monster import Monster

def draw_monster(screen):
    # 画像の読み込み
    face_img = pygame.image.load("assets/img/body_greenA.png")
    eye_img = pygame.image.load("assets/img/eye_human_green.png")
                                
    # 顔のサイズを0.7倍に縮小
    face_new_width = int(face_img.get_width() * 0.7)
    face_new_height = int(face_img.get_height() * 0.7)
    face_img = pygame.transform.scale(face_img, (face_new_width, face_new_height))

    # 目のサイズを0.5倍に縮小
    eye_new_width = int(eye_img.get_width() * 0.5)
    eye_new_height = int(eye_img.get_height() * 0.5)
    eye_img = pygame.transform.scale(eye_img, (eye_new_width, eye_new_height))

    # モンスターの作成
    face = Monster([450, 120])
    eye0 = Monster([465, 140])
    eye1 = Monster([515, 140])

    # モンスターの描画
    screen.blit(face_img, face.position)
    screen.blit(eye_img, eye0.position)
    screen.blit(eye_img, eye1.position)

# スタート画面のモンスターの描画
def the_start_monster(screen):
    # 画像の読み込み
    mouse_img = pygame.image.load("assets/img/mouthA.png")

    # 口のサイズを0.5倍に縮小
    mouse_new_width = int(mouse_img.get_width() * 0.5)
    mouse_new_height = int(mouse_img.get_height() * 0.5)
    mouse_img = pygame.transform.scale(mouse_img, (mouse_new_width, mouse_new_height))

    # モンスターの作成
    mouse = Monster([490, 190])

    # モンスターの描画
    screen.blit(mouse_img, mouse.position)

# 序盤のモンスターの描画
def the_opening_monster(screen):
    # 画像の読み込み
    mouse_img = pygame.image.load("assets/img/mouth_closed_sad.png")

    # 口のサイズを0.5倍に縮小
    mouse_new_width = int(mouse_img.get_width() * 0.5)
    mouse_new_height = int(mouse_img.get_height() * 0.5)
    mouse_img = pygame.transform.scale(mouse_img, (mouse_new_width, mouse_new_height))

    # モンスターの作成
    mouse = Monster([494, 190])

    # モンスターの描画
    screen.blit(mouse_img, mouse.position)

# 中盤のモンスターの描画
def the_middle_monster(screen):
    # 画像の読み込み
    mouse_img = pygame.image.load("assets/img/mouthE.png")

    # 口のサイズを0.5倍に縮小
    mouse_new_width = int(mouse_img.get_width() * 0.7)
    mouse_new_height = int(mouse_img.get_height() * 0.7)
    mouse_img = pygame.transform.scale(mouse_img, (mouse_new_width, mouse_new_height))

    # モンスターの作成
    mouse = Monster([485, 180])

    # モンスターの描画
    screen.blit(mouse_img, mouse.position)

# 終盤のモンスターの描画
def the_ending_monster(screen):
    # 画像の読み込み
    mouse_img = pygame.image.load("assets/img/mouthJ.png")

    # 口のサイズを0.5倍に縮小
    mouse_new_width = int(mouse_img.get_width() * 0.7)
    mouse_new_height = int(mouse_img.get_height() * 0.7)
    mouse_img = pygame.transform.scale(mouse_img, (mouse_new_width, mouse_new_height))

    # モンスターの作成
    mouse = Monster([480, 180])

    # モンスターの描画
    screen.blit(mouse_img, mouse.position)

# 終了後のモンスターの描画
def the_after_monster(screen):
    # 画像の読み込み
    mouse_img = pygame.image.load("assets/img/mouthH.png")

    # 口のサイズを0.5倍に縮小
    mouse_new_width = int(mouse_img.get_width() * 0.7)
    mouse_new_height = int(mouse_img.get_height() * 0.7)
    mouse_img = pygame.transform.scale(mouse_img, (mouse_new_width, mouse_new_height))

    # モンスターの作成
    mouse = Monster([480, 190])

    # モンスターの描画
    screen.blit(mouse_img, mouse.position)