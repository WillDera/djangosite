from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # this adds media handling feature to display a banner for each
    # article based on database info and 
    # if no image is provided, a default image would be rendered instead
    thumb = models.ImageField(default='default.png', blank=True)

    # TODO: Add author later
    
    def __str__(self):
        # display title of article in the database admin section
        return self.title
    
    def snippet(self):
        # make a 50 characters preview on the articles main page for each article
        return self.body[:50] + '...'
    