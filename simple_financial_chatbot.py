# simple_financial_chatbot.py

def simple_chatbot(user_query):
    revenue = "211.92 billion USD in 2024"
    net_income_change = "increased by 33.8% from 2023 to 2024"
    cfoa = "The cash flow from operating activities was 101.39 billion USD in 2024"
    liabilities = "Total liabilities were 222.54 billion USD in 2024"

    if user_query.lower() == "what is the total revenue?":
        return f"The total revenue is {revenue}."
    elif user_query.lower() == "how has net income changed over the last year?":
        return f"The net income has {net_income_change}."
    elif user_query.lower() == "what is the cash flow from operating activities?":
        return cfoa
    elif user_query.lower() == "what are the total liabilities?":
        return liabilities
    else:
        return "Sorry, I can only provide information on predefined queries."

if __name__ == "__main__":
    print("Welcome to the Financial Chatbot! Ask me one of the predefined questions.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}\n")
