from typing import List

import questionary

from partner_tools.models import Customer


def get_customer(customers: List[Customer]):
    choices = [f'{customer["companyProfile"]["companyName"]} - ({customer["id"]})'
               for customer in customers]

    resp = questionary.select(
        "Please select a customer",
        choices=choices).ask()

    customer = [x for x in customers
                if f'{x["companyProfile"]["companyName"]} - ({x["id"]})' == resp][0]
    return customer
