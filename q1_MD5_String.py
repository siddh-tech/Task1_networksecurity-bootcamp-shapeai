import hashlib
#print(hashlib.algorithms_available)
def function1():
    text = input("Enter Text For Converting String To MD5 : ")
    result1 = hashlib.md5(text.encode('utf-8'))
    result2 = hashlib.md5(text.encode('utf-8')).digest
    result3 = hashlib.md5(text.encode('utf-8')).hexdigest

    print("\t ** Final String From MD5 Using hashlib Is Below ** ")
    print(result1)
    print("\t ** Final String From MD5 Using hashlib(digest) Is Below ** ")
    print(result2)
    print("\t ** Final String From MD5 Using hashlib(hexdigest) Is Below ** ")
    print(result3)

function1()