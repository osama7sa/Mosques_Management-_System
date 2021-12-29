import os
from tkinter import *
from tkinter import messagebox
import folium
import webbrowser
from DataBase import Database
import difflib

"""""
Note: All the features and extra features added to the system

-for display map you have to enter Latitude and Longitude to display map correctly
"""""



Mosque_Database = Database("Database1", "Mtable")


def UpdateDB():  # Update operation
    global list_box, Mosque_Database, id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input
    for records in Mosque_Database.dispaly_all("Mtable"):
        if name_input.get() == records[1]:
            Mosque_Database.update(records[0], imam_input.get())
            messagebox.showinfo("successful", 'Imam updated')
            return

    messagebox.showerror("ERROR!", "record not found! make sure to enter correct name")


def miss(close, spell_button, spell_label):  # Encancing the search operation
    global list_box, Mosque_Database, id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input
    list_box.delete(0, END)
    list_box.insert(END, "Mosque Information:")
    listOfStrings = []

    for records in Mosque_Database.dispaly_all("Mtable"):
        listOfStrings.append(str(records[1]))
        if str(records[1]) == str(close):
            list_box.insert(END, "ID: " + str(records[0]))
            list_box.insert(END, "name: " + str(records[1]))
            name_input.delete(0, END)
            name_input.insert(0, str(records[1]))
            list_box.insert(END, "type: " + str(records[3]))
            list_box.insert(END, "Imam Name: " + str(records[6]))
            list_box.insert(END, "Address: " + records[2])
            list_box.insert(END, "Coordinates[Lon]: " + records[4])
            list_box.insert(END, "Coordinates[Lat]: " + records[5])
            spell_button.destroy()
            spell_label.destroy()


            return


def SearchDB():  # Record search
    global list_box, Mosque_Database, id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input
    list_box.delete(0, END)
    list_box.insert(END, "Mosque Information:")
    listOfStrings = []
    for records in Mosque_Database.dispaly_all("Mtable"):
        listOfStrings.append(str(records[1]))
        if str(records[1]) == str(name_input.get()):  # There is no new line in list box tkinter !
            list_box.insert(END, "ID: " + str(records[0]))
            list_box.insert(END, "name: " + str(records[1]))
            list_box.insert(END, "type: " + str(records[3]))
            list_box.insert(END, "Imam Name: " + str(records[6]))
            list_box.insert(END, "Address: " + records[2])
            list_box.insert(END, "Coordinates[Lon]: " + records[4])
            list_box.insert(END, "Coordinates[Lat]: " + records[5])

            return
    if (str(name_input.get())) == '':
        messagebox.showerror("ERROR!", "Enter name to search!")


    else:  # Encancing the search opreation (find close matcing name)
        string = str(name_input.get())
        close = difflib.get_close_matches(string, listOfStrings)
        # find common strings
        # messagebox.showinfo("Error!", "Record not found! %%do you mean{}".format(difflib.get_close_matches(string, listOfStrings)))
        spell_label = Label(text="Record not found! do you mean (({})) ?".format(close[0]), bg="red",font=('Helvetica', 10, 'bold'))
        spell_label.grid()
        spell_button = Button(text="yes", command=lambda: miss(close[0], spell_button, spell_label))
        spell_button.grid()


def desplayDB():  # Display all records
    global list_box, Mosque_Database, id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input, difflib
    list_box.delete(0, END)
    list_box.insert(END, "Mosques Information:")
    list_box.insert(END, "(Search by name for more info)")
    print('TEST 1')
    i = 1
    for records in Mosque_Database.dispaly_all("Mtable"):
        list_box.insert(END, "{}:".format(i))
        list_box.insert(END, str(records[0]) + "--> " + str(records[1]))
        list_box.insert(END, "---------------------------")
        i += 1

    if i == 1:
        list_box.insert(END, "#Empty!")


def Desplay_Map():  # display the map usinf folium and webbrowser library
    global list_box, Mosque_Database, id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input

    for records in Mosque_Database.dispaly_all("Mtable"):
        if str(records[1]) == str(name_input.get()):
            var1 = str(records[4])
            var2 = str(records[5])
            m = folium.Map(location=[var1, var2], zoom_start=15)  # Map
            folium.Marker(location=[var1, var2], popup="Mosque location").add_to(m)
            m.save("{}.html".format(name_input.get()))

            webbrowser.open('file://' + os.path.realpath("{}.html".format(name_input.get())))
            return

    messagebox.showerror("ERROR!", "record not found! make sure to enter correct name")


def insertDB():  # Add record to the table
    global id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input

    for i in Mosque_Database.dispaly_all("Mtable"):
        if str(id_input.get()) == str(i[0]):
            messagebox.showerror("ERROR!", "id must be unique!")
            return

    if '' not in (
            name_input.get(), address_entry.get(), coordinates1_input.get(), coordinates2_input.get(),
            imam_input.get()):

        Mosque_Database.insert(id_input.get(), name_input.get(), address_entry.get(), Mtype1.get(),
                               coordinates1_input.get(), coordinates2_input.get(), imam_input.get())
        messagebox.showinfo("Successful", "Mosque added!")
        id_input.delete(0, END)
        name_input.delete(0, END)
        address_entry.delete(0, END)
        coordinates1_input.delete(0, END)
        coordinates2_input.delete(0, END)
        imam_input.delete(0, END)
        print('TEST 2')
    else:
        messagebox.showerror("ERROR!", "Make sure to enter all information!")


def DeleteDB():  # Delete record from the table
    global list_box, Mosque_Database, id_input, name_input, address_entry, Mtype1, coordinates1_input, imam_input, Mosque_Database, coordinates2_input

    for records in Mosque_Database.dispaly_all("Mtable"):

        if str(id_input.get()) == str(records[0]):
            Mosque_Database.delete(id_input.get())
            id_input.delete(0, END)
            messagebox.showinfo("Successful", "Mosque Removed!")
            print('TEST 4')
            return

    if str(id_input.get()) == '':

        messagebox.showerror("ERROR!", "Enter id of the mosque!")
    else:
        messagebox.showerror("ERROR!", "Record not found !")


x = 1


def Dark_mode():
    global x
    if x == 1:
        Mosque_ui.configure(bg='#2B2B2B')
        x = 2
    elif x == 2:
        Mosque_ui.configure(bg='#F0F0F0')
        x = 1


# Tiknter code

Mosque_ui = Tk()
Mosque_ui.title("Mosques System Program")
Mosque_ui.geometry("800x350")

# type of the mosque
Mtype = ["مسجد", "مصلى", "جامع"]
Mtype1 = StringVar()
Mtype1.set(Mtype[1])

# Labels and buttons
id_label = Label(text="ID")
id_label.grid(row=0, column=0)
id_input = Entry()
id_input.grid(row=0, column=1)

name_label = Label(text="Name")
name_label.grid(row=0, column=2)
name_input = Entry()
name_input.grid(row=0, column=3)

type_label = Label(text="Type")
type_label.grid(row=4, column=0)
type_choice = OptionMenu(Mosque_ui, Mtype1, *Mtype)
type_choice.grid(row=4, column=1)

address_label = Label(text="Address")
address_label.grid(row=1, column=2)
address_entry = Entry()
address_entry.grid(row=1, column=3)

coordinates_label = Label(text="Coordinates[Lon]")
coordinates_label.grid(row=1, column=0)
coordinates1_input = Entry()
coordinates1_input.grid(row=1, column=1)

coordinatesF_label = Label(text="Coordinates[Lat]")
coordinatesF_label.grid(row=2, column=0)
coordinates2_input = Entry()
coordinates2_input.grid(row=2, column=1)

imam_label = Label(text="Imam name")
imam_label.grid(row=2, column=2)
imam_input = Entry()
imam_input.grid(row=2, column=3)

hint_lablel = Label(text='Hint: enter correct coordinates(Latitude & Longitude)\n to display the map',
                    font=("Arial", 7))
hint_lablel.grid(row=3, column=0)

list_box = Listbox(width=30, selectmode=SINGLE)
list_box.grid(row=0, column=4, rowspan=5)

display_button = Button(text="Display All", width=12, command=desplayDB)
display_button.grid(row=5, column=1)

search_button = Button(text="Search By Name", width=12, command=SearchDB)
search_button.grid(row=5, column=2)

update_button = Button(text="Update", width=12, command=UpdateDB)
update_button.grid(row=5, column=3)

add_button = Button(text="Add Entry", width=12, command=insertDB)
add_button.grid(row=6, column=1)

delete_button = Button(text="Delete Entry", width=12, command=DeleteDB)
delete_button.grid(row=6, column=2)

map_button = Button(text="Display map", width=12, command=Desplay_Map)
map_button.grid(row=6, column=3)
dark_mode_button = Button(text="Dark mode", width=12, command=Dark_mode)
dark_mode_button.grid(row=6, column=4)

Mosque_ui.mainloop()
