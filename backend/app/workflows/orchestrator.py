from langgraph.graph import StateGraph, END

from app.workflows.states.agent_state import AgentState

from app.workflows.nodes.router_node import router_node
from app.workflows.nodes.sql_node import sql_node
from app.workflows.nodes.rag_node import rag_node
from app.workflows.nodes.hybrid_node import hybrid_node
from app.workflows.nodes.synthesis_node import synthesis_node


def route_decision(state: AgentState) -> str:
    """
    Determines which branch of the graph to execute
    based on the router output.
    """
    return state["route"]


# Create graph
graph = StateGraph(AgentState)

# Register nodes
graph.add_node("router", router_node)
graph.add_node("sql", sql_node)
graph.add_node("rag", rag_node)
graph.add_node("hybrid", hybrid_node)
graph.add_node("synthesis", synthesis_node)

# Entry point
graph.set_entry_point("router")

# Conditional routing
graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "SQL": "sql",
        "RAG": "rag",
        "HYBRID": "hybrid",
    },
)

# Route all execution paths to synthesis
graph.add_edge("sql", "synthesis")
graph.add_edge("rag", "synthesis")
graph.add_edge("hybrid", "synthesis")

# End workflow
graph.add_edge("synthesis", END)

# Compile graph
workflow = graph.compile()


def run_workflow(question: str) -> dict:
    """
    Executes the LangGraph workflow.

    Args:
        question: User question

    Returns:
        Final workflow state
    """

    initial_state: AgentState = {
        "question": question,
        "route": None,
        "sql_result": None,
        "rag_result": None,
        "final_answer": None,
        "error": None,
    }

    result = workflow.invoke(initial_state)

    return result