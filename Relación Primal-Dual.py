def show(Result):
  newZ(Restriction)
  s=""
  for i in range(len(result)):
    string = ""
    
    for j in range(len(Result[i])):
      string += str(Result[i][j])
      if(j<len(result[0])-2):
          string += "y"
          string += str(j+1)
      string += " "
       
    print("Restriction ", i+1, " is: ", string)
 
  for i in range(0, len(result[0])-2):
      s+=str("y")  
      s+=str(i+1) 
      if(i<len(result[0])-3):
          s+=str(", ") 
  print(s, ">= 0")

def newZ(Restriction):
  W=[]
  for i in range(0,len(Restriction)):
        W.append(Restriction[i][2])
  string="W = "
  c=1
  for i in W:
    string +=str(i)
    string += "y"
    string += str(c)
    string += "  "
    c=c+1
  print(string)
  return W

def trasnform(Z, Restriction):
  opt=input("Que desea hacer maximizar(max) o minimizar(min) : \n")
  while(opt.lower() != "max" and opt.lower() != "min"):
      opt=input("Que es un problema de maximizar(max) o minimizar(min) : \n")
  
  sign = "<="
  if (opt == "max"):
    sign = ">="

  Result = []
  for i in range(0, len(Z)):
    a = []
    for j in range(0, len(Restriction)):
      a.append(Restriction[j][i])
    a.append(sign)
    a.append(Z[i])
    Result.append(a)

  return Result

Z = [2, 12]
Restriction = [ [1, 2, 10],
                [5, 6, 20],
                [2, 1, 12] ]
result = trasnform(Z, Restriction)
show(result)


