from account import Account
from decimal import Decimal


value = Decimal('100.00')
print(value)
# 100.00

print("\n[*]\n")

account1 = Account("Jonathan",Decimal("60001.00"))
print(f"El nombre del atributo name: {account1.name}")
print(f"El valor del atributo balance: {account1.balance}")
# Jonathan
# 60001.00

print("\n[*]\n")

# Llamar a la intancia y usar el método deposit para depositar dinero en la cuenta
account1.deposit(Decimal("10.00"))