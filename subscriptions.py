import random as rd, numpy as np
from var_limits import *

pub_nb = 10
bank_nb = 0

banks_list_vars = np.random.choice([None, ''], pub_nb, p=[bank_var, 1-bank_var])
for i in range(0, len(banks_list_vars)):
    if banks_list_vars[i] is None:
        banks_list_vars[i] = rd.choice(banks_list)
        bank_nb += 1

equal_ops_vars = np.random.choice(equal_ops, bank_nb, p=[equal_var, 1-equal_var])
for i in range(0, len(banks_list_vars)):
    if banks_list_vars[i] == '':
        equal_ops_vars = np.insert(equal_ops_vars, i, banks_list_vars[i])

amo_vars = np.random.choice([None, ''], pub_nb, p=[amo_var, 1-amo_var])
for i in range(0, len(amo_vars)):
    if amo_vars[i] is None:
        amo_vars[i] = rd.randrange(amo_int['low'], amo_int['high'])

bal_vars = np.random.choice([None, ''], pub_nb, p=[bal_var, 1-bal_var])
for i in range(0, len(bal_vars)):
    if bal_vars[i] is None:
        bal_vars[i] = rd.randrange(bal_int['low'], bal_int['high'])


with open("res/sub.txt", "w") as fd:
    for x in range(0, pub_nb):
        args = {'bank': banks_list_vars[x],
                'eq_op': equal_ops_vars[x],
                'op': rd.choice(ops),
                'amount': amo_vars[x],
                'balance': bal_vars[x]}

        banks_arg = ''
        if args['bank'] != '':
            banks_arg = '(bank,{eq_op},{bank});'.format(**args)

        amo_arg = ''
        if args['amount'] != '':
            amo_arg = '(amount,{op},{amount});'.format(**args)

        bal_arg = ''
        if args['balance'] != '':
            bal_arg = '(balance,{op},{balance})'.format(**args)

        subscription = "{{{}{}{}}}\n".format(banks_arg, amo_arg, bal_arg)

        fd.write(subscription)
