from ..yalgaar import app
import re

def hyperlinkize(l):
    '''Wraps a link inside an html tag'''
    l = l.group(0).strip()
    return "<a href='%s' target='_blank'>%s</a> " % (l,l)

@app.template_filter()
def make_internal_link(text):
    '''makes an html link for any text that looks like a link inside text that contains the link and non-link text
    
        eg. "Hey this is a good website! http://fortyplustwo.github.io|make_internal_link
             will return
            "Hey this is a good websiet! <a href='http://fortyplustwo.github.io'>http://fortyplustwo.github.io</a>"
    '''
    print "Working on ", text.encode('utf8')
    #A link is anything that starts with 'http://' and ends with ' '
    #Or it may begin with www and end with space
    http_link_inside_text = r'(((http|https)://)((\w+)|(\.)|/|\?|=|\&|\%|[0-9]){0,})(\s)*'

    r = re.compile(http_link_inside_text)

    result = r.subn(hyperlinkize, text,)
    print "replacement successfull!", result
    
    return result[0]
