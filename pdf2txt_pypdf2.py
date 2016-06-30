def pdf2txt(filename):
    text = ""
    import PyPDF2 as pp
    with open(filename, 'rb') as f:
        pdf = pp.PdfFileReader(f)
        pagesno = pdf.getNumPages()
        for page in [pdf.getPage(i) for i in xrange(pagesno)]:
            data = page.extractText().encode('utf-8')
            text += data + '\n'
    filename = "{}.txt".format(filename)
    with open(filename, 'w') as f:
        f.write(text)
    return filename
        
            
