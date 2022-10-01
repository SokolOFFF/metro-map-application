from tkinter import Button

count_of_flags = 0

class StationButton:

    def __init__(self, x, y, f, color1, color2, canvas, root, label1):
        self.x = x
        self.y = y
        self.f = f
        self.c1 = color1
        self.c2 = color2
        self.canvas = canvas
        self.root = root
        self.label1 = label1
        self.button = Button(self.root, text="  ", bg="green", activebackground="green", relief="flat", state="disabled")

        if self.f == 1:
            self.button["bg"] = "orange"
        if self.f == 0:
            self.button["bg"] = self.c1
        self.button.bind('<Button-1>', self.change_button)
        self.button.place(x=self.x + 3, y=self.y)
        if self.f == 0:
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 30, self.y + 30, outline=self.c2,
                               fill=self.c1, width=5)
        if self.f == 1:
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 30, self.y + 30, outline=self.c2,
                               fill="orange", width=5)

    def change_button(self, event):
        global count_of_flags
        if self.f == 0:
            count_of_flags += 1
            if count_of_flags > 2:
                self.label1['text'] = "You can't choose more, than 2 stations"
                count_of_flags -= 1
                return 0
            else:
                self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 30, self.y + 30, outline=self.c2,
                                   fill="orange", width=5)
                self.button["bg"] = "orange"
                self.f = 1
                self.button.place(x=self.x + 3, y=self.y)
                return 0

        if self.f == 1:
            count_of_flags -= 1
            if count_of_flags < 2:
                self.label1['text'] = ""
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 30, self.y + 30, outline=self.c2,
                               fill=self.c1, width=5)
            self.button["bg"] = self.c1
            self.f = 0
            self.button.place(x=self.x + 3, y=self.y)


station_buttons = [None] * 32


def init_stations_buttons(canvas, root, label1):
    # blue line
    station_buttons[1] = StationButton(20, 20, 0, "white", "blue", canvas, root, label1)
    station_buttons[2] = StationButton(140, 120, 0, "gray", "blue", canvas, root, label1)
    station_buttons[3] = StationButton(200, 190, 0, "white", "blue", canvas, root, label1)
    station_buttons[4] = StationButton(280, 260, 0, "white", "blue", canvas, root, label1)
    station_buttons[5] = StationButton(340, 320, 0, "white", "blue", canvas, root, label1)
    station_buttons[6] = StationButton(450, 340, 0, "palevioletred", "blue", canvas, root, label1)
    station_buttons[7] = StationButton(700, 370, 0, "mediumseagreen", "blue", canvas, root, label1)
    station_buttons[8] = StationButton(800, 300, 0, "white", "blue", canvas, root, label1)
    station_buttons[9] = StationButton(920, 360, 0, "white", "blue", canvas, root, label1)
    station_buttons[10] = StationButton(960, 450, 0, "mediumseagreen", "blue", canvas, root, label1)
    station_buttons[11] = StationButton(1060, 550, 0, "white", "blue", canvas, root, label1)

    # red line
    station_buttons[12] = StationButton(400, 200, 0, "white", "palevioletred", canvas, root, label1)
    station_buttons[13] = StationButton(430, 430, 0, "white", "palevioletred", canvas, root, label1)
    station_buttons[14] = StationButton(405, 520, 0, "white", "palevioletred", canvas, root, label1)
    station_buttons[15] = StationButton(380, 600, 0, "white", "palevioletred", canvas, root, label1)
    station_buttons[16] = StationButton(330, 680, 0, "white", "palevioletred", canvas, root, label1)
    station_buttons[17] = StationButton(290, 760, 0, "gray", "palevioletred", canvas, root, label1)
    station_buttons[18] = StationButton(260, 830, 0, "white", "palevioletred", canvas, root, label1)
    station_buttons[19] = StationButton(210, 900, 0, "white", "palevioletred", canvas, root, label1)

    # black line
    station_buttons[20] = StationButton(110, 220, 0, "white", "gray", canvas, root, label1)
    station_buttons[21] = StationButton(120, 360, 0, "white", "gray", canvas, root, label1)
    station_buttons[22] = StationButton(130, 480, 0, "white", "gray", canvas, root, label1)
    station_buttons[23] = StationButton(160, 580, 0, "white", "gray", canvas, root, label1)
    station_buttons[24] = StationButton(200, 680, 0, "white", "gray", canvas, root, label1)
    station_buttons[25] = StationButton(380, 850, 0, "white", "gray", canvas, root, label1)
    station_buttons[26] = StationButton(600, 880, 0, "gray", "mediumseagreen", canvas, root, label1)

    # green line
    station_buttons[27] = StationButton(520, 950, 0, "palevioletred", "mediumseagreen", canvas, root, label1)
    station_buttons[28] = StationButton(640, 770, 0, "white", "mediumseagreen", canvas, root, label1)
    station_buttons[29] = StationButton(680, 670, 0, "white", "mediumseagreen", canvas, root, label1)
    station_buttons[30] = StationButton(705, 580, 0, "blue", "mediumseagreen", canvas, root, label1)
    station_buttons[31] = StationButton(700, 485, 0, "white", "mediumseagreen", canvas, root, label1)
