class user:
    balance = [0,0]
    def credit(self):
        balance = self.balance
        print('Enter Amount:')
        n = input()
        if 'D' not in n:
            dollars = 0 
            cents = int(n[:-1])
        elif 'C' not in n:
            dollars = int(n[:-1])
            cents = 0 
        else:
            dollars,cents = n.split(' ')
            dollars = int(dollars[:-1])
            cents = int(cents[:-1])
        if (balance[0]+dollars)*100 + balance[1]+cents <0:
            print('Sorry! Low Balance.')
        balance[0]+=dollars
        balance[1]+=cents
        if balance[1]>100:
            balance[0]+=balance[1]//100
            balance[1] %=100
        if balance[1]<0:
            balance[0]-=1 
            balance[1]+=100
            
        print('Successful')

    def debit(self):
        balance = self.balance
        print('Enter Amount:')
        n = input()
        if 'D' not in n:
            dollars = 0 
            cents = int(n[:-1])
        elif 'C' not in n:
            dollars = int(n[:-1])
            cents = 0 
        else:
            dollars,cents = n.split(' ')
            dollars = int(dollars[:-1])
            cents = int(cents[:-1])
        if (balance[0]-dollars)*100 + balance[1]-cents <0:
            print('Sorry! Low Balance.')
        balance[0]-=dollars
        balance[1]-=cents
        if balance[1]>100:
            balance[0]+=balance[1]//100
            balance[1] %=100
        if balance[1]<0:
            balance[0]-=1 
            balance[1]+=100
            
        print('Successful')
        
    def checkbalance(self):
        balance = self.balance
        print('Current Balance is '+str(balance[0])+'D '+str(balance[1])+'C')
    
        
    def exit(self):
        print('Thank you!')
