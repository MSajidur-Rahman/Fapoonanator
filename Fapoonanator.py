from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def Fapoonanator(*args):
    
    system_message = """
    You are a word combiner. You will return the portmanteau of the given words. 
    However, it needs to be the unintuitive version. 
    The return value should be the opposite of the obvious combination.
    Example: 
    Spoon, Fork = Fapoon
    Hotel, Motor = Hotor"
    """
    template = ChatPromptTemplate.from_messages([
        ("system", system_message),     
        ("human", "{words}")])
    
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 0)
    
    formatted_template = template.format_messages(words = str(args))
    
    response = llm(formatted_template).content
    
    return response
    
print(Fapoonanator("Spoon", "Fork"))
