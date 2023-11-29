'''# Importieren Sie Aspose.Words für das Python-Modul
import aspose.words as aw

# Laden Sie die PDF-Datei und konvertieren Sie sie in das Word-DOCX-Format
pdf = aw.Document("document.pdf")
pdf.save("pdf.docx")

# Laden Sie die DOCX-Version von PDF
doc = aw.Document("pdf.docx")

# Abrufen aller Formen
shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
imageIndex = 0

# Loop durch Formen
for shape in shapes :
    shape = shape.as_shape()
    if (shape.has_image) :

        # den Namen der Bilddatei festlegen
        imageFileName = f"Image.ExportImages.{imageIndex}_{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"

        # Bild speichern
        shape.image_data.save(imageFileName)
        imageIndex += 1




from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('document.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('data\page'+ str(i) +'.jpg', 'JPEG')




'''





from spire.pdf.common import *
from spire.pdf import *
from pdf2image import convert_from_path

# Create a PdfDocument object
doc = PdfDocument()



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
        imagesToSave[i].save('data\page/Contain\Image-{0:d}.png'.format(index))
     # imageS.Save("data\page\contain\Image-{0:d}.png".format(index))
     #doc.SaveAsImage(i).Save("data\page")
      else:
        imagesToSave[i].save('data\page/no_Contain\Image-{0:d}.png'.format(index))
      #imageS.Save("data\page/no_Contain\Image-{0:d}.png".format(index))
    index += 1


# Load a PDF document
imagesToSave = convert_from_path('document.pdf')
doc.LoadFromFile('document.pdf')
#save_page(doc)

"""
  for image in images:
      imageFileName = 'data\page\Image-{0:d}.png'.format(index)
      index += 1
      image.Save(imageFileName, ImageFormat.get_Png())
"""
doc.Close()




"""
  images = convert_from_path('document.pdf')
  for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('data\page'+ str(i) +'.jpg', 'JPEG')
"""   


import fitz
docu = fitz.open("document.pdf")
for i in range(len(docu)):
    for img in docu.get_page_images(i):
        xref = img[0]
        pix = fitz.Pixmap(docu, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("data\page\images\p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("data\page\images\p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None
