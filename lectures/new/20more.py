from tkinter import *
from tkinter import ttk

root = Tk()

name = Label(root, text = "name: ")
name.grid(row = 1, column = 1)

namebox = Entry(root)
namebox.grid(row = 1, column = 2, padx = 7)

sex = Label(root, text = "sex: ")
sex.grid(row = 2, column = 1)

sexframe = Frame(root)
sexframe.grid(row = 2, column = 2, padx = 5, pady = 5)

varSex = IntVar()
malebutton = Radiobutton(sexframe, text = "male", variable = varSex, value = 1)
femalebutton = Radiobutton(sexframe, text = "female", variable = varSex, value = 0)
malebutton.grid(row = 1, column = 1)
femalebutton.grid(row = 1, column = 2)

birthday = Label(root, text = "birthday: "  )
birthday.grid(row=3, column=1)
birthdayframe = Frame(root)
birthdayframe.grid(row = 3, column = 2)

varYear = IntVar()
year = ttk.Combobox(birthdayframe, textvariable = varYear, state = 'readonly', width = 4)
year['value'] = list(range(2017, 1900, -1))
year.set("년")
year.grid(row = 1, column = 1)

varMonth = IntVar()
month = ttk.Combobox(birthdayframe, textvariable = varMonth, state = 'readonly', width = 2)
month['value'] = list(range(1, 13))
month.set("월")
month.grid(row = 1, column = 3)


varDay = IntVar()
day = ttk.Combobox(birthdayframe, textvariable = varDay, state = 'readonly', width = 2)
day['value'] = list(range(1, 32))
day.set("월")
day.grid(row = 1, column = 5)

yearlabel = Label(birthdayframe, text= '년')
yearlabel.grid(row = 1, column=2)
monthlabel = Label(birthdayframe, text= '월')
monthlabel.grid(row = 1, column=4)
daylabel = Label(birthdayframe, text= '일')
daylabel.grid(row = 1, column=6)

email = Label(root, text = "Email")
email.grid(row = 4, column = 1)

emailAddress = Entry(root)
emailAddress.grid(row = 4, column = 2, padx = 7)

at = Label(root, text = "@")
at.grid(row = 4, column = 3)

domain = Entry(root)
domain.grid(row = 4, column = 4, padx = 7)

language = Label(root)
language.grid(row = 5, column = 1)

languageframe = Frame(root)
languageframe.grid(row = 5, column = 2)





root.mainloop()
