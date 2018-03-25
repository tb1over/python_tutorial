import html

def make_element(name, value, **attrs):
    #keyvals = [' %s="%s"' % item for item in attrs.items()]
    keyvals = [' %s="%s"' % (key,value) for key, value in attrs.items()]
    attr_str = ''.join(keyvals)

    elment = '<{name}{attrs}>{value}</{name}>'.format(
                name= name,
                attrs=attr_str,
                value=html.escape(value))
    return elment

# Example
# <div id="div1" clas="class1">test</div>
s = make_element('div', 'test', id='div1', clas='class1')
print(s)