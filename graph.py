from langgraph.graph import StateGraph, END

from llm import get_llm
from prompt import get_prompt
from rag.retriever import get_retriever  

llm = get_llm()
prompt = get_prompt()


retriever = get_retriever()


def retrieve_node(state):
    query = state["input"]

   
    docs = retriever.invoke(query)

    context = "\n\n".join([d.page_content for d in docs])

    history = state.get("history", "")

    full_context = f"""
HISTORY:
{history}

RAG:
{context}
"""

    return {
        "input": query,
        "context": full_context
    }


def llm_node(state):
    chain = prompt | llm

    result = chain.invoke({
        "question": state["input"],
        "context": state["context"]
    })

    return {"output": result.content}


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("llm", llm_node)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "llm")
    graph.add_edge("llm", END)

    return graph.compile()