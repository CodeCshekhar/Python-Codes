s = 'Demo' # Single Quoted String
t = '"Demo2"' # Double Quoted String
r =  """Demo3""" # Triple Quoted String
print(s+t+r) #Simply printing All

#We are Cutting the String in simple language
slice = s[0:1] #Staring from index zero to one
slice1 = t[-3:-1] #Staring from index minus three to minus one - Negative Slicing
slice2 = r[0:4:2] #Slicing with values skip
print(slice + slice1 + slice2)