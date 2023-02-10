import sys
sys.path.append("c:\\users\\admin\\appdata\\local\\programs\\python\\python311\\lib\\site-packages")
import numpy as np
def change_array(array1,array2,M,N):
    array1=np.array(array1,dtype=list)
    array2=np.array(array2,dtype=list)
    a=[0]*(N)
    a=np.array(a,dtype=list)
    array3=[None]*(M+N-1)
    j=0
    for i in range(M+N-1):
        if array1[i]==0:
            j+=1
            a[j]=i
    a[0]=0
    for j in range(0,M+N-1):
        if 0<=j<a[1]:
            array3[j]=int(array2[j]*(j+2))
    for i in range(1,N-1):
        for j in range(0,M+N-1):
            if a[i]<j<a[i+1]:
                array3[j]=int(array2[j]*(j+1-a[i]))
            elif array1[j]==0:
                array3[j]=None
    for j in range(0,M+N-1):
        if a[N-1]<j:
            array3[j]=int(array2[j]*(j+1-a[N-1]))
        elif array1[j]==0:
            array3[j]=None
    array4=[None]*(M+N-1)
    array4=np.array(array4,dtype=list)
    arraya=[0]*(M+N)
    arraya=np.array(arraya,dtype=list)
    for i in range(0,len(arraya)):
        arraya[i]=[-1]
    for i in range(0,a[1]):
        if array3[i]==0:
            array4[i]=0
        elif array3[i]>=1:
            array4[i]=array1[array3[i]-1]

    for j in range(1,N-1):
        for i in range(a[j]+1,a[j+1]):
            if array3[i]>=1:
                array4[i]=array1[array3[i]+a[j]]
            elif array3[i]==0:
                array4[i]=0
    for i in range(a[N-1]+1,M+N-1):
        if array3[i]==0:
            array4[i]=0
        elif array3[i]!=0:
            array4[i]=array1[array3[i]+a[N-1]]
    array1=np.append(0,array1)
    array4=np.append(-2,array4)
    for i in range(0,len(a)):
        a[i]=a[i]+1

    for i in range(a[0],a[1]):
        if array4[i]==0:
            if arraya[0][0]==-1:
                arraya[0].remove(-1)
            arraya[0].append(array1[i])
    for j in range(1,N-1):
        for i in range(a[j]+1,a[j+1]):
            if array4[i]==0:
                for k in range(a[j],a[j+1]):
                    if array1[k]==0:
                        if arraya[k][0]==-1:
                            arraya[k].remove(-1)
                        arraya[k].append(array1[i])
    for i in range(a[N-1]+1,M+N):
        if array4[i]==0:
            for k in range(a[N-1],M+N):
                if array1[k]==0:
                    if arraya[k][0]==-1:
                        arraya[k].remove(-1)
                    arraya[k].append(array1[i])
    for i in range(1,M+N):
        for j in range(0,M+N):
            if array4[j]==i:
                for k in range(0,M+N):
                    if array1[k]==i:
                        if arraya[k][0]==-1:
                            arraya[k].remove(-1)
                        arraya[k].append(array1[j])
    arr=np.array((array1,arraya))
    return arr
#M=number_customer, N=number_truck