class Menu:
    def takeuserinput(self,raj):
        print('Select an option:'),
        print(str(1)+'.'+'Credit'),
        print(str(2)+'.'+'Debit'),
        print(str(3)+'.'+'Check Balance'),
        print(str(4)+'.'+'Exit')
        
        while True:
            n = int(input())
            if n not in [1,2,3,4]:
                print('Invalid Input')
                exit()
            inpt = n
            if inpt==1:
                raj.credit()
                #credit(balance)
            if inpt==2:
                raj.debit()
                #debit(balance)
            if inpt == 3:
                raj.checkbalance()
                #checkbalance(balance)
            if inpt==4:
                exit()
                break
