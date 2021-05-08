# dictionary / object


## initialise dictonary
object1 = {
    "name" : "Saravana",
    "age" : 22,
    "gender" : "male"
}


## access value using key
### 1   (throws error if the key is not present)
print(object1["name"])

### 2   (doesn't throw error if the key is not present instead returns "none")
print(object1.get("address"))


## get length of dictionary
print(len(object1))


## add or update element from dictionary  (if key already present then updates the value else creates new key and stores value)
### 1
object1.update( {"age" : 23} )
print(object1)
object1.update( {"blood group" : "A+ve"} )
print(object1)

### 2
object1["age"] = 22
object1["state"] = "TN"
print(object1)


## remove element from dictionary
### 1
object1.pop("state")
print(object1)

### 1
del object1["blood group"]
print(object1)


## get list of keys
print(object1.keys())


## get list of values
print(object1.values())


## directly check for element
if "age" in object1:
    print("age", object1["age"])
else:
    print("Not available")

if "state" not in object1:
    print("Not available")


## iterating through dictionary
### 1  
for key in object1:
    print(key)
    print(object1[key])

### 2
for key, value in object1.items():
    print(key)
    print(value)


## empty the dictionary
object1.clear()
print(object1)


# ## value of different datatype
# obj = {
#     "cities" : ["madras", "banglore", "mumbai", "delhi"],
#     "states" : {
#         "madras" : "tn",
#         "banglore" : "kt",
#         "mumbai" : "mh",
#         "delhi" : "dh"
#     }
# }

# print(obj["cities"][1])
# print(obj["states"]["madras"])