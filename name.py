"""Markdown python"""
database = {
    'personal_info': {
        'name': 'Your Name',
        'location': 'Your Location',
        'phone': 'Your phone number',
        'email': 'email address'
    },
    'objective': "Your objective",
    "education": [
        {
            "institution": "University Name",
            "location": "Location",
            "year": 1990,
            "degree": "degree name",
            "description": "your grade description"
        },
        {
            "institution": "University Name",
            "location": "Location",
            "year": 1990,
            "degree": "degree name",
            "description": "your grade description"
        }
    ],
    "employment": [
        {
            "role": "role name",
            "year": 1990,
            "company": "company name",
            "location": "location",
            "description": [
                "description 1",
                "description 2",
            ]
        },
        {
            "role": "role name",
            "year": 1990,
            "company": "company name",
            "location": "location",
            "description": [
                "description 1",
                "description 2",
            ]
        }
    ],
    "skills": [
        "Sample skills and abilities 1",
        "Sample skills and abilities 2"
    ],
    "activities": [
        "Sample activity 1",
        "Sample activity 2"
    ],
    "hobbies": [
        "Sample hobby 1",
        "Sample hobby 2"
    ]
}

def get_heading(message,level=1):
    """Return a markdown heading"""
    if level in range(1,6):
        return "{0}{1}".format("#"*level,message)
        
    return None

def get_list(list_items, ordered=False):
    result =''
    if isinstance(list_items,(list,tuple,set)):
        if not ordered:
            return "\t".join([f"*{item}" for item in list_items])
            
        else:
            return "\t".join([f"{item[0]+1} {item[1]}" 
            for item in enumerate(list_items)])
            #for item in range(0,len(list_items)):
            #    result +="{}.{}\n".format(item+1,list_items[item])
        return result
    else:
        print('Unexpected list type')
        return None

def get_paragraphs(message):
    """A method to get a markdown paragraph"""
    if isinstance(message,(list,tuple,set)):
        return "\n".join([f"{item}\n" for item in message])
    
    else:
        return f"{message}\n\n"
    


def generate_resume():
    """generates a resume in markdown"""
    resume =[]
    # Generates Heading
    resume.append(get_heading("Resume"))
    return resume

                
if __name__=='__main__':
    """print(get_heading("Resume",0))
    print(get_heading("Resume",1))
    print(get_heading("Resume",10))
    print(get_heading("Resume",5))

    print(get_list(['hello','world']))
    print(get_list(['hello','world'],True))
    print(get_list(['hello','test'],'abc'))
    print(get_list(0,'ordered'))
    #print(get_list(0,'unordered'))
    # test get_paragraph
    """
    print(get_paragraphs(['This is a test paragraph','abc']))
    print(get_paragraphs('This is a paragraph'))
    #print(get_paragraphs())
    # Test generates_resume
    #print(generate_resume('Testing Resume generator'))
    #print(generate_resume())
    #get heading
    #print(generate_resume())
    # generates 



