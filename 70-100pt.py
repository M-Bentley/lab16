# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590)
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket1Fired = False
hit = False
counter = 3
direction = 5



class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='gray')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='gray')
        self.rocketsTxt.pack()
        
        self.rocketFired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket1
        global rocket1Fired
        
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1, ry1, rx2, ry2 = drawpad.coords(rocket1)
        
        if rocket1Fired == True:
            if ry2 > 0:
                drawpad.move(rocket1, 0, -15)
            if ry2 < 0:
                x = (rx1 - px1) - 7
                y = (py1 - ry1) + 3
            if rocket1 > 0:
                    drawpad.move(rocket1, x, y)
                    rocket1Fired = False

        if ex2 > 800:
            direction = - 5
        elif ex1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        drawpad.after(5,self.animate)

    def key(self,event):
        global player
        global rocket1Fired
        global rocket1
        global counter
        
        px1,py1,px2,py2 = drawpad.coords(player)
        
        if event.char == "w":
            drawpad.move(player, 0,-4)
            drawpad.move(rocket1, 0,-4)
        if py1 < 0:
	    drawpad.move(player, 0, 4)
	    drawpad.move(rocket1, 0, 4)    
        
        if event.char == "a":
            drawpad.move(player,-4, 0)
            drawpad.move(rocket1,-4, 0)
        if px1 < 0:
	    drawpad.move(player, 4, 0)
	    drawpad.move(rocket1, 4, 0)    
        
        if event.char == "d":
            drawpad.move(player, 4, 0)
            drawpad.move(rocket1, 4, 0)
        if px2 > drawpad.winfo_width():
	    drawpad.move(player, -4, 0)
	    drawpad.move(rocket1, -4, 0)
        
        if event.char == "s":
            drawpad.move(player, 0, 4)
            drawpad.move(rocket1, 0, 4)
        if py2 > drawpad.winfo_height():
	    drawpad.move(player, 0, -4)
	    drawpad.move(rocket1, 0, -4)
	
	if event.char == " ":
	    rocket1Fired = True
	    rocket1 = rocket1 - 1
	    if rocket1 > -1:
	        self.rocketsTxt.configure(text = str(rockets))      
    
    def collisionDetect(self, rocket):
        global rocket1
        global enemy
        global hit
        global drawpad
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy)
        if (rx1 > ex1 and rx2 < ex2) and (ry1 > ey1 and ry2 < ey2 ):
            drawpad.delete(enemy)
            drawpad.delete(rocket1)
app = myApp(root)
root.mainloop()