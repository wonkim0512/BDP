from app import * # app 모듈 import

def on_closing():
    global interrupt
    if messagebox.askokcancel("Quit", "Quit?"):
        root.quit()
        interrupt = 0

if __name__ == "__main__":
    global interrupt
    interrupt = 1
    width = 4
    root = Tk() # Tk class에서 root instance 생성

    while True:
        app = App(root, width) # app 모듈의 APP 실행
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()
        if app.continue_game == 0 or interrupt == 0:
            break
    root.destroy() # indent가 한번 더 되어있었음.
