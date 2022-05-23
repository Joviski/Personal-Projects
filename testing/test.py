import paymob
from paymob.logging import log

paymob.secret_key= "sk_test_fc9856532ebc5c8b24a6c01721fb95132b3e9b477154c15b1ae533b702c2491c"

def secret():
    intent = paymob.accept.Intention.create(
        amount="150",
        currency="EGP",
        payment_methods=["card"],
        items= [
    {
        "name": "ASC1124",
        "amount": "50",
        "description": "Smart Watch",
        "quantity": "1"
    },
    {
        "name": "ERT6565",
        "amount": "100",
        "description": "Power Bank",
        "quantity": "1"
    }
    ],
        billing_data={
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Mohamed",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+201010101010",
            "shipping_method": "PKG",
            "postal_code": "01898",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah",
        },
        customer={
            "first_name": "youssef", "last_name": "tarek", "email": "youssef@tarek.com","phone_number":"+201010101010",
            "extras":{
                "surname":"Abdelsattar"
            }

        },
        delivery_needed=False,
        extras= {
            "name": "test",
            "age": "30"
        },
        #special_reference= "Special reference test 4"
    )
    log(
        "Intention Creation Response - {intent}".format(
            intent=intent
        ),
        "info",
    )
    return intent


print(secret())