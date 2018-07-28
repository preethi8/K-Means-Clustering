import csv
import json
import math
import random
import sys

clusters=sys.argv[1]
seedfile=sys.argv[2]
tweet_data=sys.argv[3]
outputFile=sys.argv[4]

cluster_ct = int(clusters)
fileout = open(outputFile,'w')
stOut = sys.stdout
sys.stdout = fileout

filein = open(tweet_data)
inp = {}

x = filein.readline()
i = 0
while (x != ''):
    data = json.loads(x)
    data['text'] = set((data['text']).split(' '))
    inp.update({data['id']: [data['text'], -1]})
    x = filein.readline()

fileseed = open(seedfile, 'rt')
header = csv.Sniffer().has_header(fileseed.read(1024))
fileseed.seek(0)
csvin= csv.reader(fileseed)
if header:
    attr_name = next(csvin)
k= [int(i[0]) for i in csvin ]

# getting centroids  randomly for k
tmp = random.sample(k, cluster_ct)
pts = {}
len_pt = len(tmp)
for i in tmp:
    pts.update({i: inp[i]})

Xlength = len(inp)
filein.close()
fileseed.close()

#finding the jaccard distance
	
def sse(Y, pt):
    length = 0
    asd = 0
    for j in pt:
        for i in Y:
            if (Y[j][1] != j): continue
            asd = 1 - float(len((Y[i][0]).intersection(Y[j][0]))) / len((Y[i][0]).union(Y[j][0]))
            length += math.pow(asd, 2)
    print 'sse:', (length/100), ' k = ', len(pt)
	
def cluster(p):
    s = 0
    for i in p:
        s += math.pow(i, 2)
    return s
	
distMeasure = {}
sub = []
previous = []
count = 0

for i in xrange(cluster_ct):
    sub.append([-1])
print 'Iterations : ',
while (count < 25 and any(t!= 0 for t in sub)):
    print count,
    previous = []
    tmp = inp.iterkeys()
	
    for j in xrange(Xlength):
        previous.append(tmp.next())

    for i in inp:
        # place each element into nearest centroid cluster.
        distMeasure = 1
        mini = 2
        idAllocate = 0
        for k_i in pts:
            distMeasure = 1 - float(len((inp[i][0]).intersection(pts[k_i][0]))) / len((inp[i][0]).union(pts[k_i][0]))
            if (distMeasure < mini):
                mini = distMeasure
                idAllocate = k_i
        inp[i][1] = idAllocate
 
	
    pts_tmp = {}
    for each in pts:
        distMeasure = 1
        sse_min = 999999999
        idAllot = 0

        for i in inp:
            if (inp[i][1] != each): continue
            tmp_set = []
            for j in inp:
                if (inp[j][1] != each): continue
                if (i == j): continue
                tmp_set.append(1 - float(len((inp[i][0]).intersection(inp[j][0]))) / len((inp[i][0]).union(inp[j][0])))
            distMeasure = cluster(tmp_set)
            if (distMeasure < sse_min):
                sse_min = distMeasure
                idAllot = i
    
        pts_tmp.update({idAllot: inp[idAllot]})

    ptsLength= len(pts)
    pts_tmp_ptr = pts_tmp.__iter__()
    sub= []
    for j in pts:
        sub.append(j - next(pts_tmp_ptr))
    pts = pts_tmp
    count += 1

print "\n"
for p in pts:
    print p,
    print '\t',
    for j in inp:
        if (p == inp[j][1]):
            print j, ',',
    print '\n\n'
sse(inp, pts)
sys.stdout = stOut
fileseed.close()
print 'Outputting to file:', outputFile

	

	
	



