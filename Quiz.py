import streamlit as st
from modules.pdf_loader import load_pdf
from modules.utils import index_pdf
from modules.langchain_utils import get_questions
import os




# Function to handle PDF upload and processing
def process_pdf():
    pdf = st.file_uploader("Upload document, only PDF files allowed", type=["pdf"], accept_multiple_files=False)
    if pdf:
        submit = st.button("Upload")
        if submit:
            with st.spinner('Loading...'):
                docs = load_pdf(pdf)
                index = index_pdf(pdf_doc=docs)
                st.session_state['indexed'] = True
                st.session_state['index'] = index


# Function to render the generate questions form
def render_generate_form():
    st.subheader("Available sources")
    with st.form('generate'):
        num_of_questions = st.number_input('Max number of questions to generate',
                                          min_value=1,
                                          max_value=5,
                                          value=3,
                                          disabled=not st.session_state.get('indexed', False))
        topic = st.text_input("Enter a topic that you're interested in:",
                              disabled=not st.session_state.get('indexed', False))
        generate_quiz_button = st.form_submit_button('Generate questions',
                                                     disabled=not st.session_state.get('indexed', False))
        return generate_quiz_button, num_of_questions, topic


def render_quiz(quiz_questions):
    answers = []
    containers = []

    for i, question in enumerate(quiz_questions.quiz):
        container = st.container()
        answer = container.radio(f'Question {i + 1}: {question.question}',
                                 question.choices)
        answers.append(question.choices.index(answer))
        containers.append(container)

    submit_quiz_button = st.form_submit_button('Submit my answers')

    return answers, containers, submit_quiz_button
# Function to generate questions
def generate_questions(num_of_questions, topic):
    with st.spinner("Generating quiz"):
        quiz = get_questions(st.session_state['index'], num_of_questions, topic)
        return quiz


# Function to handle quiz submission and calculate score
def submit_quiz(quiz_questions, answers, containers):
    score = 0
    for i, (question, answer_index, container) in enumerate(zip(quiz_questions, answers, containers)):
        container.write(f'Question {i + 1}: {question.question}')
        if str(answer_index) == question.correct:
            container.success('Your answer is correct')
            score += 1
        else:
            container.error('Your answer is incorrect')
    st.write(f'Your score: {score}/{len(quiz_questions)}')

def main():
    st.set_page_config(page_title="Upload PDF")
    st.title("Upload docs ")
    st.subheader("Generate Multiple Choice Questions for you.")

    process_pdf()
    generate_button_disabled = not st.session_state.get('indexed', False)

    if not generate_button_disabled:
        generate_quiz_button, num_of_questions, topic = render_generate_form()

        if generate_quiz_button:
            st.session_state['quizz'] = generate_questions(num_of_questions,topic)


    if st.session_state.get('quizz',False):   
         with st.form('quiz'):
            # Call function to render quiz and handle submission
            answers, containers, submit_quiz_button = render_quiz(st.session_state['quizz'])
            if submit_quiz_button:
                # Call function to submit quiz and calculate score
                submit_quiz(st.session_state['quizz'].quiz, answers, containers)
#Invoking main function
if __name__ == '__main__':
    if os.environ.get("OPENAI_API_KEY") and os.environ.get("HUGGINGFACEHUB_API_TOKEN") and os.environ.get("PINECONE_API_KEY"):
        main()
    else:
        st.markdown("<h2 style='text-align: center;'>API keys missing!! Set API Keys in settings. </h2>", unsafe_allow_html=True)