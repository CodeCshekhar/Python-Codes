s = "Hello {name}"
print(s.format(name="Alice"))  # Hello Alice
print(s.format_map({'name': 'Bob'}))  # Hello Bob
print("1\t2\t3".expandtabs(4)) # 1   2   3

table = str.maketrans("aeiou", "12345")
print("hello".translate(table))  # h2ll4
