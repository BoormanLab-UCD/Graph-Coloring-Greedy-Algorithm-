import csv, os
import string
string.ascii_lowercase

#point to a relative path
os.chdir(os.path.relpath('Stims', start='.')+'\\')

files=csv.DictReader(open('Stims Similarities.csv','r+'))
files=list(files)

# format dictionary => all stim names in one list called [stims], shuffle
stims = [files['STIMULUS NAME']]
random.shuffle(stims)

# insert first element of [stims] in [finalStims]
finalStims = []
finalStims.append(stims[0])
stims.remove(stims[0])

# remove strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] from [stims]
if ['SIMILAR IN COLOR'] in [stims]: 
    stims.remove(['SIMILAR IN COLOR'])
if ['SIMILAR IN SHAPE'] in [stims]: 
    stims.remove(['SIMILAR IN SHAPE'])
    
# remove those stims' rows from dictionary
for key in (['SIMILAR IN COLOR'] or ['SIMILAR IN SHAPE']):
    del files[key] # will this delete the whole dict? Needs to delete the entire dicts corresponding to those keys.
    
# for number of elements in [finalStims] < 4, do
for i in xrange(1,4):
#    shuffle [stims]
    random.shuffle(stims)
#    place stim name in [finalStims]    
    finalStims.append(stims[0])
    stims.remove(stims[0])
#    compare strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] with [stims]
#       if matches, then
#          remove from [stims]
    if ['SIMILAR IN COLOR'] in [stims]: 
        stims.remove(['SIMILAR IN COLOR'])
    if ['SIMILAR IN SHAPE'] in [stims]:
        stims.remove(['SIMILAR IN SHAPE'])
#          remove those stims' rows from dictionary
    for key in (list('SIMILAR IN COLOR') or list('SIMILAR IN SHAPE')):
        del files[key]
#          shuffle stims
        random.shuffle(stims)

# return [final stims], which should now be a list of 4 dissimilar fractals
print finalStims; 


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
            
            