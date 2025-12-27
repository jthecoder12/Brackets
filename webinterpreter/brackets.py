from browser import document
import binascii

brackets_scripts = document.select('script[type="text/brackets"]')

for script in brackets_scripts:
    if "src" in script.attrs: 
        with open(script.attrs["src"], "r") as f: code = f.read()
    else: code = script.text

    try:
        newtypedcode = code.replace("(", "0").replace(")", "1")
        exec(binascii.unhexlify("%x" % int(newtypedcode, 2)).decode("utf-8"))
    except Exception as e:
        print(e)