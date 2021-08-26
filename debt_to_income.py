#filtering bank list by comparing customer's debt-to-income ratio and if it is equal or less than maximum allowed

import csv
from pathlib import Path

# As a lender,
# I want to filter the bank list by comparing if the customer's debt-to-income is equal to or less than the maximum debt-to-income ratio allowed by the bank
# so that we can assess if the customer will have payment capacity according to the bank's criteria
def filter_debt_to_income(monthly_debt_ratio, bank_list):
    debt_to_income_list = []

    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            debt_to_income_list.append(bank)
        return debt_to_income_list