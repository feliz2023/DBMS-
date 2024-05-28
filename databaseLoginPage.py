import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def submitact():
    user = userEntry.get()
    password = passEntry.get()
    
    if not user or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return
    
    print(f"The name entered by you is {user} with password {password}")
    
    logintodb(user, password)

def logintodb(user, passw):
    try:
        if passw:
            db = mysql.connector.connect(
                host="localhost",
                user=user,
                password=passw,
                database="time_table_management"
            )
        else:
            db = mysql.connector.connect(
                host="localhost",
                user=user,
                database="College"
            )

        db_cursor = db.cursor()
        query = "SELECT * FROM tab1"
        db_cursor.execute(query)
        data = db_cursor.fetchall()
        
        for row in data:
            print(row)
        print("Data fetched successfully")
        
    except Error as e:
        messagebox.showerror("Error", f"Error connecting to database: {e}")
        print(f"Error: {e}")
        
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()

root = tk.Tk()
root.geometry("600x400")
root.title("DBMS login page")

UserLabel = tk.Label(root, text="Username - ")
UserLabel.place(x=60, y=30)

userEntry = tk.Entry(root, width=35)
userEntry.place(x=150, y=30, width=200)

passLabel = tk.Label(root, text="Password - ")
passLabel.place(x=60, y=60)

# Set the show option to '*' to hide the password
passEntry = tk.Entry(root, width=35, show='*')
passEntry.place(x=150, y=60, width=200)

submit_button = tk.Button(root, text="Login", bg="blue", command=submitact)
submit_button.place(x=150, y=120, width=80)

root.mainloop()
