from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date_string(value):
    """
    """
    now_aware = timezone.now()
    delta = value - now_aware

    if delta.days == 0:
        return 'Today!'
    elif delta.days < 1:
        return f'{ abs(delta.days) } { "day" if abs(delta.days) == 1 else "days" } ago.'
    elif delta.days == 1:
        return 'Tomorrow'
    elif delta.days > 1:
        return f'In { delta.days } days'
    else:
        return 'You lose!'
