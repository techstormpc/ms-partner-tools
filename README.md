# MS Partner Tools
![](https://img.shields.io/pypi/v/ms-partner-tools.svg)

Wrapper for the Microsoft Partner Center REST API.

Supports Python 3.8.

Currently, only adding devices to Autopilot is supported and the Device code authentication flow.

## Installation

`pip install ms-partner-tools`

## App Registration

Under App registrations -> API permissions, add the Microsoft Partner Center `user_impersonation` permission.
You can search for it under "APIs my organization uses".
Please note that this only supports delegated permissions, not application permissions.

The device code flow requires the "Allow public client flows" option to be turned on. This needs a client secret.

If the interactive auth flow is used, you must add the "Mobile and desktop applications" platform and set the "Redirect URI" to `http://localhost:8400`.

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