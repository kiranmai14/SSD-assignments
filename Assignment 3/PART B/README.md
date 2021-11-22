# ASSIGNMENT 3B

### How to run the code

Got to the directory where the file is present and run using the below commands in seperate terminals

```sh
python3 server.py
python3 client.py
```

### Options
- 1)Signup : 
    - Provide (user/chef) any one of the two
    - Provide username.The username is unique
    - Provide password
- 2)Login :
    - Provide username
    - Provide password
- 3)Logout : User will be able to logout.
- 4)Add item : Only chef will be able to add an item into the database.
- 5)Display Menu : This will display the list of items from menu.
- 6)Order Items :
    - User is asked to give how many the items he wants to order from menu to take as input. Provide any positive integer.
    - Then user should give input for each item in this format.
        - itemid half/full quantity
    - After selecting the items he is asked to select tip percentage.He can input any one of the following:
        - 0%
        - 10%
        - 20%
    - User is asked to give input for how many people wants to share the bill. Provide any non-negative integer as input.
    - User is asked whether he wants a play 'Test you luck' game. Provide <yes/no>
    - Then whole bill of that order will be displayed.
- 7)Show Transactions : This will display the transaction ids of the transactions done by the user.
- 8)Get Transaction details :
    - Provide transaction id as input
    - It will display the transaction details of that id
- 9)Exit : 
    - It will stop client.py

