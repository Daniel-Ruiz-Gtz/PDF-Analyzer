# PDF Analyzer

[NOT READY - I have not been able to test that it works because I exceeded my tokens] <br>
PDF Analyzer is a Python application that allows you to upload a PDF file, analyze its content, and generate a summary using OpenAI's GPT-3 language model. This README provides instructions on how to use the application and set it up.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequisites

Before you can use PDF Analyzer, you need to have the following prerequisites installed on your system:

- Python 3.x
- tkinter library
- ttkbootstrap library
- PyPDF2 library
- dotenv library
- openai library
- An OpenAI API key (You can obtain one from the OpenAI platform)

## Installation

1. Clone or download the PDF Analyzer repository to your local machine.

2. Create a virtual environment (recommended) to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

3. Install the required libraries using pip.

   ```bash
   pip install tkinter ttkbootstrap PyPDF2 dotenv openai
   ```

4. Create a file named `config.env` in the same directory as your code and set your OpenAI API key inside it.

   ```
   OPEN_API_KEY=your_api_key_here
   ```

5. Modify the code to customize it or leave it as-is to use the default summarization logic.

6. Run the application.

   ```bash
   python your_script_name.py
   ```

## Usage

1. Launch the PDF Analyzer application.

2. Click the "Upload PDF" button to browse and select a PDF file you want to analyze.

3. After selecting the PDF, click the "Generate Summary" button to initiate the summarization process.

4. The application will extract the text from the PDF and use OpenAI to generate a summary of the content.

5. The summary will be displayed in the text box below, along with information about the PDF, such as its path and the number of pages.

6. You can customize the summarization logic by modifying the code within the `generate_summary` function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
