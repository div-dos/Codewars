def dirReduc(arr):
    i = 0
    l = len(arr)
    print(arr)
    while i <= (l-2):
        print(arr[i],i)
        if arr[i] == "NORTH" and arr[i+1] == "SOUTH":
            arr = arr[:i]+arr[i+2:]
            i-=1
            l-=2
        elif arr[i] == "SOUTH" and arr[i+1] == "NORTH":
            arr = arr[:i]+arr[i+2:]
            i-=1
            l-=2
        elif arr[i] == "EAST" and arr[i+1] == "WEST":
            arr = arr[:i]+arr[i+2:]
            i-=1
            l-=2
        elif arr[i] == "WEST" and arr[i+1] == "EAST":
            arr = arr[:i]+arr[i+2:]
            i-=1
            l-=2
        else:
            i+=1
        if i==-1:
            i+=1
        print(arr)
    return arr