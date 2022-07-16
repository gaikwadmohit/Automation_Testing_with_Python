class Account:
    def __init__(self, balance):
        self.balance = balance

    # Debit method to check account balance and debit some amount

    def debitmethod(self,amt):
        """

        :param amt:
        :return:
        """



        print("Enter amount for debit thorugh account:")
        debitamount = int(input("DebitAmount : "))
        if debitamount < self.balance:
            self.balance -= debitamount
            print("Debit amount is : ", debitamount)
            print("Account balance after update : ", self.balance)
        else:
            print("Debit amount exceeded Account balance")


if __name__ == '__main__':
    amt=int(input("Enter the account balance : "))

    account = Account(amt)
    account.debitmethod()
