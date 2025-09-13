# The 'f' in f-string formatting is case insensitive, meaning you can use both lowercase f and uppercase F.
# print(f"text")
# print(F"More text")

# .2f rounds a floating point number up to 2 decimal values,
# but a colon must come before that, and the entire things need to be enclosed in curly braces.
# print(f"{3.245678:.2f}")
# You can change the 2 in .2f to any other number, and it will round to that number of values.
# print(f"{3.245678:.3f}")

# The number (35) needs to be (6) digits long, so there are spaces before the number and it is trailing behind
# This defaults to adding spaces, but you can put the 'filling' before the requirement of digits long and it will use that.
# HOWEVER, you can only use numerical numbers as custom filling (no letters, no special characters)).
# print(f"{35:6}")
# print(f"{35:06}")
# print(f"{35:_6}")     # RETURNS ERROR
# Same thing can be done in reverse and with float decimals. Since there's f, it refers to the decimal part needing to be 6 digits,
# so it adds 4 zeros after it.
# print(f"{35.35:_.6f}")

# The string "String" is 6 letters long, and by using >10, it adds 4 spaces before it, since that makes 10 in total.
# string = "String"
# print(f"{string:>10}")
# The same thing can be done after the string with <10, and while it isn't visible, the string has 4 spaces AFTER it.
# print(f"{string:<10}")
# It can also be 'centered' with 2 spaces on each side through ^10.
# print(f"{string:^10}")
# It also gets a custom filling character, which you put before the >, <, or ^ symbol.
# Since this is a string value, and not a numerical value, it isn't limited to just numerical values,
# and can have a filling of strings, numbers, and special characters
# print(f"{string:_>10}")

# It's also possible to convert things by using the specific code.
# You can convert an integer to hexadecimal.
# var = 101
# print(f"{var:x}")
# You can also convert an integer to octal.
# print(f"{var:o}")
# This converts the integer to a scientific exponential.
# print(f"{var:e}")