import sys
from tkinter import *

import stations_buttons_config
from stations_config import station_name, put_stations_name, distance_between_stations
from lines_config import lines, draw_lines_between_stations
from stations_buttons_config import init_stations_buttons, station_buttons


def find_path(event):
    count_of_flags = stations_buttons_config.count_of_flags
    pp = []
    report = [0] * 31
    length = [[1000000 for i in range(2)] for j in range(31)]
    for i in range(31):
        length[i][1] = -1
    if count_of_flags < 2:
        label1['text'] = "I can't do it"
        return 0
    if count_of_flags == 2:
        label1['text'] = ""
        for i in range(32):
            if station_buttons[i] is not None:
                if station_buttons[i].f == 1:
                    pp.append(i)
        be = pp[0] - 1
        en = pp[1] - 1
        length[be][0] = 0
        length[be][1] = be
        report[be] = 1
        for i in range(31):
            if distance_between_stations[be][i] > 0:
                length[i][0] = min(length[i][0], length[be][0] + distance_between_stations[be][i])
                length[i][1] = be

        while 1:
            minn = 10000000
            v = -12312
            for i in range(31):
                if length[i][0] < minn and report[i] == 0:
                    minn = length[i][0]
                    v = i
            if minn == 10000000:
                break

            for i in range(31):
                if report[i] == 0 and i != v and distance_between_stations[v][i] > 0:
                    if length[i][0] > length[v][0] + distance_between_stations[v][i]:
                        length[i][0] = length[v][0] + distance_between_stations[v][i]
                        length[i][1] = v
            report[v] = 1

        q = [en + 1]
        p = en
        while length[p][1] != be:
            q.append(length[p][1] + 1)
            p = length[p][1]
        q.append(be + 1)
        for i in range(len(q) - 1):
            lines[q[i]][q[i + 1]].__init__(lines[q[i]][q[i + 1]].x1, lines[q[i]][q[i + 1]].y1, lines[q[i]][q[i + 1]].x2,
                                           lines[q[i]][q[i + 1]].y2, "orange", 13)
            lines[q[i]][q[i + 1]].draw(canvas)
        for i in q:
            station_buttons[i].__init__(station_buttons[i].x, station_buttons[i].y, station_buttons[i].f, "orange", "black", canvas, root, label1)

        def show_stations(event):
            label2["text"] = ""
            for i in q:
                label2["text"] += station_name[i]
                label2["text"] += "\n"

        show_name = Button(canvas, text="SHOW", width=20, bg="tan", height=3, activebackground="tan")
        show_name.bind('<Button-1>', show_stations)
        show_name.place(x=1650, y=760)


def exi(event):
    sys.exit()


root = Tk()
root.title("СОКОЛОВ МЕТРО. Навигация по Горьковскому метрополитену в 2040 году")
root.geometry('1920x1080')

canvas = Canvas()
canvas.create_line(1500, 0, 1500, 1080, fill="black", width=5)
canvas.create_line(1100, 0, 1100, 1080, fill="black", width=5)

label1 = Label(root, text="", bg="lightblue", width=31, font="Arial 15", fg="navy")
label1.place(x=1530, y=100)

label2 = Label(root, text="", width=20, font="Arial 20", bg="lightblue", fg="navy")
label2.place(x=1140, y=100)

quit = Button(canvas, text="QUIT", width=20, bg="tan", height=3)
quit.bind('<Button-1>', exi)
quit.place(x=1650, y=900)

start_button = Button(canvas, text="START", width=20, bg="tan", height=3, activebackground="tan")
start_button.bind('<Button-1>', find_path)
start_button.place(x=1650, y=830)

put_stations_name(canvas)
draw_lines_between_stations(canvas)
init_stations_buttons(canvas, root, label1)

canvas.pack(fill=BOTH, expand=1)
root.mainloop()
