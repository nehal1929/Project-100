class Atm:
  def __init__(self, cardnumber, pin):
    self.cardnumber = cardnumber
    self.pin = pin

  def balanceinquiry(self):
    print("Your balance is: $100")

  def cashwithdrawal(self, amount):
    newAmount = 100-amount
    print("You withdrawed: $" + str(amount))
    print("Your remaining balance is: $" + str(newAmount))
  
def main():
  name = input("Hello what is your name?")
  print("Hello, " + name)
  cardnumber = input("Insert your card number: ")
  pin = input("Enter your pin: ")
  newUser = Atm(cardnumber, pin)

  print("Choose your activity: ")
  print("1. Balance inquiry")
  print("2. Cash withdrawal")
  activity = int(input("Enter activity choice: "))

  if (activity == 1):
    newUser.balanceinquiry()
  elif (activity == 2):
    amount = int(input("Enter the amount: "))
    newUser.cashwithdrawal(amount)
  else:
    print("Enter a valid number")

if __name__ == "__main__":
  main()
