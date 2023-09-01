import pygame as p

p.init()  # Инициализация Pygame
# Константы экрана
W = 1200  # Ширина экрана
H = 1920  # Высота экрана
# Создание экрана
sc = p.display.set_mode((W, H))
FPS = 120  # Скорость проигрывания кадров
CW = W // 2  # Центр ширины
CH = H // 2  # Центр высоты
# Размер кнопок
DP_SZ = 0.8  # Размер кнопок креставины
US_SZ = 1.2  # Размер кнопок действий
FN_SZ = 3.5  # Размер фонового изображения
PR_SZ = 180  # Размер персонажа
# Размер меню
MN_SZ_W = 500
MN_SZ_H = 500
DG_SZ = 0.41  # Размер кнопки диагонали
# Переменные углов наклона
DG_UG_1 = 220
DG_UG_2 = 145
DG_UG_3 = 190
DG_UG_4 = 45
# Список градусов наклона
DG_U = (DG_UG_1,
        DG_UG_2,
        DG_UG_3,
        DG_UG_4)
# Начальная позиция фона
FP_X = 0
FP_Y = 0
# Позиция мыши
mouse_x = 0
mouse_y = 0
# Позиция меню
PM_X = 300
PM_Y = 550
# Индекс переключения
SEL_INX = 0
# Положение текста на экране
# Надпись 'Level'
LV_LL_X = 230
LV_LL_Y = 0
# Надпись цыфр Level
LV_TX_X = 370
LV_TX_Y = 0
# Надпись 'Lives'
LS_LL_X = 450
LS_LL_Y = 0
# Надпись 'Level'
LS_TX_X = 610
LS_TX_Y = 0
# Надпись 'coin''
CS_LL_X = 750
CS_LL_Y = 0
# Надпись цыфр монет
CS_TX_X = 880
CS_TX_Y = 0
# Расположение кнопок крестовины
# Вверх
UP_BN_X = 170
UP_BN_Y = 1000
# Вниз
DN_BN_X = 170
DN_BN_Y = 1240
# Вправо
RT_BN_X = 290
RT_BN_Y = 1140
# Влево
LT_BN_X = 10
LT_BN_Y = 1140
# Расположение кнопок действий
# Кнопка Y
Y_BN_X = 910
Y_BN_Y = 990
# Кнопка B
B_BN_X = W - 100 - 60
B_BN_Y = 1150
# Кнопка A
A_BN_X = 780
A_BN_Y = 1150
# Кнопка X
X_BN_X = 910
X_BN_Y = 1300
# Кнопка диагонали
DG_X_1 = 30
DG_Y_1 = 1000

DG_X_2 = 320
DG_Y_2 = 1000

DG_X_3 = 40
DG_Y_3 = 1320

DG_X_4 = 320
DG_Y_4 = 1290
# Список координат кнопок крестовины
DP_K = (UP_BN_X, UP_BN_Y,
        DN_BN_X, DN_BN_Y,
        RT_BN_X, RT_BN_Y,
        LT_BN_X, LT_BN_Y)
# Список координат кнопок крестовины
DP_US = (Y_BN_X, Y_BN_Y,
         B_BN_X, B_BN_Y,
         A_BN_X, A_BN_Y,
         X_BN_X, X_BN_Y)
# Список координат кнопок диагонали
DG_SP = (DG_X_1, DG_Y_1,
         DG_X_2, DG_Y_2,
         DG_X_3, DG_Y_3,
         DG_X_4, DG_Y_4)
# Настройка прозрачности обьектов
# Значение прозрачности (от 0 до 255), где 0 - полностью прозрачно, 255 - полностью непрозрачно
US_VL = 70
K_VL = 150
M_VL = 130
DG_VL = 40
# Сокращения загрузки изображений и шрифта
LD = p.image.load
PTS = p.transform.scale
PTR = p.transform.rotate
PFF = p.font.Font
# Пути к изображениям кнопок крестовины
UP_IM_PH = 'up.png'
DN_IM_PH = 'down.png'
RT_IM_PH = 'right.png'
LT_IM_PH = 'left.png'
# Пути к изображениям кнопок действий
Y_IM_PH = 'y_m.png'  # __________Y
X_IM_PH = 'x_m.png'  # _______X_____B
A_IM_PH = 'a_m.png'  # __________A
B_IM_PH = 'b_m.png'  # B
# Путь к изображению фона
FN_IM_PH_1 = 'fon1.png'
# Путь к шрифту текста
TX_FT_PH = 'tx_1.ttf'
# Путь к  изображению меню
MN_IM_PH = 'm_1.png'
# Пути направлений персонажа
# Обычные направления
PL_UP_PH = "ups.png"
PL_DN_PH = "downs.png"
PL_RT_PH = "rights.png"
PL_LT_PH = "lefts.png"
# Направления по диагонали
# Путь к изображению кнопоки диагонали
DG_IM_PH = 'dig.png'
# В право вверх
PL_UP_RG_PH = "up_right.png"
# В лево вверх
PL_UP_LF_PH = "up_left.png"
# Вниз в право
PL_DN_RG_PH = "down_right.png"
# Вниз в лево
PL_DN_LF_PH = "down_left.png"
# Переменные состояния управления
character_control = True
menu_active = False
selected_index = 0

mn_itm = []


# функция строк меню
def mn_str():
    mn_st = PFF(TX_FT_PH, 30)
    mn_itm = ['вещи', 'земля']
    for i, item in enumerate(mn_itm):
        text = mn_st.render(item, True, 'black')
        x = PM_X + 15
        y = PM_Y + (i * 70) + 20
        sc.blit(text, (x, y))

    cursor = mn_st.render('>', True, 'black')
    cursor_x = PM_X + 15
    cursor_y = PM_Y + (selected_index * 70) + 20
    sc.blit(cursor, (cursor_x, cursor_y))


# Флаги кнопок
bn_up_pd = False
bn_down_pd = False
bn_right_pd = False
bn_left_pd = False

DG_UP_RT = False
DG_UP_LT = False
DG_DN_RT = False
DG_DN_LT = False

bn_Y_pd = False
bn_B_pd = False
bn_A_pd = False
bn_X_pd = False

mn_akt = False
# Флаг режима управления (True - персонаж, False - курсора)
CH_CN = True
# Загрузим изображения персонажа
IM_P_UP = PTS(LD(PL_UP_PH), (PR_SZ, PR_SZ))
IM_P_DN = PTS(LD(PL_DN_PH), (PR_SZ, PR_SZ))
IM_P_RT = PTS(LD(PL_RT_PH), (PR_SZ, PR_SZ))
IM_P_LT = PTS(LD(PL_LT_PH), (PR_SZ, PR_SZ))

IM_P_UP_RG = PTS(LD(PL_UP_RG_PH), (PR_SZ, PR_SZ))
IM_P_UP_LT = PTS(LD(PL_UP_LF_PH), (PR_SZ, PR_SZ))
IM_P_DN_RT = PTS(LD(PL_DN_RG_PH), (PR_SZ, PR_SZ))
IM_P_DN_LT = PTS(LD(PL_DN_LF_PH), (PR_SZ, PR_SZ))
# Загрузка изображений кнопок крестовины
im_up = LD(UP_IM_PH)
im_dn = LD(DN_IM_PH)
im_rg = LD(RT_IM_PH)
im_lf = LD(LT_IM_PH)

im_dg_1 = LD(DG_IM_PH)
im_dg_2 = LD(DG_IM_PH)
im_dg_3 = LD(DG_IM_PH)
im_dg_4 = LD(DG_IM_PH)
# Загрузка изображений кнопок действий
im_Y = LD(Y_IM_PH)
im_B = LD(B_IM_PH)
im_A = LD(A_IM_PH)
im_X = LD(X_IM_PH)

# Список ширины кнопок
bn_W = (im_up.get_width() * DP_SZ,
        im_dn.get_width() * DP_SZ,
        im_rg.get_width() * DP_SZ,
        im_lf.get_width() * DP_SZ)
# Список высоты кнопок
bn_H = (im_up.get_height() * DP_SZ,
        im_dn.get_height() * DP_SZ,
        im_rg.get_height() * DP_SZ,
        im_lf.get_height() * DP_SZ)

# Список ширины кнопок диагонали
dg_W = (im_dg_1.get_width() * DG_SZ,
        im_dg_2.get_width() * DG_SZ,
        im_dg_3.get_width() * DG_SZ,
        im_dg_4.get_width() * DG_SZ)
# Список высоты кнопок диагонали
dg_H = (im_dg_1.get_height() * DG_SZ,
        im_dg_2.get_height() * DG_SZ,
        im_dg_3.get_height() * DG_SZ,
        im_dg_4.get_height() * DG_SZ)

# Список ширины кнопок  действий
b_us_W = (im_Y.get_width() * US_SZ,
          im_B.get_width() * US_SZ,
          im_A.get_width() * US_SZ,
          im_X.get_width() * US_SZ)
# Список высоты кнопок  действий
b_us_H = (im_Y.get_height() * US_SZ,
          im_B.get_height() * US_SZ,
          im_A.get_height() * US_SZ,
          im_X.get_height() * US_SZ)
# Загрузка изображения фона
FN_1 = LD(FN_IM_PH_1)


# Определяем функцию для отображения изображений на экране
def fn_im_1():
    fn_pts_1 = PTS(FN_1, (int(FN_1.get_width() * FN_SZ), int(FN_1.get_height() * FN_SZ)))
    # Отображаем изображения на экране
    sc.blit(fn_pts_1, (FP_X, FP_Y))


# Основное меню
def mn_osn():
    im_mn_osn = PTS(LD(MN_IM_PH), (MN_SZ_W, MN_SZ_H))
    sc.blit(im_mn_osn, (PM_X, PM_Y))
    mn_str()


# Функция кнопок
def kn_dp():
    bg_dp_up = PTS(im_up, (int(bn_W[0]), int(bn_H[0])))
    bg_dp_dn = PTS(im_dn, (int(bn_W[1]), int(bn_H[1])))
    bg_dp_rg = PTS(im_rg, (int(bn_W[2]), int(bn_H[2])))
    bg_dp_lf = PTS(im_lf, (int(bn_W[3]), int(bn_H[3])))

    bg_dp_up.set_alpha(K_VL)
    sc.blit(bg_dp_up, (DP_K[0], DP_K[1]))
    bg_dp_dn.set_alpha(K_VL)
    sc.blit(bg_dp_dn, (DP_K[2], DP_K[3]))
    bg_dp_rg.set_alpha(K_VL)
    sc.blit(bg_dp_rg, (DP_K[4], DP_K[5]))
    bg_dp_lf.set_alpha(K_VL)
    sc.blit(bg_dp_lf, (DP_K[6], DP_K[7]))


def DG():
    dg_1 = PTS(im_dg_1, (int(dg_W[0]), int(dg_H[0])))
    dg_R_1 = PTR(dg_1, DG_U[0])
    dg_R_1.set_alpha(DG_VL)
    sc.blit(dg_R_1, (DG_SP[0], DG_SP[1]))

    dg_2 = PTS(im_dg_2, (int(dg_W[1]), int(dg_H[1])))
    dg_R_2 = PTR(dg_2, DG_U[1])
    dg_R_2.set_alpha(DG_VL)
    sc.blit(dg_R_2, (DG_SP[2], DG_SP[3]))

    dg_3 = PTS(im_dg_3, (int(dg_W[2]), int(dg_H[2])))
    dg_R_3 = PTR(dg_3, DG_U[2])
    dg_R_3.set_alpha(DG_VL)
    sc.blit(dg_R_3, (DG_SP[4], DG_SP[5]))

    dg_4 = PTS(im_dg_4, (int(dg_W[3]), int(dg_H[3])))
    dg_R_4 = PTR(dg_4, DG_U[3])
    dg_R_4.set_alpha(DG_VL)
    sc.blit(dg_R_4, (DG_SP[6], DG_SP[7]))


def kn_us():
    bg_dp_Y = PTS(im_Y, (int(b_us_W[0]), int(b_us_H[0])))
    bg_dp_B = PTS(im_B, (int(b_us_W[1]), int(b_us_H[1])))
    bg_dp_A = PTS(im_A, (int(b_us_W[2]), int(b_us_H[2])))
    bg_dp_X = PTS(im_X, (int(b_us_W[3]), int(b_us_H[3])))

    bg_dp_Y.set_alpha(US_VL)
    sc.blit(bg_dp_Y, (DP_US[0], DP_US[1]))
    bg_dp_B.set_alpha(US_VL)
    sc.blit(bg_dp_B, (DP_US[2], DP_US[3]))
    bg_dp_A.set_alpha(US_VL)
    sc.blit(bg_dp_A, (DP_US[4], DP_US[5]))
    bg_dp_X.set_alpha(US_VL)
    sc.blit(bg_dp_X, (DP_US[6], DP_US[7]))


# Основной цикл игры
def game_loop():
    global mouse_x
    global mouse_y
    global text, selected_index, event
    global bn_up_pd
    global bn_down_pd
    global bn_right_pd
    global bn_left_pd

    global DG_UP_RT
    global DG_UP_LT
    global DG_DN_RT
    global DG_DN_LT

    global bn_Y_pd
    global bn_B_pd
    global bn_A_pd
    global bn_X_pd

    global mn_akt
    global CH_CN

    run = True  # запуск цикла игры
    # Определим начальные координаты персонажа
    PXC = W // 2
    PYC = H // 2
    SPD = 15  # Скорость персонажа
    # здесь 0 - вверх, 1 - влево, 2 - вниз, 3 - вправо
    DETEKT = 0  # Детектор движения персонажа
    # Данные уровня, жизней и монет
    LV = 999
    MIN_LIV = 999
    MAX_LIV = 999
    COIN = 1000000
    level = f'{LV}'  # Уровень персонажа
    lives = f'{MIN_LIV}/{MAX_LIV}'  # Жизни персонажа
    coins = f'{COIN} зол.'  # Деньги
    while run:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    run = False
            elif event.type == p.MOUSEBUTTONDOWN:
                if event.button == 1:
                    (mouse_x, mouse_y) = event.pos

                    if DP_K[0] <= mouse_x <= DP_K[0] + bn_W[0] and DP_K[1] <= mouse_y <= DP_K[1] + bn_H[1]:
                        bn_up_pd = True
                    elif DP_K[2] <= mouse_x <= DP_K[2] + bn_W[1] and DP_K[3] <= mouse_y <= DP_K[3] + bn_H[1]:
                        bn_down_pd = True
                    elif DP_K[4] <= mouse_x <= DP_K[4] + bn_W[2] and DP_K[5] <= mouse_y <= DP_K[5] + bn_H[2]:
                        bn_right_pd = True
                    elif DP_K[6] <= mouse_x <= DP_K[6] + bn_W[3] and DP_K[7] <= mouse_y <= DP_K[7] + bn_H[3]:
                        bn_left_pd = True

                    elif DG_SP[2] <= mouse_x <= DG_SP[2] + dg_W[0] and DG_SP[3] <= mouse_y <= DG_SP[3] + dg_H[0]:
                        DG_UP_RT = True
                    elif DG_SP[0] <= mouse_x <= DG_SP[0] + dg_W[1] and DG_SP[1] <= mouse_y <= DG_SP[1] + dg_H[1]:
                        DG_UP_LT = True
                    elif DG_SP[6] <= mouse_x <= DG_SP[6] + dg_W[2] and DG_SP[7] <= mouse_y <= DG_SP[7] + dg_H[2]:
                        DG_DN_RT = True
                    elif DG_SP[4] <= mouse_x <= DG_SP[4] + dg_W[3] and DG_SP[5] <= mouse_y <= DG_SP[5] + dg_H[3]:
                        DG_DN_LT = True

                    elif DP_US[0] <= mouse_x <= DP_US[0] + b_us_W[0] and DP_US[1] <= mouse_y <= DP_US[1] + b_us_H[0]:
                        bn_Y_pd = True
                    elif DP_US[2] <= mouse_x <= DP_US[2] + b_us_W[1] and DP_US[3] <= mouse_y <= DP_US[3] + b_us_H[1]:
                        bn_B_pd = True

            elif event.type == p.MOUSEBUTTONUP:
                if event.button == 1:
                    bn_up_pd = False
                    bn_down_pd = False
                    bn_right_pd = False
                    bn_left_pd = False

                    DG_UP_RT = False
                    DG_UP_LT = False
                    DG_DN_RT = False
                    DG_DN_LT = False

                    bn_Y_pd = False
                    bn_B_pd = False
                    bn_A_pd = False
                    bn_X_pd = False

        #sc.fill('WHITE')
        fn_im_1()

        if DG_UP_RT:
            PXC += SPD / (2 ** 0.5)
            PYC -= SPD / (2 ** 0.5)
            DETEKT = 4

        elif DG_UP_LT:
            PXC -= SPD / (2 ** 0.5)
            PYC -= SPD / (2 ** 0.5)
            DETEKT = 5

        elif DG_DN_RT:
            PXC += SPD / (2 ** 0.5)
            PYC += SPD / (2 ** 0.5)
            DETEKT = 6

        elif DG_DN_LT:
            PXC -= SPD / (2 ** 0.5)
            PYC += SPD / (2 ** 0.5)
            DETEKT = 7

        if bn_up_pd:
            PYC -= SPD
            DETEKT = 0
        elif bn_down_pd:
            PYC += SPD
            DETEKT = 2
        elif bn_right_pd:
            PXC += SPD
            DETEKT = 3
        elif bn_left_pd:
            PXC -= SPD
            DETEKT = 1

        if bn_Y_pd:
            mn_akt = True
        elif mn_akt:
            # Обработка управления курсором меню
            if bn_up_pd:
                selected_index -= 1
                if selected_index < 0:
                    selected_index = len(mn_itm) - 1

            elif bn_down_pd:
                selected_index += 1
                if selected_index >= len(mn_itm):
                    selected_index = 0

        elif bn_B_pd:
            mn_akt = False

        # Проверяем выход персонажа за границы игрового поля
        if PXC < 0:
            PXC = 0
        elif PXC > W - PR_SZ:
            PXC = W - PR_SZ
        if PYC < 0:
            PYC = 0
        elif PYC > H - PR_SZ:
            PYC = H - PR_SZ

        if DETEKT == 0:
            sc.blit(IM_P_UP, (PXC, PYC))
        elif DETEKT == 2:
            sc.blit(IM_P_DN, (PXC, PYC))
        elif DETEKT == 3:
            sc.blit(IM_P_RT, (PXC, PYC))
        elif DETEKT == 1:
            sc.blit(IM_P_LT, (PXC, PYC))

        elif DETEKT == 4:
            sc.blit(IM_P_UP_RG, (PXC, PYC))
        elif DETEKT == 5:
            sc.blit(IM_P_UP_LT, (PXC, PYC))
        elif DETEKT == 6:
            sc.blit(IM_P_DN_RT, (PXC, PYC))
        elif DETEKT == 7:
            sc.blit(IM_P_DN_LT, (PXC, PYC))

        if mn_akt:
            mn_osn()

        DG()
        kn_dp()
        kn_us()
        p.display.update()
        p.time.Clock().tick(FPS)

    p.quit()
    exit()


# Запуск игры
game_loop()