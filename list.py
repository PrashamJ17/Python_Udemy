list_1 = [1,2,3,4,10,12,'','prasham',[[[1,'iugf',['oebfu','',33]]]]]

list_1.append(2) # adds an item at the end of the list
list_1.extend("",2,[],[[[34,'',9846,'pras']]]) # ads all the items in the end of the list 
list_1.insert(2,'u5') # adds an tem at the specified index of the list

list_1.remove('u5') # Remove the first item from the list whose value is equal to x
list_1.pop([2]) #Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list.

list_1.clear() # deletes all the elements of the list 
list_1.index(1,start = 3,stop = 5) # gives the index of the specified element in the list
# start and end means search th element btwn 3 and 5

list_1.count(1) # returns theno. of times 1 has appeared in the list
list_1.reverse() # reverses the list 
list_1.copy() # cpies the lst into another variable


