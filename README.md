
# 21th Assignments in Python

This repository contains two Python practice projects: `store.py` and `CreateMusic.py`.


## Project 1: Store Management System

`store.py` is a simple store management system that allows users to perform various operations on a product database, including adding, editing, removing, searching, and displaying products. Additionally, it supports generating QR codes for products and simulating product purchases.

### Features

- **Initialize Database**: Create a SQLite database with a `Products` table if it doesn't already exist.
- **Add Product**: Add a new product to the database with a unique code, name, price, and count.
- **Edit Product**: Edit the name, price, or count of an existing product.
- **Remove Product**: Remove a product from the database using its code.
- **Search Product**: Search for a product by its code or name.
- **Show Products**: Display all products in the database.
- **Buy Product**: Simulate buying a product by reducing its count.
- **Generate QR Code**: Generate a QR code for a product containing its details.

### How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries using:

   ```sh
   pip install qrcode
   pip install sqlite3
   ```
3. Run the Script:
    ```sh
    python store.py
    ```
### Code Overview

- Database Functions: Functions to connect to, initialize, and close the database.
- Product Operations: Functions to add, edit, remove, search, show, and buy products.
- QR Code Generation: Function to generate QR codes for products.
- Helper Functions: Functions for input validation and printing messages in a box.


## Project 2: Music Creation

'CreateMusic.py' is a script that uses the pysynth library to create WAV files for various melodies, including "Twinkle Twinkle Little Star," "Happy Birthday," and "Hedwig's Theme."

### Features
- **Create "Twinkle Twinkle Little Star":** Generate a WAV file for the melody.

- **Create "Happy Birthday":** Generate a WAV file for the melody.

- **Create "Hedwig's Theme":** Generate a WAV file for the melody from the Harry Potter series.

### How to Run
Ensure you have Python installed on your system.
Install the required libraries using:
```sh
    pip install pysynth
```

### Run the script:
```sh
    python CreateMusic.py
```

### Code Overview
- ***Define Melodies:*** Lists containing tuples of notes and their durations for each song.

- ***Generate WAV Files:*** Use the pysynth.make_wav function to create WAV files for the defined melodies.


### Credits

***Designer:*** `Zahra Eslami`