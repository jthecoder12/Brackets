import binascii

while True:
    try:
        typedcode = input(">>> ")
    except EOFError:
        print(end="")
    newtypedcode = typedcode.replace("(", "0").replace(")", "1")
    try:
        if typedcode == "exit":
            break
        else:
             exec(binascii.unhexlify("%x" % int(newtypedcode, 2)).decode("utf-8"))
    except Exception as e:
        print(e)
        
input("Press return to exit...")
