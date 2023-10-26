from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_genrator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[ random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_symbols+password_numbers+password_letters
    random.shuffle(password_list)


    password="".join(password_list)
    password_entry.insert(0,string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    new_data={
        site_entry.get():{
            "email":id_entry.get(),
            "password":password_entry.get()
        }
    }

    if len(site_entry.get())==0 or len(password_entry.get())==0:
        messagebox.showinfo(title="Oops",message="Pls dont leave any of the filed empty")
    else:
        try:
         with open("data.json","r") as file:
             data= json.load(file)
             # print(data)


        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as file:
                 json.dump(data,file,indent=4)
        finally:
             site_entry.delete(0,END)
             password_entry.delete(0,END)

def find_password():
    try:
        with open("data.json","r") as file:
            data=json.load(file)
            # lst=[key for key in data]

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="no data file found")

    else:
       if site_entry.get() in data:
                email=data[site_entry.get()]["email"]
                password=data[site_entry.get()]["password"]
                messagebox.showinfo( title= site_entry.get(),message=f"email:{email} \n password:{password}")
       else:
           messagebox.showinfo(title="warning",message="website details are  not exists")


# # ---------------------------- UI SETUP ------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)
canvas=Canvas(width=200,height=200)
i=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=i)
canvas.grid(row=0,column=1)
#label
site_label=Label(text="Website:")
site_label.grid(row=1,column=0)
id=Label(text="Email/Username:")
id.grid(row=2,column=0)
password=Label(text="Password:")

password.grid(row=3,column=0)

#entry
site_entry=Entry(width=21)
site_entry.grid(row=1,column=1,padx=20,pady=20)
site_entry.focus()
id_entry=Entry(width=40)
id_entry.grid(row=2,column=1,columnspan=2,padx=5,pady=5)
id_entry.insert(0,"pkumdale37@gamil.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,pady=5,padx=5)

#button
p_genrator_button=Button(text="Generate Password",highlightthickness=0,command=password_genrator)
p_genrator_button.grid(row=3,column=2)
add_button=Button(text="Add",width=35,command=save_pass)
add_button.grid(row=4,column=1,columnspan=2)
search_button=Button(text="search",width=13,highlightthickness=0,command=find_password)
search_button.grid(row=1,column=2)


window.mainloop()