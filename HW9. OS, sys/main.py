import os
from menu import *


class Main(object):
    def __init__(self):
        self.curr = os.environ["HOME"]
        print(self.curr)
        #self.listDir()
        while True:
            self.menuSelection()


    def listDir(self):
        print("\ncurrent dir : ", self.curr)
        dir_list = os.listdir(self.curr)
        for element in dir_list:
            print(element)

    def menuSelection(self):
        print('\n\nSelect Menu')
        print('1) Change directory')
        print('2) Search file')
        print('3) Delete directory or file')
        print('0) Quit')
        select = input("Enter : ")

        if select == '0':
            result = Quit()

        if select == '1':
            result = ChangeDirectory(self)

        if select == '2':
            #ChangeDirectory(self).search()
            pass

        if select == '3':
            #ChangeDirectory(self).delete()
            pass

    def previous(self):
        print(self.parent.curr)
        directory_list = self.parent.curr.split('/')
        parent_directory = '/'.join(directory_list[:-1])
        self.parent.curr = parent_directory
        self.parent.listDir()

if __name__ == "__main__":
    main = Main()
