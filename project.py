from tkinter import*

def button_1():
    label.config(text = "Button1 is clicked!")



def button_2():
    label.config(text = "Button2 is clicked!")


window = Tk()
window.title("MIRZA_.SAN.")

label = Label(window, text="Click a button below")
label.pack(pady =20)

button1 = Button(window, text="Button 1", command = button_1)
button1.pack(side = LEFT, padx=20, pady=20)
button2 = Button(window, text="Button 2", command = button_2)
button2.pack(side = RIGHT, padx=20, pady=20)

window.mainloop()
