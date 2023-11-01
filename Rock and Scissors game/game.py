from secrets import choice
from tkinter import *

root = Tk()

root.geometry("450x540")
root.title("Rock Paper and Scissors")

rps = ["_Rock_.", "_Paper_", "Scissors"]

def play(event):
    computer = choice(rps)
    player = event.widget.cget("text")
    
    playerLabel = Label(frame3, text=player, bg="green", relief=SUNKEN, borderwidth=5 , font=("Arial", 35))
    playerLabel.grid(row=0 , column=0)

    computerLabel = Label(frame3, text=computer , bg="green", relief=SUNKEN, borderwidth=5 , font=("Arial", 35))
    computerLabel.grid(row=0 , column=1)

#Frame 1 
frame1 = Frame(root , bg="lightblue" )
frame1.pack(fill=X)

titleLabel = Label(frame1 , text="Rock Paper Scissors", font=("Arial", 30), bg="yellow")
titleLabel.pack()

# Frame 2

frame2 = Frame(root , bg="lightgreen" )
frame2.pack(fill=X)

playerLabel = Label(frame2, text="Player___", bg="green", relief=SUNKEN, borderwidth=5 , font=("Arial", 35))
playerLabel.grid(row=0 , column=0)

computerLabel = Label(frame2, text="Computer___", bg="green", relief=SUNKEN, borderwidth=5 , font=("Arial", 35))
computerLabel.grid(row=0 , column=1)

#Frame 3

frame3 = Frame(root , bg="lightgreen" )
frame3.pack(fill=X)

playerLabel = Label(frame3, text="_____", bg="green", relief=SUNKEN, borderwidth=5 , font=("Arial", 35))
playerLabel.grid(row=0 , column=0)

computerLabel = Label(frame3, text="_____", bg="green", relief=SUNKEN, borderwidth=5 , font=("Arial", 35))
computerLabel.grid(row=0 , column=1)

# Frame 4

frame4 = Frame(root , bg="lightblue")
frame4.pack(fill=X)

rockButton = Button(frame4, text="_Rock_." , bg="orange" , relief=RAISED, borderwidth=5 , font=("Arial" , 35))
rockButton.pack()
rockButton.pack()
rockButton.bind("<Button-1>" , play)

rockButton = Button(frame4, text="_Paper_" , bg="orange" , relief=RAISED, borderwidth=5 , font=("Arial" , 35))
rockButton.pack()
rockButton.bind("<Button-1>" , play)

rockButton = Button(frame4, text="Scissors" , bg="orange" , relief=RAISED, borderwidth=5 , font=("Arial" , 35))
rockButton.pack()
rockButton.bind("<Button-1>" , play)

#Frame 5

frame5 = Frame(root , bg="lightblue")
frame5.pack(fill=X)

winnerLabel = Label(frame5 , text="____Winner____" , relief=RAISED, borderwidth=5, font=("Arial", 35))
winnerLabel.pack()



root.mainloop()