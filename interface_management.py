import tkinter as tkinter
from tkinter import *
import customtkinter
import costumer_management as cust

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

customer_ids = []

def refresh():
    customer_ids = cust.customer_refresh()
    print(customer_ids)


def new():
    pass

def edit():
    pass


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

class SelectorFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        row_count = 0
        customer_ids = cust.customer_refresh()
        for id_num in customer_ids:
            customer_data = cust.customer_load(id_num)
            if customer_data is not None:
                cust_name = customer_data.get("Customer Name")
                self.customer = customtkinter.CTkButton(master=self, text=cust_name)
                self.customer.grid(row=row_count, column=0, padx=20,pady=20)
                row_count = row_count + 1



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)



        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.custframe = SelectorFrame(master=self)
        self.custframe.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")


app = App()
app.mainloop()