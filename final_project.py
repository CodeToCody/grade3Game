import tkinter
import random

# 輸入按鍵
key = ""
koff = False


def key_down(e):  # 按下按鍵會觸發的函式在這裡
    global key, koff
    key = e.keysym
    koff = False


def key_up(e):  # 放開按鍵會觸發的函式在這裡
    global key
    key = ""


# 定義角色移動變數
DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]  # 動作的連貫圖片順序
BLINK = ["#fff", "#ffc", "#ff8", "#fe4", "#ff8", "#ffc"]

idx = 0
# 計時器
tmr = 0
# 獲得分數
score = 0
candy = 0
stage = 1  # 關卡數

# 移動物件座標
pen_x = 0
pen_y = 0
pen_d = 0  # 方向
pen_a = 0  # 影像編號

# 敵人座標
red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0  # red起始位置的x座標
red_sy = 0  # red起始位置的y座標

map_data = []


def set_stage():  # ---------------------------------------------------設定關卡
    global map_data, candy
    global red_sx, red_sy
    if stage == 1:
        # 地圖設計
        # 0是整塊冰 1是往上會遇到的冰 2是沒有東西的路
        map_data = [
            [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
            [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
            [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
            [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
            [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
            [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
            [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 32
        red_sx = 630
        red_sy = 450
    if stage == 2:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 3, 0],
            [0, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 0],
            [0, 2, 1, 3, 3, 3, 3, 3, 3, 1, 2, 0],
            [0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 0],
            [0, 3, 3, 1, 2, 1, 1, 2, 1, 3, 3, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 38
        red_sx = 630
        red_sy = 90
    if stage == 3:
        map_data = [
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 1, 3, 1, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0],
            [0, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 0],
            [0, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 3, 3, 2, 2, 2, 0, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 23
        red_sx = 630
        red_sy = 450
    if stage == 4:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 3, 0, 3, 3, 1, 3, 0, 3, 0, 3, 0],
            [0, 3, 1, 0, 3, 3, 3, 0, 3, 1, 3, 0],
            [0, 3, 3, 0, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 0, 1, 3, 3, 3, 1, 3, 3, 3, 0],
            [0, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 50
        red_sx = 150
        red_sy = 270
        #kuma_sx = 510
        #kuma_sy = 270
        #kuma_sd = DIR_UP
    if stage == 5:
        map_data = [
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 0, 3, 0, 1, 3, 3, 1, 0, 3, 0],
            [0, 2, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0],
            [0, 2, 1, 3, 1, 1, 3, 3, 1, 1, 3, 0],
            [0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 40
        red_sx = 630
        red_sy = 450
        #kuma_sx = 390
        #kuma_sy = 210
        #kuma_sd = DIR_RIGHT


def set_chara_pos():  # ------------------------------------------------角色初始位置設定
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    # 設定角色座標
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN  # 角色面向下
    pen_a = 3  # 操控角色起始動作的圖片
    # 設定敵人座標
    # 帶入sx和sy
    red_x = 630
    red_y = 450
    red_d = DIR_DOWN  # 敵人面向下
    red_a = 3  # 敵人起始動作的圖片


def draw_txt(txt, x, y, siz, col):  # ---------------------------------------------------分數文字顯示函數
    fnt = ("Consolas", siz, "bold")  # 調整字體還有大小
    canvas.create_text(x+2, y+2, text=txt, fill="black",
                       font=fnt, tag="SCREEN")  # 直接先印黑色的字然後偏移就變成等一下要印的字的陰影
    canvas.create_text(x, y, text=txt, fill=col,
                       font=fnt, tag="SCREEN")  # 做出字體


def draw_screen():  # ----------------------------------------------------- 繪製遊戲畫面
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            # 用圖塊繪製迷宮
            # 已知img_bg中那些圖片是甚麼意思，把想要的畫面輸入進map_data，這裡把它印出來
            canvas.create_image(
                x*60+30, y*60+30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(
        pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")  # 顯示操控角色物件
    canvas.create_image(
        red_x, red_y, image=img_red[red_a], tag="SCREEN")  # 顯示敵人
    draw_txt("SCORE: "+str(score), 200, 30, 30, "orange")  # 顯示分數
    draw_txt("STAGE: "+str(stage), 520, 30, 30, "lime")  # 顯示關卡數


def check_wall(cx, cy, di, dot):  # ----------------------------------------------------確認每個方向是否有牆壁
    chk = False  # 把False帶入chk
    if di == DIR_UP:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1:  # 左上
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:  # 右上
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1:  # 左下
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:  # 右下
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:  # 左上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1:  # 左下
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:  # 右上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1:  # 右下
            chk = True
    return chk


def move_penpen():  # ------------------------------------------------移動操控角色 將60下修為20 讓腳色移動看起來更順暢
    global score, candy, pen_x, pen_y, pen_d, pen_a
    if key == "Up":
        pen_d = DIR_UP  # 操控角色面向
        if check_wall(pen_x, pen_y, pen_d, 20) == False:  # 如果20單位後不是牆壁
            pen_y = pen_y - 20
    if key == "Down":
        pen_d = DIR_DOWN  # 操控角色面向
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    if key == "Left":
        pen_d = DIR_LEFT  # 操控角色面向
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    if key == "Right":
        pen_d = DIR_RIGHT  # 操控角色面向
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d*3 + ANIMATION[tmr % 4]  # 計算 並圖片轉換 ->動態
    mx = int(pen_x/60)
    my = int(pen_y/60)
    # 如果踩到3(印有糖果的圖片)，加100分，然後把圖片換成沒有糖果的圖片，看起來就會是糖果被吃掉了
    if map_data[my][mx] == 3:
        score = score + 100
        map_data[my][mx] = 2
        candy = candy - 1


def move_enemy():
    global idx, tmr, red_x, red_y, red_d, red_a
    speed = 10
    if red_x % 60 == 30 and red_y % 60 == 30:  # 剛好在圖片上時隨機改變方向
        # 增加一點敵人往角色移動的趨勢
        red_d = random.randint(0, 6)
        if red_d >= 4:
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
    # 各個方向判斷若非牆壁便向那個方向移動
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d*3 + ANIMATION[tmr % 4]  # 計算 並圖片轉換 ->動態
    # 如果接觸到角色 idx變成2 tmr歸0 進行攻擊
    if abs(red_x-pen_x) <= 40 and abs(red_y - pen_y) <= 40:
        idx = 2
        tmr = 0


def main():  # ----------------------------------------------------------------主要迴圈
    # 隨著時間進行不斷的判斷各種撞牆吃分數之類的，並以100微秒更新
    global key, koff, idx, tmr, score, stage
    tmr = tmr + 1
    draw_screen()
    if idx == 0:  # 標題畫面(idx為0意思是到遊戲開頭)
        canvas.create_image(360, 200, image=img_title, tag="SCREEN")
        if tmr % 10 < 5:  # -------------------------------------------------tmr除10餘不超過5
            draw_txt("Press SPACE !", 360, 380, 30, "yellow")
            if key == "space":
                stage = 1
                score = 0
                set_stage()
                set_chara_pos()
                idx = 1
    if idx == 1:  # 玩遊戲
        move_penpen()
        move_enemy()
        if candy == 0:
            idx = 4  # idx變4 後面會檢驗就過關
            tmr = 0  # tmr變0
    if idx == 2:  # 被敵人攻擊
        draw_txt("GAME OVER", 360, 270, 40, "red")
        if tmr == 50:
            idx = 0
    # -----------------------------------------idx拿來判斷 idx為4是遊戲通關意思
    if idx == 4:
        if stage < 5:
            draw_txt("STAGE CLEAR!", 360, 720, 40, "pink")
        else:
            draw_txt("ALL STAGE CLEAR!", 360, 270, 40, "violet")
        if tmr == 30:
            if stage < 5:
                stage = stage + 1
                set_stage()
                set_chara_pos()
                idx = 1
            else:
                idx = 5
                tmr = 0
    if idx == 5:  # 結尾
        if tmr < 60:
            xr = 8*tmr
            yr = 6*tmr
            canvas.create_oval(360-xr, 270-yr, 360+xr, 270 +
                               yr, fil="black", tag="SCREEN")
        else:
            canvas.create_rectangle(0, 0, 720, 540, fill="black", tag="SCREEN")
            canvas.create_image(360, 360, image=img_ending, tag="SCREEN")
            draw_txt("Congratulations!", 360, 160, BLINK[tmr % 6])
        if tmr == 300:
            idx = 0
    if koff == True:
        key = ""
        koff = False
    root.after(100, main)  # 從300縮成100


root = tkinter.Tk()
# ------------------------------------------------------------------------------地圖的四個圖片
img_bg = [
    tkinter.PhotoImage(
        file="./image_penpen/chip00.png"),
    tkinter.PhotoImage(
        file="./image_penpen/chip01.png"),
    tkinter.PhotoImage(
        file="./image_penpen/chip02.png"),
    tkinter.PhotoImage(file="./image_penpen/chip03.png")
]
# -------------------------------------------------------------------------------讓操控角色藉這些圖片(以產生動態錯覺)
img_pen = [
    tkinter.PhotoImage(file="./image_penpen/pen00.png"),
    tkinter.PhotoImage(file="./image_penpen/pen01.png"),
    tkinter.PhotoImage(file="./image_penpen/pen02.png"),
    tkinter.PhotoImage(file="./image_penpen/pen03.png"),
    tkinter.PhotoImage(file="./image_penpen/pen04.png"),
    tkinter.PhotoImage(file="./image_penpen/pen05.png"),
    tkinter.PhotoImage(file="./image_penpen/pen06.png"),
    tkinter.PhotoImage(file="./image_penpen/pen07.png"),
    tkinter.PhotoImage(file="./image_penpen/pen08.png"),
    tkinter.PhotoImage(file="./image_penpen/pen09.png"),
    tkinter.PhotoImage(file="./image_penpen/pen10.png"),
    tkinter.PhotoImage(file="./image_penpen/pen11.png")
]
# --------------------------------------------------------------------------------敵人的圖片庫
img_red = [
    tkinter.PhotoImage(file="./image_penpen/red00.png"),
    tkinter.PhotoImage(file="./image_penpen/red01.png"),
    tkinter.PhotoImage(file="./image_penpen/red02.png"),
    tkinter.PhotoImage(file="./image_penpen/red03.png"),
    tkinter.PhotoImage(file="./image_penpen/red04.png"),
    tkinter.PhotoImage(file="./image_penpen/red05.png"),
    tkinter.PhotoImage(file="./image_penpen/red06.png"),
    tkinter.PhotoImage(file="./image_penpen/red07.png"),
    tkinter.PhotoImage(file="./image_penpen/red08.png"),
    tkinter.PhotoImage(file="./image_penpen/red09.png"),
    tkinter.PhotoImage(file="./image_penpen/red10.png"),
    tkinter.PhotoImage(file="./image_penpen/red11.png")
]
# ---------------------------------------------------------------------------------標題圖片
img_title = tkinter.PhotoImage(
    file="./image_penpen/title.png")
# ------------------------------------------------------------結尾影像
img_ending = tkinter.PhotoImage(
    file="./image_penpen/ending.png")


root.title("死暈船仔")
root.resizable(False, False)
# 設定按下還有放開案件觸發的函數
# key_down和key_up寫在上面
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=720, height=540)
canvas.pack()
set_stage()
set_chara_pos()
main()
root.mainloop()
