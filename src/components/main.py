from payment_processor.services import payment_service
from payment_processor.models import Payment

def process_payment(card_number, expiration_date, cvv, amount):
    try:
        payment = Payment(
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
            amount=amount
        )
        payment_service.process_payment(payment)
    except ValueError as e:
        print(f"Error processing payment: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    card_number = input("Enter your card number: ")
    expiration_date = input("Enter your card expiration date: ")
    cvv = input("Enter your card cvv: ")
    amount = float(input("Enter the amount to pay: "))
    process_payment(card_number, expiration_date, cvv, amount)

if __name__ == "__main__":
    main()