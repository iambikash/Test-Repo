Bikash Adhikari
Prabin
Prince

"""Markdown python"""
def get_heading(message,level=1):
    """Return a markdown heading"""
    if level in range(1,6):
        return "{0}{1}".format("#"*level,message)
        
    return None

def get_list(list_items, type='unordered'):
    result =''
    if isinstance(list_items,(list,tuple,set)):
        if type=='unordered':
            for item in list_items:
                result +="*{}\n".format(item)

        elif type=='ordered':
            for item in range(0,len(list_items)):
                result +="{}.{}\n".format(item+1,list_items[item])
        else:
            print('Unexpected list type')
        return result
    else:
        print('Unexpected list type')
        return None
                
if __name__=='__main__':
    print(get_heading("Resume",0))
    print(get_heading("Resume",1))
    print(get_heading("Resume",10))
    print(get_heading("Resume",5))

    print(get_list(['hello','world']))
    print(get_list(['hello','world'],'ordered'))
    print(get_list(0,'ordered'))

