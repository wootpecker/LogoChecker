#paid model - 
#To Do need to get site of current image

# Importieren Sie Aspose.Words für das Python-Modul
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

