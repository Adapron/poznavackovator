from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
import os
from PIL import Image

# Set the name of the PDF file
pdf_file = 'my_pdf.pdf'

# Set the size of the PDF page (in this case, letter size)
page_size = letter

# Create a new PDF canvas
c = Canvas(pdf_file, pagesize=page_size)

# Set the font and font size for the text
c.setFont('Helvetica', 20)

# Set the base directory where the images are stored
base_dir = './imgs'

# Get a list of all the image files in the base directory
image_files = [f for f in os.listdir(base_dir) if f.endswith('.jpeg')]

# Set the gap between the images
gap = 10

# Set the y coordinate for the first image
y = 50

# Keep track of the current name
current_name = None

# Iterate through the image files
for image_file in image_files:

  name = image_file.split('_')[0]
  
  # Check if the name has changed
  if name != current_name:
    # Update the current name
    current_name = name
    
    # Reset the y coordinate
    y = 50

    
 
  
  
  # Get the width and height of the page
  page_width, page_height = page_size

  # Set the width and height of the image to one fifth of the page size
  
  image_height = page_height / 6

  # Open the image file using the Image module
  im = Image.open(os.path.join(base_dir, image_file))
  
  # Get the original width and height of the image
  original_width, original_height = im.size

  # Calculate the aspect ratio of the original image
  aspect_ratio = original_width / original_height

  # Calculate the new width of the image based on the aspect ratio and desired height
  image_width = image_height * aspect_ratio

  # Add the image to the PDF canvas, specifying the width and height
  c.drawImage(os.path.join(base_dir, image_file), 0, y, width=image_width, height=image_height)
  
  # Increment the x coordinate for the next image
  y += image_height + gap
  
  # Add the name to the bottom of the page
  
  
  if y + image_height > page_height:
    c.drawString(0, 10, " ".join(name.split("+")))
    # Create a new page

    c.showPage()
    
    
    # Reset the y coordinate
    y = 0

# Save the PDF to disk
c.save()
