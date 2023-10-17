from django.db import models

class Book(models.Model):
    ACTUALITY = (
        ('Актуален', 'Актуален'),
        ('50 на 50', '50 на 50'),
    )
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    video = models.URLField(null=True)
    actuality = models.CharField(max_length=100, choices=ACTUALITY, default=ACTUALITY[0], null=True)

    def __str__(self):
        return self.title

class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )

    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
       return self.text_review
    #return text_review