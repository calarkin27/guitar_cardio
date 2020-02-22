from tkinter import *


#replace/use this for execution of cardio function
def click():
    selections = selection_box.get()        #this collects checkbox selections

window = Tk()
window.geometry('1000x600')
window.title("Guitar Cardio")
window.configure(background="black")

Label (window, text="Select the parameters for your workout.", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

#replace with checkbox selection
selection_box = CheckButton(window, width=20, bg="white")
selection_box.grid(row=2, column=0, sticky=W)

Button(window, text="Submit", width=6, command=click). grid(row=3, column=0, sticky=W)

Frame(window)
workout_output = Text(window, width=75, height=6, wrap=WORD, background="white")
workout_output.grid(row=5, column=0, columnspan=2, stick=W)


"""

widgets are added here

"""

window.mainloop()
