#Variables defined in a function are only known in the function. That’s because of the scope of the variable. 
#In general that’s not a problem, unless you want to use the function output in your program.

#def getPerson():
 #   name = "Leona"
  #  age = 35
   # country = "UK"
    #return name,age,country
#name,age,country = getPerson()
#print(name)
#print(age)
#print(country)