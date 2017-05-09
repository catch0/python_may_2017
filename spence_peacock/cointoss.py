import random
flips=0
heads=0
tails=0
coin=""
while flips < 5001:
    headortail=random.randint(0,1)
    if headortail==0:
        heads=heads+1
        coin="heads"
    else:
        tails=tails+1
        coin="tails"
    flips=flips+1
    print "Attempt #{}: Throwing a coin... It's a {}! So far we have {} heads and {} tails".format(flips,coin,heads,tails)

    
