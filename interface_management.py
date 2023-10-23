import pprint
import tkinter as tkinter
from tkinter import *
import customtkinter
import costumer_management as cust
import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

customer_ids = []
customer_names = []
Kunde = "K"
Telefon = "T"
Mobil = "0151/1"
Letzer_Termin = "Unix"
Mitarbeiter = "Sanel"
Service = "absbc"


def refresh():
    customer_ids = cust.customer_refresh()
    print(customer_ids)
    for id in customer_ids:
        customer_data = cust.customer_load(id)
        customer_name = customer_data.get("Customer_Name")
        customer_names.append(customer_name)

    print(customer_names)


def new():
    pass


def edit():
    pass


def display(customer_name):
    customer_ids = cust.customer_refresh()
    for customer_id in customer_ids:
        customer_data = cust.customer_load(customer_id)
        if customer_data is not None and customer_data.get("Customer_Name") == customer_name:
            # Initialize variables with the same names as the keys
            Kunde = customer_data.get("Customer_Name")
            Telefon = customer_data.get("Customer_Phone")
            Mobil = customer_data.get("Customer_Mobile")
            Letzer_Termin = customer_data.get("Last_Sessions")
            Mitarbeiter = customer_data.get("Employee Name")
            Service = customer_data.get("Treatment")
            customer_number = customer_data.get("Customer Number")
            # MyTextbox.insert(0.0, "New Text")
            print(Kunde, Telefon, Mobil, Letzer_Termin, Mitarbeiter, Service)

            # Clear Previous data, otherwise it pushed it down.
            textbox.delete(0.0, 99.99)
            # Write the data from the selected entry to the textbox
            textbox.insert("1.0", "Kunde: " + Kunde + '\n\n')
            textbox.insert("2.0", "Telefon: " + str(Telefon) + '\n\n')
            textbox.insert("3.0", "Mobil: " + str(Mobil) + '\n\n')
            textbox.insert("4.0", "Letzer Termin: " + str(Letzer_Termin) + '\n\n')
            textbox.insert("5.0", "Mitarbeiter: " + Mitarbeiter + '\n\n')
            textbox.insert("6.0", "Service: " + Service + '\n\n')

            # Return the variables
            return customer_number


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.refresh = customtkinter.CTkButton(master=self, command=refresh, text="Refresh")
        self.refresh.grid(row=0, column=0, padx=20, pady=20)
        self.new = customtkinter.CTkButton(master=self, command=new, text="New Customer")
        self.new.grid(row=1, column=0, padx=20, pady=20)
        self.edit = customtkinter.CTkButton(master=self, command=edit, text="Edit Customer")
        self.edit.grid(row=2, column=0, padx=20, pady=20)


class MyTextbox(customtkinter.CTkTextbox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.configure(state="disabled") <--- Does not work as read in wiki -.-

        # As we are not technically using the class's default instance we do not want to bother with inserting defaults here as it screws up the drawing process (Uncomment to see what I mean)
        self.insert("1.0", "Kunde: " + Kunde + '\n\n')
        self.insert("2.0", "Telefon: " + Telefon + '\n\n')
        self.insert("3.0", "Mobil: " + Mobil + '\n\n')
        self.insert("4.0", "Letzer Termin: " + Letzer_Termin + '\n\n')
        self.insert("5.0", "Mitarbeiter: " + Mitarbeiter + '\n\n')
        self.insert("6.0", "Service: " + Service + '\n\n')


class Notebook(customtkinter.CTkTabview):

    def save(self, name, tel, mob, date, emp, ser):
        print(name, tel, mob, date, emp, ser)
        pass
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Utility")
        self.add("Kunden")
        self.add("Neuer Kunde")

        # add widgets on tabs
        self.my_frame = MyFrame(master=self.tab("Utility"))
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        customer_ids = cust.customer_refresh()
        for id in customer_ids:
            customer_data = cust.customer_load(id)
            customer_name = customer_data.get("Customer_Name")
            customer_names.append(customer_name)
        self.selector = customtkinter.CTkComboBox(master=self.tab("Kunden"), values=customer_names, state="readonly",
                                                  command=display)
        self.selector.grid(row=0, column=0, padx=10, pady=10)

        # Possibly a work around, we make a global variable of the master. (As i cannot for the life of me figure out who to specify it eg: Notebook.tab("Kunden") <-- did not work 🤷‍♂️)
        # global TxtMaster
        # TxtMaster = self.tab("Kunden")

        # Spawn textbox instance based on class defaults
        self.textbox = MyTextbox(master=self.tab("Kunden"), width=600, corner_radius=10)
        self.textbox.grid(row=2, column=0)

        # We can simply global this text box to make changes to its sepcific instance
        global textbox
        textbox = self.textbox


        entry_name = customtkinter.CTkEntry(master=self.tab("Neuer Kunde"),
                                            placeholder_text="Name",
                                            width=200,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        entry_name.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        entry_tel = customtkinter.CTkEntry(master=self.tab("Neuer Kunde"),
                                            placeholder_text="Telefon",
                                            width=200,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        entry_tel.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        entry_mob = customtkinter.CTkEntry(master=self.tab("Neuer Kunde"),
                                            placeholder_text="Handy",
                                            width=200,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        entry_mob.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

        entry_last = customtkinter.CTkEntry(master=self.tab("Neuer Kunde"),
                                            placeholder_text="Datum",
                                            width=200,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        entry_last.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        entry_emp = customtkinter.CTkEntry(master=self.tab("Neuer Kunde"),
                                            placeholder_text="Mitarbeiter",
                                            width=200,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        entry_emp.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

        entry_serv = customtkinter.CTkEntry(master=self.tab("Neuer Kunde"),
                                            placeholder_text="Behandlung",
                                            width=200,
                                            height=100,
                                            border_width=2,
                                            corner_radius=10)
        entry_serv.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
        name = entry_name.get()
        tel = entry_tel.get()
        mob = entry_mob.get()
        date = entry_last.get()
        emp = entry_emp.get()
        ser = entry_serv.get

        #entry_save = customtkinter.CTkButton(self, text="Speichern", command=Notebook.save(name, tel, mob, date, emp, ser))
        #entry_save.grid(row=1,column=1)



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
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")


app = App()
app.title('Salon am Bankplatz')
app.iconbitmap(r'data/appdata/icon_app.ico')
app.mainloop()

