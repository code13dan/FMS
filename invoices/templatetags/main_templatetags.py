"""Invoices template tags"""

from django import template

register = template.Library()


@register.simple_tag
def active_nav(request, item_target):
    """Returns 'active' if request namespace is equal nav item_target"""
    if request.resolver_match.namespace == item_target:
        return 'active'
    return ''
