import pyxel
import random


#TODO : définir des constantes pour toutes les types d'animation
class Monstre:
 
 
    def __init__(self,x,y) -> None:
        nbM=+1
        rdm=random.randint(0,1)
        if rdm==0 :
           self.x=x
           self.y=0
        else :
            self.y=y
            self.x=0  
        self.estTue = True

           
    

    '''def mouvementX(self,personnage : Personnage):        
        xPlayer=personnage.x
        if self.x > xPlayer :
            self.x=-1
        elif self.x < xPlayer :
            self.x=+1
'''
    '''def mouvementY(self,personnage : Personnage):
        yPlayer=personnage.y
        if self.y > yPlayer :
            self.y=-1
        elif self.y < yPlayer :
            self.y=+1
    '''
    def update(self):
        self.draw()
            

    def draw (self) :
        if self.x<pyxel.width-12 and self.y<pyxel.width-12 and pyxel.frame_count>=150:
            if pyxel.frame_count % 10 == 0:
                self.x+=1
            pyxel.blt(self.x,self.y,0,0,120,15,15, 5) 


    #def portee():
     #   if self
    #def attaqueGros():
            

class Personnage :
    def __init__(self) -> None:
        self.x=0
        self.y=0
        self.u=0
        self.v=8
        self.cord_marche=[16,16]
        self.direction = 1
        self.enMouvement=False
        self.vitesse = 2
        self.z_ok = False
        self.s_ok = False
        self.d_ok = False
        self.q_ok = False

    def update(self, cailloux):
        self.enMouvement=False

        self.z_ok = False
        self.s_ok = False
        self.d_ok = False
        self.q_ok = False

        self.mouvement(cailloux)
    
    def mouvement(self, cailloux):
        for caillou in cailloux:
            cord = caillou.getCord()
            for i in range (3):
                for j in range(16):
                    if self.x + 16 + i != cord[0] and self.y + j != cord[1]:
                        self.d_ok = True

        if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_UP) and self.y - 2 >= 0:            
            self.enMouvement=True
            self.y -= self.vitesse

        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) and self.y + 2 <= 112 :            
            self.enMouvement=True
            self.y += self.vitesse

        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT) and self.x + 2 < 112 and self.d_ok:            
            self.enMouvement = True
            self.direction = 1
            self.x += self.vitesse

        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_LEFT) and self.x - 2 > 0:            
            self.enMouvement = True
            self.direction = -1
            self.x -= self.vitesse
    

    def animationMarche(self) :
        if self.enMouvement :
            if pyxel.frame_count % 8 > 4:
                self.u = 16
                self.v = 24
            else:
                self.u = 0
                self.v = 8

    def draw(self) :
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.direction * self.cord_marche[0], self.cord_marche[1], 5)
        if pyxel.btn(pyxel.KEY_KP_0) or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.direction == -1:
                pyxel.blt(self.x - 32, self.y + 3, 0, 32, 16, self.direction * 32, 7, 5)

            else:
                pyxel.blt(self.x + 17, self.y + 3, 0, 32, 16, self.direction * 32, 7, 5)

    def getPosition(self):
        return self.x,self.y


class Cailloux:

    def __init__(self, x, y, u, v, w, h) -> None:
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 5)

    def getCord(self):
        return [self.x, self.y, self.w, self.h]

class Barille:
    
    def __init__(self, x, y, u, v, w, h) -> None:
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.duree_explosion = 0
        self.en_explossion = False
    
    def update(self):
        if pyxel.frame_count == 30 * 3:
            self.explose()
        if self.en_explossion:
            if self.duree_explosion < 6:
                self.u = 132
                self.v = 36
                self.w = 8
                self.h = 8
            elif self.duree_explosion < 12:
                self.u = 147
                self.v = 34
                self.w = 11
                self.h = 11
            elif self.duree_explosion < 18:
                self.u = 161
                self.v = 33
                self.w = 14
                self.h = 14
            elif self.duree_explosion < 24:
                self.u = 176
                self.v = 32
                self.w = 16
                self.h = 16
            elif self.duree_explosion < 30:
                self.u = 192
                self.v = 32
                self.w = 16
                self.h = 16
            elif self.duree_explosion < 36:
                self.u = 208
                self.v = 32
                self.w = 16
                self.h = 16
            elif self.duree_explosion < 42:
                self.u = 224
                self.v = 32
                self.w = 16
                self.h = 16
            else:
                self.u = 208
                self.v = 64
                self.w = 16
                self.h = 16
            self.duree_explosion += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 5)

    def explose(self):
        self.en_explossion = True
        

class App:

    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", quit_key = pyxel.KEY_ESCAPE, fps = 30)
        pyxel.load("3.pyxres")
        self.personnage = Personnage()
        ## list des cailloux
        self.cailloux = []
        ## Dessin grosse pierre : centre-gauche
        self.cailloux_1 = Cailloux(random.randint(10,30), random.randint(45,60), 224, 128, 31, 16)
        ## Dessin petite pierre : haut-droite
        self.cailloux_2 = Cailloux(random.randint(50, 70), random.randint(10,30), 175, 128, 32, 22)
        ## Dessin petite pierre : bas-droite
        self.cailloux_3 = Cailloux(random.randint(60, 80), random.randint(75,90), 192, 128, 32, 22)
        ## Ajouts des cailloux dasn la liste
        self.cailloux.append(self.cailloux_1)
        self.cailloux.append(self.cailloux_2)
        self.cailloux.append(self.cailloux_3)

        ## liste des barilles
        self.barilles = []
        ## barille bas-gauche
        self.barille_1 = Barille(random.randint(10,15), random.randint(90,100), 194, 115, 9, 10)
        ## barille centre-droit
        self.barille_2 = Barille(random.randint(75,95), random.randint(50,60), 176, 114, 14, 12)
        ## barille haut-gauche
        self.barille_3 = Barille(random.randint(15,30), random.randint(15,30), 194, 115, 9, 10)
        ## Ajouts des barilles
        self.barilles.append(self.barille_1)
        self.barilles.append(self.barille_2)
        self.barilles.append(self.barille_3)
        ## Run les fonctions update et draw
        self.monstres = [Monstre(random.randint(5,112),random.randint(5,112)) for i in range(random.randint(1,5))]
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.personnage.update(self.cailloux)
        for monstre in self.monstres : 
            monstre.update()
        for barille in self.barilles:
            barille.update()
        

    def draw(self):
        pyxel.cls(5)
        self.personnage.draw()
        if pyxel.frame_count > 150:
            for i in range(len(self.monstres)) : 
                self.monstres[i].draw()
        else :
            for i in range(len(self.monstres)) : 
                self.monstres[i].draw()

        pyxel.text(125,0,str(self.score),0)
        for cailloux in self.cailloux:
            cailloux.draw()

        for barille in self.barilles:
            barille.draw()
App()