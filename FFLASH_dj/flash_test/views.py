from django.shortcuts import render,redirect

import paymob
from paymob.logging import log
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def secret(request):
    paymob.secret_key = 'sk_test_fc9856532ebc5c8b24a6c01721fb95132b3e9b477154c15b1ae533b702c2491c'
    if request.method == 'GET':
        intent = paymob.accept.Intention.create(
            amount="100000",
            currency="EGP",
            payment_methods=["card","valu","wallets"],
            items=[
                {
                    "name": "ASC1124",
                    "amount": "100000",
                    "description": "Smart Watch",
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
                "first_name": "youssef", "last_name": "tarek", "email": "youssef@tarek.com",
                "phone_number": "+201010101010",
                "extras": {
                    "surname": "Abdelsattar"
                }

            },
            delivery_needed=False,
            extras={
                "name": "test",
                "age": "30"
            },
            # special_reference= "Special reference test 4"
        )
        log(
            "Intention Creation Response - {intent}".format(
                intent=intent
            ),
            "info",
        )

        return JsonResponse({"client_secret": intent['client_secret']})



def index(request):
    if request.method == "GET":
        return render(request,'index.html')


# Create your views here.
def secret_live(request):
    paymob.secret_key = 'sk_live_248f6ca5e9a57e4074d845cb450acf46b3b979b174baa7d3caaa2cc7e576c169'
    if request.method == 'GET':
        intent = paymob.accept.Intention.create(
            amount="100",
            currency="EGP",
            payment_methods=[1982362,"card-moto","Wallets","Kiosk", "Card-Installment"],
            items=[
                {
                    "name": "ASC1124",
                    "amount": "100",
                    "description": "Smart Watch",
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
                "first_name": "youssef", "last_name": "tarek", "email": "youssef@tarek.com",
                "phone_number": "+201010101010",
                "extras": {
                    "surname": "Abdelsattar"
                }

            },
            delivery_needed=False,
            extras={
                "name": "test",
                "age": "30"
            },
            # special_reference= "Special reference test 4"
        )
        log(
            "Intention Creation Response - {intent}".format(
                intent=intent
            ),
            "info",
        )
        return JsonResponse({"client_secret": intent['client_secret']})



def index_live(request):
    if request.method == "GET":
        return render(request,'index_live.html')


def secret_sec(request):
    paymob.secret_key = 'sk_test_f234e71998de3547c083f00ad35ffa287e08a2cba7cc679b45ba16855daa4798'
    if request.method == 'GET':
        intent = paymob.accept.Intention.create(
            amount="100000",
            currency="EGP",
            payment_methods=["card"],
            items=[
                {
                    "name": "ASC1124",
                    "amount": "100000",
                    "description": "Smart Watch",
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
                "first_name": "youssef", "last_name": "tarek", "email": "youssef@tarek.com",
                "phone_number": "+201010101010",
                "extras": {
                    "surname": "Abdelsattar"
                }

            },
            delivery_needed=False,
            extras={
                "name": "test",
                "age": "30"
            },
            # special_reference= "Special reference test 4"
        )
        log(
            "Intention Creation Response - {intent}".format(
                intent=intent
            ),
            "info",
        )
        #print(intent)
        return JsonResponse({"client_secret": intent['client_secret']})



def index_sec(request):
    if request.method == "GET":
        return render(request,'index_sec.html')
