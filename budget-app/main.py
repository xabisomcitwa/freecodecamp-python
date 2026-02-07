# this is a simple budget app that tracks spending in different categories 
# and can show the relative spending percentage on a graph
import math 

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []    #contains list of transactions

    def deposit(self, amount, description=''):
        new_deposit = {'amount': amount, 'description': description}
        self.ledger.append(new_deposit)
    
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        withdrawal = {'amount': -amount, 'description': description}
        self.ledger.append(withdrawal)
        return True
    
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance+= i.get('amount')
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    
    def check_funds(self, amount):
        if amount>self.get_balance():
            return False
        else:
            return True
    
    def get_amount_spent(self):
        amount_spent=0
        for i in self.ledger:
            if i.get('amount')<0:
                amount_spent+=i.get('amount')
        return -amount_spent

        
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        for i in self.ledger:
            items+=f'{i.get("description")[:23]:23}{i.get("amount"):>7.2f}\n'
        total = f'Total: {self.get_balance()}'
        return title+items+total
    
    def __len__(self):
        return len(self.name)
'''
def create_spend_chart(categories):
    print('Percentage spent by category')
    total = 0
    for category in categories:
        total += category.get_balance()
    
    percentages = []
    for category in categories:
        percentages.append(int(round((category.get_balance()/total)*100,-1)))

    for y in range(0,110,10):
        for x in range(0,(4+len(categories)*3)):
            if x==0:
                print(f'{100-y:>3}', end='')
            elif x==1:
                print('|', end='')
            elif x==2:
                print(' ', end='')
            elif x%3==0:
                index=(x-3)//3
                #print(index)
                if index==len(percentages):
                    pass
                elif (100-y)<=percentages[index]:
                    print('o', end='')
                else:
                    print (' ',end='')
            else:
                print(' ',end='')
    
        print()

    print(' '*4,end='')
    print('_'*(len(categories)*3))

    for i in range(len(max(categories,key=len))):
        for index, category in enumerate(categories):
            if index==0:
                print(' '*5,end='')
            if len(category)<=i:
                print(' ',end='  ')
            else:
                print(category.name[i], end='  ')
        print()
'''

def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    cart = ''
    total_spent = 0

    for category in categories:
        total_spent += category.get_amount_spent()

    percentages = []
    for category in categories:
        percentage = (category.get_amount_spent()/total_spent)*100
        percentages.append(percentage)

    for y in range(0,110,10):
        for x in range(0,(4+len(categories)*3)):
            if x==0:
                cart+= f'{100-y:>3}'
            elif x==1:
                cart+= '|'
            elif x==2:
                cart+=' '
            elif x%3==0:
                index=(x-3)//3
                #print(index)
                if index==len(percentages):
                    pass
                elif (100-y)<=(percentages[index]//10)*10:
                    cart+='o'
                else:
                    cart+=' '
            else:
                cart+=' '
    
        cart+='\n'

    x_axis = '-'*((len(categories)*3)+1)
    cart+=f"{x_axis:>{len(x_axis)+4}}\n"

    for i in range(len(max(categories,key=len))):
        for index, category in enumerate(categories):
            if index==0:
                cart+=' '*5
            if len(category)<=i:
                cart+=' '*3
            else:
                cart+=f'{category.name[i]}  '
        if i<len(max(categories,key=len))-1:
            cart+='\n'
    
    return title+cart

def main():
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(37.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    auto = Category('Auto')
    auto.deposit(300, 'deposit')
    auto.withdraw(100)
    print(food)
    print(clothing)
    print(auto)

    categories = [food, clothing, auto]

    print(create_spend_chart(categories))

if __name__ == "__main__":
    main()