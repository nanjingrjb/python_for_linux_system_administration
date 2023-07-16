import os
import glob
import PyPDF2
import tkinter as tk
from tkinter import filedialog


def hmi():
    root = tk.Tk()
    root.withdraw()
    #folderPath = filedialog.askdirectory()  # 获得选择好的文件夹
    Filepath = filedialog.askopenfilename(title="请选择一个要插入的pdf文件",filetypes=[('pdf', '*.pdf'), ('All Files', '*')]) #获得选择好的文件
    #data = list()
    #fileSet = os.listdir(folderPath)
    return Filepath
def get_all_pdf_files(path):
    #得到目录路径
    dir=os.path.dirname(path)
    all_pdfs = glob.glob("{0}/*.pdf".format(dir))
    all_pdfs.sort(key=str.lower)
    return all_pdfs


#将所有pdf文件合并成一个文件
def mergeAllpdf():
    all_pdfs = get_all_pdf_files(os.path.expanduser('.'))
    if not all_pdfs:
        raise SystemExit('No pdf file found!')

    merger = PyPDF2.PdfMerger()

    with open(all_pdfs[0], 'rb') as first_obj:
        merger.append(first_obj)

    for pdf in all_pdfs[1:]:
        with open(pdf, 'rb') as obj:
            reader = PyPDF2.PdfReader(obj)
            merger.append(fileobj=obj, pages=(0, len(reader.pages)))

    with open('merge-pdfs.pdf', 'wb') as f:
        merger.write(f)

#将列表中的某个pdf插入其他pdf后面
def insertOne2End(InsertPdfName):
    #all_pdfs = get_all_pdf_files(os.path.expanduser(InsertPdfName))
    all_pdfs = get_all_pdf_files(InsertPdfName)
    if not all_pdfs:
        raise SystemExit('No pdf file found!')


    #排除指定的pdf文件(当选择时，选用的pdir/end.pdf,而列表返回的是pdir\\end.pdf)
    pdir=os.path.dirname(InsertPdfName)
    name=os.path.basename(InsertPdfName)
    switchPath=pdir+"\\"+name
    if switchPath in all_pdfs:
        all_pdfs.remove(switchPath)


    for pdf in all_pdfs[0:]:
        merger = PyPDF2.PdfMerger()

        with open(pdf, 'rb') as first_obj:
            merger.append(first_obj)
        with open(InsertPdfName, 'rb') as sec_obj:
            #reader = PyPDF2.PdfReader(sec_obj)
            #merger.append(fileobj=sec_obj, pages=(0, len(reader.pages)))
            merger.append(sec_obj)
            newpdf =pdf[0:-4]+"_add.pdf"
            with open(newpdf, 'wb') as f:
                merger.write(f)






if __name__ == '__main__':
    #mergeAllpdf()
    insertPdfName = hmi()
    insertOne2End(insertPdfName)
