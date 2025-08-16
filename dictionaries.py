#  in a dictionary , a key : is assigned a value 
#  for eg , below the key prasham is assigned a value Jain . and so on


dic1 = {
    "Prasham": "Jain","Hrishi": "Bhalaria","Ankit":"Agrawal",
    "Arjun":"Singh",123:245,1999:"Hello"}
print(dic1["Ankit"])
dic1["World"] = 99999
print(dic1["World"])

dic2 ={}
print(dic2)

dic1[245] = 10000
print(dic1[245])

for i in dic1 :
    print(dic1[i]) # this only gives us the value and not the key
    print(i) # this gives the key and not the value
    
dic = {
    "Prasham": "Jain","Hrishi": "Bhalaria","Ankit":"Agrawal",
    "Arjun":"Singh",123:245,1999:"Hello","PR":[1,34,"FUCK OFF"],
    "HELLO":["damn",999,{567:889}]}
print(dic["PR"][2])
print(dic["HELLO"][2][567])

