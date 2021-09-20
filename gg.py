def playlist(time):
    # Write your code here
    # number os song pairs 
    # must be pair so that count can be incremented 
    # mod by 60? 
    # 
    # we can reuse the same number again 
    # brute force double for loop time and space contrainst might matter 
    # 20 30 40 100 150
    # if we have  
    remainders = collections.defaultdict(int)
    ret = 0
    for t in time:
        if t % 60 == 0: # check if a%60==0 && b%60==0
            ret += remainders[0]
        else: # check if a%60+b%60==60
            ret += remainders[60-t%60]
        remainders[t % 60] += 1 # remember to update the remainders
    return ret