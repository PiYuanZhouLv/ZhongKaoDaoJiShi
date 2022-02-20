import datetime
import tkinter


root = tkinter.Tk()
root.title('中考倒计时')
# root.geometry('200x100+0+0')
root.attributes('-topmost', True)
root.resizable(False, False)
root.attributes('-toolwindow', True)
closed = False
rop = None


def on_close(*args):
    if not closed:
        close()
    else:
        reopen()


def close(*args):
    global closed, rop
    root.attributes('-alpha', 0.2)
    closed = True
    root.attributes('-transparentcolor', '#F0F0F0')
    rop = root.after(10 * 60 * 1000, reopen)


def reopen(*args):
    global closed
    root.after_cancel(rop)
    root.attributes('-alpha', 0.6)
    closed = False
    root.attributes('-transparentcolor', '')


tkinter.Label(root, text='距离中考还有', font=('default', 20)).pack()
tkinter.Label(root, text=f'{(datetime.date(datetime.date.today().year, 6, 17)-datetime.date.today()).days}天',
              anchor='center', fg='red', font=('default', 30, 'bold')).pack()
root.bind('<Enter>', lambda *args: root.attributes('-alpha', 1.0 if not closed else 0.2))
root.bind('<Leave>', lambda *args: root.attributes('-alpha', 0.6 if not closed else 0.2))
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
