# Global Ai Hub - Akbank Python Bootcamp Project
# PizzaCall - Pizza Order System

The program is for ordering pizzas with different sauces. It provides a menu of pizzas to choose from and an option to add sauces to the pizza. 
The program then calculates the cost of the pizza with the added sauces and takes the customer's name, checks if the entered TC number conforms to the 
Turkish ID number algorithm and checks if the entered credit card number, expiry date and cvv code are valid for the order.

The program consists of several classes: Pizza, Decorator, and six sauce classes (Olive, Mushroom, GoatCheese, Meat, Onion, and Corn). 
The Pizza class is the parent class that contains the basic structure for a pizza. 
The Decorator class is a child of the Pizza class and is used to add sauces to the pizza. 
The six sauce classes are children of the Decorator class and represent the different sauces that can be added to the pizza.

The program imports the necessary classes and libraries, configures the logging system, displays the menu of pizzas, takes input from the user, 
creates an instance of the selected pizza class, asks the user if they want to add sauces, takes input for the selected sauces, 
creates instances of the selected sauce classes, calculates the total cost of the pizza with the added sauces, 
takes the customer's name, Turkish Identification Number, and credit card infos and logs the order information in a file called orders.log.
