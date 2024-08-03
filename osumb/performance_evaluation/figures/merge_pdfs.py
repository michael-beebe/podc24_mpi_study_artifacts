import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory, output_filename):
    # Get the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the full paths to the specified directory and output file
    input_directory = os.path.join(script_directory, directory)
    output_file_path = os.path.join(script_directory, output_filename)

    # Get a list of all PDF files in the specified directory
    pdf_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.pdf')]

    # Sort the PDF files to ensure they are merged in the correct order
    pdf_files.sort()

    if not pdf_files:
        print(f"No PDF files found in the directory: {input_directory}")
        return

    # Create a PDF merger object
    merger = PdfMerger()

    # Merge all the PDF files
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            merger.append(file)

    # Remove the output file if it already exists
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # Output the merged PDF to the specified output file
    with open(output_file_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"Merged {len(pdf_files)} PDF files into '{output_filename}'.")

if __name__ == "__main__":
    merge_pdfs('blocking_collectives', 'blocking_collectives.pdf')
    merge_pdfs('pt2pt', 'pt2pt.pdf')
    merge_pdfs('non_blocking_collectives', 'non_blocking_collectives.pdf')
    merge_pdfs('loglog_blocking_collectives', 'loglog_blocking_collectives.pdf')
    merge_pdfs('loglog_pt2pt', 'loglog_pt2pt.pdf')


    # merge_pdfs('.', 'device_to_device.pdf')

