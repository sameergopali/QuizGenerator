# Check your understaing with Quiz Generator

This Streamlit app allows you to generate multiple-choice quiz questions using a Language Model (LLM). The app takes a PDF document as input, processes it to extract relevant information, and generates questions based on the extracted content.

## Features

- **PDF Upload:** Upload a PDF document to generate quiz questions from its content.
- **Question Generation:** Generate multiple-choice questions based on the uploaded PDF content.
- **Topic Specification:** Specify a topic of interest for generating questions related to that topic.

## How to Run the App

1. Make sure you have Python and Streamlit installed.

2. Clone this repository:
   ```bash
   git clone https://github.com/your_username/streamlit-quiz-generator.git
   cd streamlit-quiz-generator

3. Install the required dependencies:
    ```bash 
    pip install -r requirements.txt

4. Run the Streamlit app:
    ```bash 
    streamlit run app.py

5. Access the app in your browser
## Usage
1. Set API keys in settings page
2. Upload a PDF document containing the content for which you want to generate quiz questions.
3. Click the "Upload" button to start processing the PDF and indexing its content.
4. Once indexed, enter the maximum number of questions you want to generate and specify a topic related to the content.
5. Click the "Generate questions" button to generate the quiz questions.
6. Review the generated questions and choose the answers for each question.
7. Click the "Submit my answers" button to see your quiz score
