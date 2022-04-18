user1=int(input("enter your amount: "))
def indian():
    rupee=user1*75
    print(rupee)
def us():
    dollar=user1/75
    print("$",dollar)
def choice():
    user=input("enter your choice: ")
    if user=="$":
        us()
    else:
        indian()
choice()