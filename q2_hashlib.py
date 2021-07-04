import hashlib
print(hashlib.algorithms_available)
def function1():
    text = input("Enter Text For Convert String to Different Alogorithams : ")
    result1 = hashlib.sha224(text.encode('utf-8'))
    result2 = hashlib.sha256(text.encode('utf-8')).digest
    result3 = hashlib.sha512(text.encode('utf-8')).hexdigest

    print("\t ** Final String From sha224 Using hashlib Is Below ** ")
    print(result1)
    print("\t ** Final String From sha256 Using hashlib(digest) Is Below ** ")
    print(result2)
    print("\t ** Final String From sha512 Using hashlib(hexdigest) Is Below ** ")
    print(result3)

function1()