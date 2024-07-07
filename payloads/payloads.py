def create_booking_payload(
        firstname="John", 
        lastname="Doe", 
        totalprice=22222, 
        depositpaid=True, 
        checkin="2124-01-01", 
        checkout="2124-01-02", 
        additionalneeds="All inclusive"
    ):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }

def update_booking_payload(
        firstname="Jane", 
        lastname="Doe", 
        totalprice=22222, 
        depositpaid=False, 
        checkin="2124-11-01", 
        checkout="2124-11-02", 
        additionalneeds="Pool and sauna"
    ):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }