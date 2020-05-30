""" Module for create one pdf file from some count of img """
import os
import fitz

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class ImgToPDF:
    """ Class for creating pdf """

    @staticmethod
    def create_pdf(name):
        """ Create new pdf file """
        with open(rf'{THIS_FOLDER}\..\output\{name}.pdf', 'w') as pdf:
            images = os.listdir(path=rf'{THIS_FOLDER}\..\img')
            for i, item in enumerate(images):
                image = fitz.open(rf'{THIS_FOLDER}\..\img\{images[i]}')
                image.save(rf'{THIS_FOLDER}\..\output\{name}.pdf')
            print(images)
