def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Cannot add non-numeric values"

result = function(5, "5")
print(result)

result = function("abc", "5")
print(result)