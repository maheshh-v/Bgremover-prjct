from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from .forms import ImageUploadForm
from .models import ProcessedImage
import os
from PIL import Image
from rembg import remove
import io
import uuid

def home(request):
    return render(request, 'bgremover/home.html', {
        'form': ImageUploadForm()
    })

def remove_bg(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            processed_img = form.save(commit=False)
            processed_img.save()
            
            # original image ka path
            original_path = processed_img.original_image.path
            
            # Create output path
            output_path = os.path.join(settings.MEDIA_ROOT, 'results', f"{uuid.uuid4()}.png")
            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))
            
            # Process the image to remove background
            with open(original_path, 'rb') as i:  #'rb' ka matlab hai read binary mode.
                input_image = i.read()
                output_image = remove(input_image)
                
                output_img = Image.open(io.BytesIO(output_image)).convert("RGBA")
                output_img.save(output_path)
            
            # Update the model with the path to the processed image
            relative_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
            processed_img.processed_image = relative_path
            processed_img.save()
            
            # Redirect to a page with the processed image
            return render(request, 'bgremover/result.html', {
                'image': processed_img,
                'form': ImageUploadForm()
            })
    else:
        form = ImageUploadForm()
    
    return render(request, 'bgremover/home.html', {'form': form})
#📌 Images binary data me stored hoti hain, isliye 'rb' use karna padta hai. 
# 📌 Binary mode se image ka raw data milta hai, jo processing me helpful hota hai.
#  📌 Text mode ('r') images ke liye kaam nahi karega, kyunki wo sirf normal text read kar sakta hai.