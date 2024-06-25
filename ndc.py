import random
import pyxel

class Personnage :
    def __init__(self) -> None:
        self.x=0
        self.y=0
        self.vie=3
    def update(self):
        pass
    
    def updateTir(self) :
        pass
    def tir() :
        pass
        # TODO : parcourir la liste des tirs, afficher une image du tir sur la map
    def mouvement():
   
        '''
            -avancer : d ou fleche droite
            -reculer : q ou fleche gauche
            -sauter : z ou fleche haut
            -baisser : s ou fleche bas
        if frame_cou
        '''
    def draw(self) :
        
        pyxel.blt(0,0,0,0,8,12,12, 5)
    def getPosition(self):
        return self.x,self.y

class Monstre:
    hp = 5
    atk = 1
    nbM=0
    MAXMONSTRE=5
    def __init__(self,x,y) -> None:
        nbM=+1
        rdm=random.randint(0,1)
        if rdm==0 :
           self.x=x
           self.y=0
        else :
            self.y=y
            self.x=0     
    

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
        if self.x<pyxel.width-12 and self.y<pyxel.width-12 and not(estTue())and pyxel.frame_count>=150:
            if pyxel.frame_count % 10 == 0:
                self.x+=1
            pyxel.blt(self.x,self.y,0,0,120,15,15, 5) 


    #def portee():
     #   if self
    #def attaqueGros():
        
       
                
class App:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code",quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("3.pyxres")
        self.personnage = Personnage()
        self.monstres = [Monstre(random.randint(5,112),random.randint(5,112)) for i in range(random.randint(1,5))]
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        for monstre in self.monstres : 
            monstre.update()
        self.personnage.update()

    def draw(self):
        pyxel.cls(5)
        nbFrame=1
        if pyxel.frame_count==300 and nbFrame<1:
            for i in range(len(self.monstres)) : 
                self.monstres[i].draw()
            nbFrame+=1
        else :

            for i in range(len(self.monstres)) : 
                self.monstres[i].draw()
        pyxel.text(125,0,str(self.score),0)
        self.personnage.draw()

App()