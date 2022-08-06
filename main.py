from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import string
import pyperclip


def generate_password():
    letters = list(string.ascii_lowercase+string.ascii_uppercase)
    number = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','&','*','(',')']




    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_number = [choice(number) for _ in range(randint(2,4))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_number + password_symbol

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Error",message="Please make sure you havent left any field empty")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail :{email} \nPassword : {password} \nPress ok to save:")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)




window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=50)
canvas = Canvas(height = 250,width=200)
logo_img = PhotoImage(file="password.png")
canvas.create_image(100,125,image=logo_img)
canvas.grid(row=0,column=1)


website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email / Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


website_entry = Entry(width=70)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=70)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"arnavkamramalout@gmail.com")
password_entry = Entry(width=54)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Button",command=generate_password)
generate_password_button.grid(row = 3,column=2)
add_button = Button(text="Add",width=60,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()