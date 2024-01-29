# Python function that accept a string and calculate the no.of upper case and lower case letters
def string_test(s):
    d={"upper_case":0,"lower_case":0}
    for i in s:
        if i.isupper():
            d["upper_case"]+=1
        elif i.islower():
            d["lower_case"]+=1
        else:
            pass
    print("upper case letters:",d["upper_case"])
    print("lower case letters:", d["lower_case"])
string_test("I am the Mechanical Engineer Working in the OIL AND GAS Industry for Static and Rotary Equipment")











