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
    
  def __str__(self):
    result = self.category.center(30, "*")
    for entry in self.ledger:
      result += "\n"
      result += f"{entry['description'][0:23]:<23}"
      result += f"{'{amount:.2f}'.format(amount = entry['amount'])[0:7]:>7}"
    total = 0
    for entry in self.ledger:
      total += entry["amount"]
    result += "\n"
    result += f"Total: {total}"
    return result



def create_spend_chart(categories):
  # Get the total for each category
  total_category_spend = []
  for category in categories:
    spend = 0
    for entry in category.ledger:
      if entry["amount"] < 0:
        spend += abs(entry["amount"])
    total_category_spend.append(round(spend, 2))
    
  # Get the total spend
  total_spend = round(sum(total_category_spend), 2)
  # Get the percentage of each category (rounded down to the nearest 10)
  spent_percentage = list(map(lambda amount: int((((amount / total_spend) * 10) // 1) * 10), total_category_spend))
  # print(spent_percentage)

  # Create the bar chart substrings
  header = "Percentage spent by category\n"

  chart = ""
  for value in range(100, -1, -10):
      chart += str(value).rjust(3) + '|'
      for percent in spent_percentage:
        if percent >= value:
          chart += " o "
        else:
          chart += "   "
      chart += " \n"

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"

  # Create category name display
  category_names = []
  longest = 0

  for category in categories:
    category_names.append(category.category)
    if len(category.category) > longest:
      longest = len(category.category)

  # Make all the category names the same string length:
  for i in range(len(categories)):
    category_names[i] = category_names[i].ljust(longest)

  categories = ""
  for i in range(longest):
    categories += ' ' * 5
    for category in category_names:
      categories += category[i] + '  '
    if i != longest-1:
      categories += '\n'

  
  return (header + chart + footer + categories).rstrip("\n")