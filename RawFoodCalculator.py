#Some rules for this Calculator! 
#For adult dogs under 15lbs with a moderate activity level: 
#    Up to 5 lbs: 5% of their body weight
#    From 6-10 lbs: 4% of their body weight
#    From 11-15 lbs: 3% of their body weight
#    To gain or lose weight: +1% or -1% accordingly
#For adult dogs over 15lbs with moderate activity
#    2% of their body weight to maintain
#    To gain or lose weight: 2% of target weight
#For Puppies
#From 2-4 months: 6-10% of their body weight
#From 4-7 months: 4-5% of their body weight
#From 7-12 months: 3-4% of their body weight
#From 12+ months: 2% of their body weight

#Name
dogName = raw_input("What is your pet's name?")
type(dogName)

#Decide which calculation based on age of the pet (whether we should go through adult or puppy calculations)
pupDog = raw_input(Is your pet a dog or puppy. (Puppy is calculated between 2 and 12 months) )
type(pupDog)

#If dog is an adult - break down into above or below 15lbs based on input weight.
dogWeight = raw_input("What is your dog's current weight? In pounds please!")
if dogWeight > 15
    idealWeight = raw_input("What is the ideal weight for your dog?")
    while True:
	
        qweight = input("")

#If its a pup, the dog food is going to be calculated based on months && current weight