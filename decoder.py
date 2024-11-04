import binascii

typedcode = input("")
newtypedcode = typedcode.replace("(", "0").replace(")", "1")
print(binascii.unhexlify("%x" % int(newtypedcode, 2)).decode("utf-8"))

try:
    input("Press return to exit...")
except EOFError:
    pass
