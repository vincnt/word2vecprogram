import gensim, logging

#convert trainingtext.txt into lists
text = ""
training = open(text, 'r')
listOfText = []
for line in training.readlines():
    words = line.strip().split(' ')
    listOfText.append(words)

#print somelist
training.close()

#train on text
model = gensim.models.Word2Vec(listOfText, min_count = 1)
print '-----------------------------------------------'
print 'trained on ' + text
print
print 'Functions Available:'
print 'PosMinusNeg'
print 'similarity'
print 'oddoneout'
print 'vectors'
print
##############################################################
def posminusneg():
    positivematch = raw_input("positive term = ")
    negativematch = raw_input("negative term = ") 
    mostsimilar = model.most_similar(positive=[positivematch], negative=[negativematch], topn=1)
    print '--------------------------data---------------------'
    print 'MOST SIMILAR' + '  '+  positivematch + '  -minus-  '+ negativematch
    print mostsimilar
    print
def similarity():
    similar1 = raw_input("similar1 = ")
    similar2= raw_input("similar2 = ")
    similarity = model.similarity(similar1, similar2)
    print '--------------------------data---------------------'
    print 'SIMILARITY' +' between ' + similar1 + ' and ' +  similar2
    print similarity
    print
def oddoneout():
    nomatch = raw_input("odd one out: ")
    doesntmatch = model.doesnt_match(nomatch.split())
    print '--------------------------data---------------------'
    print  'doesn\'t match: ' + nomatch 
    print doesntmatch
    print
def vectors():
    word = raw_input('Enter word:')
    print model[word]
###############################################################
while  __name__ == "__main__":
    try:
        functionchosen = raw_input('choose function:')
        print
        if(functionchosen == 'PosMinusNeg'):
            posminusneg()
        if(functionchosen == 'similarity'):
            similarity()
        if(functionchosen == 'oddoneout'):
            oddoneout()
        if(functionchosen == 'vectors'):
            vectors()
    except KeyboardInterrupt:
        print
        break
    except:
        print 'error'
        continue
