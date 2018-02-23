import string
def next_str(str):
  
   return ''.join([chr(ord(c) + 2)  if c in string.ascii_lowercase and ord(c) < 121 else chr(ord(c) - 24) if c in string.ascii_lowercase  else c for c in str])

def next_str2(str):
    dict = {'k':'m','o':'q','e':'q' }
    trantab = str.maketrans(dict)
    return ''.join(str.translate(trantab))

    
if __name__ == "__main__":
    print(next_str("koe"))
    print(next_str("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))
    
    #print(len(string.ascii_lowercase))
    # IMMUTABLE
    # greeting = "Hello, world!"
    #greeting[0] = 'J'            # ERROR!
