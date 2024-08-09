from src.constants import *
from src.retriever import create_code_retriever
from langchain.prompts import PromptTemplate
from langchain.llms.ctransformers import CTransformers
from langchain.chains.question_answering import load_qa_chain 

def create_codebase():
    llm=CTransformers(model= MODEL, model_type= MODEL_TYPE,temperature= TEMPERATURE,max_new_tokens=MAX_NEW_TOKENS)

    prompt= PromptTemplate(template=PROMPT_TEMPLATE, input_variables=INP_VARS)
    coder=load_qa_chain(llm=llm,chain_type='stuff',prompt=prompt)

    return coder