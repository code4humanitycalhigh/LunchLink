from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import WebBaseLoader
import os 
from langchain import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import TextLoader
import openai
from langchain_openai import ChatOpenAI
import pandas as pd
pd.set_option('display.max_columns', None)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain import hub
import getpass
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import CacheBackedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.storage import LocalFileStore
import warnings

from langchain.text_splitter import RecursiveCharacterTextSplitter
warnings.filterwarnings("ignore")
# taps into external documents, combines info retrieval with text generation
# rag uses documents (like wikipedia, blends them with the query to create an enriched context, which can then be processed by a text generator to 
# produce the final answer
# uses current fresh data, reduces errors, hallucinations

#print(os.getenv('OPENAI_API_KEY'))

def rag_bot(prompt):
    os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_PRIVATE_KEY')

    df=pd.read_csv("data/form.csv")
    feedback= [x for x in df["Feedback"].values.tolist() if str(x) != 'nan']
    #print(feedback)
    with open('data/feedback.txt', 'w') as f:
        for line in feedback:
            f.write(f"{line}\n")

    form_loader=TextLoader("data/feedback.txt").load()
    


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50,
        length_function = len
    )

    form_chunks = text_splitter.transform_documents(form_loader)
    '''
    index system
    1. load documents
    2. break down documents in smaller parts
    3. embed documents (convert them to vector format)
    4. keep embeds and text counterparts for retrieval
    '''



    store = LocalFileStore("./cachce/")

    # create an embedder
    core_embeddings_model = OpenAIEmbeddings()

    embedder = CacheBackedEmbeddings.from_bytes_store(
        core_embeddings_model,
        store,
        namespace = core_embeddings_model.model
    )

    # store embeddings in vector store
    vectorstore = FAISS.from_documents(form_chunks, embedder)
    '''
    steps in retrieval system
    1. obtain user query
    2. embed user query
    3. vector search using embedded query
    4. return relevant documents
    '''


    # instantiate a retriever

    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(model="gpt-4-0125-preview")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_prompt = hub.pull("rlm/rag-prompt")
    #print(rag_prompt)
    

    
    prompt_template = PromptTemplate.from_template(
    template="""
    You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know and explain why. 
    You collected data about student preferences on a high school lunch system by 
    sending out a survey. 
    Your data is a list of student feedback addressing varying lunch items, lunch systems, and advice.
    Note that each line is a new piece of feedback, and that feedback such as 'None', 'Thank you',
    'Alright', etc should be ignored.
    Answer any questions the lunch staff have. 
    Quote the feedback if needed, but don't paraphrase, and include it AFTER your answer. 
    Try not to include more than 5 excerpts.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    
    )
    #print(prompt_template)
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )
    #prompt += "If you can't answer the question, please say 'Sorry, I can't accurately answer that.', and explain why."
    return rag_chain.invoke(prompt)

#print(rag_bot("what could use improving?"))

