#dictionaries
laptop ={"make":"lenovo" ,"colour":"black" ,"weight":"1.2kg","year":"2000"}
print(laptop["make"])
print(laptop["colour"])

#to modify a value
laptop["colour"] = "red"
print(laptop["colour"])

#to add a value
laptop["size"]="256GB"
print(laptop["size"])
#deleting the element
del laptop["colour"]
print(laptop)

laptop_siz = laptop.copy()
print(laptop_siz)
"""
for key,value in laptop.items():
    print("\n")
    print(key)
    print(value)
"""
