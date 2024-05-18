import sqlite3
import qrcode


# Function to establish database connection
def connect_database():
    connection = sqlite3.connect('Assignment21/products.db')
    cursor = connection.cursor()
    return connection, cursor


# Function to close database connection
def close_database(connection):
    connection.commit()
    connection.close()


# Function to initialize database
def initialize_database():
    connection, cursor = connect_database()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            code INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            count INTEGER
        )
    ''')
    close_database(connection)


# Function to generate a unique numerical product code starting from 1000
def generate_product_code():
    connection, cursor = connect_database()
    cursor.execute('SELECT MAX(CAST(code AS INTEGER)) FROM Products')
    max_code = cursor.fetchone()[0]
    if max_code is None:
        code = 1000
    else:
        code = max_code + 1
    close_database(connection)
    return code


# Helper function to get valid input for price
def get_valid_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print_boxed_message("Invalid input. Please enter a valid price (e.g., 12.34).")


# Helper function to get valid input for count
def get_valid_count():
    while True:
        try:
            count = int(input("Enter count: "))
            return count
        except ValueError:
            print_boxed_message("Invalid input. Please enter a valid count (e.g., 10).")


# Helper function to print messages inside a box
def print_boxed_message(message):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    print("+" + "-" * (max_length + 2) + "+")
    for line in lines:
        print("| " + line.ljust(max_length) + " |")
    print("+" + "-" * (max_length + 2) + "+")


# Function to add a product to the database
def add_product():
    connection, cursor = connect_database()
    code = generate_product_code()  
    print(f'code: {code}')
    name = input("Enter name: ")
    price = get_valid_price()
    count = get_valid_count()
    cursor.execute('INSERT INTO Products VALUES (?, ?, ?, ?)', (code, name, price, count))
    close_database(connection)
    print_boxed_message(f"Product added successfully. Code: {code}")


# Function to edit a product in the database
def edit_product():
    connection, cursor = connect_database()
    code = input("Enter the product code: ")
    cursor.execute('SELECT * FROM Products WHERE code = ?', (code,))
    product = cursor.fetchone()
    if product:
        valid_fields = ['name', 'price', 'count']
        field = input("Select the field to edit (name/price/count): ")
        if field in valid_fields:
            if field == 'price':
                new_value = get_valid_price()
            elif field == 'count':
                new_value = get_valid_count()
            else:
                new_value = input(f"Enter the new {field}: ")
            cursor.execute(f'UPDATE Products SET {field} = ? WHERE code = ?', (new_value, code))
            close_database(connection)
            print_boxed_message("Product updated successfully.")
        else:
            print_boxed_message("Invalid field. You can only edit 'name', 'price', or 'count'.")
    else:
        print_boxed_message("Product not found. Please enter a valid product code.")


# Function to remove a product from the database
def remove_product():
    connection, cursor = connect_database()
    code = input("Enter the product code to remove: ")
    cursor.execute('SELECT * FROM Products WHERE code = ?', (code,))
    product = cursor.fetchone()
    if product:
        cursor.execute('DELETE FROM Products WHERE code = ?', (code,))
        close_database(connection)
        print_boxed_message("Product removed successfully.")
    else:
        close_database(connection)
        print_boxed_message("Product not found. Please enter a valid product code.")


# Function to generate a QR code for a product
def generate_qr_code():
    connection, cursor = connect_database()
    code = input("Please enter the product code: ")
    cursor.execute('SELECT * FROM Products WHERE code = ?', (code,))
    product = cursor.fetchone()
    close_database(connection)
    if product:
        file_name = f"{product[1]}\n{product[2]}\n{product[3]}"
        img_QR = qrcode.make(file_name)
        img_QR.save(f"{product[1]}.png")
        print_boxed_message("Your product QR code successfully generated.")
        print_boxed_message(f"Product Information:\nCode: {product[0]}\nName: {product[1]}\nPrice: {product[2]}\nCount: {product[3]}")
    else:
        print_boxed_message("Product not found.")


# Function to search for a product in the database
def search_product():
    connection, cursor = connect_database()
    user_input = input("Enter user keyword: ")
    cursor.execute('SELECT * FROM Products WHERE code = ? OR name = ?', (user_input, user_input))
    product = cursor.fetchone()
    close_database(connection)
    if product:
        message = "{:<10} {:<20} {:<10} {:<10}\n".format("Code", "Name", "Price", "Count")
        message += "-" * 50 + "\n"
        message += "{:<10} {:<20} {:<10} {:<10}".format(product[0], product[1], product[2], product[3])
        print_boxed_message(message)
    else:
        print_boxed_message("Product not found.")


# Function to display all products in the database
def show_products():
    connection, cursor = connect_database()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    close_database(connection)
    message = "{:<10} {:<20} {:<10} {:<10}\n".format("Code", "Name", "Price", "Count")
    message += "-" * 60 + "\n"
    for product in products:
        message += "{:<10} {:<20} {:<10} {:<10}\n".format(product[0], product[1], product[2], product[3])
    message += f"\nTotal products: {len(products)}"
    print_boxed_message(message)


# Function to simulate buying a product
def buy_product():
    while True:
        connection, cursor = connect_database()
        code = input("Enter the product code: ")
        cursor.execute('SELECT * FROM Products WHERE code = ?', (code,))
        product = cursor.fetchone()
        if product:
            quantity = get_valid_count()
            if product[3] >= quantity:
                cursor.execute('UPDATE Products SET count = ? WHERE code = ?', (product[3] - quantity, code))
                print_boxed_message("Product added to cart.")
            else:
                print_boxed_message("Insufficient stock.")
        else:
            print_boxed_message("Product not found.")
        close_database(connection)
        choice = input("Do you want to buy more products? (y/n): ")
        if choice.lower() != 'y':
            break


# Main function to execute the program
def main():
    initialize_database()

    print_boxed_message('Welcome to Py Store 🛒')

    while True:
        print("\nMenu:")
        print('1 -> Add')
        print('2 -> Edit')
        print('3 -> Remove')
        print('4 -> Search')
        print('5 -> Show Product')
        print('6 -> Buy')
        print('7 -> Generate QR Code')
        print('8 -> Exit')
        choice = input('\nEnter your choice: ')
        if choice == '1':
            add_product()
        elif choice == '2':
            edit_product()
        elif choice == '3':
            remove_product()
        elif choice == '4':
            search_product()
        elif choice == '5':
            show_products()
        elif choice == '6':
            buy_product()
        elif choice == '7':
            generate_qr_code()
        elif choice == '8':
            print_boxed_message("Thank you for using Py Store. Goodbye!")
            break
        else:
            print_boxed_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
