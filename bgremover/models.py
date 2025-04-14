from django.db import models
import uuid #unique namees ki file bnnane ke liye
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1] #isse to file la extension nikal lo 
    filename = f"{uuid.uuid4()}.{ext}"  #ek unique nam bn jaega then use next line ki help se upload folder me updload kr
    return os.path.join('uploads/', filename)

def get_output_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('results/', filename)

class ProcessedImage(models.Model):
    original_image = models.ImageField(upload_to=get_file_path)
    processed_image = models.ImageField(upload_to=get_output_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
