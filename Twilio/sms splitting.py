
def segments(message):
    max_length = 160
    if len(message) <= max_length:
        return [message]
    res = []
    subarr = []
    # subarr_length need to be 5 cause we need to put (1/5) at the end
    subarr_length = 0
    word = ''
    message += ' '
    for char in message:
        if char != ' ':
            word += char
        else:
            if len(subarr) + subarr_length + len(word) <= max_length - 5:
                subarr.append(word)
                subarr_length += len(word)
            else:
                temp = ' '.join(subarr)
                if len(temp) == max_length - 5:
                    word = ' ' + word
                else:
                    temp += ' '
                res.append(temp)
                subarr = [word]    
                subarr_length = len(word)
            word = ''
    
    # add the last line
    res.append(' '.join(subarr))
    
    # add total page to the result
    l = len(res)
    for i in range(l):
        res[i] += '({}/{})'.format(i+1, l)
    
    return res