
"""author name:Saloni Jaiswal

Date:20-1-2018

Feature Extraction"""

import csv
import feature_extraction as f

code = list(list())
feature = dict(dict())
#function to get only opcodes
def openf(filename):
    with open(filename, mode='r', encoding='UTF-8') as file:
        text = file.readlines()
    opcode = []
    for i in range(len(text)):
        op = text[i][75:83]
        if op != '':
            if op[0] == ' ':
                op = op[1:]
            if op[-1] == '%' or op[-1] == '$' or op[-1] == '0' or op[-1] == '-' or op[-1] == '(':
                op = op[:-1]
            if op[-1:] == '\n':
                #print(op)
                op = op[:-1]
            if op[0] != '0' and op[0] != '.':
                opr = op
                opcode.append(opr)
    return opcode



#for clean files we take all opcode with its count corresponding to a file and save in dictionary of dictionary 
for k in range(100):
    filename = 'clean files/'+str(k+1)+'_disa.txt'
    code.append(openf(filename))
    feature['file'+str(k+1)] = {}
    for i in range(len(code[k])):
        if code[k][i] not in feature['file'+str(k+1)]:
            feature['file'+str(k+1)][code[k][i]] = 1
        else:
            feature['file'+str(k+1)][code[k][i]] = feature['file'+str(k+1)][code[k][i]] + 1
    feature['file'+str(k+1)]['class'] = 'clean'
    
#for malware files we take all opcode with its count corresponding to a file and save in dictionary of dictionary
for k in range(100):
    filename = 'malware files/'+str(k+1)+'_disa.txt'
    code.append(openf(filename))
    feature['file'+str(k+101)] = {}
    for i in range(len(code[k])):
        if code[k][i] not in feature['file'+str(k+101)]:
            feature['file'+str(k+101)][code[k][i]] = 1
        else:
            feature['file'+str(k+101)][code[k][i]] = feature['file'+str(k+101)][code[k][i]] + 1
    feature['file'+str(k+101)]['class'] = 'malware'
#print(feature)

#In this all features name is taken in list
attributes = []
for i in range(len(feature)):
    key = list(feature['file'+str(i+1)].keys())
    for j in range(len(key)):
        if key[j] not in attributes:
            attributes.append(key[j])
#print(attributes)

for i in range(len(feature)):
    for k in range(len(attributes)):
        if attributes[k] not in feature['file'+str(i+1)]:
            feature['file'+str(i+1)][attributes[k]] = 0
"""for i in range(len(feature)):
    print("number of attribute in file",i+1,":",len(feature['file'+str(i+1)]))"""

#saving all in a file  
with open('dataset.csv', 'w') as csvfile:
    fieldnames = f.attributes
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(f.feature)):
        writer.writerow(f.feature['file'+str(i+1)])  
csvfile.close()

print("file is created..")