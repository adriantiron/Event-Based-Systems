import pandas as pd
import datetime as dt

banks_list = ["BCR", "BRD", "Transilvania", "Alpha", "Carpatica", "EXIMBANK", "UniCredit", "ING", "Veneto", "BROM",
              "CEC", "Citibank", "Credit Agricole", "Garanti", "Libra", "Piraeus", "Porsche", "ProCredit", "Raiffeisen",
              "Idea", "Nextebank", "Intesa Sanpaolo", "Volksbank", "Leumi", "Marfin", "Millennium", "Blom", "RBS"]
trans_type = ["withdrawal", "deposit", "payment"]
amo_int = {"low": 1, 'high': 3000}
bal_int = {"low": -10000, 'high': 50000}
ops = ["=", "!=", "<", "<=", ">", ">="]
dates_list = pd.date_range(dt.datetime(2020, 1, 1), dt.datetime(2023, 1, 1), closed='right')\
             .strftime('%d-%m-%Y').tolist()

bank_var = 0.9
amo_var = 0.6
bal_var = 0.5

equal_var = 0.5
equal_ops = ["=", "!="]
