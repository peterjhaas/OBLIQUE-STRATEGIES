
					###### Stuff we'll need to use this application
import random		# We'll need to make random numbers
import datetime		# We'll need to access the computer's clock and calendar
import os			# need to do some file handling stuffs
import shutil		# more o/s stuff I don't understand, I'm an artist, five days a week...



def display_text(filename):			
	"""
	Args:
        filename (string): name of file to be opened and read
	"""
										# Most of the display in this application is from text files, so this function reads those files and opens them on the screen
	f = open(filename + '.txt', 'r')	# Take the name of 'thisfile' and add '.txt' to the end so it accesses the text file, for read purposes only
	print f.read()						# Print the contents of the file to screen.
	f.close()							# Close the file that was opened.

########


def name_change(reader):						#####
													#
	named = reader + '.txt'							# gather the text sent to the function and make it a text file name to reference to lists to pull from.
	occupations = open(named, 'r').readlines()		# open the file with the cards list
	occuno = random.randint(1, len(occupations)-1)	# gather a random item from the first item in the list until the length of the file minus one line
	OccupationForDisplay = occupations[occuno][:-1]	# set the value of the item and remove the end of line data for the value


	print ""
	print ""
	print "  " + OccupationForDisplay
	print ""
	print ""
	print "###########################################################################"
	print ""
	return OccupationForDisplay						#### return the value of the randomly selected item



###########################

def main():

	os.system('clear') 
	display_text('OblqStrat_opening')	
	name_change('OblqStrat_cards')



if __name__ == '__main__':
	main()
	
	