"""
Write a python script to create 5 variables each of them containing different types of data like 
                            (35, True, "MySirG", 5.46, 3+4j)
Now print values of all the variables along with their data types
"""

# creating and initializing variables
int_var, bool_var, str_var, float_var, complex_var = 35, True, "MySirG", 5.46, 3+4j

# printing values along with data type
print(
      "int =",int_var,"type =",type(int_var), 
      "\nbool =",bool_var,"type =",type(bool_var), 
      "\nstr =",str_var,"type =",type(str_var),
      "\nfloat =",float_var,"type =",type(float_var),
      "\ncomplex =",complex_var,"type =",type(complex_var),
     )
