from tkinter import *
import math

def runDraw(width = 300, height = 300):
    root = Tk()
    root.title("Simple Analysis")
    canvas = Canvas(root, width = width, height = height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Done")


def draw(canvas, width, height):
    cx, cy, r = width/2, height/2, min(width, height)/3
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = 'yellow')
    r*=0.8
    for hour in range(1, 13):
        hourAngle = math.pi/2 - (2*math.pi)*(hour/12)
        hourx = cx + r*math.cos(hourAngle)
        houry = cy - r*math.sin(hourAngle)
        label = str(hour)
        canvas.create_text(hourx, houry, text = label)

runDraw(400, 400)
