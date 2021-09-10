matrix= [
[1 , 2 , 3 ,4],
[5 , 6 , 7 ,8],
[9 , 10 , 11 ,12],
[13 , 14 , 15 ,16]
]




def rotateImage270(matrix):
    l , r= 0, len(matrix)-1 
    while l < r: 
        t, b = l, r
        for i in range(r-l):
            # once you have saved the value try and see where to start 
            # and this is the core algorithms of it 
            saveTopLeftValue=matrix[t][l+i]
            matrix[t][l+i]=matrix[t+i][r]
            matrix[t+i][r]=matrix[b][r-i]
            matrix[b][r-i]=matrix[b-i][l]
            matrix[b-i][l]=saveTopLeftValue
        l+=1
        r-=1

    print(matrix)
    


#-90 is actually the same as the 270
def rotateImagen90(matrix):
    l , r= 0, len(matrix)-1 
    while l < r: 
        t, b = l, r
        for i in range(r-l):
            # once you have saved the value try and see where to start 
            # and this is the core algorithms of it 
            saveTopLeftValue=matrix[t][l+i]
            matrix[t][l+i]=matrix[t+i][r]
            matrix[t+i][r]=matrix[b][r-i]
            matrix[b][r-i]=matrix[b-i][l]
            matrix[b-i][l]=saveTopLeftValue
        l+=1
        r-=1

    print(matrix)


def rotateImage180(matrix):
    l , r= 0, len(matrix)-1 
    
    while l < r: 
        t, b = l, r
        for i in range(r-l):
            matrix[t][l+i], matrix[b][r-i]=matrix[b][r-i], matrix[t][l+i]
            matrix[b-i][l], matrix[t+i][r]=matrix[t+i][r], matrix[b-i][l]
        l+=1
        r-=1


    print(matrix)






# swap with top left with bot right 
# swap bot bot left top right 

