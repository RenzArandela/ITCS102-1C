amount = eval(input("\nEnter the amount that you want to deposit-->"))
print("Here's the breakdown of your deposit-->")

oneK = amount // 1000
amount = amount % 1000
print(onethou,"\t- 1000")

fiveH = amount // 500 
amount = amount % 500
print(fivehund,"\t- 500")

twoH = amount // 200
amount = amount % 200
print(twohund,"\t- 200")

oneH = amount // 100
amount = amount % 100
print(onehund,"\t- 100")

fifty = amount // 50
amount = amount % 50
print(fifty,"\t- 50")

twenty = amount // 20
amount = amount % 20
print(twenty,"\t- 20")

ten = amount // 10
amount = amount % 10
print(ten,"\t- 10")

five = amount // 5
amount = amount % 5
print(five,"\t- 5")

one = amount // 1
amount = amount % 1
print(one,"\t- 1")
