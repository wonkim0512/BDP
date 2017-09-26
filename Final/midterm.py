import math
from tkinter import *


class Song(object):
    def __init__(self, title = None, rating = 6):
        self.title = title
        self.rating = rating

class Playlist(object):
    def __init__(self, songs = []):
        self.songs = songs

    def averageRating(self):
        score = 0
        for song in self.songs:
            score += song.rating

        return score / len(self.songs)

    def addSong(self, song):
        self.songs.append(song)

    def __eq__(self, other):
        return self.songs == other.songs


def file_reader(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)

    except FileNotFoundError:
        print("Sorry, the file "+filename+" dose not exist.")


def draw_clock():
    root = Tk()
    width, height = 300, 300
    canvas = Canvas(root, width = width, height = height)
    canvas.pack()

    cx, cy, r = width/2, height/2, 50
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = 'yellow')

    r *= 0.8
    for hour in range(1, 13):
        hourAngle = math.pi/2 - (2*math.pi)*(hour/12)
        hourx = cx + r*math.cos(hourAngle)
        houry = cy - r*math.sin(hourAngle)
        canvas.create_text(hourx, houry, text = str(hour))
        canvas.pack()

    root.mainloop()



class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()


class Queue(object):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def report(self):
        print(self.items)

    def delete(self):
        return self.items.pop(0)


if __name__ == "__main__":
    song1 = Song("Happy", 10)
    assert((song1.title == "Happy") and (song1.rating == 10))

    song2 = Song("Joyful")
    assert((song2.title == "Joyful") and (song2.rating == 6))

    playlist1 = Playlist([song1, song2])
    assert(playlist1.songs == [song1, song2]) # instances are inserted
    assert(playlist1.averageRating() == 8)

    playlist2 = Playlist([song1])
    assert(playlist2.songs == [song1])
    assert(playlist2.averageRating() == 10)
    assert(not (playlist1 == playlist2))

    playlist2.addSong(song2) # if it were a list, addSong would have been written with 'extend'
    assert(playlist2.songs == [song1, song2])
    assert(playlist2.averageRating() == 8)
    assert(playlist2 == playlist1)

    file_reader("alice.txt")
    file_reader('recovery.txt')

    draw_clock()