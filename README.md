# Shopify Backend Developer Intern Challenge - Summer 2022

This is an inventory tracking web application for a logistics company. 

# Features
This web app was built using Python Flask and sqlite3. It provides the user with the basic CRUD functionality: create inventory items, edit each inventory item, delete inventory items and view a list of all inventory items. EXTRA FEATURE: An additional feature is the ability to add deletion comments when deleting items as well as undeletion.

# How To Use
This web application is currently hosted on https://akula-shopifychallenge.herokuapp.com. Please click view inventory on the top navbar to view functionality.

# Description
The home page is merely a line of text  telling the user to click the 'View Inventory' link on the top navbar to see a list of the items in the inventory. 
The 'View Inventory' page shows a list of all items in the inventory as well as a list of items that have been deleted in case undeletion is neccessary. Deleted items are shown with a deletion comment if it was given at the time of deletion. Users can add an item to the inventory, edit details of each item and delete items. Undeletion is only possible on items that have been deleted from the inventory. 

# Improvements for the future
* Front end improvements will drastically improve the user experience for this app. 

* Logic for incrementing stock if user adds an item already in inventory

* Option for users to delete a quanity of stock of each item rather than the entire entry in the inventory
