# Learn python the Hardway ex4

# set cars equal to 100 type int
cars = 100
# set space in a equal to 4.0 type float
space_in_a_car = 4
drivers = 30
passengers = 90
# calcualted mesaure for cars not drive number of cars
# minus drivers
cars_not_driven = cars - drivers
cars_driven = drivers
#calculating carpacity
carpool_capacity = cars_driven * space_in_a_car
# calculating average passengers in a car
average_passengers_per_car = passengers / cars_driven

# print statment showing cars available
print "There are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."