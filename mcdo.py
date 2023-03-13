#!/usr/bin/env python3

print('''
    _..----.._
  .'     o    '.
 /   o       o  \\
|o        o     o|
/'-.._o     __.-'\\
\      `````     /
|``--........--'`|
 \              /
  `'----------'`
''')

from mcdo.customer import Customer

# Add required imports
# ...

# The order method will print
#   Type of bun
#   sauce
#   With or without cheese
#   Type of steak
#   Tomato
#   Salad
#   sauce
#   Type of bun

straight = Customer()
straight.order()

veggie = Customer(restrictions=['vegetarian'])
veggie.order()

gluten_freak = Customer(restrictions=['gluten_free'])
gluten_freak.order()

lactose_intol = Customer(restrictions=['lactose_intolerant'])
lactose_intol.order()

annoying_guy = Customer(restrictions=['lactose_intolerant', 'gluten_free'])
annoying_guy.order()

trend_guy = Customer(restrictions=['vegetarian', 'gluten_free'])
trend_guy.order()

complete_freak = Customer(restrictions=['vegetarian', 'gluten_free', 'lactose_intolerant'])
complete_freak.order()
