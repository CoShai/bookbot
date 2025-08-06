def get_word_count(text):
    words=text.split()
    return len(words)

def get_char_count(text):
    d={}
    for c in text:
        cl= c.lower()
        if cl in d:
            d[cl]+=1
        else:
            d[cl]=1
    return d

def sort_on(items):
    return items["num"]

def get_sorted_list(dictionary):
    my_list=[]
    for key in dictionary:
        my_list.append({'char': key,"num":dictionary[key]})
    
    my_list.sort(reverse=True,key=sort_on)
    return my_list