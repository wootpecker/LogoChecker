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

