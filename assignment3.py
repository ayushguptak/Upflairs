import os
import shutil
os.makedirs("JECRC1")
os.makedirs("text_folder")
os.makedirs("pdf_folder")
os.makedirs("img_folder")
source_folder = r"K:\MLWithAI\JECRC1"
text_folder = r"K:\MLWithAI\text_folder"
pdf_folder = r"K:\MLWithAI\pdf_folder"
img_folder = r"K:\MLWithAI\img_folder"
os.chdir(source_folder)

files = os.listdir()
for i in files:
    file_extension = os.path.splitext(i)[1]
    if file_extension in [".txt"]:
        shutil.move(os.path.join(source_folder, i), os.path.join(text_folder,i))
    if file_extension in [".pdf"]:
        shutil.move(os.path.join(source_folder, i), os.path.join(pdf_folder,i))
    if file_extension in [".png"]:
        shutil.move(os.path.join(source_folder, i), os.path.join(img_folder,i))