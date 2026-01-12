from services.rag_service import rag_answer

while True:
    question = input("\nAsk a question (or 'exit'): ")
    if question.lower() == "exit":
        break

    answer = rag_answer(question, niche="restaurant")
    print("\nAnswer:\n", answer)