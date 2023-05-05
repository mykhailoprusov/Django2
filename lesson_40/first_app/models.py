from django.db import models


class Title(models.Model):
    title_new = models.CharField(max_length=110)

    def __str__(self):
        return self.title_new
class Notes(models.Model):
    title = models.ForeignKey(Title,on_delete=
                              models.CASCADE)
    text = models.TextField()
    reminder = models.DateTimeField(auto_now=True)




