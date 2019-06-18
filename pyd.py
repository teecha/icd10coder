import csv
import re
reader = csv.reader(open('ICD10_Codes.csv', 'r'))
#lol = ['A','B','C','D','E','F','G',"H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#loll = ["A.csv","B.csv","C.csv","D.csv","E.csv","F.csv","G.csv","H.csv","I.csv","J.csv","K.csv","L.csv","M.csv","N.csv","O.csv","P.csv","Q.csv","R.csv","S.csv","T.csv","U.csv","V.csv","W.csv","X.csv","Y.csv","Z.csv"]
icd = {}
code = []
name = []
first = []
firstcode = []
for row in reader:
    k, v = row
    icd[v] = k
    code.append(k)
    name.append(v)
print("Successfull")
#print(code[0])
#print(name[0])
symptom1 = input("Enter the primary symptom ")
lower = symptom1.lower()
#print("The Icd 10 code for " + a + " is " + icd[Disease])
i = 0
#for j in range(0,26):
    #regex = lol[j]
    #art = loll[j]
    #print(art)
while i<91096:
    string = code[i]
    #match = re.match(regex,string)
        #print(str(code[i]))
#    if match:
        #print(regex)
    #    file = open(str(art), 'a')
    #    file.write(code[i]+",")
##        file.close()
    string = name[i]
    if lower in string:
        print(code[i])
        first.append(name[i])
        firstcode.append(code[i])
    i += 1
symptom2 = input("enter the secondary symptom ")
j = 0
while j<len(first):
    #print(first)
    #print(firstcode)
    if symptom2 in first[j]:
        print(firstcode[j])
    j += 1
