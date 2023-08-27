from langchain.prompts import ChatPromptTemplate

from langchain.chat_models import ChatOpenAI

from flask import Flask, request, render_template


def fapoonanator(*args):
    
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
    


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        word1 = request.form["word1"]
        word2 = request.form["word2"]
        result = fapoonanator(word1, word2)
    return render_template("home.html", result=result)

if __name__ == '__main__':
    app.run(debug=True,port=8080) 