from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    print(value)
    print(arg)
    return value.replace(arg,'v')





# register.filter('cut',cut)



