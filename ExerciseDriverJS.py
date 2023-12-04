from ProgramExerciseJS import FoodOrder 
def create_order_list():
    order_list = []
    num_items = int(input("Enter the number of items to purchase: "))
    
    while num_items < 1:
        print("Please enter a valid number greater than or equal to 1.")
        num_items = int(input("Enter the number of items to purchase: "))
    
    for _ in range(num_items):
        food_name = input("Enter the name of the item: ")
        amount = float(input("Enter the amount of the item in pounds: "))
        
        while amount <= 0:
            print("Please enter a valid amount greater than 0.")
            amount = float(input("Enter the amount of the item in pounds: "))
        
        order = FoodOrder(food_name, amount)
        order_list.append(order)
    
    return order_list

def display_order_list(order_list):
    print("\nOrder List:")
    for order in order_list:
        print(f"\nFood Name: {order.get_food_name()}")
        print(f"Amount in Pounds: {order.get_amount_in_pounds()}")
        print(f"Standard Price per Pound: ${order.get_standard_price_per_pound():.2f}")
        calculated_price = order.get_calculated_price()
        if calculated_price is not None:
            print(f"Calculated Price: ${calculated_price:.2f}")
        else:
            print("Unable to calculate price.")

def calculate_total_cost(order_list):
    total_cost = 0  
    for order in order_list:
        calculated_price = order.get_calculated_price()
        if calculated_price is not None:
            total_cost += float(calculated_price)
    return total_cost 


def main():
    orders = create_order_list()
    display_order_list(orders)
    total_cost = calculate_total_cost(orders)
    print(f"\nTotal Cost of All Items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
