# x = 30   this is a global varible.
def funct1():

    print(x)

def funct2():

    print(x) 
x = 30   # This is a global varible.
funct1()
funct2()

"""
scope resolution : Order - > LEGB

    Built-in Variable 
          ^
          |
          
    Global variable

          ^
          |
          
     Enclosed variable
     
          ^
          |

     Local varible 




"""