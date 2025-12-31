from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_community.llms import Ollama


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# llm = Ollama(model="llama2")


class DecisionState(TypedDict):
    goal: str
    proposal: str
    pros: str
    cons: str
    risks: str
    final_decision: str


def pros_agent(state: DecisionState):
    msg = HumanMessage(
        content=f"List the benefits of this proposal:\nGoal: {state['goal']}\nProposal: {state['proposal']} \nDo not use symbols like * for bold, etc"
    )
    return {"pros": llm.invoke([msg]).content}


def cons_agent(state: DecisionState):
    msg = HumanMessage(
        content=f"List the downsides of this proposal:\nGoal: {state['goal']}\nProposal: {state['proposal']} \nDo not use symbols like * for bold, etc"
    )
    return {"cons": llm.invoke([msg]).content}


def risk_agent(state: DecisionState):
    msg = HumanMessage(
        content=f"Identify risks or failure points:\nGoal: {state['goal']}\nProposal: {state['proposal']} \nDo not use symbols like * for bold, etc"
    )
    return {"risks": llm.invoke([msg]).content}


def decision_agent(state: DecisionState):
    msg = HumanMessage(
        content=f"""
        Based on:
        Pros: {state['pros']}
        Cons: {state['cons']}
        Risks: {state['risks']}
        Give a final recommendation. \nDo not use symbols like * for bold, etc
        """
    )
    return {"final_decision": llm.invoke([msg]).content}


def build_decision_graph():
    graph = StateGraph(DecisionState)

    graph.add_node("pros", pros_agent)
    graph.add_node("cons", cons_agent)
    graph.add_node("risks", risk_agent)
    graph.add_node("final", decision_agent)

    graph.set_entry_point("pros")
    graph.add_edge("pros", "cons")
    graph.add_edge("cons", "risks")
    graph.add_edge("risks", "final")

    return graph.compile()