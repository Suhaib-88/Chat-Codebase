REPO_PATH = "C:\\Users\\DELL\\chat-codebase\\codebase"
GLOB = "**/*"
SUFFIXES = [".py"]
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
EMBEDDER = "thenlper/gte-large"
EMBEDDER_KWARGS = {'device': 'cpu'}
SEARCH_KWARGS = {"k": 2}
MODEL = "codellama-7b-instruct.Q4_K_M.gguf"
MODEL_TYPE = "llama"
TEMPERATURE = 0.3
MAX_NEW_TOKENS = 512
DO_SAMPLE = True
PROMPT_TEMPLATE = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
{context}
Question: {question}
Helpful Answer:
"""
INP_VARS = ["context", "question"]