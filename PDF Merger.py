from PyPDF2 import PdfMerger
pdf_files = [r"D:\Python Programming\1.pdf", r"D:\Python Programming\2.pdf"]

pdfmerge = PdfMerger()
for newpdf in pdf_files:
    pdfmerge.append(newpdf)

pdfmerge.write(r"D:\Python Programming\Merged.pdf")
pdfmerge.close()

# import os
#
# pdf_files = [r"D:\Python Programming\1.pdf", r"D:\Python Programming\2.pdf"]
#
# for pdf in pdf_files:
#     if os.path.exists(pdf):
#         print(f"✅ File Found: {pdf}")
#     else:
#         print(f"❌ File Not Found: {pdf}")
# # import os
# # print("Current Directory:", os.getcwd())