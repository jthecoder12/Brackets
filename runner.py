import sys
import binascii

try:
     with open(sys.argv[1], "r") as f:
        newtypedcode = f.read().replace("(", "0").replace(")", "1")
        exec(binascii.unhexlify("%x" % int(newtypedcode, 2)).decode("utf-8"))
except Exception as e:
    print(e)
    
input("Press return to exit...")
