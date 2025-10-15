isDirty = True 

while isDirty == True:
     wash_again = input ("continue washing the clothes yes / no --> ").lower()

     if wash_again == "yes":
          print("washing the clothes again...")
          continue
     else:
          print("washing stops now...")
          break
