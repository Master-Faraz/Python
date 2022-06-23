from pprint import pprint

def rem(str):
    return str.replace(" ","")


name="This is my first key value pair which consist of letters "

n=rem(name)


a=dict()
for i in n:
    if i not in a.keys():
        a[i]=1
    else:
        a[i]+=1

# pprint(a,width=1)

sorted_List=sorted(a.items() , key=lambda kv:kv[1] , reverse=True)
# print(sorted_List )

print(sorted_List[0])
