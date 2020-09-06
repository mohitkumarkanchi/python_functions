def unformat_n(x):
    ''' this function takes a string like value 10,000 and converts it into
    normal int value with out comma'''
    
    values=[]
    values=x.split(',')
    #print(values)
    values = ''.join(map(str, values))
    #print(values)
    
    #print(type(values))
    n=len(values)
    
    sum=0
    for i in range(0,n):
        sum=sum+(int(values[i])*pow(10,n-i-1))
    return sum
    
    
    #call the function
    '''
    
    n=unformat_n(1,50,000)
    print(n)
    
    output:
    150000 in int format
    
 
    
    
    
    '''
