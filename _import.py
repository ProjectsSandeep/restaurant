import csv
from orders.models import MenuPrice, Category, Topping, Topping_qty, Size, Price_List, Item_List

def import_menu_prices_from_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        for category, name, topping_qty, size, price in reader:
            category_obj = Category.objects.get(pk=category)
            if topping_qty == "" and size == "":
                product = MenuPrice(category=category_obj, name=name, topping_qty=None, size=None, price=price)
            elif topping_qty == "":
                product = MenuPrice(category=category_obj, name=name, topping_qty=None, size=Size.objects.get(pk=size), price=price)
            else:
                product = MenuPrice(category=category_obj, name=name, topping_qty=Topping_qty.objects.get(pk=topping_qty), size=Size.objects.get(pk=size), price=price)
            product.save()

def import_toppings_from_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        for name in reader:
            topping = Topping(name=name)
            topping.save()

def import_price_list_from_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        for name, base_price, large_supp in reader:
            product = Price_List(name=name, base_price=base_price, large_supp=large_supp)
            product.save()

def import_item_list_from_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        for category, name, base_price_id in reader:
            product = Item_List(category=Category.objects.get(pk=category), name=name, base_price_id=Price_List.objects.get(pk=base_price_id))
            product.save()

if __name__ == "__main__":
    import_menu_prices_from_csv("products.csv")
    import_toppings_from_csv("toppings.csv")
    import_price_list_from_csv("pricelist.csv")
    import_item_list_from_csv("itemlist.csv")
