from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField('Nom',max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "artiste"

class Contact(models.Model):
    email = models.EmailField('Email',max_length=100)
    name = models.CharField('Nom',max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "prospect"

class Album(models.Model):
    reference = models.IntegerField('Réference',null=True)
    created_at = models.DateTimeField('Date de création', auto_now_add=True)
    available = models.BooleanField('disponible',default=True)
    title = models.CharField('titre',max_length=200)
    picture = models.ImageField('Image',upload_to='cover/', null=True)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "disque"

class Booking(models.Model):
    created_at = models.DateTimeField('Date d\'envoi',auto_now_add=True)
    contacted = models.BooleanField('demande traitée ?', default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = 'reservation'