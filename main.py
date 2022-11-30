from tkinter import filedialog
from tkinter import *
import cv2
import os
root = Tk()

root.title('아스키코드로 변환')

root.geometry('1000x800')


def img_path():
    root.file = filedialog.askopenfile(title='파일을 선택하세요')
    txt.configure(text='경로: ' + root.file.name)


def img_ascll():
    chars = ' .,-~:;=!*#%@'
    nw = 100
    img = cv2.imread(root.file.name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    nh = int(h / w * nw)
    img = cv2.resize(img, (nw * 2, nh))
    del_path = str(root.file.name).split('/')

    for i in del_path:
        del_path = i

    re_img = open('/Users/dotslashdash/Downloads/'+del_path[:-3]+'txt', 'w')
    for row in img:
        for pixel in row:
            index = int(pixel / 256 * len(chars))
            re_img.write(chars[index])
        re_img.write('\n')


# 아스키코드 변환 버튼
path_button = Button(root, text='아스키코드로 변환', width=15, command=img_ascll)
path_button.pack(side='bottom')

# 파일 버튼 생성
path_button = Button(root, text='파일 선택', width=15, command=img_path)
path_button.pack(side='bottom')

# 파일 경로
txt = Label(root, text="경로:")
txt.pack(side='bottom')

# GUI 실행
root.mainloop()
