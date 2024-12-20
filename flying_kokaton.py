import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)
    k3_pmg = pg.image.load("fig/3.png")
    k3_pmg = pg.transform.flip(k3_pmg, True, False)
    kk_rct = k3_pmg.get_rect()
    tmr = 0
    kk_rct.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        elif key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        elif key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        elif key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((1, 0))
        else:
            kk_rct.move_ip(-1, 0)  # キーが押されていない場合は左に移動

        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg2_img, [x + 1600, 0])
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bg2_img, [x + 4800, 0])
        screen.blit(k3_pmg, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
