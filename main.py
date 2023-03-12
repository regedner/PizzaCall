import csv
import datetime
import sub_class_pizza as sub_pizza
import sauce_class
import logging


def main():

    logging.basicConfig(
        filename='orders.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

    try:
        f = open("Menu.txt", "r", encoding="utf-8")
        print(f.read())

        pizza_menu = input('Choose your Pizza: ')

        if pizza_menu == "1":
            pizza = sub_pizza.ClassicPizza()
            print("You choosed Classic Pizza!")
        elif pizza_menu == "2":
            pizza = sub_pizza.MargheritaPizza()
            print("You choosed Margherita Pizza!")
        elif pizza_menu == "3":
            pizza = sub_pizza.TurkishPizza()
            print("You choosed Turkish Pizza!")
        elif pizza_menu == "4":
            pizza = sub_pizza.PlainPizza()
            print("You choosed Plain Pizza!")
        else:
            print('Error! Please enter a valid number')
            exit()

        sauces = []
        selected_sauces = set()

        while True:
            answer = input("Do you want to add sauce? (Y/N): ")
            if answer.lower() == "y":
                while True:
                    sauce_choice = input("Please choose a sauce (11-16): ")
                    if sauce_choice in {"11", "12", "13", "14", "15", "16"}:
                        if sauce_choice in selected_sauces:
                            print(
                                "You have already selected this sauce. Please choose another one.")
                            continue
                        else:
                            selected_sauces.add(sauce_choice)
                            if sauce_choice == "11":
                                my_sauce = sauce_class.Olive()
                            elif sauce_choice == "12":
                                my_sauce = sauce_class.Mushroom()
                            elif sauce_choice == "13":
                                my_sauce = sauce_class.GoatCheese()
                            elif sauce_choice == "14":
                                my_sauce = sauce_class.Meat()
                            elif sauce_choice == "15":
                                my_sauce = sauce_class.Onion()
                            elif sauce_choice == "16":
                                my_sauce = sauce_class.Corn()
                            sauces.append(my_sauce)
                            print("Your selected sauces are:")
                            for sauce in sauces:
                                print("-", sauce.description)
                            break
                    else:
                        print("Invalid choice. Please try again.")
            elif answer.lower() == "n":
                break
            else:
                print("Please give a valid answer.")

        account = pizza.get_cost()
        for sauce in sauces:
            account += sauce.get_cost()

        sauces_description = ", ".join(
            [sauce.get_description() for sauce in sauces])

        name = input('Please enter your name:')

        def validate_tc(tc):
            if len(tc) != 11 or tc[0] == "0" or not tc.isdigit():
                return False
            last_digit = int(tc[10])
            first_digits_sum = sum(map(int, tc[:10]))
            if first_digits_sum % 10 != last_digit:
                return False
            return True

        while True:
            tc = input(
                "Please enter your TC Identification Number (11 digits): ")
            if validate_tc(tc):
                break
            else:
                print(
                    "Invalid TC Identification Number. Please enter a valid 11-digit number.")

        def is_valid_credit_card(credit_card_number):
            cc_num_list = [int(num) for num in str(credit_card_number)[::-1]]
            doubled_second_digits = []
            for idx, num in enumerate(cc_num_list):
                if idx % 2 == 1:
                    doubled_second_digits.append(num*2)
                else:
                    doubled_second_digits.append(num)
            summed_digits = []

            for num in doubled_second_digits:
                if num < 10:
                    summed_digits.append(num)
                else:
                    summed_digits.append(1 + (num % 10))
            total = sum(summed_digits)
            return total % 10 == 0

        while True:
            credit_card_number = input(
                'Please enter your card number without spaces: ')
            if not credit_card_number.isnumeric():
                print("Invalid input. Please enter a numeric value.")
                continue
            if not is_valid_credit_card(credit_card_number):
                print("Invalid credit card number. Please try again.")
                continue
            break

        while True:
            exp_date_str = input(
                "Please enter your credit cards expiration date (MM/YY): ")
            try:
                exp_date = datetime.datetime.strptime(exp_date_str, "%m/%y")
                if exp_date < datetime.datetime.now():
                    print("You entered an expired card. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid date format. Please enter in MM/YY format.")

        while True:
            cvv = input("Please enter your credit cards CVV: ")
            if cvv.isdigit() and len(cvv) == 3:
                break
            else:
                print("Invalid CVV. Please try again.")

        date = datetime.datetime.now()
        date = date.strftime("%c")

        fields = ['pizza_type', 'name', 'id_card_no', 'card_number', 'exp_date',
                  'cvv', 'description', 'sauce_description', 'order_date', 'total_price']
        rows = [[pizza.__class__.__name__, name, tc, credit_card_number, exp_date_str,
                 cvv, pizza.get_description(), sauces_description, date, account]]

        filename = 'Orders_Database.csv'

        with open(filename, mode='a', newline='', encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            if csv_file.tell() == 0:
                writer.writerow(fields)
            writer.writerows(rows)

        logging.info('Order added successfully')
        print('Order is successful')

    except Exception as e:
        logging.error('Failed to add order: ' + str(e))
        print(f"An error occurred: {e}")


main()
