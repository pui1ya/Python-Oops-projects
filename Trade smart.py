# File to store all products
open("product_list.txt", "a").close()

# Wholesale stock maintenance
class stock_maintenance:

    def __init__(self, new_product='', old_product=''): # Constructor
        self.new_product = new_product
        self.old_product = old_product

    def add_product(self): # To add new product
        with open("product_list.txt", "a") as f:
            f.write(self.new_product + '\n')

        print('Product added successfully')
        view_file = input('Do you wish to see the product list (y/n): ').strip().lower()
        if view_file == 'y':
            with open("product_list.txt", "r") as f:
                content = f.read()
                print('Product list:\n', content)
        else:
            return

    def remove_product(self): # To remove a product
        with open("product_list.txt", "r") as f:
            lines = f.readlines()
        found = False
        
        with open("product_list.txt", "w") as f:
            for line in lines:
                if line.strip().lower() != self.old_product.lower():
                    f.write(line)  # Remove the product and prints everything except it
                else:
                    found = True

        if found:
            print(f"Product '{self.old_product}' removed successfully.")
        else:
            print(f"Product '{self.old_product}' not found in the product list.")

        view_file = input('Do you wish to see the product list (y/n)? ').strip().lower()
        if view_file == 'y':
            with open("product_list.txt", "r") as f:
                content = f.read()
                print("Current Product List:\n" + content)
        else:
            return

class billing_system:

    def __init__(self):
        self.items = []
        self.item_costs = []

    def new_bill(self):
        
        open("bill.txt", "w").close()

        items_no = int(input("Enter the number of items: "))
        for _ in range(items_no):
            item = input("\nEnter the item: ")
            item_cost = int(input("\nEnter the price of this item: "))
            self.items.append(item)
            self.item_costs.append(item_cost)

            with open("bill.txt", "a") as f:
                f.write(f"Item: {item}, Cost: {item_cost}\n")

    def add_total(self):
        return sum(self.item_costs)

    def print_bill(self):
        with open("bill.txt", "r") as f:
            bill = f.read()
        print("Bill:\n", bill)
        print("Total amount is:", self.add_total())

def main():
    print('Welcome')
    operation = input('\nDo you want to add or remove a product or bill everything? ').strip().lower()

    if operation == 'add':
        product = input('Enter the product to be added: ').strip()
        manager = stock_maintenance(new_product=product)
        manager.add_product()

    elif operation == 'remove':
        product = input('Enter the product to be removed: ').strip()
        manager = stock_maintenance(old_product=product)
        manager.remove_product()

    elif operation == 'bill':
        bill_operation = input("Do you want to create a new bill? (yes/no): ").strip().lower()

        if bill_operation == 'yes':
            manager = billing_system()
            manager.new_bill()
            manager.print_bill()

        else:
            print('Exit')

    else:
        print('Please input correct operation (add/remove/bill)')

if __name__ == "__main__":
    main()
