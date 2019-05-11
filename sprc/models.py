from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.URLField()
    appstore = models.URLField()
    playstore = models.URLField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Post(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.URLField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Card(models.Model):
    name = models.CharField(max_length=200)
    health = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    superpow = models.TextField()
    starpower = models.TextField()
    
    photo = models.URLField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name
