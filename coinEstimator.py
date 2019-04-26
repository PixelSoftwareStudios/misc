import math
weights = {"penny": 2.5, "nickel": 5.0, "dime": 2.268, "quarter": 5.670}
countperwrapper = {"pennies": 50, "nickels": 40, "dimes": 50, "quarters": 40}

total = {"pennies": 0, "nickels": 0, "dimes": 0, "quarters": 0}
wrappersNeeded = {"pennies": 0, "nickels": 0, "dimes": 0, "quarters": 0}

penniesWeight = float(input("What is the weight of your pennies: "))
if penniesWeight:
	total["pennies"] = math.floor(penniesWeight / weights["penny"])
	wrappersNeeded["pennies"] = math.ceil(total["pennies"] / countperwrapper["pennies"])

nickelsWeight = float(input("What is the weight of your nickels: "))
if nickelsWeight:
	total["nickels"] = math.floor(nickelsWeight / weights["nickel"])
	wrappersNeeded["nickels"] = math.ceil(total["nickels"] / countperwrapper["nickels"])

dimesWeight = float(input("What is the weight of your dimes: "))
if dimesWeight:
	total["dimes"] = math.floor(dimesWeight / weights["dime"])
	wrappersNeeded["dimes"] = math.ceil(total["dimes"] / countperwrapper["dimes"])

quartersWeight = float(input("What is the weight of your quarters: "))
if quartersWeight:
	total["quarters"] = math.floor(quartersWeight / weights["quarter"])
	wrappersNeeded["quarters"] = math.ceil(total["quarters"] / countperwrapper["quarters"])

if total["pennies"]:
	print("You need " + str(wrappersNeeded["pennies"]) + " coin wrappers for your pennies")
if total["nickels"]:
	print("You need " + str(wrappersNeeded["nickels"]) + " coin wrappers for your nickels")
if total["dimes"]:
	print("You need " + str(wrappersNeeded["dimes"]) + " coin wrappers for your dimes")
if total["quarters"]:
	print("You need " + str(wrappersNeeded["quarters"]) + " coin wrappers for your quarters")
print("You have " + str(total["pennies"] + total["nickels"] + total["dimes"] + total["quarters"]) + " total coins")
print("The total money you have is: $" + str(round((total["pennies"] * 0.01) + (total["nickels"] * 0.05) + (total["dimes"] * 0.10) + (total["quarters"] * 0.25), 2)))
