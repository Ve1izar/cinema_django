from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    is_watched = models.BooleanField(default=False)
    trailer_url = models.URLField(max_length=500, blank=True, null=True)
    actors = models.CharField(max_length=500, blank=True, null=True, verbose_name="Актори")

    def get_embed_trailer_url(self):
        if not self.trailer_url:
            return None
        
        if "youtube.com/embed/" in self.trailer_url:
            return self.trailer_url
            
        if "watch?v=" in self.trailer_url:
            video_id = self.trailer_url.split("watch?v=")[1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"
            
        if "youtu.be/" in self.trailer_url:
            video_id = self.trailer_url.split("youtu.be/")[1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"
            
        return self.trailer_url

    def __str__(self):
        return self.title