from pypdf import PdfWriter, PdfReader

file1="pdf1.pdf"
file2="pdf2.pdf"
output = "merged.pdf"

writer = PdfWriter()

for pdf in [file1, file2]:
    reader = PdfReader(pdf)

    for page in reader.pages:
        writer.add_page(page)

with open(output, "wb") as f:
    writer.write(f)

print(f"Merged {file1} and {file2} into {output}")