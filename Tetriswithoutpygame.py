from tkinter import *
from copy import *
from random import randint
import time
from copy import deepcopy

class Create_tetraminos:
    def __init__(self,Tetris):
        self.Tetris = Tetris
        
        self.pieces = [[[[0,0,0,0],
                        [1,1,1,1],
                        [0,0,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,2,2,0],
                        [0,0,2,0],
                        [0,0,2,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,4,4,0],
                        [0,0,4,4],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,5,5,0],
                        [5,5,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,6,0],
                        [0,6,6,6],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,7,7,0],
                        [0,7,0,0],
                        [0,7,0,0]
                       ]],
                       [[[0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0]
                       ],
                       [[0,0,0,0],
                        [0,0,0,2],
                        [0,2,2,2],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,4,0],
                        [0,4,4,0],
                        [0,4,0,0],
                        [0,0,0,0]
                       ],
                       [[0,5,0,0],
                        [0,5,5,0],
                        [0,0,5,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,6,0],
                        [0,0,6,6],
                        [0,0,6,0]
                       ],
                       [[0,0,0,0],
                        [7,7,7,0],
                        [0,0,7,0],
                        [0,0,0,0]
                       ]],
                       [[[0,0,0,0],
                        [1,1,1,1],
                        [0,0,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,2,0,0],
                        [0,2,0,0],
                        [0,2,2,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,4,4,0],
                        [0,0,4,4],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,5,5,0],
                        [5,5,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,0,0],
                        [0,6,6,6],
                        [0,0,6,0]
                       ],
                       [[0,0,0,0],
                        [0,0,7,0],
                        [0,0,7,0],
                        [0,7,7,0]
                       ]],
                       [[[0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0]
                       ],
                       [[0,0,0,0],
                        [0,2,2,2],
                        [0,2,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,4,0],
                        [0,4,4,0],
                        [0,4,0,0],
                        [0,0,0,0]
                       ],
                       [[0,5,0,0],
                        [0,5,5,0],
                        [0,0,5,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,6,0],
                        [0,6,6,0],
                        [0,0,6,0]
                       ],
                       [[0,0,0,0],
                        [7,0,0,0],
                        [7,7,7,0],
                        [0,0,0,0]
                       ]]]
                
        self.grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],]
        
        self.score = 0
        self.lignes_detruite = 0
        self.jeuTemps = int(time.time())
        self.defaite = False
        self.saved = False
        self.rotation = 0
        self.random = randint(0,6)
        self.colors = ["blue", "yellow", "pink", "green", "cyan", "red", "orange"]
        self.pieceId = 1
        self.tetra = deepcopy(self.pieces[self.rotation][self.random])
        self.tetra_x = 6
        self.tetra_y = 3
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.random+1:
                    self.tetra[j][i] = self.pieceId
        
    
    def cadriage(self):
        couleur = 'black'
        #self.Tetris.create_rectangle(0,0,400,800,fill=couleur)
        for i in range(0, 400, 40):
            couleur = 'white'
            self.Tetris.create_rectangle(i, 0, i+2, 800,fill=couleur)
        for i in range(0, 800, 40):
            couleur = 'white'
            self.Tetris.create_rectangle(0, i, 400, i+2,fill=couleur)

    def draw_game(self):
        self.Tetris.delete("all")
        for i in range(3,13):
            for j in range(2,22):
                if self.grid[j][i] != 0 and self.defaite:
                    couleur = 'red'
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)
                elif self.grid[j][i] == self.pieceId:
                    couleur = self.colors[self.random]
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)
                elif self.grid[j][i] == 0:
                    couleur = 'black'
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)

    def collagePiece(self):
        for j in range(0,4):
            for i in range(0,4):
                if self.grid[j+self.tetra_y][i+self.tetra_x] == 0:
                    if self.tetra[j][i] == self.pieceId:
                        self.grid[j+self.tetra_y][i+self.tetra_x] = self.pieceId

    def nettoyeur3000(self):
        for j in range(0,4):
            for i in range(0,4):
                if self.grid[j+self.tetra_y][i+self.tetra_x] == self.pieceId:
                    self.grid[j+self.tetra_y][i+self.tetra_x] = 0
    
    def SaTouchePas(self):
        satouchepas = True
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.pieceId:
                    if self.grid[j+self.tetra_y][i+self.tetra_x] != self.pieceId and self.grid[j+self.tetra_y][i+self.tetra_x] != 0:
                        satouchepas = False
        return satouchepas

    def jeu(self):
        self.collagePiece()
        self.draw_game()
        self.cadriage()


    def rtt(self):
        self.nettoyeur3000()
        self.rotation += 1
        if self.rotation == 4:
            self.rotation = 0
        self.tetra = deepcopy(self.pieces[self.rotation][self.random])
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.random+1:
                    self.tetra[j][i] = self.pieceId
        self.nettoyeur3000()
        self.jeu()
        
    def handleLeftKey(self):
        self.nettoyeur3000()
        self.tetra_x -= 1
        if self.SaTouchePas():
            self.nettoyeur3000()
            self.jeu()
        else:
            self.tetra_x += 1
            self.jeu()
        
    def handleRightKey(self):
        self.nettoyeur3000()
        self.tetra_x += 1
        if self.SaTouchePas():
            self.nettoyeur3000()
            self.jeu()
        else:
            self.tetra_x -= 1
            self.jeu()
    
    def autodown(self):
        self.nettoyeur3000()
        self.tetra_y += 1
        if self.SaTouchePas():
            self.nettoyeur3000()
            self.jeu()
        else:
            self.tetra_y -= 1
            self.jeu()
            self.check()
            self.Testdefaite()
            self.rePiece()
    
    def check(self):
        supernombre=0
        for j in range(21, 3, -1):
            c_oui = True
            for i in range(3,13):
                if self.grid[j+supernombre][i] == 0:
                    c_oui = False
            if c_oui:
                self.score += 100
                self.lignes_detruite += 1
                for jk in range(j+supernombre, 2, -1):
                    for i in range(3,13):
                                self.grid[jk][i] = self.grid[jk-1][i]
                supernombre+=1
        if supernombre > 1:
            self.score += supernombre*100
        print("ton score est de:", self.score)
    
    def Testdefaite(self):
        j = 4
        for i in range(3,13):
                if self.grid[j][i] != 0:
                    self.defaite = True
              
    def rePiece(self):
        self.rotation = 0
        while True :
            self.newRandom = randint(0,6)
            if self.newRandom != self.random:
                self.random = self.newRandom
                break
        self.colors = ["blue", "yellow", "pink", "green", "cyan", "red", "orange"]
        self.pieceId += 1
        self.tetra = deepcopy(self.pieces[self.rotation][self.random])
        self.tetra_x = 6
        self.tetra_y = 3
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.random+1:
                    self.tetra[j][i] = self.pieceId

class Tetris:

    clock = time.time()

    def run(self):
        fenWin = Tk()
        fenWin.title('Tetris')
        fenWin.geometry('400x805')

        self.Tetris = Canvas(fenWin,width = 400, height = 800)
        self.Tetris.pack()

        self.tetraminos = Create_tetraminos(self.Tetris)
        self.tetraminos.jeu()
        
        fenWin.bind('<Key>', self.handleKeyboardEvent)

        while True:
            if time.time()>(self.clock+1*(0.98**(self.tetraminos.pieceId-1))) and not self.tetraminos.defaite:
                self.clock = time.time()
                self.tetraminos.autodown()
            if self.tetraminos.defaite:
                self.tetraminos.draw_game()
                if not self.tetraminos.saved:
                    self.tetraminos.saved = True
                    with open("Tetris_historique_parties.txt", "a", encoding="utf_8") as file:
                        file.write(f"\n\n\npartie joué le {time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year} à {time.localtime().tm_hour}h{time.localtime().tm_min}")
                        file.write(f"\nscore : {self.tetraminos.score}\nlignes détruites : {self.tetraminos.lignes_detruite}\npieces jouées : {self.tetraminos.pieceId-1}\ntemps de jeu : {time.localtime(int(time.time())-self.tetraminos.jeuTemps).tm_min}min{time.localtime(int(time.time())-self.tetraminos.jeuTemps).tm_sec}s")
            fenWin.update_idletasks()
            fenWin.update()


        
    def handleKeyboardEvent(self, event):

        if (event.keysym == "Left") and not self.tetraminos.defaite:
            self.tetraminos.handleLeftKey()
            
        if (event.keysym == "Right") and not self.tetraminos.defaite:
            self.tetraminos.handleRightKey()
        
        if (event.keysym == "Up") and not self.tetraminos.defaite:
            self.tetraminos.rtt()
        
        if (event.keysym == "Down") and not self.tetraminos.defaite:
            self.tetraminos.autodown()


tetris = Tetris()
tetris.run()
