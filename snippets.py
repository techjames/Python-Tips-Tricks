
# Create a single string from all the elements in a list
a = ["The", "Sly", "Fox"]
b = "".join(a)
print(b)


# Reverse a String
a ="TheSlyFox"
print(a[::-1]) 


# Split substrings
a = "The Sly Fox"
print(a.split())


# Dictionary merge
dict_one =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dict_two =	{
  "brand": "Triumph",
  "model": "Dolomite"
}

merged = {**dict_one, **dict_two}
print(merged)


# Find the most common element in a list
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))


# Ternary operators
age = 16
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')

