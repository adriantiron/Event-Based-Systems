import pandas as pd
import datetime as dt

banks_list = ["BCR", "BRD", "Transilvania", "Alpha", "Carpatica", "EXIMBANK", "UniCredit", "ING", "Veneto", "BROM",
              "CEC", "Citibank", "Credit Agricole", "Garanti", "Libra", "Piraeus", "Porsche", "ProCredit", "Raiffeisen",
              "Idea", "Nextebank", "Intesa Sanpaolo", "Volksbank", "Leumi", "Marfin", "Millennium", "Blom", "RBS"]
amo_int = {"low": 1, 'high': 3000}
bal_int = {"low": -10000, 'high': 50000}
ops = ["=", "!=", "<", "<=", ">", ">="]

bank_var = 0.9
amo_var = 0.6
bal_var = 0.5

equal_var = 0.5
equal_ops = ["=", "!="]
