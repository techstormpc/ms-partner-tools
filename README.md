# MS Partner Tools

Wrapper for the Microsoft Partner Center REST API.

Supports Python 3.8.

Currently, only adding devices to Autopilot is supported and the Device code authentication flow.

## Installation

`pip install ms-partner-tools`

## App Registration

Need to add the Microsoft Partner Center user_impersonation permission under the API permissions tab.

The device code flow requires the "Allow public client flows" option to be turned on.

## Sample Usage


### CLI

```bash
$ partnertools-cli register-device
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code <CODE> to authenticate.
? Please select a customer: Test Customer - (00000000-0000-0000-0000-000000000000)
? Please select a device type: Surface Laptop 4 - Microsoft Corporation
? Please enter the serial number: 000000 

Device was added
```

### SDK

```python
import os
from partner_tools.auth import DeviceCode
from partner_tools import PartnerTools

client = PartnerTools(auth_info=DeviceCode(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    tenant_id=os.getenv('TENANT_ID')
))

customers = client.customer.get_customers()

for customer in customers:
    print(f'Customer: {customer["companyProfile"]["companyName"]}, Tenant ID: {customer["id"]}')
```