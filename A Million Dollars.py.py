print('What would you do with a million dollars? (Pick one :/ )')
print('1. Buy a Farari')
print('2. Buy a Manshion')
print('3. Pay off all your debts')
print('4. Party Like a rockstar!')
def options():
    print('I`d choose: ')
    choise = input()
    if choise == 1:
        print('You don`t know how to drive a sports car and get in a wreck.')
    elif choise == 2:
        print('You blow all your money on the manshion estate and end up unable to pay your basic utility bills.')
    elif choise == 3:
        print('You pay off all your debts and have plenty left over to invest in your future and live hapilly for many years')
    elif choise == 4:
        print('You get totally wasted at the party and end up in an unfortinate accident during the events that night and didn`t survive the trip to the hospital.')
    else:
        print('Invalid choise, try again')
        return options()
options()
print('--end of line--')
#WRITTEN IN PYTHON 2.7
