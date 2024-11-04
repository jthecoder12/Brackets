bintoconv = input("Binary to convert: ")
newtypedcode = bintoconv.replace("0", "(").replace("1", ")").replace(" ", "")
print(newtypedcode)

try:
    input("Press return to exit...")
except EOFError:
    print(end="")
