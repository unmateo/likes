from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(BaseModel):

    class Meta:
        ordering = ["-created_at"]

    name = models.CharField(max_length=200, unique=True)
    link = models.URLField()
    tags = models.ManyToManyField('Tag', through='ItemTag')

    def __str__(self):
        return self.name

class Tag(BaseModel):

    name = models.CharField(max_length=200, unique=True)
    items = models.ManyToManyField(Item, through='ItemTag')

    def __str__(self):
        return self.name

class ItemTag(BaseModel):

    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['item', 'tag'], name='unique_item_tag')
        ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item}|{self.tag}"
