import csv, os
import string
string.ascii_lowercase

#point to a relative path
os.chdir(os.path.relpath('Stims', start='.')+'\\')


files=csv.DictReader(open('Stims Similarities.csv','r+'))
files=list(files)

'''overall i think this looks good. But it looks like the way you wrote this is to be a function, that's called everytime we start up an experiment. This is a 
great idea, I think. But you should put everything below inside a function then. 

I wonder if it might be even better to write this as a class we can just draw from. Idk. mmmmmm, probably not. we can talk about 
later maybe.'''


# format dictionary => all stim names in one list called [stims]

# create empty list called [finalStims] 

''' you dont need to choose a random row. If you're going to interate through 
       all the elements anyway, just shuffle them and start from the beginning'''
# choose random row in dictionary

'''im not sure i understand the reason you have final stims; if its just to hold 
the final 4 stimuli, you'll get that for free as you widdle down your stim list.
then just index the first 4 in that list.'''
# place stim name in [finalStims]
# remove strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] from [stims]
# remove those stims' rows from dictionary
'''should this be a while loop? like 'while theres more than 4 things in the list'?'''
# for number of elements in [finalStims] < 4, do
#    choose random row in dictionary 
#    place stim name in [finalStims]
#    compare strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] with [stims]
#       if matches, then
#          remove from [stims]
#          remove those stims' rows from dictionary
''' handy tip: python doesn't requie that tell it to end a loop of if-statement. It just knows by the way you're indenting'''
#       end if
# end for
'''return statement'''
# [final stims] should now be a list of 4 dissimilar fractals



#--------------------------------------------------------------------------------


#letters
#letters=list(string.ascii_lowercase)


#for i in files[0:5]:
#    #update our dicts to have neighbor entry
#    i.update({'MatchingLetter':[]})
    
#    if files.index(i)==0:
#        i['MatchingLetter']=letters[0]
#    else:
        #look through all the files
#        for l in files:
#            if l['STIMULUS NAME'] in i['SIMILAR IN COLOR'] or l['STIMULUS NAME'] in i['SIMILAR IN SHAPE']:
#                i['MatchingLetter'].append(l['STIMULUS NAME'])
            
            