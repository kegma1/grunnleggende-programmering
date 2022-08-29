from http.client import ImproperConnectionState

x = 1
print(x)
x = "Hello world"
print(x)

x = 2
y = 3

x, y = y, x

print(f"x = {x}\ny = {y}")