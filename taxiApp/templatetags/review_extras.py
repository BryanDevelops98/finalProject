from django import template

register = template.Library()

@register.filter(name='rating_badge')
def get_review_rating_badge_class(review_rating) -> str:
    if review_rating == 1:
        return "terrible"
    elif review_rating == 2:
        return "bad"
    elif review_rating == 3:
        return "bg-primary"
    elif review_rating == 4:
        return "good"
    else:
        return "outstanding boxShadowStyle"