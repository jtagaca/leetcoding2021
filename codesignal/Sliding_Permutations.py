input="1000"

output=""


def printCombintations(number):
    result = []
    for i in range(len(number)):
        #0
        j=0
        # while we our currentLength is in bounds 
        while j+i< len(number):
            #if j+i <len(number):
            result.append(number[j:j+i+1])
            j+=1;
        
    print(result)
    
printCombintations(input)
# 