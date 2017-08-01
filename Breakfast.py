# Eggs, Bacon, Hash Browns, Pancakes
#WRITTEN IN PYTON 2.7
def Textentry(question):
    print(question)
    value = int(input())
    #if (value).is_integer() == True:
    #    if value <= 5:
    #        return(value)
    #else:
    #    print('INVALID entry, please use a value between 1 and 5 only')
    #    Textentry()
    return(value)
    
eggs=0
bacons=0
hashs=0
pancakes=0
value=0
#--------------
def Egg():
    question='How many eggs do you want today?'
    value = Textentry(question)
#    global eggs
#    eggs = eggs+int(value)
    return value
    
def Bacon():
    question='How many pieces of bacon do you want today?'
    value = Textentry(question)
#    global bacons
#    bacons = bacons+int(value)
    return value
    
def Hash():
    question='How many hash browns do you want today?'
    value = Textentry(question)
#    global hashs
#    hashs = hashs+int(value)
    return value
    
def Pancake():
    question='How many pancakes do you want today?'
    value = Textentry(question)
#    global pancakes
#    pancakes = pancakes+int(value)
    return value
    
def Questions():
    global eggs
    global bacons
    global hashs
    global pancakes
    global eggst
    global baconst
    global hashst
    global pancakest
    if eggs == 0: #script start
        print('Welcome to your local breakfast diner, where we serve only the best breakfast! but you must work your way up to the better meals!')
    print('------')#break code sectional output
##----------------------------------## EGGS
    if eggs < 10:
        eggst = Egg()
    eggs = eggs+eggst
    
    print('you eat '+str(eggst)+' Eggs today. [[Total:'+str(eggs)+']]')
    #print(str(eggs))####troubleshooting output
##----------------------------------## BACON
    if eggs >= 10: #enough eggs
        if bacons == 0:
            print('You`ve eaten enough eggs to have bacon with breakfast!')
        if bacons < 10 :
            baconst = Bacon()
        bacons = bacons+baconst
        print('you eat '+str(baconst)+' bacon strips today [[Total:'+str(bacons)+']]')
##----------------------------------## HASH BROWNS
    if bacons >= 10: #enough bacon
        if hashs == 0:
            print('You`ve eaten enough bacon strips to have hash browns with breakfast!')
        if hashs < 10:
            hashst = Hash()
        hashs = hashs+hashst
        print('you eat '+str(hashst)+' hash browns today [[Total:'+str(hashs)+']]')
##----------------------------------## PANCAKES
    if hashs >= 10: #enough hash browns
        if pancakes == 0:
            print('You`ve eaten enough hash browns to have pancakes with breakfast!')
        pancakest = Pancake()
        pancakes = pancakes+pancakest
        print('you eat '+str(pancakest)+' pancakes today [[Total:'+str(pancakes)+']]')
##----------------------------------## END
    if pancakes >=10:
        print('I think you`ve eaten enough today.')
        print('You`ve eaten '+str(eggs)+' eggs, '+str(bacons)+' bacon, '+str(hashs)+' Hash browns, and '+str(pancakes)+' pancakes.')
        return
    #Ask again
    Questions()
    
#Start sequence
Questions()
