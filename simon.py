from tkinter import *
import random
import threading
import time

win = Tk()
win.title("Simon Game")
win.geometry('400x500')
win.resizable(width=0, height=0)
from tkinter import *

win.configure(bg='#011F3F')


# Global variables
global Green
global Red
global Yellow
global Blue
global watch
global count
global tmp
global gameover
global timer_coun6
global score
score = 0
timer_count = 0
watch = True
gameover = False
stt = []
tmp = len(stt)
tmp_stt = []

if gameover == False:
    # Function to change the colors of buttons based on the pattern in 'stt'
	def ChangeColor(i=1):
		global stt
		global watch
		global count
		global timer_count
		count = len(stt)

		# Iterate through the pattern 'stt' and change the colors accordingly
		for i in stt:
			time.sleep(0.2)

			if i == 1:
				win.after((timer_count + 300), lambda: Green.config(bg='green'))
				win.after((timer_count + 500), lambda: Green.config(bg='#003300'))

			elif i == 2:
				win.after((timer_count + 300), lambda: Red.config(bg='red'))
				win.after((timer_count + 500), lambda: Red.config(bg='#550000'))

			elif i == 3:
				win.after((timer_count + 300), lambda: Yellow.config(bg='yellow'))
				win.after((timer_count + 500), lambda: Yellow.config(bg='#555500'))

			elif i == 4:
				win.after((timer_count + 300), lambda: Blue.config(bg='blue'))
				win.after((timer_count + 500), lambda: Blue.config(bg='#000055'))

			timer_count += 220

    # Function to handle button presses
	def press(num=1):
		global watch
		global gameover
		global count
		global score
		if count > 0 and watch == False:
			if watch == False:
				if num == 1:
					tmp_stt.append(1)
					check(count, (len(tmp_stt) - 1), num)
					count -= 1

				elif num == 2:
					tmp_stt.append(2)
					check(count, (len(tmp_stt) - 1), num)
					count -= 1

				elif num == 3:
					tmp_stt.append(3)
					check(count, (len(tmp_stt) - 1), num)
					count -= 1

				elif num == 4:
					tmp_stt.append(4)
					check(count, (len(tmp_stt) - 1), num)
					count -= 1

		if count <= 0 and gameover == False:
			score += 1
			l0.config(text='LEVEL '+str(score))
			watch = True
			tmp_stt.clear()
			start(watch, gameover)

    # Function to check the user input against the generated pattern
	def check(count=100, x=0, num=1):
		global stt
		global gameover
		if stt[x] != num:
			gameover = True
			l1.configure(text="GAMEOVER")

# Label to display the score

l0 = Label(win, text="LEVEL 0", font=("Comic Sans MS", 15,"bold"))
l0.grid(padx=10, pady=2, row=0, columnspan=2)

# Label to display the game status
l1 = Label(win, text="WATCH FIRST, PLAY AFTER",font=("Comic Sans MS", 15,"bold"))
l1.grid(padx=10, pady=2, row=1, columnspan=2)

# Buttons for the four colors

Green = Button(win, text="", font=1, bg="green", activebackground='green', width=8, height=5, command=lambda: press(1),bd=6)
Green.grid(padx=55, pady=10, row=2, column=0)

Red = Button(win, text="", font=1, bg="red", activebackground='red', width=8, height=5, command=lambda: press(2),bd=6)
Red.grid(padx=5, pady=10, row=2, column=1)

Yellow = Button(win, text="", font=1, bg="yellow", activebackground='yellow', width=8, height=5, command=lambda: press(3),bd=6)
Yellow.grid(padx=5, pady=10, row=3, column=0)

Blue = Button(win, text="", font=1, bg="blue", activebackground='blue', width=8, height=5, command=lambda: press(4),bd=6)
Blue.grid(padx=5, pady=10, row=3, column=1)

# Function to generate the first pattern
def first():
    global watch
    global gameovers
    if watch == True and gameover == False:
        tmp = random.randint(1, 4)
        stt.append(tmp)
        #print("stt=", stt)
        win.after(1000, ChangeColor)
        watch = False

# Function to start the game
def start(a=True, b=False):
    global watch
    global stt
    if a == True and b == False:
        tmp = random.randint(1, 4)
        stt.append(tmp)
        #print("stt=", stt)
        ChangeColor()
        watch = False

# Start the game by generating the first pattern
if __name__ == "__main__":
    first()
    mainloop()
