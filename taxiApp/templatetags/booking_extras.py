from django import template

register = template.Library()

@register.filter(name='booking_badge')
def get_booking_status_badge_class(booking_status) -> str:
    if booking_status == 1:
        return "bg-primary"
    elif booking_status == 2:
        return "bg-success"
    elif booking_status == 3:
        return "bg-danger"