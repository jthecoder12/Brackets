import binascii
from sys import argv

codesrc: str

with open(argv[1], "r") as code:
    codesrc = code.read()

content:str = str(bin(int(binascii.hexlify(codesrc.encode("utf-8")), 16))).replace("0b", "").replace("0", "(").replace("1", ")")

with open(argv[2], "w") as compiled:
    compiled.write(content)

