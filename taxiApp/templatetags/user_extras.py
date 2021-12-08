from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='is_driver')
def is_user_in_driver_group(user) -> bool:
    return user.groups.filter(name='drivers').exists()