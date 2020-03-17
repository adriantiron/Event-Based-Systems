import random as rd
from var_limits import *

pub_nb = 10
with open("res/pub.txt", "a") as fd:
    for x in range(0, pub_nb):
        args = {'bank': rd.choice(banks_list), 'trans': rd.choice(trans_type), 'date': rd.choice(dates_list),
                'amount': rd.randrange(amo_int['low'], amo_int['high']),
                'balance': rd.randrange(bal_int['low'], bal_int['high'])}

        publication = "{{(bank,{bank});(transaction,{trans});(amount,{amount});(balance,{balance});(date,{date})}}\n"\
                      .format(**args)

        fd.write(publication)
