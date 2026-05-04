from fastapi import BackgroundTasks

def process_order(order_id: int):
    print(f"Processing order {order_id}")
