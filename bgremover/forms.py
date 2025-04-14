from django import forms
from .models import ProcessedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ProcessedImage
        fields = ['original_image']
        
    def clean_original_image(self):
        image = self.cleaned_data.get('original_image')
        if image:
            # Validate file extension
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("Only JPG, JPEG, and PNG images are allowed.")
                
            # Validate file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Image size should not exceed 5MB.")
                
        return image 