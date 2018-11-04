domName = input("Write domain: ")
dN = domName.split("/")
dN = dN[2]
dN = dN.split('.')
dN = dN[:-1]
print(dN)
for dNw in dN:
    if dNw == "www":
        continue
    else:
        dName = dNw
print(dName)
