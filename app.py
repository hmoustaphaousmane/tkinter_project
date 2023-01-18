from tkinter import *
# from tkinter import ttk
from sqlite3 import *

# Connecting to my_app_db data base
connection = connect ("my_app_db")
        
class Add (Toplevel) :
    def __init__ (self, parent) :
        super ().__init__ (parent)
        
        self.geometry ("500x200")
        self.title ("Add a Person")
        self.resizable(height=False, width=False)
        self ["bg"] = "yellow"
        
        self.first_name_var = StringVar ()
        self.last_name_var = StringVar ()
        self.age_var = IntVar ()
        
        self.create_person ()
        
    def create_person (self) :
        padding = {"padx" : 5, "pady" : 5}
        text = Label (self, text = "Add a Person", font = "Algerian 16 bold" ).grid (column = 1, row = 0, **padding)

        # First Name
        first_name_label = Label (self, text = "First Name :")
        first_name_label.grid (column = 0, row = 1, **padding)
        
        first_name_entry = Entry (self, textvariable = self.first_name_var)
        first_name_entry.grid (column = 1, row = 1, **padding)
        first_name_entry.focus ()
        
        # Last Name
        last_name_lable = Label (self, text = "Last Name :")
        last_name_lable.grid (column = 0, row = 2, **padding)
        
        last_name_entry = Entry (self, textvariable = self.last_name_var)
        last_name_entry.grid (column = 1, row = 2, **padding)
        
        # Age
        age_label = Label (self, text = "Age :")
        age_label.grid (column = 0, row = 3)
        
        age_entry = Entry (self, textvariable = self.age_var)
        age_entry.grid (column = 1, row = 3, **padding)
        
        # Add button
        add_button = Button (self, text = "Add", command = self.add_person)
        add_button.grid (column = 0, row = 4, **padding)
        
        # Cancel button
        cancel_button = Button (self, text = "Cancel", command = lambda : [self.destroy ()])
        cancel_button.grid (column = 1, row = 4, **padding)
        
        
    # Methode add_person pour ajouter une personne a la db
    def add_person (self) :
        global connection
        self.cursor = connection.cursor ()
        self.cursor.execute ("""CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        );""")
        connection.commit ()
        self.cursor.execute ("""INSERT INTO person (first_name, last_name, age) VALUES (?, ?, ?);""",
                       (self.first_name_var.get (), self.last_name_var.get (), self.age_var.get ())
                      )
        connection.commit ()

class Introduce (Toplevel) :
    def __init__ (self, parent) :
        super ().__init__ (parent)
        self["bg"] = "cyan"
        
        self.id_var = IntVar ()
        
        self.open_introduce ()
        
    def open_introduce (self) :
        id_label = Label (self, text = "ID :")
        id_label.place(x='10',y='30')
#         id_label.grid (column = 0, row = 0)
        
        id_entry = Entry (self, textvariable = self.id_var)
        id_entry.place(x='40',y='30')
#         id_entry.grid (column = 1, row = 0)
        
        id_ok_button = Button (self, text = "OK", command = self.introduce_id )
        id_ok_button.place(x='50',y='60')
#         id_ok_button.grid (column = 0, row = 1)
       
    def introduce_id (self) :
        global connection
        self.cursor = connection.cursor ()
        
#         self.f_name = self.cursor.execute ("""SELECT first_name FROM person WHERE id = ?;""", self.id_var.get ())
#         self.l_name = self.cursor.execute ("""SELECT last_name FROM person WHERE id = ?;""", self.id_var.get ())
#         self.age = self.cursor.execute ("""SELECT age FROM person WHERE id = ?;""", self.id_var.get ())
        
        self.introduce_label = Label (self).pack (expand = True)
#         self.introduce_label.grid (column = 0, row = 1, columnspan = 3)
#         self.introduce_label.config (text = f"Mon prenom est {self.f_name}.\n\
#         Mon nom de famille est {self.l_name}.\nJe suis age de {self.age} ans.")

        the_person = self.cursor.execute ("""SELECT * FROM person WHERE id = ?;""",
                             self.id_var.get ()
        )
        self.introduce_label.config (text = f"""Mon prenom est {the_person [1]}.
                                    Mon nom de famille est {self.the_person [2]}.
                                    Je suis age de {self.the_person [3]} ans.""")

class List (Toplevel) :
    def __init__ (self, parent) :
        super ().__init__ (parent)
        self.title ("List of Persons")
        self.geometry ("500x200")
        self.resizable (height=False, width=False)
        self["bg"] = "cyan"
        
        self.list_persons ()
        
    def list_persons (self) :
        global connection
        self.cursor = connection.cursor ()
        persons = self.cursor.execute ("""SELECT * FROM person;""")
        i, j = 0, 0
        for person in persons :
            Label (self, text = f"{person [0]}").grid (column = 0, row = j)
            Label (self, text = f"{person [1]}").grid (column = 1, row = j)
            Label (self, text = f"{person [2]}").grid (column = 2, row = j)
            Label (self, text = f"{person [3]}").grid (column = 3, row = j)
            j += 1
            
#             print (person)
#             print (f"Mon nom est {person [1]}, mon nom de famille est {person [2]} et j'ai {person [3]} ans.")
#             Label (self, text = f"Mon nom est {person [1]}, mon nom de famille est {person [2]} et j'ai {person [3]} ans.").pack (expand = True)
            
#             Label (self, text = f"Mon nom est {person [1]}, mon nom de famille est {person [2]} et j'ai {person [3]} ans.").grid (row = i)
#             i += 1
        
class Age (Toplevel) :
    def __init__ (self, parent) :
        super ().__init__ (parent)
        self.title ("Age Groupe")
        self.resizable(height=False, width=False) 
        self.geometry ("300x150")
        self["bg"] = "cyan"
#         self.age_var = IntVar ()
        self.id_var = IntVar ()
        
        
#         age_group = Entry (self, textvariable = self.age_var).pack (expand = True)
#         age = self.age_var.get ()
        label_age=Label(self, text="Age:").place(x='10',y='30')
        id_person = Entry (self, textvariable = self.id_var).place(x='40', y='30')
#         the_id = self.id_var.get ()
        Button (self, text = "OK", command = lambda : [self.age_group]).palce(x='40', y='40')
        
        self.age_group_label = Label (self)
#         self.age_group_label.pack (expand = True)
#         self.age_group_label.grid (column = 3, row = 3, columnspan = 3)
        
        
#         self.age_group (age)
        
    def age_group (self) :
#         if self.age_var.get () >= 0 and self.age_var.get () <= 18 :
#             self.age_group_label.config (text = "Jeune")
#         elif self.age_var.get () <= 45 :
#             self.age_group_label.config (text = "Adulte")
#         elif self.age_var.get () > 45 :
#             self.age_group_label.config (text = "Vieux")
#         else :
#             return
        
        
        global connection
        self.cursor = connection.cursor ()
        the_person = self.cursor.execute ("""SELECT * FROM person WHERE id = ?;""",
                             self.id_var.get ()
        )
        self.age_group_label = Label (self)
        self.age_group_label.pack (expand = True)
        if the_person [2] >= 0 and the_person [2] <= 18 :
            self.age_group_label.config (text = "Jeune")
        elif the_person [2] <= 45 :
            self.age_group_label.config (text = "Adulte")
        elif the_person [2] > 45 :
            self.age_group_label.config (text = "Vieux")
        else :
            pass

class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('450x225')
        self.resizable(height=False,width=False)
        self.title('Main Window')
        self["bg"] = "cyan"
      
        self.menu_bar ()
        exit_button = Button (self, text = "Exit", command = self.exit_page).pack (expand = True)
    
    def exit_page (self) :
        global connection
        connection.close ()
        self.destroy ()
        
    def menu_bar (self) :
        # Create a menu_bar
        menu_bar = Menu (self)
        self.config (menu = menu_bar)
        
        # Create a menu file name file_menu in the menu_bar
        file_menu = Menu (menu_bar, tearoff=0)
        
        # Add commands to file_menu
        file_menu.add_command (
            label = "Add",
            command = self.open_add_window
        )
        file_menu.add_separator()
        file_menu.add_command (
            label = "List All",
            command = self.open_list
        )
        file_menu.add_separator()
        file_menu.add_command (
            label = "Introduce",
            command = self.open_introduce
        )
        file_menu.add_separator()
        file_menu.add_command (
            label = "Age Group",
            command = self.open_age_group
        )
        
        # Add the file menu to the menu bar
        menu_bar.add_cascade (
            label = "Menu",
            menu = file_menu,
            underline = 0
        )
        

    def open_add_window (self) :
        window = Add (self)
        window.grab_set()
        
    def open_introduce (self) :
        window = Introduce (self)
        window.grab_set ()
    
    def open_list (self) :
        window = List (self)
        window.grab_set ()
        
    def open_age_group (self) :
        window = Age (self)
        window.grab_set ()
        
# Disabling connection to the data base
# conection.close ()

if __name__ == "__main__":
    app = App()
    app.mainloop()
Footer
