#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, item, num, quantity = 1):
    self.total += num*quantity
    self.last_transaction = 0
    self.last_transaction += num*quantity
    for i in range(quantity):
      self.items.append(item)
    return (self.total, self.items)
  
  def apply_discount(self):
    if self.discount != 0:
      self.total = int(self.total - (self.total * (self.discount/100)))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    return self.total

