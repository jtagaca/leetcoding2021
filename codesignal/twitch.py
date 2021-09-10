
import collections

#could have just made the list as part of the objects instead of passing it 
class Streamer:
    def __init__(self, streamerName, views, category ):
        self.streamerName = streamerName
        self.views = views
        self.category = category
        

#Adding Streamer to the listofStreamers
def StreamerOnline(listStreamers, currentStreamer):
    listStreamers[currentStreamer.streamerName] = currentStreamer
    
#updating the view count depending on the user and the currentCategory
def UpdateViews(listStreamers, key, newViews, currentCategory):
    if listStreamers[key].category == currentCategory:
        listStreamers[key].views = newViews
    
#updating the view category as long as the arguement is the same as the category of the streamer
def UpdateCategory(listStreamers, key, currentcategory, newcategory):
    if listStreamers[key].category == currentcategory:
        listStreamers[key].category = newcategory

#removing the streamer given the name and the category
def StreamerOffline(listStreamers, streamerName, category):
    if listStreamers[streamerName].category!=category:
        return
    del listStreamers[streamerName]
    
#getting the max num of views in a category given as an arguement
def ViewsInCategory(listStreamers, currentCategory):
    hashm=collections.defaultdict(int)
    for key, value in listStreamers.items():
        hashm[value.category]+=int(value.views)
    return hashm[currentCategory] if currentCategory in hashm else 0

#getting the topStreamer who has the max views in a category given as an arguement
# could have possibly merged with the ↑ other function
def TopStreamerInCategory(listStreamers, currentCategory):
    maxTotal=0
    topPerson=None
    for key, value in listStreamers.items():
        if value.category==currentCategory and int(value.views)> maxTotal:
            topPerson=value.streamerName
            maxTotal=int(value.views)
    return topPerson

#getting topStreamer based on how many views 
def TopStreamer(listStreamers):
    maxViews=0
    output=None
    for key, value in listStreamers.items():
        currentVal=int(value.views)
        if currentVal > maxViews:
            output=value.streamerName
            maxViews=currentVal
        
    return output
    


def solution(streamerInformation, commands):
    listStreamers={}
    #build a map of objects 
    for i in range(0,len(streamerInformation),3):
        listStreamers[streamerInformation[i]] =(Streamer(streamerInformation[i], streamerInformation[i+1], streamerInformation[i+2]))
    step=0

    result=[]
    # checking what command are we using 
    # step is a way to check how many arguements are getting passed
    # for each pass we are only able to have one command and we go to the next IDX
    while step< len(commands):
        currentCommand=commands[step]
        
        if currentCommand=="StreamerOnline":
            currentStreamer=Streamer(commands[step+1], commands[step+2], commands[step+3])
            StreamerOnline(listStreamers, currentStreamer)
            step+=4
        elif currentCommand=="UpdateViews":
            UpdateViews(listStreamers, commands[step+1], commands[step+2], commands[step+3])
            step+=4
        elif currentCommand=="StreamerOffline":
            StreamerOffline(listStreamers,commands[step+1],commands[step+2] )
            step+=3
        elif currentCommand=="UpdateCategory":
            UpdateCategory(listStreamers ,commands[step+1],commands[step+2],commands[step+3])
            step+=4
        elif currentCommand=="ViewsInCategory":
            result.append(str(ViewsInCategory(listStreamers ,commands[step+1])))
            step+=2
        elif currentCommand=="TopStreamerInCategory":
            result.append(TopStreamerInCategory(listStreamers, commands[step+1]))
            step+=2
        elif currentCommand=="TopStreamer":
            result.append(TopStreamer(listStreamers))
            step+=1
            
    return result
    
