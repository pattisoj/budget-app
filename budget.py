class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.get_balance() > amount:
      self.ledger.append({"amount": (0 - amount), "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance = balance + entry["amount"]
    return balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.category}")
      category.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False



# def create_spend_chart(categories):