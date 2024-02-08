from pdf2image import convert_from_path
import os
import requests
import asyncio

# os.startfile("C:/Users/robid/Downloads/Bolshaya_kniga_proektov_Python_2022_Svei_774_gart_E.pdf")


# Specify the path to your PDF file
pdf_path = 'C:/Users/robid/Downloads/humo-ariza.pdf'



# Convert the PDF to images
for i, image in enumerate(convert_from_path(pdf_path)):
    image.save(f'page_{i}.jpg', 'JPEG') # Save each page as an image

