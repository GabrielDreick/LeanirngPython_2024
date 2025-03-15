# todo

# class ShopItem:
#     def __init__(self, name='<unnamed>', price=000.00, utility=0, description="<undefined>"):
#         self.name = name
#         self.price = price
#         self.utility = utility
#         self.description = description.format(self.utility)
class ShopItem:

    def __init__(self, name='<unnamed>', price=000.00, utility=0, description="<undefined>"):
        self.dict = {"name": name, "price": price, "utility": utility, "description": description}

    def name(self):
        x = len(self.dict["name"]) + 1
        return f'\033[4m {self.dict["name"]:{x}}\033[m'

    def pricetag(self):
        return f'\033[48;2;60;60;60m${self.dict["price"]:.2f}\033[m'

    def price(self, price):
        self.dict["price"] = price
        return self.dict


apple = ShopItem("Apple",
                 1.2,
                 2,
                 "A delicious apple. Restores 2 hp")

empty_bottle = ShopItem('Empty Bottle',
                        20,
                        1,
                        "An empty bottle. Useful to store something.")

upgrade_module_m = ShopItem("Upgrade module",
                          300,
                          1,
                          "An upgrade module used to upgrade stuff")


upgrade_module_e = ShopItem("Upgrade module",
                          300,
                          1,
                          "An upgrade module used to upgrade stuff")

list_store_manacai = [apple, empty_bottle, upgrade_module_m.price(400)]
list_store_esterlia = [apple, empty_bottle, upgrade_module_e.price(700)]
while True:
    go_to = str(input('[1] Manacai store\n'
                      '[2] Esterlia store\n'
                      'Which store?\n'
                      '>')).strip().upper()

    if go_to in ["1", "MANACAI"]:

        print("┌───────────────┐\n"
              "│ Manacai Store │\n"
              "├───────────────┘")
        for item in list_store_manacai:
            print(f'│{item.name():<25}\t{item.pricetag():} - {item.dict["description"]}')


    elif go_to in ["2", "ESTERLIA"]:
        print("┌────────────────┐\n"
              "│ Esterlia Store │\n"
              "├────────────────┘")
        for item in list_store_esterlia:
            print(f'│{item.name():<25}\t{item.pricetag():} - {item.dict["description"]}')
