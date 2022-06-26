def stritm(xstr,ystr,zstr):
    results = []
    for i in range(len(xstr)):
        if(ystr in xstr[i:i+len(ystr)]):
            intc = 0
            fstr = []
            for a in range(len(xstr)):
                intc += 1
                fstr = xstr[i:i+len(ystr) + intc]
                if(fstr.__contains__(zstr)):
                    xstr.replace(fstr, "")
                    fstr = fstr.replace(ystr, "").replace(zstr, "")
                    if(results.__contains__(fstr) == 0):
                        results.append(fstr)
                        break
    return results
