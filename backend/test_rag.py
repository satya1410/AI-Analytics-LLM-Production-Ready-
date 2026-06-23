from app.agents.rag_agent import RAGAgent


agent = RAGAgent()

result = agent.answer(
    "What is the refund policy?"
)

print(result)