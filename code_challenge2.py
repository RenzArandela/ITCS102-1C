amount = eval(input("Enter any amount to deposit --> "))

print("Here is a breakdown of your deposited amount using the PH denominations")

# 1000
isanglibo = amount // 1000
amount = amount % 1000
print(isanglibo, "- 1000")

# 500
limangdaan = amount // 500
amount = amount % 500
print(limangdaan, "- 500")

# 200
dalawangdaan = amount // 200
amount = amount % 200
print(dalawangdaan, "- 200")

# 100
isangdaan = amount // 100
amount = amount % 100
print(isangdaan, "- 100")

# 50
limampu = amount // 50
amount = amount % 50
print(limampu, "- 50")

# 20
dalawampu = amount // 20
amount = amount % 20
print(dalawampu, "- 20")

# 10
sampu = amount // 10
amount = amount % 10
print(sampu, "- 10")

# 5
lima = amount // 5
amount = amount % 5
print(lima, "- 5")

# 1
isa = amount // 1
amount = amount % 1
print(isa, "- 1")
