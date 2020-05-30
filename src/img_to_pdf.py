""" Module for create one pdf file from some count of img """
import os
import fitz

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class ImgToPDF:
    """ Class for creating pdf """

    @staticmethod
    def create_pdf(name):
        """ Create new pdf file """
        pdf = fitz.open()
        images = os.listdir(path=rf'{THIS_FOLDER}\..\img')
        for i, item in enumerate(images):
            pdf.insertPage(i)
            page = pdf.loadPage(i)
            rect = fitz.Rect(0, 0, 2480, 3508)
            img = fitz.Pixmap(rf'{THIS_FOLDER}\..\img\{images[i]}')
            page.insertImage(rect, pixmap=img)
        pdf.save(rf'{THIS_FOLDER}\..\output\{name}.pdf')
