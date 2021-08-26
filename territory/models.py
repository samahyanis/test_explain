from django.db import models

# Create your models here.


class Terriotry(models.Model):

    code = models.CharField(max_length=60)
    name = models.CharField(max_length=150)
    kind = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_current = models.BooleanField()
    population = models.CharField(max_length=30)
    official_website_url = models.TextField()
    articles_count = models.CharField(max_length=50)
    admin_docs_count = models.CharField(max_length=50)
    impacters_count = models.CharField(max_length=50)
    websites_count = models.CharField(max_length=50)
    sources_count = models.CharField(max_length=50)

    class Meta:
        db_table = 'terriotry'

class TerritorysParents(models.Model):

    child_id = models.CharField(max_length=60)
    parent_id = models.CharField(max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'territory_parents'

