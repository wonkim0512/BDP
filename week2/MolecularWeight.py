# compute molecular weight
# hwere are basic weights
# C: carbon 12.011, H: hydrogen 1.0079, O: oxygen 15.994

def molecular_weight():
    print("Please enter the number of each atom")
    C = eval(raw_input("carbon:"))
    H = eval(raw_input("hydrogen:"))
    O = eval(raw_input("oxygen:"))
    W = C*12.011 + H*1.0079 + O*15.994
    print "The weight is", W

molecular_weight()
