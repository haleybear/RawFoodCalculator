#Name
dogName = raw_input("What is your pet's name?")
type(dogName)

#Decide which calculation based on age of the pet (whether we should go through adult or puppy calculations)
pupDog = raw_input(Is your pet a dog or is it a puppy?(Puppy is calculated between 2 and 12 months) )
type(pupDog)
if pupDog in ("dog", "Dog"):
    age =;
	dogWeight = raw_input("What is your dog's current weight? In pounds please!")
	idealWeight = raw_input("What is the ideal weight for your dog?")
	if dogWeight > idealWeight
		#This means that the pup need to lose weight
		#Use 2% of idealWeight for over 15lbs
		#Use -1% of whatever weight group the pup falls into for < 15
		#for less than 15lbs:
			#    Up to 5 lbs: 5% of their body weight
			#    From 6-10 lbs: 4% of their body weight
			#    From 11-15 lbs: 3% of their body weight
			#    To gain or lose weight: +1% or -1% accordingly
		
	else dogweight < idealWeight
	    #+2% of idealWeight for dogs over 15lbs
		#Use +1% of whatever weight group the pup falls into for <15
		#for less than 15lbs:
			#    Up to 5 lbs: 5% of their body weight
			#    From 6-10 lbs: 4% of their body weight
			#    From 11-15 lbs: 3% of their body weight
			#    To gain or lose weight: +1% or -1% accordingly
		
	elif dogweight == idealWeight
		#for over 15lb 2% to maintain
		#for less than 15lbs:
			#    Up to 5 lbs: 5% of their body weight
			#    From 6-10 lbs: 4% of their body weight
			#    From 11-15 lbs: 3% of their body weight
			#    To gain or lose weight: +1% or -1% accordingly
			
elif pupDog in ("puppy", "Puppy"):
    age =;
	pupAge = raw_input("What is your pup's current age in the closest full month?")
	#For Puppies
    #From 2-4 months: 6-10% of their body weight
    #From 4-7 months: 4-5% of their body weight
    #From 7-12 months: 3-4% of their body weight
    #From 12+ months: 2% of their body weight
