from typing import List

from partner_tools.cli.interactive.question_wrapper import ask, QuestionType
from partner_tools.models import Customer


def get_customer(customers: List[Customer]):
    choices = [f'{customer.companyProfile.companyName} - ({customer.id})'
               for customer in customers]

    resp = ask(QuestionType.select,
               "Please select a customer:",
               choices=choices)

    customer = [x for x in customers
                if f'{x.companyProfile.companyName} - ({x.id})' == resp][0]
    return customer
