from pydantic import BaseModel


class CompanyProfile(BaseModel):
    companyName: str
    domain: str
    tenantId: str


class Customer(BaseModel):
    """
    Represents a customer, there are more fields present
    """
    id: str  # This is also the tenant ID
    companyProfile: CompanyProfile
    relationshipToPartner: str
