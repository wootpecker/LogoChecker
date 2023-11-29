"""
#Simple pdf to image form
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('data/pdf/document.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('data/page/'+ str(i) +'.jpg', 'JPEG')


"""


from spire.pdf.common import *
from spire.pdf import *
from pdf2image import convert_from_path



def save_page(doc):
  index = 0
  # Get a specific page
  for i in range(len(doc.Pages)):
    page = doc.Pages[i] #doc.Pages[1]

  # Extract images from the page
    images = []
    for image in page.ExtractImages():
        images.append(image)

# Save images to specified location with specified format extension
    with doc.SaveAsImage(i) as imageS:
      if(len(images)>0):
        imagesToSave[i].save('data/page/Contain/Image-{0:d}.png'.format(index))
     # imageS.Save("data\page\contain\Image-{0:d}.png".format(index))
     #doc.SaveAsImage(i).Save("data\page")
      else:
        imagesToSave[i].save('data/page/no_Contain/Image-{0:d}.png'.format(index))
      #imageS.Save("data\page/no_Contain\Image-{0:d}.png".format(index))
    index += 1



# Create a PdfDocument object
doc = PdfDocument()

# Load a PDF document
imagesToSave = convert_from_path('data/pdf/document.pdf')
doc.LoadFromFile('data/pdf/document.pdf')
save_page(doc)
doc.Close()

"""
  for image in images:
      imageFileName = 'data/page/Image-{0:d}.png'.format(index)
      index += 1
      image.Save(imageFileName, ImageFormat.get_Png())
"""




"""
  images = convert_from_path('document.pdf')
  for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('data/page'+ str(i) +'.jpg', 'JPEG')
"""   