from src.importer.entities import Category, Customer, Gender, Invoice, Payment, ShoppingMall, Payment, ShoppingMall
from src.importer.utils import CsvReader, DatabaseConnection


def save_category(data):
    # insert category
    with DatabaseConnection() as cursor:
        cursor.execute(
            "INSERT INTO category (category_id, category) VALUES(%s, %s)",
            [data.category_id, data.category]
        )


def save_gender(data):
    with DatabaseConnection() as cursor:
        # insert gender
        cursor.execute(
            "INSERT INTO gender(gender_id, gender) VALUES (%s, %s)",
            [data.gender_id, data.gender])


def save_customer(data):
    with DatabaseConnection() as cursor:
        # insert customer
        cursor.execute(
            "INSERT INTO customer (customer_id, customer_no, gender_id, age) VALUES(%s, %s, %s, %s)",
            [data.customer_id, data.customer_no, data.gender.gender_id, data.age]
        )


def save_payment(data):
    with DatabaseConnection() as cursor:
        # insert payment
        cursor.execute(
            "INSERT INTO payment(payment_id, payment_method, quantity, price) VALUES (%s, %s, %s, %s)",
            [data.payment_id, data.payment_method,data.quantity, data.price]
        )


def save_shopping_mall(data):
    with DatabaseConnection() as cursor:
        # insert shopping mall
        cursor.execute(
            "INSERT INTO shopping_mall(shopping_mall_id, shopping_mall) VALUES (%s,%s)",
            [data.shopping_mall_id, data.shopping_mall]
        )


def save_invoice(data):
    with DatabaseConnection() as cursor:
        # insert invoice
        cursor.execute(
            "INSERT INTO invoice (invoice_id, invoice_no, invoice_date, total, customer_id, payment_id, category_id, "
            "shopping_mall_id) VALUES(%s, %s, TO_TIMESTAMP(%s,'DD-MM-YYYY'), %s, %s, %s, %s, %s)",
            [data.invoice_id, data.invoice_no, data.invoice_date, data.total, data.customer.customer_id,
             data.payment.payment_id, data.category.category_id, data.shopping_mall.shopping_mall_id]
        )
    print("INSERTING ", data.invoice_no)


def main():
    categories = set()
    genders = set()
    customers = set()
    shopping_malls = set()

    with CsvReader('/csv/customer_shopping_data.csv') as reader:
        for row in reader:
            # Get category and check if already exists
            if not any(category_obj.category == row['category'] for category_obj in categories):
                category = Category(
                    row['category']
                )

                save_category(category)
                categories.add(category)
            else:
                for category_obj in categories:
                    if category_obj.category == row['category']:
                        category = category_obj
                        break

            # Get gender and check if already exists
            if not any(gender_obj.gender == row['gender'] for gender_obj in genders):
                gender = Gender(
                    row['gender']
                )

                genders.add(gender)
                save_gender(gender)
            else:
                for gender_obj in genders:
                    if gender_obj.gender == row['gender']:
                        gender = gender_obj
                        break

            # Get customer and check if already exists
            if not any(customer_obj.customer_no == row['customer_id'] for customer_obj in customers):
                customer = Customer(
                    row['customer_id'],
                    gender,
                    row['age']
                )

                customers.add(customer)
                save_customer(customer)
            else:
                for customer_obj in customers:
                    if customer_obj.customer_no == row['customer_id']:
                        customer = customer_obj
                        break

            # Get payment
            payment = Payment(
                row['payment_method'],
                row['quantity'],
                row['price']
            )

            save_payment(payment)

            # Get shopping mall and check if already exists
            if not any(shopping_mall_obj.shopping_mall == row['shopping_mall'] for shopping_mall_obj in shopping_malls):
                shopping_mall = ShoppingMall(
                    row['shopping_mall']
                )

                shopping_malls.add(shopping_mall)
                save_shopping_mall(shopping_mall)
            else:
                for shopping_mall_obj in shopping_malls:
                    if shopping_mall_obj.shopping_mall == row['shopping_mall']:
                        shopping_mall = shopping_mall_obj

            # Get invoice
            invoice = Invoice(
                row['invoice_no'],
                row['invoice_date'],
                row['total'],
                customer,
                payment,
                category,
                shopping_mall
            )

            # store data into database
            save_invoice(invoice)


if __name__ == "__main__":
    main()
