# This is built by googletrans package.
# Import package
import tkinter as tk
import tkinter.messagebox as tkMsg
from tkinter import ttk
import googletrans


# Initial
translator = googletrans.Translator()

# Langcode dict
langcode = {'英文': 'en', '繁體中文': 'zh-tw', '日文': 'ja', '韓文': 'ko'}

# Basic Translate
# results = translator.translate()

# GUI
win = tk.Tk()
win.title('翻譯小工具')
win.geometry('250x200+200+200')
win.resizable(0, 0)
win.attributes('-alpha', 0.9)
win.config(background='#323232')

# Button event function


def comfirm_clicked(tmp=1):
    try:
        src = ip_value.get()
        lang = lang_cb.get()
        if len(src) <= 35:
            result = translator.translate(src, dest=langcode.get(lang))
            op_value.set(result.text)
        else:
            tkMsg.showerror('字數過長！', '請別輸入超過20個字元！')
    except TypeError:
        tkMsg.showerror('輸入空白！', '輸入不得留白！')


def quit_clicked():
    win.destroy()


# Bind keyboard
win.bind('<Return>', comfirm_clicked)

# Label
op_value = tk.StringVar()
style = ttk.Style().configure('TLabel', background='#323232',
                              foreground='white', font='微軟正黑體 12')
input_lbl = ttk.Label(win, text='輸入:').place(x=20, y=10)
ouput_lbl = ttk.Label(win, text='輸出:').place(x=20, y=45)
ouput_result = ttk.Label(win, textvariable=op_value,
                         wraplength=150,
                         justify='left').place(x=70, y=45)

# Entry
ip_value = tk.StringVar()
input_entry = ttk.Entry(win, textvariable=ip_value).place(
    x=70, y=12, width=160)

# ComboBox
lang_cb = ttk.Combobox(
    win, values=[
        "英文",
        "繁體中文",
        "日文",
        "韓文"],
    state="readonly",)

lang_cb.place(x=160, y=150, width=75)
lang_cb.current(0)

# Button
style = ttk.Style().configure('TButton', font='微軟正黑體 10', width=5)
comfirm_btn = ttk.Button(
    win, text='確認', command=comfirm_clicked).place(x=20, y=150)
quit_btn = ttk.Button(win, text='關閉', command=quit_clicked).place(x=80, y=150)


# Main
if __name__ == '__main__':
    win.mainloop()
