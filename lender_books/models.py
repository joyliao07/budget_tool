"""To set up models for lender_books app."""
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Book(models.Model):
    """To set up Book class."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    cover_imgage = models.ImageField(max_length=400)
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=50)

    # Do a list comprehension:
    years = []
    for x in range(1200, 2020):
        years.append((x, x))

    year = models.CharField(max_length=4, default='2019', choices=years)

    STATES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-out'),
    ]
    status = models.CharField(max_length=11, default='available', choices=STATES)

    date_added = models.DateTimeField(default=timezone.now)
    last_borrowed = models.DateTimeField(auto_now=True)

    # def __repr__(self):
    #     return ''

    def __str__(self):
        return f'{self.title} ({self.status})'


@receiver(models.signals.post_save, sender=Book)
def set_book_completed_date(sender, instance, **kwargs):
    """Update the date completed if completed."""
    if instance.status == 'Complete' and not instance.date_completed:
        instance.date_completed = timezone.now
        instance.save()
