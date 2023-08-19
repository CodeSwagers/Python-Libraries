#Tuple vs List Example
tuple_example=(1,2,3)
list_example = [1,2,3]

list_example.append("2")
try:
    tuple_example.append("5")
except AttributeError as e:
    print(f"Tuple Error {e}")

print(f"list: {list_example}")
print(f"tuple: {tuple_example}")