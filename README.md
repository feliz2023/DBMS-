             DBMS Login Page
This project is a simple graphical user interface (GUI) application for logging into a database management system (DBMS). The application is built using Python's Tkinter library for the GUI and MySQL Connector for interacting with the MySQL database.

             Features
        
User Authentication: Users can enter their username and password to log into the database.

Secure Password Entry: Passwords are masked as they are typed to ensure security.

Database Connection: The application attempts to connect to a MySQL database using the provided credentials.

Error Handling: Proper error handling is implemented to display messages for incorrect username/password or database connection issues.

Data Retrieval: On successful login, the application retrieves and displays data from a specific table in the database.


            Code Overview
submitact(): Retrieves user input (username and password) from the GUI and calls the logintodb() function to attempt a database connection.

logintodb(user, passw): Connects to the MySQL database using the provided credentials. If the connection is successful, it executes a query to fetch data from the table. If there are any errors, appropriate error messages are displayed.

            GUI Components:
Labels and Entry widgets for username and password input.

A Login button to trigger the authentication process.

The password Entry widget is configured to mask the password input with asterisks (*).

           Prerequisites
Python 3.x   

MySQL Server

mysql-connector-python package (can be installed using pip install mysql-connector-python)


           How to Run
Ensure you have MySQL Server installed and running.

Create a MySQL database and a table named tab1.

Update the database connection details in the code if necessary.

Run the Python script to start the GUI application.

        
