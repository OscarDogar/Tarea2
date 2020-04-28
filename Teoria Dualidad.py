from scipy.optimize import linprog

cantI=2 #cantidad de terminos independientes
cantE=3 #cantidad de inecuaciones

c=[20,30] #funcionobjetivo
A_ub=[[2,2],[3,1],[1,2]] #Matriz de coeficientes
b_ub=[5,3,4] #terminos independientes o vector solucion


#*Como sabemos que las restricciones del primal son >= al pasarlo a dual 
#estas pasan a ser <=, entonces realizamos el siguiente procedimiento

for x in range(cantE):
    b_ub[x]=b_ub[x]*-1
    for y in range(cantI):
        A_ub[x][y]=A_ub[x][y]*(-1)

#pasamos los valores a la funcion linprog para realizar la optimizacion
res=linprog(c,A_ub,b_ub,bounds=(0,None))

print(res)
print("Valor optimo: ",res.fun, "\nX: ",res.x) 

    
    