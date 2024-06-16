# -*- coding: utf-8 -*-
import sys
import time
import tkinter as tk
import qrcode as cd
import tkinter.messagebox as tkm
import tkinter.ttk
from PIL import Image


# 进度条函数
def show():
    # 进度条
    progressbarOne = tk.ttk.Progressbar(window, length=sw / 2, orient=tkinter.HORIZONTAL)
    progressbarOne.pack(side=tk.LEFT)
    progressbarOne.place(rely=0.9)
    # 样式设置
    s = tk.ttk.Style()
    s.theme_use('winnative')  # clam, alt, default, classic, vista, aqua, xpnative, winnative
    # 进度值最大值
    progressbarOne['maximum'] = 100
    # 进度值初始值
    progressbarOne['value'] = 0
    for i in range(1, 101):
        progressbarOne['value'] = i
        # 更新画面
        window.update()
        time.sleep(0.05)


# 生成二维码
def main_pro(txt, l2, l1, gl):
    try:
        code = cd.QRCode(
            version=1,
            error_correction=cd.constants.ERROR_CORRECT_H,  # 容错率为高
            box_size=10,
            border=4,
        )
    except UnicodeEncodeError:
        tkm.showwarning(title='UnicodeEncodeError',
                        message=f'UnicodeEncodeError: '
                                f'\n\'latin-1\' codec can\'t encode characters in position 0-{len(txt)}'
                                f'\nClick \"确定\" and QUIT')
        sys.exit()
    show()
    code.add_data(txt)
    code.make(fit=True)
    try:
        code_img = code.make_image(fill_color=l2, back_color=l1)
    except ValueError:
        tkm.showwarning(title='ValueError',
                        message=f'ValueError: \n'
                                f'unknown color specifier: {l2} or {l1}\n'
                                f'Click \"确定\" and QUIT')
        sys.exit()
    code_size_w, code_size_h = code_img.size
    ratio = 6
    if gl == '*.png':
        pass
    else:  # 粘贴图片
        logo = Image.open(gl)
        logo_w, logo_h = int(code_size_w / ratio), int(code_size_h / ratio)
        icon = logo.resize((logo_w, logo_h), 5)  # Use Image.Resampling.NEAREST (0), Image.Resampling.LANCZOS (1),
        # Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3), Image.Resampling.BOX (4) or
        # Image.Resampling.HAMMING (5)
        x, y = int((code_size_w - logo_w) / 2), int((code_size_h - logo_h) / 2)
        code_img.paste(icon, (x, y))
    time.sleep(2)
    # code_img.show()
    tkm.showinfo(message='二维码已生成，请在程序所在目录查找\n\"code.png\"', title='提示信息')
    with open('code.png', 'wb') as file:
        code_img.save(file)


def part1():
    a, b, c, d = url.get(), choose_color2.get(), choose_color1.get(), get_logo.get()
    print('Loading......')
    main_pro(a, b, c, d)


def part0():
    main_label = tk.Label(window, text='QR-Code Maker',
                          font=(r'C:\Windows\Fonts\msyh.ttc', 20),
                          fg='#000000',
                          compound='center')
    main_label.place(relx=0.5, rely=0.05, anchor='center')


if __name__ == '__main__':
    # 主窗口
    window = tk.Tk()
    window.title('QR-Code Maker')
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    win_info = f'{int(sw / 2)}x{int(sh / 2)}+{int(sw / 4)}+{int(sh / 4)}'
    window.geometry(win_info)
    window.resizable(False, False)
    part0()
    # 标签
    label = tk.Label(window,
                     text='输入内容',
                     font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                     fg='#000000',
                     compound='center'
                     )
    # 输入框
    url = tk.StringVar()
    input_ing = tk.Entry(window, width=50, textvariable=url)
    input_ing.delete(0, 0)
    # input_ing.insert(0, "默认文本...")
    label.place(relx=0.15, rely=0.2)
    input_ing.place(relx=0.35, rely=0.2)

    # 背景颜色
    choose_color1 = tk.StringVar()
    cc1 = tk.Entry(window, width=50, textvariable=choose_color1)
    cc1.delete(0, 'end')
    cc1.insert(0, '#ffffff')

    label1 = tk.Label(window,
                      text='背景颜色',
                      font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                      fg='#000000',
                      compound='center')
    label1.place(relx=0.15, rely=0.3)
    cc1.place(relx=0.35, rely=0.3)

    # 前景颜色
    choose_color2 = tk.StringVar()
    cc2 = tk.Entry(window, width=50, textvariable=choose_color2)
    cc2.delete(0, 'end')
    cc2.insert(0, '#000000')

    label2 = tk.Label(window,
                      text='前景颜色',
                      font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                      fg='#000000',
                      compound='center')
    label2.place(relx=0.15, rely=0.4)
    cc2.place(relx=0.35, rely=0.4)

    # 获取中部图片
    label3 = tk.Label(window,
                      text='LOGO',
                      font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                      fg='#000000',
                      compound='center')
    get_logo = tk.StringVar()
    tl = tk.Entry(window, width=50, textvariable=get_logo)
    tl.delete(0, 'end')
    tl.insert(0, '*.png')
    label3.place(relx=0.15, rely=0.5)
    tl.place(relx=0.35, rely=0.5)

    func = tk.Button(window,
                     text='生成',
                     fg="#000000",
                     width=7,
                     compound='center',
                     command=part1)
    # 把部件贴上去
    func.place(anchor='center', relx=0.5, rely=0.7)

    window.mainloop()
