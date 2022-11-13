a=input("enter the first number: ")                                                   
b=input("enter the second number: ")                                                      
operator=input("enter the operator: ")                                                     
if operator== "+":                                                                   
    print(float(a)+float(b))                                                              
elif operator=="-":                                                                       
    print(float(a)-float(b))                                                      
elif operator=="*":                                                                     
    print(float(a)*float(b))                                                               
elif operator=="%":                                                                     
    print(float(a)%float(b))                                                              
elif operator=="**":                                                                   
    print(float(a)**float(b))                                                           
elif operator=="/":                                                                        
    print(float(a)/float(b))                                                               
elif operator=="//": 
    print(float(a)//float(b))
else:
    print("invalid input")
