from typing import TypedDict


class CompanyProfile(TypedDict):
    address: str
    email: str
    companyName: str
    domain: str
    tenantId: str


class Customer(TypedDict):
    """
    Represents a customer, there are more fields present
    """
    id: str  # This is also the tenant ID
    companyProfile: CompanyProfile
