class BankAccount:
    """The BankAccount allows working with accounts """
    isWithinOperatingHours = False

    def __init__(self, _account_id, _account_name, _balance):
        if not self.isWithinOperatingHours:
            print("Outside operating hours")
        else:
            self.account_id = _account_id
            self.account_name = _account_name
            self.balance = _balance


print(BankAccount.__dict__)
jd_account = BankAccount(1234, "JD", 1)
alejandro_account = BankAccount(2345, "Alex", 10)
BankAccount.isWithinOperatingHours = True
rachel_account = BankAccount(1817, "Rachel", 15)
print(jd_account.__dict__)
print(alejandro_account.__dict__)
print(rachel_account.__dict__)


# print(jd_account.__dict__)
# print(alejandro_account.__dict__)
# print(jd_account.isWithinOperatingHours, alejandro_account.isWithinOperatingHours)
# BankAccount.isWithinOperatingHours = True
# print(jd_account.isWithinOperatingHours, alejandro_account.isWithinOperatingHours)
# jd_account.isWithinOperatingHours = False
# print(jd_account.isWithinOperatingHours, alejandro_account.isWithinOperatingHours)




