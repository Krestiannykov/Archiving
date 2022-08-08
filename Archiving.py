def archiving(a):
    ## Python 3.9.13
    ## Simple string archiving script
    ## Check alphabetical only symbols
    if not a.isalpha():
        return 'String may be alphabetical only'
    ## Convert to list
    a1=list(a)
    b1=list(a[0])
    count=1
    for i in range(1,len(a1)):
        ## Calculating symbols
        if a[i]==a[i-1]:
            count+=1
        ## Writing count of first symbols    
        elif a[i-1]==b1[-1]:
            b1.append(str(count))
            count=1
        ## Writing count of middle symbols     
        else:
            b1.append(a[i-1])
            b1.append(str(count))            
            count=1
    ## Writing last symbols and count of last symbols
    if b1[-1]!=a[-1]:
        b1.append(a[-1])
    b1.append(str(count))
    ## Check length
    if len(b1)>len(a):
        return a
    else:
        return ''.join(b1)
