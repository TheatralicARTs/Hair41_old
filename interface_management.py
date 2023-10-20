import pprint
import tkinter as tkinter
from tkinter import *
import customtkinter
import costumer_management as cust

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


customer_ids = []
customer_names = []
def refresh():
    customer_ids = cust.customer_refresh()
    print(customer_ids)
    for id in customer_ids:
        customer_data = cust.customer_load(id)
        customer_name = customer_data.get("Customer Name")
        customer_names.append(customer_name)

    print(customer_names)



def new():
    pass

def edit():



class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.refresh = customtkinter.CTkButton(master=self, command=refresh,text="Refresh")
        self.refresh.grid(row=0, column=0, padx=20, pady=20)
        self.new = customtkinter.CTkButton(master=self, command=new, text="New Customer")
        self.new.grid(row=1, column=0, padx=20, pady=20)
        self.edit = customtkinter.CTkButton(master=self, command=edit, text="Edit Customer")
        self.edit.grid(row=2, column=0, padx=20, pady=20)

class Selector(customtkinter.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)




class Notebook(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Utility")
        self.add("Kunden")

        # add widgets on tabs
        self.my_frame = MyFrame(master=self.tab("Utility"))
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        customer_ids = cust.customer_refresh()
        for id in customer_ids:
            customer_data = cust.customer_load(id)
            customer_name = customer_data.get("Customer Name")
            customer_names.append(customer_name)
        self.selector = customtkinter.CTkComboBox(master=self.tab("Kunden"), values=customer_names, state="readonly")
        self.selector.grid(row=0, column=0, padx=10, pady=10)
        self.edit = customtkinter.CTkButton(master=self.tab("Kunden"),command=edit, text="Bearbeiten")
        self.edit.grid(row=3, column=0,padx=10, pady=10)
        self.create = customtkinter.CTkButton(master=self.tab("Kunden"), command=new, text="Neuer Eintrag")
        self.create.grid(row=3, column=1, padx=10, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1800x1280")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=5)

        self.tab_view = Notebook(master=self)
        self.tab_view.grid(row=0,column=0,padx=20,pady=20,sticky="nswe")




app = App()
app.title('Salon am Bankplatz')
app.iconbitmap(r'data/appdata/icon_app.ico')
app.mainloop()