#WRITTEN IN PYTHON 2.7
print('enter 6 items')
one=raw_input()
two=raw_input()
three=raw_input()
four=raw_input()
five=raw_input()
six=raw_input()
lista=[one,two,three,four,five,six]
print('your list of things is: '+str(lista[:])+'. with '+str(len(lista))+' elements in it')
print('what item do you want?')
x=input()
print('here is item #'+str(x)+', which is: '+str(lista[x-1]))
