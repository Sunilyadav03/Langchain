
l1= [1,1,1,2,1,2,2, 3,3,3,3,3,2]
s1= set(l1)
k1= []
for i in s1:
    count= 0
    for j  in l1:
        if i== j:
            count+= 1
            if count== 3:
                k1.append(i)
                break
        elif i!= j and count> 0 and count< 3:
            break
print(k1)
                
