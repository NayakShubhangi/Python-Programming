# _ in front of a variable when you initialize it makes it protected,
# but not private, so while it warns users not to change it, it can still be changed. It is
# hidden from users who use from import, but not from those who just use import.
# __ makes it private. It can no longer be changed by the user.
# The difference between from import and regular import is that from import specifies what the user wants,
# while regular import just imports everything. When you use from import to import a protected variable, Python hides it,
# but when you use regular import, Python doesn't hide the protected variable.
# Both imports cause the file you're importing to run, except when you use if __name__ == "__main__":, because when you import the file,
# it doesn't get the name "main", so it won't run.

var = "str"
var2 = 2
_var3 = "protected"
if __name__ == "__main__":
    print(var)
    print(var2)
    print(_var3)
    print(__name__)