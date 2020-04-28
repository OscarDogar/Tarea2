Z=[0.4,0.5,0] 
C=[0.3,0.1,2.7] 
E=[0.5,0.5,6] 
R=[0.6,0.4,6]
 
newC = str(C[0]) +'+'+ str(C[1]) +'=<'+ str(C[2]) 
newE = str(E[0])+'+'+str(E[1])+'='+str(E[2]) 
newR = str(R[0])+'+'+ str(R[1])+'=>'+str(R[2])
 
cantI = 2
 
for x in range(cantI): 
     Z[x] = Z[x]*-1
 
X=[0,0,0,0] 
for x in range(cantI): X[x] = str(C[x]) +'+'+ str(E[x]) +'+'+ str(R[x]) + '=>' + str(Z[x])
 
print(X[0]) 
print(X[1])
