from django import template

register = template.Library()

 
@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username

@register.simple_tag(takes_context=True)
def get_blog_display(context, users):
    contributors = []
    for contrib in users:
        if contrib == context['user']:
            contributors.append('vous')
        else:
            contributors.append(contrib.username)
    return ', '.join(contributors)


from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

@register.filter
def get_posted_at_display(time):
    seconds_ago = (timezone.now() - time).total_seconds()
    if seconds_ago <= HOUR:
        return f'Publié il y a {int(seconds_ago // MINUTE)} minutes.'
    elif seconds_ago <= DAY:
        return f'Publié il y a {int(seconds_ago // HOUR)} heures.'
    return f'Publié le {time.strftime("%d %b %y à %Hh%M")}'
