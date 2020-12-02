# Import module 
from pdf2image import convert_from_path


# Store Pdf with Converter_from_path
def pdf_to_image(path):
  images = convert_from_path('example.pdf')
  
  for img in images:
    img.save('output.jpg','JPEG)
    
