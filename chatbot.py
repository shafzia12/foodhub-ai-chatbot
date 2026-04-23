import os
from database import fetch_order

USE_OPENAI = False  # toggle

def get_response(user_input):
    if USE_OPENAI:
        return call_llm(user_input)
    else:
        return rule_based_response(user_input)

def rule_based_response(user_input):
    words = user_input.split()
    order_id = next((w for w in words if w.isdigit()), None)

    if order_id:
        order = fetch_order(order_id)
        if order:
            return f"Order {order[0]} is {order[2]} (ETA: {order[3]})"
        return "Order not found."

    return "Ask me about your order status."

def call_llm(prompt):
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content