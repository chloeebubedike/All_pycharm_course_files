#String formatting
# Example 1
price = 50
txt = "The price is {} pounds"
print(txt.format(price))

# Example 2

txt = "The price is {0:4.2f} dollars"
print(txt.format(price))

var1 = 1
var2 = 2
var3 = 3
#Using d with variable 2 results in error
text = "text {0:5.3f} more text {1:3d} even more text {2}"
print(text.format(var1, var2, var3))