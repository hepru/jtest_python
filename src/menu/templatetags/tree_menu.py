import re

from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from ..models import TreeMenu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):

    vis_child = set([]);
    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:

        is_url = re.compile(r'^http[s]?://')
        current_path = context['request'].path \
            if 'request' in context and isinstance(context['request'], HttpRequest) \
            else ''

        data = TreeMenu.objects.select_related()\
            .filter(category__name=name)\
            .order_by('pk')

        menu = []

        for item in data:

            link = item.link.strip()

            target = '_self'

            if is_url.match(link):
                url = link
                target = '_blank'
            else:
                try:
                    url = reverse(link)
                except NoReverseMatch:
                    url = link

            url_without_sl = url.removesuffix('/')

            active = True if url == current_path else False
            visible = 1 if url_without_sl in current_path else 0

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': active,
                'visible': visible,
            })
            if active:
                vis_child.add(item.id)
            if visible:
                vis_child.add(item.parent_id or 0)

    for idx in range(len(menu)):
        if menu[idx]['parent'] in vis_child:
            menu[idx]['visible'] = 1

    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
