from django.db import models

# Create your models here.
class DashboardModel(models.Model):
    class Meta:
        permissions = [
            ("index_viwer", "Can show to index view (function-based)"),
        ]