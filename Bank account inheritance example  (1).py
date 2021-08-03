#!/usr/bin/env python
# coding: utf-8

# # Bank account example

# In[1]:


class Bank_Account:
    def __init__ (self, deposit, withdraw, savings):
        self.deposit = deposit
        self.withdraw = withdraw
        self.savings =savings
        
    def bank_deposit(self):
        if self.deposit > 0:
            print(f"{self.deposit} has been deposited into your account")
        else:
            print(f"{self.deposit} is your New Total Balance")
            
    def bank_withdrawal(self):
        print(f"{self.deposit} Is the available withdrawable amount in your account")
        
    def bank_savings(self):
        print(f"{self.savings} is the total amount of savings in your account")
        
class Bank_Account_HNI(Bank_Account): #This is inheriting from the BAnk Acct class
    def __init__ (self, deposit, withdraw, savings, bank_ID):
        self.bank_ID = bank_ID
        super().__init__( deposit, withdraw, savings)
        
    def bank_deposit(self):
        if self.deposit > 0:
            print(f"{self.deposit} has been deposited into your account user {self.bank_ID}")
        else:
            print(f"{self.deposit} is your New Total Balance")
            
    def Credentials(self):
        print(f" Hey, your bank ID is {self.bank_ID}")

class Bank_Account_Company(Bank_Account):

    """ This is inheriting from the Bank_Account_HNI 
        and the Bank Acct class, Mutiple inheritance
    """
    
    def __init__ (self, deposit, withdraw, savings,company_ID):
        self.company_ID = company_ID
        super().__init__( deposit, withdraw, savings)
        
    def Credentials(self,comp_name):
        print(f" Hey, {comp_name} your bank ID is {self.company_ID}")
        
    def bank_withdrawal(self, comp_name):
        print(f" Hey, {comp_name} your bank ID is {self.company_ID} and {self.deposit} Is the available withdrawable amount in your account")
        
    
   


# In[2]:




#Creation of objects

alpha = Bank_Account_Company(80000000,0,58000000000000000, "A&N_2585")
alpha.bank_deposit()
alpha.bank_withdrawal("A&N Investment mangement")


# In[ ]:


#polymorphism  different forms 

def student(name):
    print(f"my name is {name}")


# In[ ]:


stud1 = student("Isaiah")


# In[ ]:


#Using input example 

stud1 = input("What is your name? ")

print(f"my name is {stud1}")


# In[ ]:




