from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from PyPDF2 import PdfReader
from ttkbootstrap.constants import *
from dotenv import load_dotenv
import os
import openai

# Set up your OpenAI API key
load_dotenv('config.env')
openai.api_key = os.environ.get("OPEN_API_KEY")

# Store the path of the currently loaded PDF
file_path = ""

def browse_pdf():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        generate_summary_button.config(state="normal")

def generate_summary():
    try:
        global file_path
        if not file_path:
            messagebox.showerror("Error", "Please upload a PDF first.")
            return
        
        reader = PdfReader(file_path)
        num_pages = len(reader.pages)
        
        # Extract text from PDF (you can replace this with your own PDF summarization logic)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()
        
        # Use OpenAI to generate a summary
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Summarize the following PDF:\n{pdf_text}\nSummary:",
            max_tokens=1,
        )
        summary = response.choices[0].text.strip()
        
        # Display the summary in the result_text text box
        result_text.delete(1.0, ttk.END)
        result_text.insert(ttk.END, f"PDF Path: {file_path}\n")
        result_text.insert(ttk.END, f"Pages: {num_pages}\n")
        result_text.insert(ttk.END, "Summary:\n")
        result_text.insert(ttk.END, summary)
    except Exception as e:
        messagebox.showerror("Error", f"Error generating summary: {str(e)}")

# Create the main window
root = ttk.Window(title="PDF Analyzer", themename="darkly")
root.geometry("700x500")
# Change the window icon
root.iconbitmap("public/icon.ico")

# Button to browse and load a PDF
load_pdf_button = ttk.Button(root, text="Upload PDF", command=browse_pdf, bootstyle="success-outline")
load_pdf_button.pack(pady=10)

# Button to generate the PDF summary
generate_summary_button = ttk.Button(root, text="Generate Summary", command=generate_summary, bootstyle="primary")
generate_summary_button.pack(pady=10)
generate_summary_button.config(state="disabled")  # Initially disable the button

# Text box to display the result
result_text = ttk.Text(root, wrap=ttk.WORD, width=70, height=30)
result_text.pack(padx=10, pady=10)

root.mainloop()
