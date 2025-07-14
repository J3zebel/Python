customers=[]
while True:
    n = int(input("Is there any customer available:(Y/N)"))
    if n == 'n':
        break

    name = input("Enter customer name: ")
    items = []

    print("Enter items one by one(type 'stop' to finish):")
    while True:
        item = input("Items:")
        if item == "stop":
            break
        if item:
            items.append(item)

        customers.append({"name" : name,"items": items})
n = input("Is there any customer available:(Y/N)")




