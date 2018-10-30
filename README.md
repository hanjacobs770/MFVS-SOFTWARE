# MFVS-SOFTWARE
An online store
Installation Guide
Hi, and welcome to the Group 32 MFVS Installation guide!
The first thing you are going to want to do is to load up your computer and make sure that there are no background processes running in order to make the installation go as smoothly as possible, once you have done that then please take the following steps to install your software.
1.	Before doing anything, you need to make sure you have an appropriate python IDE installed on your computer. In our case we have chosen to use PyCharm, you will need to download the PyCharm installer from https://www.jetbrains.com/pycharm/download/#section=windows. Once you have downloaded the installer please follow the prompts in order to install PyCharm.

2.	Now that PyCharm has been installed please insert the flash drive containing the software or download the zip file onto your computer.

3.	Once downloaded please unzip the file into an appropriate location. Be sure to name the main folder with an easily identifiable name like “MFVS SOFTWARE”.

4.	Open the “MFVS SOFTWARE” folder and locate the file “maininterface.py”.

5.	The next step is that you will need to open the “maininterface.py” class with PyCharm.

6.	Now that you have opened the “maininterface.py” class please feel free to login using the following pre-created user accounts: 
                     User     Pass    Email                            Phone         SecurityQSn   Security Answer
Admin        Admin     |Pass1234| admin@mfvs.com |99123456    |MFVS                  |MFVS|
Customer: Customer|Pass1234|cust@monash.com|0412345678 |Which Uni? |Monash|

7.	Alternatively, you can Setup a new account by following the prompts and instructions given on the main menu (although you may only have one admin account), once the account has been created wait for confirmation.

8.	Now that your account is all ready to go begin adding products to your store through the links provided on the main administration menu. Be sure to add appropriate information regarding the price, origin and all other information relating to the specific products.

9.	You can also start exploring some of the other main menu options. You can change and change edit user information. You can search for product, check your transaction history, edit user accounts and add a discount. If you are logged in as a customer you can purchase a product and add it to your cart for checkout.

10.	The final step is to customise any other aspects of the store to your liking. Things such as the number of products on the shelf at any one time or if you would like to apply any storewide discounts.
11.	Your software is now ready to go! Wasn’t that easy! All you need to do now is sit back and reap the rewards of your now MFVS system!

Functionalities: The following is a list of the major functionalities we implemented with a brief description as to each one: as well as instructions as to how to complete the desired operation:
1.Register Account and Login:

One of the most basic functionalities we’ve implemented, and one which would have to be implemented in any normal system was the ability to register and login. This was a pretty straightforward functionality with the only qualifying feature being that if customer fails to login 3 times they would be shown one security question.
In terms of the login details we have also implemented a validation check for the password attribute. This validation requires that passwords cannot contain any special characters, although they can be either upper or lower case.

•	In order to logon please simply select the login option from the main meu when first activating the software.
 
•	Next please enter username and password. If the system does not detect the existence of your username or password you will be given the option to register for a new account.
















1.Register Account and Login:

•	Once the details have been verified the user is successful











•	In the event that login is unsuccessful you may be prompted for additional details, please refer to the user list text file in the main folder for a full account of user details, for our pre-created accounts the details are:
                          User     Pass    Email                            Phone         SecurityQSn   Security Answer
Admin        Admin     |Pass1234| admin@mfvs.com |99123456    |MFVS                  |MFVS|
Customer: Customer|Pass1234|cust@monash.com|0412345678 |Which Uni? |Monash|

•	Conversely, in order to register for a new account please simply, follow the instructions provide on screen.









•	To register as an admin please use the admin keyword for the username input. 
NB: This system comes with a pre-created user account so there is no need to register


















2.Register Account and Login:

•	Conversely to use the system as a customer please create an account using any other username input other than admin
NB: This system comes with a pre-created customer account.
 




































3.User editing and updating details:

On creation of their account all users are required to provide details regarding their name, email and phone, i.e. these details cannot be null. Following registration, the user is also given the opportunity to update these details. 

•	In order to edit user details as either a customer or an admin please simply select the edit user details option from the user menu after having logged on.
 
•	The next step will be to choose exactly which details the user would like to be edited from the main user menu.
 


•	The user will then be prompted to input for the specific details they requested to change. If the data passes the validation requirements then the user information will successfully change.

 






4.Owner updating product info and store inventory:

The way our store has been setup is that the owner has full control of the entire system. That is to say he can edit existing product data for specific products as well as editing and changing customer accounts. He can cancel orders and he can also edit the storewide inventory. He can accomplish this by either adding or deleting products form the shelf class. Finally, the admin can also implement storewide discounts over all products.

•	In order to edit product data or add/remove products from the shelf class please login to the system as the admin user. Next please select the edit product information option from the main menu.
 
•	You will then be asked to select which product you would like to edit. Next you will be able to choose which aspects of the product you would like to update and you will be asked to enter in the new information and update the product

 


•	You will then be asked to select which product you would like to edit. Next you will be able to choose which aspects of the product you would like to update and you will be asked to enter in the new information and update the product













4.Owner updating product info and store inventory:















•	Alternatively, to edit the inventory list please select the edit inventory option from the same admin user menu. You can then choose to add or remove products form the shelf array. Please note that when adding a product to the store inventory in this manner a new product class object will automatically be created to store the information.



































5.Owner can access transaction history:
Another functionality given to the owner is their ability to view and access all past transaction history including the:
•	Date of the transaction
•	Total price of the transaction.
•	And whether the purchase is an in-store pickup or directly purchased form the store.

-In order to access the transaction history please logon to the system as the admin and then select the view transaction history option. The total sales data will then be displayed to the user.






















•	After pressing enter, all of the transaction history will be displayed. As we have not yet had any purchases there is nothing to display at present.















6.Searching and View Products:
A search product function has also been enabled which allows all users and even guest visitors to search for products on the store. The search can be completed in a number of ways including by searching according to category or name.

•	In order to search for a product, the user should first be logged in. They can then simply choose the search product option from the main user menu when opening the software.
•	The software will then prompt the user for a search phrase. If the phrase matches a product a search result will be returned.
























•	If the user would like to view all fruits or all vegetable than they simply need to type either “fruit” or “vegetable” input space followed by the word category

 







6.Searching and View Products:

•	Conversely to view products please select option 4 and select the option to display the product info for all current products either by price or name.
































7.Purchase and edit Cart:

The final and arguably most important functionality is the ability for the customer to purchase products through the use of the cart function. The online cart is used by the customer to edit their order before finally confirming it. 

•	In order to purchase a product, the customer must be logged in. Once logged in the customer can choose to add items to their shopping cart through selecting that option on the main customer menu. Once they have made that selection they can view their cart contents. If they are happy with the cart contents they can then choose the checkout option from the customer menu which will allow them to confirm their order and select a pickup time. 
 








•	Next please select the purchase option, you will be given a choice to either purchase a product individually or by pack.


7.Purchase and edit Cart:


 
•	Once a product has been confirmed select option 4 on the main menu to view the current cart
 











7.Purchase and edit Cart:

•	If the user selects the number 1 then the cart is checked out. The user can then later view their transaction record by selecting option “6” check my transaction from the main menu:

 


