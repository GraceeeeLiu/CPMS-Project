from django import template
register = template.Library()

@register.filter
def div( value, arg ):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        nvalue = int( value )
        narg = int( arg )
        if nvalue > 0:
            nvalue -= 1

        if nvalue > narg:
            nvalue = narg-1

        if narg: return round((nvalue / narg) * 100, 2)
    except: pass
    return ''