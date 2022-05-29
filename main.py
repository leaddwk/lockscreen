from tkinter import *

root = Tk()

pressed_f4 = False  # Is Alt-F4 pressed?


def do_exit():
    global pressed_f4
    if pressed_f4:  # Deny if Alt-F4 is pressed
        pressed_f4 = False  # Reset variable


root.bind('<Alt-F4>', do_exit)
root.bind('<Escape>', do_exit)
root.protocol("WM_DELETE_WINDOW", do_exit)


def bvalue():
    value1 = e1.get()
    if value1 == "taskkill":
        root.destroy()
    elif value1 == "destroy":
        root.destroy()
    elif value1 == "redeemcodeboom":
        root.destroy()
    else:
        pass


# root.iconbitmap('login.ico')
# root.iconphoto(False, PhotoImage(file='login.png'))
root.wm_attributes("-topmost", 1)
root.attributes('-fullscreen', True)
e1 = Entry(root)
e1.insert(0, '리딤코드 입력!')
e1.pack()
button1 = Button(root, text="얻기", command=bvalue)
button1.pack()
root.wm_attributes('-alpha', 0.1)

root.mainloop()
# -----------------------------

secu = 0
inFp = open("settings.set", "r", encoding='utf-8')
outFp = open("settings.set", "w", encoding="utf-8")
for inStr in inFp.readlines():
    out_str = ""
    for s in inStr:
        tmp = ord(s) + secu
        out_str += chr(tmp)
    outFp.writelines(out_str)

inFp.close()
outFp.close()
# -------------------------
outFp = None
outStr = ""
outFp = open("/settings.set", "w")

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr+"\n")
    else:
        break
outFp.close()