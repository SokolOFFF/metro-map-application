class Lines:
    def __init__(self, x1, y1, x2, y2, color, wid):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.wid = wid

    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color, width=self.wid)


lines = [[None for i in range(50)] for j in range(50)]

# blue line
lines[1][2] = Lines(20, 20, 140, 120, "blue", 13)
lines[2][1] = Lines(20, 20, 140, 120, "blue", 13)
lines[2][3] = Lines(140, 120, 200, 190, "blue", 13)
lines[3][2] = Lines(140, 120, 200, 190, "blue", 13)
lines[3][4] = Lines(280, 260, 200, 190, "blue", 13)
lines[4][3] = Lines(280, 260, 200, 190, "blue", 13)
lines[4][5] = Lines(280, 260, 340, 320, "blue", 13)
lines[5][4] = Lines(280, 260, 340, 320, "blue", 13)
lines[5][6] = Lines(460, 350, 350, 330, "blue", 13)
lines[6][5] = Lines(460, 350, 350, 330, "blue", 13)
lines[6][7] = Lines(460, 350, 700, 378, "blue", 13)
lines[7][6] = Lines(460, 350, 700, 378, "blue", 13)
lines[7][8] = Lines(700, 388, 800, 320, "blue", 13)
lines[8][7] = Lines(700, 388, 800, 320, "blue", 13)
lines[8][9] = Lines(800, 305, 920, 365, "blue", 13)
lines[9][8] = Lines(800, 305, 920, 365, "blue", 13)
lines[9][10] = Lines(925, 365, 965, 450, "blue", 13)
lines[10][9] = Lines(925, 365, 965, 450, "blue", 13)
lines[10][11] = Lines(1060, 550, 955, 450, "blue", 13)
lines[11][10] = Lines(1060, 550, 955, 450, "blue", 13)

# red line
lines[12][6] = Lines(456, 340, 407, 200, "palevioletred", 13)
lines[6][12] = Lines(456, 340, 407, 200, "palevioletred", 13)
lines[6][13] = Lines(463, 340, 445, 430, "palevioletred", 13)
lines[13][6] = Lines(463, 340, 445, 430, "palevioletred", 13)
lines[13][14] = Lines(421, 520, 445, 430, "palevioletred", 13)
lines[14][13] = Lines(421, 520, 445, 430, "palevioletred", 13)
lines[14][15] = Lines(421, 520, 395, 600, "palevioletred", 13)
lines[15][14] = Lines(421, 520, 395, 600, "palevioletred", 13)
lines[15][16] = Lines(348, 680, 395, 600, "palevioletred", 13)
lines[16][15] = Lines(348, 680, 395, 600, "palevioletred", 13)
lines[16][17] = Lines(348, 680, 305, 760, "palevioletred", 13)
lines[17][16] = Lines(348, 680, 305, 760, "palevioletred", 13)
lines[17][18] = Lines(275, 830, 310, 760, "palevioletred", 13)
lines[18][17] = Lines(275, 830, 310, 760, "palevioletred", 13)
lines[18][19] = Lines(280, 830, 230, 900, "palevioletred", 13)
lines[19][18] = Lines(280, 830, 230, 900, "palevioletred", 13)
lines[19][27] = Lines(520, 960, 230, 913, "palevioletred", 13)
lines[27][19] = Lines(520, 960, 230, 913, "palevioletred", 13)

# green line
lines[27][26] = Lines(520, 975, 600, 900, "mediumseagreen", 13)
lines[26][27] = Lines(520, 975, 600, 900, "mediumseagreen", 13)
lines[26][28] = Lines(655, 770, 610, 900, "mediumseagreen", 13)
lines[28][26] = Lines(655, 770, 610, 900, "mediumseagreen", 13)
lines[28][29] = Lines(655, 770, 695, 670, "mediumseagreen", 13)
lines[29][28] = Lines(655, 770, 695, 670, "mediumseagreen", 13)
lines[29][30] = Lines(720, 580, 695, 670, "mediumseagreen", 13)
lines[30][29] = Lines(720, 580, 695, 670, "mediumseagreen", 13)
lines[30][31] = Lines(710, 485, 715, 580, "mediumseagreen", 13)
lines[31][30] = Lines(710, 485, 715, 580, "mediumseagreen", 13)
lines[31][7] = Lines(710, 485, 710, 370, "mediumseagreen", 13)
lines[7][31] = Lines(710, 485, 710, 370, "mediumseagreen", 13)
lines[30][10] = Lines(705, 595, 960, 465, "mediumseagreen", 13)
lines[10][30] = Lines(705, 595, 960, 465, "mediumseagreen", 13)

# black line
lines[2][20] = Lines(152, 120, 123, 220, "gray", 13)
lines[20][2] = Lines(152, 120, 123, 220, "gray", 13)
lines[20][21] = Lines(130, 360, 120, 220, "gray", 13)
lines[21][20] = Lines(130, 360, 120, 220, "gray", 13)
lines[21][22] = Lines(140, 480, 130, 360, "gray", 13)
lines[22][21] = Lines(140, 480, 130, 360, "gray", 13)
lines[22][23] = Lines(135, 480, 165, 580, "gray", 13)
lines[23][22] = Lines(135, 480, 165, 580, "gray", 13)
lines[23][24] = Lines(206, 680, 165, 580, "gray", 13)
lines[24][23] = Lines(206, 680, 165, 580, "gray", 13)
lines[17][24] = Lines(206, 690, 290, 760, "gray", 13)
lines[24][17] = Lines(206, 690, 290, 760, "gray", 13)
lines[17][25] = Lines(290, 760, 380, 850, "gray", 13)
lines[25][17] = Lines(290, 760, 380, 850, "gray", 13)
lines[26][25] = Lines(600, 890, 380, 860, "gray", 13)
lines[25][26] = Lines(600, 890, 380, 860, "gray", 13)


def draw_lines_between_stations(canvas):
    for i in range(1, 50):
        for j in range(1, 50):
            if lines[i][j] is not None:
                lines[i][j].draw(canvas)
