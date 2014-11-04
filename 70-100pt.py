#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="white")

# Create your "enemies" here, before the class
enemy1 = drawpad.create_rectangle(50,50,100,75, fill = "red")
enemy2 = drawpad.create_rectangle(150,150,200,125, fill = "gold")
enemy3 = drawpad.create_rectangle(250,250,300,225, fill = "green")
enemy4 = drawpad.create_rectangle(350,350,400,325, fill = "lightblue")
enemy5 = drawpad.create_rectangle(450,450,500,425, fill = "#9005FA")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "white")
       	    self.up.grid(row=0,column=1)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="Left", background= "white")
       	    self.left.grid(row=1,column=0)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="Right", background= "white")
       	    self.right.grid(row=1,column=3)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "white")
       	    self.down.grid(row=3,column=1)
       	    
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		

app = MyApp(root)
root.mainloop()