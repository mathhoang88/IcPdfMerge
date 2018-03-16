###################################################################
#list_name.sort(key= lambda x: float(x.strip('something'))) 
#C:\Python27\ArcGIS10.2\Scripts\pyinstaller.exe --onefile --windowed app.py
#version 0.3: Merge PDF files
import re
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
import datetime
import sys

defaul_pdf_name = "Merged_"
pdf_ext = ".pdf"
help_opt = "-HELP"

help_desc = """
------------------------------------------------------------------------------
ICmergePdf is a tiny tool to merge pdf file together:
ICMergePdf {Path_Contains_PDF_files} [Input_PDF_Wild_Card] [Output_PDF_File]
    
    Note:
        1) missing input wild card, all pdf files are being combined
        2) missing output name, output file will be have default name
------------------------------------------------------------------------------

"""

if (str(sys.argv[1]).upper() == help_opt):
    print (help_desc)
    sys.exit() 

os.chdir(str(sys.argv[1]))

wild_file = {}

try:
    wild_file = sys.argv[2].split(',')
except:
    wild_file = {''}

pdf_file_name =""

try:
    pdf_file_name = sys.argv[3] + pdf_ext
except:
    pdf_file_name = defaul_pdf_name + datetime.datetime.now().strftime("%H_%M_%S_%m_%d_%Y") + pdf_ext



files_dir = os.getcwd()
all_files = list()

########################### SORT FUNCTION #######################
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


for wild_card in wild_file:
    page_pdf = sorted([f for f in os.listdir(files_dir) if wild_card in f and 'pdf' in f])

    page_pdf.sort(key=natural_keys) # real sort

    all_files.extend(page_pdf)



merger = PdfFileMerger()

for f in all_files:
    merger.append(PdfFileReader(f), 'rb')

merger.write(pdf_file_name)
