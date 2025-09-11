class User:
    def __init__(self, name, contact):
        self._name = name  # Protected attribute for encapsulation
        self._contact = contact  # Protected sensitive info
        self.orders = []  # Instance attribute for user's orders

    def display_info(self):
        # Polymorphic method; overridden in subclasses
        return f"Name: {self._name}, Contact: {self._contact}"

    def place_order(self, *args):
        # Stub for polymorphism; implemented in Customer
        raise NotImplementedError("This method should be implemented in subclasses.")


class Customer(User):
    def __init__(self, name, contact, address):
        super().__init__(name, contact)
        self.address = address  # Instance attribute

    def display_info(self):
        # Polymorphism: Overrides base to add customer-specific info
        return f"Customer - {super().display_info()}, Address: {self.address}"

    def place_order(self, restaurant, items):
        # Instance method: Creates and places an order
        order = DeliverySystem.place_order(self, restaurant, items)
        self.orders.append(order)
        return order


class DeliveryPerson(User):
    def __init__(self, name, contact, vehicle):
        super().__init__(name, contact)
        self.vehicle = vehicle  # Instance attribute
        self.assigned_orders = []  # Orders assigned to this delivery person

    def display_info(self):
        return f"Delivery Person - {super().display_info()}, Vehicle: {self.vehicle}"

    def deliver_order(self, order):
        if order in self.assigned_orders:
            order.update_status("Delivered")
            order.restaurant.update_earnings(order.total_cost * 0.8)  # Restaurant earns 80%
            DeliverySystem.total_revenue += order.total_cost * 0.2  # System keeps 20%
            self.assigned_orders.remove(order)
            return "Order delivered successfully."
        return "Order not assigned to this delivery person."


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []  # List of FoodItem
        self._earnings = 0.0  # Private earnings

    def add_menu_item(self, item):
        self.menu.append(item)

    def get_menu(self):
        return [(item.name, item.price) for item in self.menu]

    def update_earnings(self, amount):
        self._earnings += amount

    def get_earnings(self):
        return self._earnings


class Order:
    def __init__(self, order_id, customer, restaurant, items):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.total_cost = self.calculate_total()
        self.status = "Pending"
        self.delivery_person = None

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def update_status(self, new_status):
        self.status = new_status


class DeliverySystem:
    users = {}  # Class attribute
    restaurants = []
    orders = []
    total_revenue = 0.0
    order_counter = 0

    @classmethod
    def register_user(cls, username, user):
        cls.users[username] = user

    @classmethod
    def add_restaurant(cls, restaurant):
        cls.restaurants.append(restaurant)

    @classmethod
    def place_order(cls, customer, restaurant, items):
        cls.order_counter += 1
        order = Order(cls.order_counter, customer, restaurant, items)
        cls.orders.append(order)
        return order

    @classmethod
    def assign_delivery(cls, order, delivery_person):
        order.delivery_person = delivery_person
        delivery_person.assigned_orders.append(order)
        order.update_status("Assigned")

    @classmethod
    def generate_report(cls):
        return {
            "Total Orders": len(cls.orders),
            "Total Revenue": cls.total_revenue,
            "Restaurant Earnings": {r.name: r.get_earnings() for r in cls.restaurants}
        }

    @staticmethod
    def calculate_delivery_fee(distance):
        return distance * 0.5  # $0.5 per unit distance


# -------------------- CLI Interface --------------------
def run_cli():
    print("Welcome to the Online Food Delivery System!")
    while True:
        print("\nOptions:")
        print("1. Register Customer")
        print("2. Register Delivery Person")
        print("3. Add Restaurant")
        print("4. Add Menu Item to Restaurant")
        print("5. Place Order")
        print("6. Assign Delivery")
        print("7. Deliver Order")
        print("8. Generate System Report")
        print("9. Display User Info")
        print("10. Calculate Delivery Fee")
        print("11. Exit")

        choice = input("Enter choice (1-11): ")

        try:
            if choice == "1":
                username = input("Enter username: ")
                if username in DeliverySystem.users:
                    print("Username already exists!")
                    continue
                name = input("Enter name: ")
                contact = input("Enter contact: ")
                address = input("Enter address: ")
                customer = Customer(name, contact, address)
                DeliverySystem.register_user(username, customer)
                print(f"Customer {name} registered successfully.")

            elif choice == "2":
                username = input("Enter username: ")
                if username in DeliverySystem.users:
                    print("Username already exists!")
                    continue
                name = input("Enter name: ")
                contact = input("Enter contact: ")
                vehicle = input("Enter vehicle type: ")
                delivery_person = DeliveryPerson(name, contact, vehicle)
                DeliverySystem.register_user(username, delivery_person)
                print(f"Delivery Person {name} registered successfully.")

            elif choice == "3":
                name = input("Enter restaurant name: ")
                restaurant = Restaurant(name)
                DeliverySystem.add_restaurant(restaurant)
                print(f"Restaurant {name} added successfully.")

            elif choice == "4":
                if not DeliverySystem.restaurants:
                    print("No restaurants available!")
                    continue
                print("Available restaurants:", [r.name for r in DeliverySystem.restaurants])
                restaurant_name = input("Enter restaurant name: ")
                restaurant = next((r for r in DeliverySystem.restaurants if r.name == restaurant_name), None)
                if not restaurant:
                    print("Restaurant not found!")
                    continue
                item_name = input("Enter food item name: ")
                item_price = float(input("Enter item price: "))
                restaurant.add_menu_item(FoodItem(item_name, item_price))
                print(f"Item {item_name} added to {restaurant_name}'s menu.")

            elif choice == "5":
                username = input("Enter customer username: ")
                customer = DeliverySystem.users.get(username)
                if not isinstance(customer, Customer):
                    print("Invalid customer username!")
                    continue

                print("Available restaurants:", [r.name for r in DeliverySystem.restaurants])
                restaurant_name = input("Enter restaurant name: ")
                restaurant = next((r for r in DeliverySystem.restaurants if r.name == restaurant_name), None)
                if not restaurant:
                    print("Restaurant not found!")
                    continue

                print("Menu:", restaurant.get_menu())
                item_names = input("Enter item names (comma-separated): ").split(",")
                items = [item for item in restaurant.menu if item.name.strip() in [name.strip() for name in item_names]]

                if not items:
                    print("No valid items selected!")
                    continue

                order = customer.place_order(restaurant, items)
                print(f"Order placed: ID {order.order_id}, Total: ${order.total_cost}, Status: {order.status}")

            elif choice == "6":
                order_id = int(input("Enter order ID: "))
                order = next((o for o in DeliverySystem.orders if o.order_id == order_id), None)
                if not order:
                    print("Order not found!")
                    continue
                username = input("Enter delivery person username: ")
                delivery_person = DeliverySystem.users.get(username)
                if not isinstance(delivery_person, DeliveryPerson):
                    print("Invalid delivery person username!")
                    continue
                DeliverySystem.assign_delivery(order, delivery_person)
                print(f"Order {order_id} assigned to {delivery_person._name}.")

            elif choice == "7":
                order_id = int(input("Enter order ID: "))
                order = next((o for o in DeliverySystem.orders if o.order_id == order_id), None)
                if not order or not order.delivery_person:
                    print("Order not found or no delivery person assigned!")
                    continue
                print(order.delivery_person.deliver_order(order))
                print(f"Order status: {order.status}")

            elif choice == "8":
                report = DeliverySystem.generate_report()
                print("System Report:")
                print(f"Total Orders: {report['Total Orders']}")
                print(f"Total Revenue: ${report['Total Revenue']}")
                print("Restaurant Earnings:", report['Restaurant Earnings'])

            elif choice == "9":
                username = input("Enter username: ")
                user = DeliverySystem.users.get(username)
                if not user:
                    print("User not found!")
                    continue
                print(user.display_info())

            elif choice == "10":
                distance = float(input("Enter distance (in units): "))
                fee = DeliverySystem.calculate_delivery_fee(distance)
                print(f"Delivery Fee: ${fee}")

            elif choice == "11":
                print("Exiting system. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 11.")

        except ValueError as e:
            print(f"Invalid input! Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_cli()
