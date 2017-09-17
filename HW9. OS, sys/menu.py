import os
import glob

class Quit(object):
    def __init__(self):
        quit()


class ChangeDirectory(object):
    def __init__(self, parent):
        self.parent = parent
        print(self.parent)
        self.keepgoing = True

        while self.keepgoing:
            try:
                self.change()

            except PermissionError:
                print("PermissionError")
                self.previous()

            except FileNotFoundError:
                print('FileNotFoundError')
                self.previous()

    def change(self):
        print("\n\nchange directory")
        print('\nenter a directory or path')
        path = input('enter ".." for the parent dir, and q to exit : ')

        if path == "q":
            self.keepgoing == False
            return

        try:
            if path == "..":
                print("go to parent")
                self.previous()



            else:
                want_to_go = (self.parent.curr + '/' + path)
                print(want_to_go)
                os.chdir(want_to_go)
                curr_path = os.getcwd()
                print(curr_path)

        except:
            print("error occur, there is no file ")

    def previous(self):
        print(self.parent.curr)
        directory_list = self.parent.curr.split('/')
        parent_directory = '/'.join(directory_list[:-1])
        self.parent.curr = parent_directory
        self.parent.listDir()

#class SearchFile(self, parent)