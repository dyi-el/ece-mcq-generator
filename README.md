# ✅ Electronics Engineer Licensure Exam Generator
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ece-mcq.streamlit.app)
## Overview

This project is a Retrieval-Augmented Generation (RAG) application designed to generate practice exam questions for the Electronics Engineer Licensure Exam. The project is a collaborative effort by **JL Bualoy** and **Denver Magtibay** from Smart Edge ECE Review Specialist. Currently, the application supports topics under Electronics Systems and Technologies.

## Features

- Generate multiple-choice questions (MCQs) based on selected topics.
- Update the local database with new documents for enhanced context.
- View the generated questions and answers directly within the application.

## Requirements

- Python 3.x
- Streamlit
- OpenAI API key
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ece-exam-generator.git
    cd ece-exam-generator
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) For local development, ensure the `pysqlite3` package is used for SQLite:
    ```python
    # Remove this when running locally
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
    ```

5. Set up your Streamlit secrets. Create a file named `.streamlit/secrets.toml` in the root directory of your project and add your API keys:
    ```toml
    [secrets]
    NO_API_KEY = "your_no_api_key"
    OPENAI_API_KEY = "your_openai_api_key"
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run main.py
    ```

2. Open the application in your web browser at `http://localhost:8501`.

3. Use the sidebar to input your OpenAI API key. If you do not have one, you can get it from the [OpenAI Platform](https://platform.openai.com/).

4. Select a topic from the dropdown menu and specify the number of MCQs you want to generate.

5. Click the "Generate Exam" button to create the exam questions.

6. The generated questions will be displayed on the main page, and the answer key can be viewed by expanding the section in the sidebar.

### Updating the Database

- To update the database with new documents, upload a PDF file via the sidebar after entering your API key.
- Click "Update Database" to initiate the update process. Note that this functionality works only locally.

## Supported Topics

Supports ESAT topics based on the PRC TOS 2022.
- Signal Spectra and Processing
- Principles of Communication
- Digital Communications
- Transmission and Antenna Systems
- Electronic Systems and Design
- Data Communications

Will support more subjects soon. In the meantime, you can upload your own pdf to add more context to the model.

## Contributors

- **JL Bualoy**
- **Denver Magtibay**

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

-<img src="assets/smart-edge-logo.png" alt="Smart Edge Logo" width="256"/>

