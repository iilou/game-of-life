from os import kill
from tkinter import *
from iterate import *
from math import *

uwu = Tk()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pixelImage=PhotoImage(file = "images/1x1.png")
width=1280
height=720
uwu.geometry("1280x720")
uwu.resizable(False,False)

primarycolour='#ae8bff'
secondarycolor='#94ffca'
color3='#a1f2f7'

row = get_row()
col = get_col()

navcontent = Frame(uwu)
navbar = Frame(uwu, background=primarycolour, width=width, height=120)
sidebar = Frame(uwu, background='#C3C3C3', width=380, height=height-120)
mainview = Frame(uwu, background='#E6E6E6', width=width-380, height=height-120)


cellFrames = [[Frame(uwu, background='#F3F3F3', width=15,height=15, highlightcolor='#E2E2E2',highlightthickness=1) for i in range(60)] for j in range(40)]

navbar.grid(row=0,rowspan=9,column=0,columnspan=100)
sidebar.grid(row=9,rowspan=100,column=0,columnspan=9)
mainview.grid(row=9,rowspan=100,column=9,columnspan=100,ipadx=0,ipady=0)

for i in range(40): 
    for j in range(60):
        cellFrames[i][j].grid(row=i+10,column=j+10)

def hello():
    print("hello")

coords = Label(uwu, text="")
coords.grid(row=48,column=0,columnspan=10,rowspan=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


dragged1 = False
dragged2 = False
running = False

def drag1(event):
    global dragged1
    dragged1 = True

def release1(event):
    global dragged1
    dragged1 = False

def drag2(event):
    global dragged2
    dragged2 = True

def release2(event):
    global dragged2
    dragged2 = False

def paintCell(x, y):
    cr = floor(y / 15)
    cc = floor(x / 15)

    addCell(cr,cc)
    cellFrames[cr][cc].configure(background=secondarycolor)

    coords.configure(text='{}, {}'.format(cr,cc))

def eraseCell(x, y):
    cr = floor(y / 15)
    cc = floor(x / 15)

    killCell(cr,cc)
    cellFrames[cr][cc].configure(background='#F3F3F3')

    coords.configure(text='{}, {}'.format(cr,cc))

def motion(event):
    locx=uwu.winfo_pointerx()
    locy=uwu.winfo_pointery()
    x=uwu.winfo_pointerx() - uwu.winfo_rootx()
    y=uwu.winfo_pointery() - uwu.winfo_rooty()
    # print('{}, {}'.format(x,y))
    # coords.configure(text='{}, {}'.format(x,y))

    if running: return

    if dragged1:
        paintCell(x - 380, y-120)

    elif dragged2:
        eraseCell(x - 380, y - 120)


init_grid(40,60)

def run():
    if running:
        mp = iterate()
        for i in range(40): 
            for j in range(60):

                if mp[i + 1][j + 1] == 0 :
                    cellFrames[i][j].configure(background='#B2B2B2', highlightcolor='#B2B2B2')
                else:
                    cellFrames[i][j].configure(background=color3, highlightcolor=color3)
    if running: uwu.after(1000, run)
    else: end_sim()
     

def end_sim():
    global running
    running = False

    mp = get_map()
    for i in range(40): 
        for j in range(60):
            if mp[i + 1][j + 1] == 0:
                cellFrames[i][j].configure(background='#F3F3F3', highlightcolor='#E2E2E2')
            else: cellFrames[i][j].configure(background=secondarycolor, highlightcolor='#E2E2E2')

    startSimButton.configure(text="Start Simulation", command=start_sim)

def end_init():
    global running
    running = False

    # uwu.after(1000,end_sim)

def start_sim():
    global running
    running = True

    mp = get_map()
    for i in range(40): 
        for j in range(60):
            if mp[i + 1][j + 1] == 0:
                cellFrames[i][j].configure(background='#858585', highlightcolor='#B2B2B2')
            else: cellFrames[i][j].configure(background=color3, highlightcolor=color3)


    startSimButton.configure(text="End Simulation", command=end_init)

    run()


startSimButton = Button(uwu, text="Start Simulation", font=("Calibri, 32"),bg=secondarycolor ,fg='#FFFFFF', borderwidth=0, command=start_sim)

startSimButton.grid(row=36,column=0,rowspan=20,columnspan=9)

uwu.bind("<Motion>", motion)
uwu.bind("<Button-1>",drag1)
uwu.bind("<ButtonRelease-1>",release1)
uwu.bind("<Button-3>",drag2)
uwu.bind("<ButtonRelease-3>",release2)
uwu.mainloop()