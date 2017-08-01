#WRITTEN IN PYTHON 3.6
import random
answer=['It is certain.','It is decidedly so.','Yes','Reply hazy, try again.','Ask again later.','Concentrate and ask again.','My reply is no.','Outlook not so good','Very Doubtful']
r=random.randint(0,8)
print('Ask your question and the magic 8 Ball will tell you what lies ahead.')
input() #input is not relevent or even used, only to make user think it has meaning
print('Magic 8 Ball says:')
print(answer[r])
print('DEBUG: Element:'+str(r)+' | Total Elements:'+str(len(answer))) #comment out to hide debug/verbose output
