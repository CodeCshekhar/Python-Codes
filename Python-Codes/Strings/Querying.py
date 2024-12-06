s = "hello"
print(s.startswith('he'))     # True
print(s.endswith('lo'))       # True
print(s.isalpha())            # True
print(s.isalnum())            # True
print("123".isdecimal())      # True
print("123".isdigit())        # True
print("½".isnumeric())        # True
print("name".isidentifier())  # True
print("abc".islower())        # True
print("ABC".isupper())        # True
print("   ".isspace())        # True
print("Hello World".istitle()) # False
