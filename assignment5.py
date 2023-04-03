import json
x={
"name": "abhi",
"age":23,
"company":"cloudeq",
"fav_colors":[{1:"Blue"},{2:"Pink"},{3:"White"},{4:"Black"}]
}
print(json.dumps(x));

#Parameters which are used in dumps function
#Dumps function converts object to the string
#4 parameters are used syntax is: dumps(name of the object,indent,separators,sort_key)
#indent defines the number of indents
#separators is used to separates the key form values by using separator symbol
#sort_key is used to ensure that the result is in sorting order or not

print(json.dumps(x,indent=4,separators=(". ", " = "),sort_keys=True))

## raise exception
# Python program to handle simple runtime error
#Python 3
 
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")

# file compehnsion
colors=["green","blue","pink","orange","white","black"]
newlist=[x for x in colors if "r" in x]
print(newlist)

newlists=["Even" if i%2==0 else "Odd" for i in range(10)]
print(newlists)