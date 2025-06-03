#*******************14-May-2025*******************
## interger typcast to other data type
##integer
print(int('12.2')) # got an error
print(int('12')) 
print(int('ten')) # got an error
print(int(10+20j)) # got an error

###################################################
#float

print(float(1))
print(float(12.0))
print(float('12.0'))
print(float('ten'))#error
print(float(10+20j))


####################################
#string
print(str(1))
print(str(12.3))
print(str('12.3'))
print(str(True))
print(str(12+12j))

##########################
##boolean
print(bool(1.1))
print(bool(0+0j))
print(bool(1+12j))
print(bool('test'))

##Complex Data type
print(complex(0))
print(complex(1))
print(complex('10'))
print(complex(10,10))
print(complex(True))
print(complex(True,False))




