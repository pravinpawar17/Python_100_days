
#head or Tail
import random
# random_side = random.randint(0,1)
# if random_side == 0:
#     print("head")
# else:
#     print("Tail")

name_string = input("give me everybody's name :")
names = name_string.split(", ")
num_item = len((names))
random_choice = random.randint(0, num_item-1)
pearson_who_pay = names[random_choice]
print(pearson_who_pay + "is going to pay bill")
