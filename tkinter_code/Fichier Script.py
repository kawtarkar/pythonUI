import tkinter as tk
from tkinter import messagebox
import sqlite3
import xml.etree.ElementTree as ET


class Medicament:
    def __init__(self, id_m, nom_m, description, fournisseur, prix, quantite, date_peremption):
        self.id_m = id_m
        self.nom_m = nom_m
        self.description = description
        self.fournisseur = fournisseur
        self.prix = prix
        self.quantite = quantite
        self.date_peremption = date_peremption


class MyApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Gestion des Médicaments")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.config(background='#41B77F')

        title_label = tk.Label(self.window, text="Gestion des Médicaments", font=("Courier", 20))
        title_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.create_table()

        self.medicaments = []

        self.create_widgets()

    def save_to_xml(self):
        try:
            root = ET.Element("medicaments")
            for medicament in self.medicaments:
                med_element = ET.SubElement(root, "medicament")
                ET.SubElement(med_element, "id_m").text = str(medicament.id_m)
                ET.SubElement(med_element, "nom_m").text = medicament.nom_m
                ET.SubElement(med_element, "description").text = medicament.description
                ET.SubElement(med_element, "fournisseur").text = medicament.fournisseur
                ET.SubElement(med_element, "prix").text = str(medicament.prix)
                ET.SubElement(med_element, "quantite").text = str(medicament.quantite)
                ET.SubElement(med_element, "date_peremption").text = medicament.date_peremption

            tree = ET.ElementTree(root)
            tree.write("pharmacie_data.xml")
            messagebox.showinfo("Information", "Data saved to pharmacie_data.xml")
        except Exception as e:
            messagebox.showerror("Error", "Error saving data to XML: " + str(e))

    def load_from_xml(self):
        try:
            tree = ET.parse("pharmacie_data.xml")
            root = tree.getroot()
            self.medicaments = []
            self.records_listbox.delete(0, tk.END)
            for med_element in root.findall("medicament"):
                id_m = int(med_element.find("id_m").text)
                nom_m = med_element.find("nom_m").text
                description = med_element.find("description").text
                fournisseur = med_element.find("fournisseur").text
                prix = float(med_element.find("prix").text)
                quantite = int(med_element.find("quantite").text)
                date_peremption = med_element.find("date_peremption").text
                medicament = Medicament(id_m, nom_m, description, fournisseur, prix, quantite, date_peremption)
                self.medicaments.append(medicament)
                self.records_listbox.insert(tk.END, f"{medicament.id_m} - {medicament.nom_m}")
            messagebox.showinfo("Information", "Data loaded from pharmacie_data.xml")
        except Exception as e:
            messagebox.showerror("Error", "Error loading data from XML: " + str(e))

    def create_table(self):
        try:
            con = sqlite3.connect("data.db")
            cursor = con.cursor()
            query = '''
                    CREATE TABLE IF NOT EXISTS MEDICAMENTS (
                        id_m INTEGER PRIMARY KEY,
                        nom_m TEXT,
                        description TEXT,
                        fournisseur TEXT,
                        prix REAL,
                        quantite INTEGER,
                        date_peremption TEXT
                    )
                    '''
            cursor.execute(query)
            con.commit()
            print("Table 'MEDICAMENTS' created successfully.")
        except Exception as e:
            print("Error in creating table:", str(e))
        finally:
            cursor.close()
            con.close()

    def create_widgets(self):
        self.frame = tk.Frame(self.window, bg='#41B77F')
        self.frame.pack(expand=tk.YES)

        button_frame = tk.Frame(self.frame, bg='#41B77F')
        button_frame.pack(side=tk.TOP)

        self.create_modify_button(button_frame)
        self.create_delete_button(button_frame)
        self.create_add_button(button_frame)
        self.create_show_button(button_frame)

        self.create_records_listbox(self.frame)

        # Buttons for saving and loading XML
        save_button = tk.Button(button_frame, text="Enregistrer XML", font=("Courier", 15),
                                command=self.save_to_xml)
        save_button.pack(side=tk.LEFT, padx=10)

        load_button = tk.Button(button_frame, text="Charger XML", font=("Courier", 15),
                                command=self.load_from_xml)
        load_button.pack(side=tk.LEFT, padx=10)

    def create_modify_button(self, frame):
        modify_button = tk.Button(frame, text="Modifier", font=("Courier", 15), bg='white',
                                  command=self.modify_function)
        modify_button.pack(side=tk.LEFT, padx=10)

    def create_delete_button(self, frame):
        delete_button = tk.Button(frame, text="Supprimer", font=("Courier", 15), bg='white',
                                  command=self.delete_function)
        delete_button.pack(side=tk.LEFT, padx=10)

    def create_add_button(self, frame):
        add_button = tk.Button(frame, text="Ajouter", font=("Courier", 15), bg='white',
                               command=self.add_function)
        add_button.pack(side=tk.LEFT, padx=10)

    def create_show_button(self, frame):
        show_button = tk.Button(frame, text="Afficher", font=("Courier", 15), bg='white',
                                command=self.show_function)
        show_button.pack(side=tk.LEFT, padx=10)

    def create_records_listbox(self, frame):
        self.records_listbox = tk.Listbox(frame, height=10, width=50, font=("Courier", 12))
        self.records_listbox.pack(pady=10, fill=tk.X)
        self.records_listbox.bind('<<ListboxSelect>>', self.on_select)

    def add_function(self):
        add_window = tk.Toplevel(self.window)
        add_window.title("Ajouter un médicament")

        tk.Label(add_window, text="Nom:", font=("Courier", 15)).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Description:", font=("Courier", 15)).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Fournisseur:", font=("Courier", 15)).grid(row=2, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Prix:", font=("Courier", 15)).grid(row=3, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Quantité:", font=("Courier", 15)).grid(row=4, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Date de Péremption:", font=("Courier", 15)).grid(row=5, column=0, padx=10, pady=5)

        entry_nom_add = tk.Entry(add_window, font=("Courier", 15))
        entry_description_add = tk.Entry(add_window, font=("Courier", 15))
        entry_fournisseur_add = tk.Entry(add_window, font=("Courier", 15))
        entry_prix_add = tk.Entry(add_window, font=("Courier", 15))
        entry_quantite_add = tk.Entry(add_window, font=("Courier", 15))
        entry_date_peremption_add = tk.Entry(add_window, font=("Courier", 15))

        entry_nom_add.grid(row=0, column=1, padx=10, pady=5)
        entry_description_add.grid(row=1, column=1, padx=10, pady=5)
        entry_fournisseur_add.grid(row=2, column=1, padx=10, pady=5)
        entry_prix_add.grid(row=3, column=1, padx=10, pady=5)
        entry_quantite_add.grid(row=4, column=1, padx=10, pady=5)
        entry_date_peremption_add.grid(row=5, column=1, padx=10, pady=5)

        add_button = tk.Button(add_window, text="Ajouter", font=("Courier", 15),
                               command=lambda: self.add_record(entry_nom_add.get(),
                                                               entry_description_add.get(),
                                                               entry_fournisseur_add.get(),
                                                               entry_prix_add.get(),
                                                               entry_quantite_add.get(),
                                                               entry_date_peremption_add.get()))
        add_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_record(self, nom_m, description, fournisseur, prix, quantite, date_peremption):
        try:
            prix = float(prix)
            quantite = int(quantite)
            con = sqlite3.connect("data.db")
            cursor = con.cursor()
            data = (nom_m, description, fournisseur, prix, quantite, date_peremption)
            query = "INSERT into MEDICAMENTS (nom_m, description, fournisseur, prix, quantite, date_peremption) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, data)
            con.commit()
            messagebox.showinfo("Information", "Medicament record created successfully.")
            con.close()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"Error in record creation: {str(e)}")

    def show_function(self):
        try:
            con = sqlite3.connect("data.db")
            cursor = con.cursor()
            query = "SELECT * from MEDICAMENTS"
            result = cursor.execute(query)
            self.medicaments = []  # Reset the list
            self.records_listbox.delete(0, tk.END)  # Clear the listbox

            if result:
                for row in result:
                    medicament = Medicament(*row)
                    self.medicaments.append(medicament)
                    self.records_listbox.insert(tk.END, f"{medicament.id_m} - {medicament.nom_m}")

            else:
                messagebox.showinfo("Information", "No records found")
        except Exception as e:
            messagebox.showerror("Error", "Error in reading records: " + str(e))
        finally:
            cursor.close()
            con.close()

    def on_select(self, event):
        try:
            selected_index = self.records_listbox.curselection()[0]
            selected_medicament = self.medicaments[selected_index]
        except IndexError:
            pass

    def modify_function(self):
        try:
            selected_index = self.records_listbox.curselection()[0]
            selected_medicament = self.medicaments[selected_index]
            self.modify_record(selected_medicament)
        except IndexError:
            pass

    def delete_function(self):
        try:
            selected_index = self.records_listbox.curselection()[0]
            selected_medicament = self.medicaments[selected_index]
            self.delete_record(selected_medicament)
        except IndexError:
            pass

    def update_record(self, id_m, nom_m, description, fournisseur, prix, quantite, date_peremption, window):
        try:
            prix = float(prix)
            quantite = int(quantite)
            con = sqlite3.connect("data.db")
            cursor = con.cursor()
            data = (nom_m, description, fournisseur, prix, quantite, date_peremption, id_m)
            query = "UPDATE MEDICAMENTS SET nom_m=?, description=?, fournisseur=?, prix=?, quantite=?, date_peremption=? WHERE id_m=?"
            cursor.execute(query, data)
            con.commit()
            messagebox.showinfo("Information", "Medicament record modified successfully.")
            window.destroy()
            con.close()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"Error in record modification: {str(e)}")

    def delete_record(self, medicament):
        try:
            con = sqlite3.connect("data.db")
            cursor = con.cursor()
            query = "DELETE FROM MEDICAMENTS WHERE id_m=?"
            cursor.execute(query, (medicament.id_m,))
            con.commit()
            messagebox.showinfo("Information", "Medicament record deleted successfully.")
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error in record deletion: {str(e)}")
    def import_from_xml(self):
        try:
            tree = ET.parse("pharmacie_data.xml")
            root = tree.getroot()
            self.medicaments = []
            self.records_listbox.delete(0, tk.END)
            for med_element in root.findall("medicament"):
                id_m = int(med_element.find("id_m").text)
                nom_m = med_element.find("nom_m").text
                description = med_element.find("description").text
                fournisseur = med_element.find("fournisseur").text
                prix = float(med_element.find("prix").text)
                quantite = int(med_element.find("quantite").text)
                date_peremption = med_element.find("date_peremption").text
                medicament = Medicament(id_m, nom_m, description, fournisseur, prix, quantite, date_peremption)
                self.medicaments.append(medicament)
                self.records_listbox.insert(tk.END, f"{medicament.id_m} - {medicament.nom_m}")
            messagebox.showinfo("Information", "Data imported from pharmacie_data.xml")
        except Exception as e:
            messagebox.showerror("Error", "Error importing data from XML: " + str(e))

# Create the main window
root = tk.Tk()
app = MyApp(root)
root.mainloop()