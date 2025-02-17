import sqlite3

class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
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
        self.cursor.execute(query)
        self.conn.commit()

    def insert_medicament(self, nom_m, description, fournisseur, prix, quantite, date_peremption):
        query = '''
            INSERT INTO MEDICAMENTS (nom_m, description, fournisseur, prix, quantite, date_peremption)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (nom_m, description, fournisseur, prix, quantite, date_peremption))
        self.conn.commit()

    def get_medicaments(self):
        query = "SELECT * FROM MEDICAMENTS"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def delete_medicament(self, medicament_id):
        query = "DELETE FROM MEDICAMENTS WHERE id_m = ?"
        self.cursor.execute(query, (medicament_id,))
        self.conn.commit()
        
    def update_record(self, id_m, nom_m, description, fournisseur, prix, quantite, date_peremption, window):
        prix = float(prix)
        quantite = int(quantite)
        data = (nom_m, description, fournisseur, prix, quantite, date_peremption, id_m)
        query = "UPDATE MEDICAMENTS SET nom_m=?, description=?, fournisseur=?, prix=?, quantite=?, date_peremption=? WHERE id_m=?"
        self.cursor.execute(query, data)
        self.conn.commit()
    def get_medicament_data(self, medicament_id):
        query = "SELECT * FROM MEDICAMENTS WHERE id_m = ?"
        self.cursor.execute(query, (medicament_id,))
        medicament_data = self.cursor.fetchone()
        return medicament_data
        
       