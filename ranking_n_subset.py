
"""author name:Saloni Jaiswal
Date:24-1-2018
Module3-ranking and making subset of selected feature"""

import csv
import math
infogain=[]
symm_uncer={}
symm_uncer1={}
symm={}
l=[]

"""loading the file"""
def loadDataset(filename):
	with open(filename, 'rt') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	return dataset

"""calculate the class labels and probablity"""
def separateByClass(c,dataset):
	separated = {}
	t=[]  
	for i in range(len(dataset)): 
		vector = dataset[i]   
		if (vector[c] not in separated):
			separated[vector[c]] = []
		separated[vector[c]].append(vector)
        
	for key, value in separated.items():
          k=[]            
          a=len([item for item in value if item])
          """no.of tuples in individual separation"""
          t.append(a)
          
	for key in separated:
         k.append(key)
	entropy_c=0 
    
	for i in range(len(t)):
         s=t[i]/(len(dataset))
         """calculating entropy of the class"""
         entropy_c=entropy_c+s*(math.log(s)/math.log(2))
	entropy_c=-1*entropy_c        
	return k,entropy_c
dataset=loadDataset('dataset1.csv')
l,entropy_c=separateByClass(-1,dataset)

"""calculating all the parameters for each feature"""
def attribute_separation(att_n,dataset,c_n):
	separated = {}
	t=[]
	s=0
	r=0
	a3=0
	p=[]
	q=[]
    
	"""This call is for getting no. of separation and entropy"""
	l,entropy_c=separateByClass(c_n,dataset)
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[att_n] not in separated):
			separated[vector[att_n]] = []
		separated[vector[att_n]].append(vector)
        
	for key, value in separated.items(): 
          a=len([item for item in value if item])
          t.append(a)    
	entropy_a=0
    
	for i in range(len(t)):
         n=t[i]/(len(dataset))
         entropy_a=entropy_a+n*(math.log(n)/math.log(2))    
	entropy_a=-1*entropy_a   
     
	for key in separated:
              s=0
              r=0
              for j in range(len(dataset)):
                  vector=dataset[j]
                  if(vector[att_n]==key):
                      if(vector[-1]==l[0]):
                          s=s+1
                      else:
                          r=r+1
              p.append(s)
              q.append(r)    
              
	for i in range(len(separated)):
		a1=p[i]/t[i]     
		a2=q[i]/t[i]
		if(p[i]==0):
			a1=1
		if(q[i]==0):
			a2=1    
		a3=a3+(t[i]/(len(dataset)))*(a1*(math.log(a1)/math.log(2))+a2*(math.log(a2)/math.log(2)))#gain is calculated
	gain=entropy_c-a3
	infogain.append(gain)
	"""symmetric uncertainity is calculated"""
	s_u=(2*gain)/(entropy_c+entropy_a) 
	symm_uncer[att_n]=s_u  
	if(c_n==415):
		symm[att_n]=s_u       

"""main function"""    
def main():    
    th=0
    count=[]
    count1=[]
    count2=[]
    dataset=loadDataset('dataset1.csv')
    del dataset[0]
    for i in range(0,791):
        """This call gives the symmetric uncertainity"""
        attribute_separation(i,dataset,-1) 
    """sorting in descending order"""
    t=sorted(symm_uncer, key=symm_uncer.get,reverse=True)
    
    for r in t:
        symm_uncer1[r]=symm_uncer[r]
    th=sum(symm_uncer1.values())
    """finding threshold value"""
    th=th/792
    
    for key, value in symm_uncer1.items():
        if(value<th):
            count.append(key)
            
    for i in range(len(count)):
        symm_uncer1.pop(count[i])#removing features which are smaller than threshold
        
    for key,value in symm_uncer1.items():
        count1.append(key)
    c=count1[17]
    #print(count1)
    
    for i in count1:
        """This call gives the symmetric uncertainity corresponding to highest symmetric uncertainity with class"""
        attribute_separation(i,dataset,c)
        """calculate the SU(p,q) with SU(q,c)"""
        if(symm_uncer1[i]<=symm[i]):
            symm_uncer1.pop(i)

    for key,value in symm_uncer1.items():
        count2.append(key)
    print("total features selected:",len(count2))    
    data=loadDataset('dataset1.csv')
    print("features name selected by correlation algorithm:")
    p=1
    print("RANKING:-")
    for i in count2:
        
       print (p,":-",data[0][i])
       p=p+1
    
    count2=[]
    i=0
    for key,value in symm_uncer1.items():
        if(i<159 or i>445):
            count2.append(key)
        i=i+1
        
    count2.append(791)
    #print(len(count2))
    data=loadDataset('dataset1.csv')
    rows=[]
    for j in range(len(dataset)):
        z=[]
        for i in count2:
            z.append(data[j][i])
        rows.append(z)
    filename = "result.csv"
    #print(rows) 
    """ writing to csv file"""
    with open(filename, 'w') as csvfile:
        """creating a csv writer object"""
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
    print("-------file created------")
       
main()