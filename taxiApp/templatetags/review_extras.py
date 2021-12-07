from django import template

register = template.Library()

@register.filter(name='rating_badge')
def get_review_rating_badge_class(review_rating) -> str:
    if review_rating < 3:
        return "bg-danger"
    elif review_rating == 3:
        return "bg-primary"
    else:
        return "bg-success"