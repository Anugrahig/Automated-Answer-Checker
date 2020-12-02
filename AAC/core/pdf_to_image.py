# Import module 
from pdf2image import 
convert_from_path

# Store Pdf with Converter_from_path
def my_function(path):
  images = convert_from_path('example.pdf')
  
  for img in images:
    img.save('output.jpg','JPEG)
    
