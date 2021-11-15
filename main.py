def takeuserinput():
    print('Select an option:'),
    print(str(1)+'.'+'Credit'),
    print(str(2)+'.'+'Debit'),
    print(str(3)+'.'+'Check Balance'),
    print(str(4)+'.'+'Exit')
    n = int(input())
    if n not in [1,2,3,4]:
        print('Invalid Input')
        exit()
    return n

def credit(balance):
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
    if balancce[1]<0:
        balance[0]-=1 
        balance[1]+=100
    print('Successful')
     
    
    
def debit(balance):
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
    if balancce[1]<0:
        balance[0]-=1 
        balance[1]+=100
    print('Successful')
    
def checkbalance(balance):
    print('Current Balance is '+str(balance[0])+'D '+str(balance[1])+'C')
    
    
def exit():
    print('Thank you!')
    
def main():
    balance = [0,0]
    while True:
        inpt = takeuserinput()
        if inpt==1:
            credit(balance)
        if inpt==2:
            debit(balance)
        if inpt == 3:
            checkbalance(balance)
        if inpt==4:
            exit()
            break
    

    
if __name__ == '__main__':
    main()

    
                

    
