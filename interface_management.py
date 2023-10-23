import pprint
import tkinter as tkinter
from tkinter import *
import customtkinter
import costumer_management as cust
import datetime

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


customer_ids = []
customer_names = []
Kunde = "K"
Telefon = "T"
Mobil = "0151/1"
Letzer_Termin = "Unix"
Mitarbeiter =  "Sanel"
Service = "absbc"
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
    pass



def display(id):
    cust.customer_refresh()
    print(id)
    customer_data = cust.customer_load(id)
    if customer_data is not NONE:
        Kunde = customer_data.get("Customer Name")
        Telefon = customer_data.get("Customer Phone")
        Mobil = customer_data.get("Customer Mobile")
        Letzer_Termin = datetime.datetime.fromtimestamp(customer_data.get("Last Sessions"))
        Mitarbeiter = customer_data.get("Treatment")
        Service = customer_data.get("Customer Name")







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

class MyTextbox(customtkinter.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.insert("1.0", "Kunde: " + Kunde + '\n\n')
        self.insert("2.0", "Telefon: " + Telefon + '\n\n')
        self.insert("3.0", "Mobil: " + Mobil + '\n\n')
        self.insert("4.0", "Letzer Termin: " + Letzer_Termin + '\n\n')
        self.insert("5.0", "Mitarbeiter: " + Mitarbeiter + '\n\n')
        self.insert("6.0", "Service: " + Service + '\n\n')



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
        self.selector = customtkinter.CTkComboBox(master=self.tab("Kunden"), values=customer_names, state="readonly",command=display)
        self.selector.grid(row=0, column=0, padx=10, pady=10)

        self.textbox = MyTextbox(master=self.tab("Kunden"), width=600, corner_radius=10)
        self.textbox.grid(row=2, column=0)

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

