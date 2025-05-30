# Practical 01
“”“
Logic Exercise:
Answer: 
Jones is programmer, Brown is consultant, Smith is project manager.

Reason: 
Because programmer is the only child, so programmer is not Brown (Brown has sister). Due to Smith earns more money than consultant, and programmer earns the least money, there are only three people, so programmer is not Smith.
As a result, Programmer is Jones.
Smith is not consultant, so Smith is project manager.
So Brown is consultant.

Algorithms with I, P, O
1.Write an algorithm to calculate the brew ratio of coffee, given the dose (quantity of coffee beans in grams) and the yield (brewed coffee in grams).
Example: A dose 剂量of 18g and yield of 45g is a 1 to 2.5 brew ratio.

the algorithm:
get the dose (quantity of coffee beans in grams), get the yield (brewed coffee in gram)
the brew ratio of coffee= the yied/ the dose
display ratio

2.Write an algorithm to determine if you can afford to buy an item based on its price and the money you have in your pocket.

the algorithm:
get the money you have
get price of item 
if the price of item > the money you have
    cannot afford 
else
can afford



3.Write an algorithm to instruct a teenager how to clean their room. They have lots of things on the floor, and need to pick them up until there are no more things on the floor.

the algorithm:
pick the things on the floor
while the floor still have things
     pick the things
rest now

2:
repeat until flooe clean
   pick thing from floor
rest now




problem Decomposition:
1.Happy Photos needs a way to calculate the total charge for a customer's booking. The system will use the customer's name and the date of the booking to make a unique booking id. The hourly charge, and number of hours will be entered, and the total charge and id code will be displayed.

(1)the nouns: 
the total charge, customer’s name, the date of booking, booking ID, the hourly charge, the number of hours
(2)the verbs:
calculate( total charge) , display( total chatge, id code)
(3)the algorithm:
get the hourly charge, the number of hours, the customer’s name, the date of booking
the total charge= the hourly charge * the number of hours
the ID code= the cusyomer’s name+ the date of booking
diaplay total charge
display the ID code

2.A road trip planning system will ask the user for the distance travelled (in km) and the travel time in minutes. The user will then be shown the average speed (in km/hour) over the trip.

(1)the nouns: 
the distance traveled (in km), the travel time (in minutes), the average speed (in km/hour) 
(2)the verbs
shown( average speed)
(3)the algorithm:
get the distance travelled (in km), get the travel time (in minuties)
the travel time (in hour)= the travel time (in minuties) /60
the average speed ( in km/ hour) = the distance (in km) / the travel time (in hour)
print the average speed ( in km/ hour)



 

”“”