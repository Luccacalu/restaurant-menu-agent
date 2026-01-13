from services.query_planner import build_query_plan
from services.query_execution_service import execute_query_plan


def run_test(question: str, niche: str = "restaurant"):
    print("\n==============================")
    print("QUESTION:")
    print(question)

    plan = build_query_plan(question)

    print("\nQUERY PLAN:")
    print(plan)

    answer = execute_query_plan(
        question=question,
        niche=niche,
        plan=plan,
    )

    print("\nANSWER:")
    print(answer)
    print("==============================\n")


if __name__ == "__main__":
    run_test(
        "Give me the cheapest 5 vegan options with rice, no beans, that goes well with wine. Also, I hate bitter stuff."
    )
