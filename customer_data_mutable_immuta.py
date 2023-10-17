"""
For example developing a data processing application in Python for a financial institution.
The application deals with customer accounts, and you need to ensure that sensitive customer data is handled securely.
Explain how Python's object reference mechanism impacts the handling of customer data in your application.
Provide code examples to illustrate your explanation.

"""

# Define a class to represent customer accounts
class CustomerAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Customer Name: {self.customer_name}, Balance: {self.balance}"


# Function to handle customer account creation
def create_customer_account():
    # Input: Get account details from the user
    account_number = input("Enter account number: ")
    customer_name = input("Enter customer name: ")

    while True:
        try:
            balance = float(input("Enter initial balance: "))
            break  # Exit the loop if the input is successfully converted to a float
        except ValueError:
            print("Invalid input. Please enter a valid numeric balance.")

    # Create a customer account object
    customer = CustomerAccount(account_number, customer_name, balance)

    return customer


# Function to simulate a financial transaction
def perform_transaction(customer):
    while True:
        try:
            # Input: Get transaction details from the user
            transaction_type = input("Enter transaction type (Deposit/Withdraw): ").lower()
            amount = float(input("Enter transaction amount: "))
            break  # Exit the loop if the input is successfully converted to a float
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

    # Perform the transaction
    if transaction_type == "deposit":
        customer.balance += amount
    elif transaction_type == "withdraw":
        if amount <= customer.balance:
            customer.balance -= amount
        else:
            print("Insufficient balance for withdrawal.")
    else:
        print("Invalid transaction type. Use 'Deposit' or 'Withdraw'.")

    # Display the updated account information
    print("Updated Account Information:")
    print(customer)


# Call the functions to demonstrate dynamic input
customer1 = create_customer_account()
print("\nNew Customer Account Created:")
print(customer1)

perform_transaction(customer1)





















# class CustomerAccount:
#     def __init__(self, customer_name, account_number, initial_balance, username, password):
#         self._customer_name = customer_name
#         self._account_number = account_number
#         self.__balance = initial_balance
#         self.__username = username
#         self.__password = password
#
#     def get_customer_details(self):
#         customer_info = {
#             "_customer_name": self._customer_name,
#             "account_number": self._account_number,
#             "balance": self.__balance
#         }
#         return customer_info
#
#     def authenticate(self, entered_username, entered_password):
#         return self.__username == entered_username and self.__password == entered_password
#
#     def withdraw(self, withdraw_amount, entered_username, entered_password):
#         if self.authenticate(entered_username, entered_password):
#             if withdraw_amount <= self.__balance:
#                 self.__balance -= withdraw_amount
#                 print("Withdrawal successful! Remaining balance:", self.__balance)
#             else:
#                 print("Insufficient funds!")
#         else:
#             print("Authentication failed. Withdrawal not allowed.")
#
# customer_name = input("Enter customer name: ")
# account_number = int(input("Enter account number: "))
# initial_balance = float(input("Enter initial balance: "))
# user_name = input("Give a username for the customer: ")
# password = input("Give a password for the customer account: ")
# sensitive_data = (customer_name, account_number, initial_balance, user_name, password)
#
# account = CustomerAccount(*sensitive_data)
#
# while True:
#     print("Calling methods from class:\n1. Get customer info\n2. Withdraw amount\n3. Deposit amount")
#
#     call_method = input("Enter the number of the method you wish to call from the class (1/2/3): ")
#
#     if call_method == "1":
#         customer_info = account.get_customer_details()
#         print(f"Customer info: {customer_info}")
#         break
#     elif call_method == "2":
#         entered_username = input("Enter correct username: ")
#         entered_password = input("Enter correct password: ")
#         withdraw_amount = float(input("Enter the amount to withdraw: "))
#         account.withdraw(withdraw_amount, entered_username, entered_password)
#         break
#     elif call_method == "3":
#         # Add deposit functionality here if needed
#         pass
#     else:
#         print("Invalid choice. Please select a valid option (1/2/3).")
#
