#Nested List to Flattened List

def FlattenedList(Nested_List):
    Flattened=[]
    for i in Nested_List:
        if isinstance(i,list):
            Flattened.extend(list(i))
        else:
            Flattened.append(i)
    return Flattened

L=[1,2,[3,4,5],[6,7,8]]
result=FlattenedList(L)
print("Flattened List:",result)