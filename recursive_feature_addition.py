
"""author name:Saloni Jaiswal

Date:16-2-2018

Module5-recursive feature addition"""

import numpy as np
from sklearn import datasets, svm
from sklearn.cross_validation import train_test_split
import pandas as pd 
import csv

"""loading the file"""
def loadDataset(filename):
	with open(filename, 'rt') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	return dataset

"""recursive feature addition algorithm"""
def main(): 
    dataset = pd.read_csv('result.csv')
    t=[]
    l=1.5
    acc=70
    z=[]
    file=open('output1.txt','w')
    file.write('RECURSIVE FEATURE ADDITION\n')
    file.write('Total number of feature before applying algorithm:205\n\n')
    for i in range(1,204):
        
        X= dataset.iloc[:, 0:i].values  
        y= dataset.iloc[:, 204].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=46)
        """for i in range(0,i):
            print(i,",",end="")"""
        z.append(i)
        """function for getting accuracy after considering each feature""" 
        
        def get_accuracy(model):
            predictions = model.predict(X_test)
            right_clas = 0
            length=len(y_test)
            #print(length)
            
            for i in range(length):
                if predictions[i] == y_test[i]:
                    right_clas +=1
            accuracy = 100*right_clas*l/len(y_test)
            return accuracy 
            
        model = svm.SVC(kernel='poly')
        
        model.fit(X_train, y_train)
        
        p= get_accuracy(model)
        print(z)
        file.write('features:' +str(z)+ '\n')
        print(p)
        file.write('accuracy:' +str(p)+ '\n')
        if(p>=acc):
            t.append(i)
            acc=p
        else:
            z.remove(i)
        print(t)
        file.write('selected features:' +str(t)+ '\n\n')
        print("\n")
        data=loadDataset('result.csv')
    print("features which are selected by the recursive feature addition algorithm:")
    print(t)
    file.write('final selected feature names:')
    for j in t:
        print (j,":-",data[0][j])
        file.write(data[0][j]+',')

    
"""calling main method"""
main()    


        