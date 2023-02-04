def find_and_strip_substrings_1(xstr,ystr,zstr):
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

def find_and_strip_substrings_2(xstr, ystr, zstr):
    result = ""
    i = 0
    while i < len(xstr):
        y_start = xstr.find(ystr, i)
        if y_start == -1:
            break
        z_start = xstr.find(zstr, y_start + len(ystr))
        if z_start == -1:
            break
        fstr = xstr[y_start:z_start + len(zstr)]
        if fstr not in result:
            result += (fstr)
        i = z_start + len(zstr)
    return result.replace(ystr,"").replace(zstr,"")

def find_and_strip_substrings_3(xstr, ystr, zstr):
    result = []
    i = 0
    while i < len(xstr):
        y_start = xstr.find(ystr, i)
        if y_start == -1:
            break
        z_start = xstr.find(zstr, y_start + len(ystr))
        if z_start == -1:
            break
        fstr = xstr[y_start:z_start].replace(ystr, "").replace(zstr, "")
        result.append(fstr)
        i = z_start + len(zstr)
    return "".join(result)
