# -*- coding: utf-8 -*-
import sys
import time
import tkinter as tk
import pyqrcode as pcd
import tkinter.messagebox as tkm
import tkinter.ttk


# 进度条函数
def show():
    for i in range(1, 101):
        progressbarOne['value'] = i
        # 更新画面
        window.update()
        time.sleep(0.05)


# 生成二维码
def main_pro():
    try:
        txt = url.get()
        code = pcd.create(txt)
    except UnicodeEncodeError:
        tkm.showwarning(title='UnicodeEncodeError',
                        message=f'UnicodeEncodeError: '
                                f'\n\'latin-1\' codec can\'t encode characters in position 0-{len(txt)}'
                                f'\nClick \"确定\" and quit')
        sys.exit()
    show()
    code.png('url_png.png', scale=8)
    time.sleep(2)
    tkm.showinfo(message='二维码已生成，请在程序所在目录查找\n\"url_png.png\"', title='提示信息')


# 主窗口
window = tk.Tk()
window.title('二维码生成器')
sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
win_info = f'{int(sw / 2)}x{int(sh / 2)}+{int(sw / 4)}+{int(sh / 4)}'
window.geometry(win_info)
window.resizable(False, False)
# 标签
label = tk.Label(window,
                 text='请在下方输入内容',
                 font=(r'C:\Windows\Fonts\msyh.ttc', 15),
                 fg='#000000',
                 width=30,
                 compound='center')
# 输入框
url = tk.StringVar()
input_ing = tk.Entry(window, width=50, textvariable=url)
input_ing.delete(0, "end")
# input_ing.insert(0, "默认文本...")
# 按钮
func = tk.Button(window,
                 text='生成',
                 fg="#000000",
                 width=7,
                 compound='center',
                 command=main_pro)
# 把部件贴上去
label.place(anchor='center', relx=0.5, rely=0.2)
input_ing.place(anchor='center', relx=0.5, rely=0.3)
func.place(anchor='center', relx=0.5, rely=0.4)

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

window.mainloop()
