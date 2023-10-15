from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from modules.outputSchema import Quiz
from langchain.output_parsers import PydanticOutputParser


def init_llm():


    
    prompt_template = """You are a teacher coming up with questions to ask on a quiz. 
    Given the following document delimited by three backticks please generate {num_questions} multiple choices question based on that document.
    A question should be concise and based explicitly on the document's information. It should be asking about one thing at a time.
    Answer choices should be written clearly and similarly to each other in content, length, and grammar; avoid giving clues through the use of faulty grammatical construction; avoid using commas in answers choices. 
    Make all distractors plausible; they should be common misconceptions that learners may have.
    Try to generate a question that can be answered by the whole document not just an individual sentence.
    If there are several questions they should be separated by a newline character.
    When formulating a question, don't reference the provided document or say "from the provided context", "as described in the document", "according to the given document" or anything similar.
    Reference the correct answer by its numeric value only. Make sure that output is in valid json format:
    ```
    {context_str}
    ```"""

    parser = PydanticOutputParser(pydantic_object=Quiz)
    pyda = parser.get_format_instructions()
   
    prompt = PromptTemplate(
        template= prompt_template +"\n{format_instructions}" ,
        input_variables=["num_questions", "context_str"],
        partial_variables={"format_instructions": pyda}
        )

    llm =  OpenAI(temperature=0.0,model="text-davinci-003")

    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return llm_chain,parser


def get_similiar_docs(index,query, k=2):
    similar_docs = index.similarity_search(query, k=k)
    return similar_docs

def get_questions(index,num_questions,query):
  relevant_docs = get_similiar_docs(index,query)
  llm_chain, parser =  init_llm()
  response = llm_chain.run({"num_questions":num_questions, "context_str":relevant_docs})
  print(response)
  quiz =  parser.parse(response)
  return quiz
