prediction = open("/Users/alfred/PycharmProjects/NER/output.txt", "r")
label = open("/Users/alfred/PycharmProjects/NER/outputlist.txt", "r")

first=[]
last=[]

for token in label:
    first.append(token.strip())

print(first)

for token in prediction:
    last.append(token.strip())
#print(last)

print(len(first))


txt = open('final.txt', 'w')
count = 0
i=0
j=0
while i<len(first) and j<len(first):
         if (first[i]).split(" ")[0] == (last[j]).split("@")[0]:
            first[i] = first[i] + " " + (last[j]).split("@")[-1]
            print(first[i].split(" ")[0], last[j].split("@")[0])
            print(first[i], file=txt)
            i =i+1
            j =j+1
            count = count+1

         if (first[i]).split(" ")[0] != (last[j]).split("@")[0]:
            first[i] = first[i] + " O"
            print(first[i], file=txt)
            #print(first[i].split(" ")[0], last[j].split("@")[0])
            i=i+1


txt.close()

print(i)
print(j)
print(count)