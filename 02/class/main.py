class BankAccount:
  def __init__(self,name:str):
    self.name = name
    self.balance = 0
    self.interest_rate = 0.01

  def deposit(self,num):
    self.balance += num

  def withdraw(self,num):
    self.balance -= num

  def get_balance(self):
    return self.balance
  
  def set_interest_rate(self,rate):
    self.interest_rate = rate

  def apply_interest(self):
    self.balance = self.balance * (1 + self.interest_rate)


if __name__ == "__main__":
  bank = BankAccount("にちぎん")
  print(bank.name)
  bank.deposit(10)
  bank.withdraw(5)
  print(bank.get_balance())
  bank.set_interest_rate(0.2)
  bank.apply_interest()
  print(bank.interest_rate)
  print(bank.get_balance())