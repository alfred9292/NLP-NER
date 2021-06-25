spacy = open("/Users/alfred/PycharmProjects/NER/final.txt", "r")
stanford = open("/Users/alfred/PycharmProjects/NER/stanford_finalresult.txt", "r")

spacy_list=[]
stanford_list=[]
account=0
account1=0
account2=0
account3=0
account4=0
account5=0

for i in spacy:
    spacy_list.append(i)
print(len(spacy_list))

for i in stanford:
    if i!="\n":
     stanford_list.append(i)
print(len(stanford_list))

#detect errors for spacy result
#for i in range(len(spacy_list)):
 #   account=account+1
  #  if spacy_list[i].split(' ')[-2].strip()!= spacy_list[i].split(' ')[-1].strip() and spacy_list[i].split(' ')[-1].strip() != stanford_list[i].split(' ')[-1].strip() :
   #    print(spacy_list[i],stanford_list[i])
    #   account4=account4+1
     #  print(account)
#print(account4)


#detect errors for stanford result
for i in range(len(stanford_list)):
   account1=account1+1
   if stanford_list[i].split(' ')[-2].strip()!= stanford_list[i].split(' ')[-1].strip()and spacy_list[i].split(' ')[-1].strip() == stanford_list[i].split(' ')[-2].strip():
       print(spacy_list[i],stanford_list[i])
       account5=account5+1
       print(account1)
print(account5)

#detect errors made by both system:

#for i in range(len(stanford_list)):
 #   account2=account2+1
  #  if stanford_list[i].split(' ')[-2].strip()!= stanford_list[i].split(' ')[-1].strip() and spacy_list[i].split(' ')[-2].strip()!= spacy_list[i].split(' ')[-1].strip():
   #    account3= account3+1
    #   print(spacy_list[i],stanford_list[i])
     #  print(account2)
#print(account3)



