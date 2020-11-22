# article/model.py

from django.conf import settings
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    """
    """
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status="published")


class Article(models.Model):
    """
    """
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    CONTENT_LANGUAGE_CHOICES = (
        ("html", "HTML",),
        ("mark", "Markdown"),
    )
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    content_html = models.TextField(blank=True, null=True, editable=False)
    # tags = TaggableManager()
    language = models.CharField(max_length=20,
                                choices=CONTENT_LANGUAGE_CHOICES,
                                default='html',
                                help_text="Select Content Language")
    # slug = models.SlugField(max_length=250,
    #                         unique_for_date="publish",
    #                         blank=True,
    #                         null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default="draft")

    class Meta:
        ordering = ("-publish", )

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     # print("Save method called")
    #     if not self.id:
    #         self.slug = slugify(self.title)
    #     self.body_content = markdown_format(self.body)

    #     super(Post, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     published_localtime = timezone.localtime(self.publish)
    # return reverse('blog:post_detail',
    #                args=[self.publish.year,
    #                      self.publish.month,
    #                      self.publish.day,
    #                      self.slug])
    # return reverse(
    #     "blog:post_detail",
    #     args=[
    #         published_localtime.year,
    #         published_localtime.strftime("%m"),
    #         published_localtime.strftime("%d"),
    #         self.slug,
    #     ],
    # )
