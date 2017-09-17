import os
import sys
import glob
import shutil


global cur_path
# os.chdir((cur_path +'\\'+chandir))
# cur_path = 'C:\Users\User'
# print('THIS IS HOME ',os.environ['HOMEPATH'])
os.chdir(os.environ['HOMEPATH'])
cur_path=os.getcwd()
# print(os.getcwd())

def os_menu():
    menu_num = -1

    while (menu_num != '0'):
        print("curent director : ",os.getcwd() )

        # print(os.getcwd())
        # for i,j in os.environ.items():
        #     print((i,j))
        print("select menu")
        print("1) Change Directory")
        print("2) Search file")
        print("3) Delete directory ")
        print("0) Quit")
        menu_num = input("Enter : ")

        switcher = {
            '1': change_dir,
            '2': Search_file,
            '3': Delete_directory,
            '0': Quit

        }

        selected_func = switcher.get(menu_num, print_wrong)

        selected_func()

    return

def change_dir() :
    print("change_directory")
    print("enter a directory or path")
    try :
        chandir = input("(enter '..' for the parent dir. and q to exit) :")
        if chandir== 'q' :
            return
        else :
            try :
                global cur_path
                # cur_path = os.getcwd()
                # print(cur_path)
                # print(chandir)
                os.chdir((cur_path +'\\'+chandir))
                cur_path=os.getcwd()
                print(cur_path)
                change_dir()
            except:
                print("error occur, there is no file ")
                change_dir()
    except PermissionError :
        print("PermissionError, go to the previous dirctory")
        pass



def Search_file():
    print('\nsearch file\n')
    print(cur_path)
    keyword = input("enter a keyword to search file or directory (enter q to exit) : ")
    if keyword== 'q' :
        return
    else :

        # print(cur_path+'/*/%s' %keyword)
        # for f in glob.iglob(cur_path+'/*/%s' %keyword ):  # generator, search immediate subdirectories
        #     print(f)
        # Search_file()

        for f in glob.iglob(cur_path+"/**/*%s*" %keyword, recursive=True): # generator, search immediate subdirectories
                print (f)

        Search_file()



def Delete_directory() :
    print("Delete_directory")
    A = os.listdir(cur_path)
    for i in range(int(len(A) / 3) + 1):
        print("\t\t\t".join(A[i * 3:(i + 1) * 3]))
    print("\ndelete directory or file")
    delfile= input("enter a directory or file (enter q to exit) : ")
    if delfile == 'q':
        return
    try :
        os.removedirs((cur_path + '\\%s') % delfile)
        print("delete success")
        print("--------------------")

    except FileNotFoundError:
        print("there is no such directory" , delfile)
    except OSError:
        print("this directory is not empty")
        print("Do you really want to delete this directory? ")
        answer = input("enter y/n :")
        if answer == 'y':
            shutil.rmtree((cur_path + '\\%s') % delfile)
            print("delete success")
        else :
            pass
    Delete_directory()


def Quit():
    quit()
    return

def print_wrong():
    print("\nwrong menu number.")
    return
