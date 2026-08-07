def find_max(a:list) -> int:
    
    maks = a[0]
    for  x in range(len(a)):
        for k in a:
           if k > a[x]:
               if k > maks:
                   maks = k
    print(maks)


# def find_max(a: list) -> int:
#       maks = a[0]
#       for x in a:
#           if x > maks:
#               maks = x
#       return maks




find_max([-3, -5, -7])