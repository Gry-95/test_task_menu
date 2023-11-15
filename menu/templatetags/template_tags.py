from django import template
from ..models import Menu

register = template.Library()

@register.simple_tag()
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    print(menu)
    html = '<ul>'
    for item in menu.items.filter(parent__isnull=True):
        html += f'<li><a href="{item.url}">{item.title}</a>{draw_children(item)}</li>'
    html += '</ul>'
    return html

def draw_children(item):
    children = item.children.all()
    if children:
        html = '<ul>'
        for child in children:
            html += f'<li><a href="{child.url}">{child.title}</a>{draw_children(child)}</li>'
        html += '</ul>'
        return html
    else:
        return ''