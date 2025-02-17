# Medicine Record Management System

## Overview

This project is a CRUD (Create, Read, Update, Delete) application designed to manage medicine records using a graphical user interface (GUI). The application is built using Python with PyQT for the UI and SQLite for database management. It enables users to add, update, view, and delete medicine records efficiently.

## Features

- **Add Medicine:** Users can add new medicine records with details like name, description, supplier, price, quantity, and expiration date.
- **View Medicines:** Users can view the list of medicines stored in the database.
- **Update Medicine:** Users can modify existing medicine records.
- **Delete Medicine:** Users can remove medicine records from the database.
- **Graphical Interface:** The UI is built using PyQT to provide an interactive and user-friendly experience.

## Project Structure

The project consists of the following key components:

- **DatabaseHandler (db.py):**  
  Manages the SQLite database and executes queries.  
  Implements CRUD operations.

- **Main Window (Ui_afficher.py):**  
  Displays the list of medicines.  
  Provides buttons to add, update, delete, and view medicines.

- **Add Medicine Window (Ui_MainWindow.py):**  
  Allows users to input medicine details and add them to the database.

- **Update Medicine Window (Ui_MainWindow2.py):**  
  Displays medicine details and enables users to modify them.

## Database Structure

The database consists of a single table named `MEDICAMENTS` with the following columns:

| Column Name      | Data Type   | Description                                  |
|------------------|-------------|----------------------------------------------|
| `id_m`           | INTEGER     | Unique identifier for each medicine.         |
| `nom_m`          | TEXT        | Name of the medicine.                        |
| `description`    | TEXT        | Description of the medicine.                 |
| `fournisseur`    | TEXT        | Supplier of the medicine.                    |
| `prix`           | REAL        | Price of the medicine.                       |
| `quantite`       | INTEGER     | Quantity available.                          |
| `date_peremption`| TEXT        | Expiration date of the medicine.             |

## Code Explanation

### DatabaseHandler Class

Handles database operations including:

- `create_table()`: Creates the `MEDICAMENTS` table if it does not exist.
- `insert_medicament()`: Adds a new medicine record.
- `get_medicaments()`: Retrieves all medicine records.
- `delete_medicament()`: Deletes a medicine record by ID.
- `update_record()`: Updates an existing medicine record.
- `get_medicament_data()`: Retrieves data for a specific medicine.

### Ui_afficher Class

Provides the main UI to manage medicines.

- Displays medicine records in a `QListWidget`.
- Connects buttons to corresponding CRUD functions.
- Uses `open_window()` to open the add medicine window.
- Uses `open_window2()` to open the update medicine window.
- Implements `delete_medicament()` to remove selected medicine.
- Implements `show_medicaments()` to refresh the medicine list.

### Ui_MainWindow Class

Provides a form to enter medicine details.

- Captures user input and calls `add_medicament()` to insert data into the database.

## Installation Requirements

Before running the application, install the required dependencies:
-PyQT : https://pypi.org/project/PyQt5/
-SQLite : https://www.sqlite.org/download.html

## Conclusion
This project provides a functional medicine management system using PyQT and SQLite. It demonstrates CRUD operations within a simple yet effective GUI.

