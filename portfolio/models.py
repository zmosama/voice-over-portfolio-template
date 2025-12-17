from django.db import models
from ckeditor.fields import RichTextField

class Category(models.TextChoices):
    ADS = 'ads', 'ADS'
    NARRATION = 'narration', 'Narration'
    DOCUMENTARY = 'documentary', 'Documentary'
    DUBBING = 'dubbing', 'Dubbing'
    BOOKS = 'books', 'Audio Books'
    OTHER = 'other', 'Other'

class VoiceOver(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = RichTextField(blank=True)
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.OTHER)
    
    audio_file = models.FileField(upload_to='audio/%Y/%m/')
    cover_image = models.ImageField(upload_to='covers/%Y/%m/', blank=True, null=True)
    
    is_featured = models.BooleanField(default=False, help_text="Check to show on the Home page showcase")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
