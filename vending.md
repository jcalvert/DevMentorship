The goal is to model a simple vending machine as a web service

Requirements:
- The machine only accepts quarters. Nothing else will physically go in.
- Every item costs .50
- The machine is assumed on start up to hold 3 different items with an inventory of 5 of each item.
- You can only dispense a single item at a time
- After dispensing an item, the machine should return any unused quarters.
- You should return JSON

Endpoints your Vending Machine needs to support:
- For inserting a coin
- For getting the current inventory state
- For attempting to vend an item
- Coin return

