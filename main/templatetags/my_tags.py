from django import template

register = template.Library()


@register.simple_tag
def active_menu(request, pattern):
    path = request.path
    if path == pattern:
        return 'sub-group-active'
    return ''


@register.simple_tag
def active(request, pattern):
    path = request.path
    if path == pattern:
        return 'menu-active'
    return ''
