# CompanyStaffAndPay
A Python program that can manage and merge payment requests from different classes of employees from different departments in a company
```python
from abc import ABC, abstractmethod
import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None  # default='warn'
# You may want to enable (i.e., hashtag) chained_assignment until you are more confident with your data 


class Company:
    
    '''A class that accepts and merges payment requirements from numerous departments into a single document for a company'''
    
    #Initiating the classes managed by Company
    def __init__(self):
        self.employee = self.Employee()
        self.hourlyemployee = self.HourlyEmployee()
        self.salariedemployee = self.SalariedEmployee()
    ...
