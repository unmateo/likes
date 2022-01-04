from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BaseLikeModel(BaseModel):

    class Meta:
        abstract = True

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Item(BaseLikeModel):

    class Meta:
        ordering = ["-created_at"]

    web = models.URLField()
    tags = models.ManyToManyField('Tag', through='ItemTag')


class Tag(BaseLikeModel):

    items = models.ManyToManyField(Item, through='ItemTag')


class ItemTag(BaseModel):

    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['item', 'tag'], name='unique_item_tag')
        ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item}|{self.tag}"
