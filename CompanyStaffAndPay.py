# -*- coding: utf-8 -*-
"""
Created on 29 June 2020

@author: Charles Umesi
"""

from abc import ABC, abstractmethod
import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None  # default='warn'
# You may want to enable (i.e., hashtag) chained_assignment until you are more confident with your data 


class Company:
    
    '''Program for managing payment requirements of employees in a larger company (typically hundreds of employees)'''
    
    '''Initiating the classes managed by Company'''
    
    def __init__(self):
        self.employee = self.Employee()
        self.hourlyemployee = self.HourlyEmployee()
        self.salariedemployee = self.SalariedEmployee()
        self.manager = self.Manager()
        self.executive = self.Executive()
        self.conclusion = self.Conclusion()
        
    '''Abstract class'''

    class Employee(ABC):
        
        def determination_of_pay(self):
            pass  
    
    '''Subclasses'''                        
    
    class HourlyEmployee(Employee):
        
        '''Payment requests from hourly employees with details of hours worked'''
        
        def payments_for_clearing(self):
            
            # Department 1 hourly employees
            df1 = pd.read_excel('Department1_Hourly.xlsx')
            # Department 2 hourly employees
            df2 = pd.read_excel('Department2_Hourly.xlsx')
            # Department 3 hourly employees
            df3 = pd.read_excel('Department3_Hourly.xlsx')
            
            # Recently hired hourly employees  
            df_hourly_hired = pd.read_excel('Hourly_hired.xlsx')
            
            # Total hourly staff to be paid
            df_hourly_total = pd.concat([df1,df2,df3,df_hourly_hired])
            df_hourly_total.to_csv('TotalHourly.csv',index=False)
            
            return Company.SalariedEmployee.payments_for_clearing(self)
                   
    class SalariedEmployee(Employee):
        
        def payments_for_clearing(self):
            
            '''Payment requirements for non-managerial salaried employees'''
            
            df_salaried = pd.read_excel('Salaried.xlsx')
            
            # Recently hired non-managerial salaried employees
            df_salaried_hired = pd.read_excel('Salaried_hired.xlsx')
            
            # Total non-managerial salaried staff to be paid
            df_salaried_total = pd.concat([df_salaried,df_salaried_hired])
            df_salaried_total.to_csv('TotalSalaried.csv',index=False)
    
            return Company.Manager.payments_for_clearing(self)
            
    class Manager(Employee):
        
        def payments_for_clearing(self):
            
            '''Payment requirements for managers'''
            
            df_managers = pd.read_excel('Managers.xlsx')
            
            # Recently hired managers
            df_managers_hired = pd.read_excel('Managers_hired.xlsx')
            
            # Total managers to be paid
            df_managers_total = pd.concat([df_managers,df_managers_hired])
            df_managers_total.to_csv('TotalManagers.csv',index=False)
                
            return Company.Executive.payments_for_clearing(self)
       
    class Executive(Employee):
        
        def payments_for_clearing(self):

            '''Payment requirements for executives'''
                
            df_executives = pd.read_excel('Executives.xlsx')
            
            # Recently hired executives
            df_executives_hired = pd.read_excel('Executives_hired.xlsx')
            
            # Total executives to be paid
            df_executives_total = pd.concat([df_executives,df_executives_hired])
            df_executives_total.to_csv('TotalExecutives.csv',index=False)
            
            return Company.Conclusion.payments_for_clearing(self)
        
    class Conclusion(Employee):
        
        def payments_for_clearing(self):
            
            '''Merges files'''
            
            # Read individual totals for wages and salaries
            df_hourly_again = pd.read_csv('TotalHourly.csv')
            df_salaried_again = pd.read_csv('TotalSalaried.csv')
            df_managers_again = pd.read_csv('TotalManagers.csv')
            df_executives_again = pd.read_csv('TotalExecutives.csv')
            
            # Merge all totals for wages and salaries into one file
            Company_total = pd.concat([df_hourly_again,df_salaried_again,df_managers_again,df_executives_again])
            Company_total.to_csv('Company_WagesAndSalaries.csv',index=False)
            
            # Read files for staff of all grades leaving the company
            df_hourly_leaving = pd.read_excel('Hourly_leaving.xlsx')
            df_salaried_leaving = pd.read_excel('Salaried_leaving.xlsx')
            df_manager_leaving = pd.read_excel('Managers_leaving.xlsx')
            df_executives_leaving = pd.read_excel('Executives_leaving.xlsx')
            
            # Merge all files for staff of all grades leaving the company
            z = pd.concat([df_hourly_leaving,df_salaried_leaving,df_manager_leaving,df_executives_leaving])
            z.to_csv('Company_leaving.csv',index=False)
            
            print('Processing of pay requirements complete.')
            print("Now submit the 'Company_WagesAndSalaries.csv' and 'Company_leaving.csv' files to the company's clearing house for payment processing.")
        
                    

a = Company()
b = a.HourlyEmployee()
b.payments_for_clearing()