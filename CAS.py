def writeAsYouSpeak(n):
    term = "1"

    for _ in range(n-1):
        next_term=""
        i=0

        while i< len(term):
            count=1
            while i+1 < len(term) and term[i]==term[i+1]:
                i+=1
                count+=1

            next_term+=str(count)+ term[i]
            i+=1
        term =next_term

    return term

