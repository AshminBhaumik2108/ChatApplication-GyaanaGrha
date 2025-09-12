from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from backend.llm import get_llm
from backend.vectorstore import get_vectorstore
from backend.sentiment import analyze_sentiment
from backend.escalation import should_escalate, escalation_reason
from backend.utils import timeit

# Initialize ConversationBufferMemory for the session....
# This stores both user and assistant messages....
# {'history': [HumanMessage(content='Hi'), AIMessage(content='Hello, how can I help?')]}

# Will return the Message in Raw format for return_messages = True..
memory = ConversationBufferMemory(return_messages=True)

# Prompt template for the LLM, now includes both context and history....
answer_prompt = PromptTemplate(
    # Template : Haves the prompt....
    template=(
        "We are a warm, empathetic, and highly efficient customer support agent, trained to respond in a "
        "professional yet approachable manner. Your responses must balance emotional understanding with practical, "
        "actionable solutions.\n\n"
        "### Instructions:\n"
        "1. First, acknowledge the customer's emotions explicitly (e.g., frustration, confusion, excitement) "
        "and reassure them that We are here to help.\n"
        "2. Then, address their query using ONLY the provided context — do not invent facts.\n"
        "3. Provide the solution in clear, concise steps (numbered if more than one step).\n"
        "4. If there is insufficient context, clearly state that and politely ask a targeted clarifying question.\n"
        "5. Keep the tone positive, respectful, and human.\n"
        "6. Where appropriate, give brief encouragement or appreciation for their patience.\n\n"
        "### Customer State:\n"
        "Sentiment: {sentiment_label}\n"
        "Mood: {mood}\n"
        "Escalation Risk: {escalation_flag}\n\n"
        "### Relevant Context:\n"
        "{context}\n\n"
        "### Conversation History:\n"
        "{history}\n\n"
        "### Customer's Question:\n"
        "{query}\n\n"
        "### Your Goal:\n"
        "Craft a short but thorough reply that leaves the customer feeling understood, supported, "
        "and confident in the next steps."
    ),
    input_variables=["query", "context", "sentiment_label", "mood", "escalation_flag", "history"]
)

# Get tone guidance based on sentiment.....
def get_tone_guidance(label):
    if label == "NEGATIVE":
        return "apologetic, calm, step-by-step, offer escalation if needed"
    elif label == "NEUTRAL":
        return "friendly, concise, solution-first"
    else:
        return "warm and concise, confirm resolution"

# Decoder function for the file to produce the result, latency for the return type.....
# It a Sugar coating of the function for the file that is Declared in the utils.py file of the backend folder....
@timeit
def run_chain(query, history, temperature=0.5, top_k=4):
    # Initialize vector store and retriever : Function is Declared in the vectorstore.py file.....
    vs = get_vectorstore()
    # .as_retriever() : cosine similarity (or Chroma’s nearest-neighbor search).....
    # Top k most similar chunks to return by the as_retriever().....
    retriever = vs.as_retriever(search_kwargs={"k": top_k})

    # Analyze sentiment : NEGATIVE, NEUTRAL, POSITIVE...
    sentiment = analyze_sentiment(query)
    escalation_flag = should_escalate(history)
    escalation_info = {"flag": escalation_flag, "reason": escalation_reason(history) if escalation_flag else ""}

    # Update memory with all turns in history (user and assistant)....
    for turn in history:
        if turn["role"] == "user":
            memory.chat_memory.add_user_message(turn["text"])
        elif turn["role"] == "assistant":
            memory.chat_memory.add_ai_message(turn["text"])

    # Build conversation history string for prompt......
    conversation_history = ""
    for msg in memory.chat_memory.messages:
        if msg.type == "human":
            conversation_history += f"User: {msg.content}\n"
        elif msg.type == "ai":
            conversation_history += f"Assistant: {msg.content}\n"

    # Retrieve context from ChromaDB.....
    # .get_relevant_documents() : Function is Declared in the vectorstore.py file....
    # Does an ANN (Approximate nearest Neighour) Search from the CromaDB vector Database..... cosine Similarity....
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join(d.page_content[:1000] for d in docs)

    # Compose prompt variables for the LLM.......
    prompt_vars = {
        "query": query,
        "context": context,
        "sentiment_label": sentiment["label"],
        "mood": sentiment["mood"],
        "escalation_flag": escalation_flag,
        "history": conversation_history.strip()
    }

    # Set Temperature and peompt Text.....
    llm = get_llm(temperature=temperature)

    # EXAMPLE FILES :   <EXAMPLE FILES>
    # template = "Hello {name}, welcome to {place}!"
    # values = {"name": "Ashmin", "place": "LangChain World"}
    # print(template.format(**values)) # Hello Ashmin, welcome to LangChain World!
    
    prompt_text = answer_prompt.format(**prompt_vars) # Parse the varibles that are needed in the prompt....
    output = llm(prompt=prompt_text) # Passing the prompt_text to LLM for the Response....

    # Add the latest user and assistant messages to memory for next turn....
    memory.chat_memory.add_user_message(query)
    memory.chat_memory.add_ai_message(str(output))
    # Grab the Sources to attach with the Output Shown for Sources like NotebookLLM....
    sources = [
        {"title": getattr(d.metadata, "source", ""), "snippet": d.page_content[:120]}
        for d in docs
    ]

    # Return the Output type : 
    # Returns : result, timeInMS...

    # It can be returned in the following format....
    # result = ChatResponse(
    #       answer="Hello, how can I help you?",
    #       sources=[{"title": "FAQ", "snippet": "password reset steps..."}],
    #       sentiment={"label": "POSITIVE", "score": 0.85, "mood": "relieved"},
    #       escalation={"flag": False, "reason": ""},
    #       latency_ms=120
    # )
    # return result

    return {
        "answer": f"**Question:** {query}\n\n{output}",
        "sources": sources,
        "sentiment": sentiment,
        "escalation": escalation_info
    }
