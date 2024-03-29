from django.db import models
from django.conf import settings
from django.urls import reverse


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    # def get_absolute_url(self):
    #     # return reverse('blog:post_detail',
    #     #                args=[self.publish.year,
    #     #                      self.publish.month,
    #     #                      self.publish.day,
    #     #                      self.slug])
    #
    #     return reverse('images:create',
    #                    args=[self.id])

    def __str__(self):
        return self.title
