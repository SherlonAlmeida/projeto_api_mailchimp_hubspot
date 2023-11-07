"""import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "1b8fa1c47faf718dc31ae1ad220f2f25-us21",
    "server": "YOUR_SERVER_PREFIX"
  })

  response = client.root.get_root()
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))"""

"""from mailchimp_marketing import Client

mailchimp = Client()
mailchimp.set_config({
  "api_key": "YOUR_API_KEY",
  "server": "YOUR_SERVER_PREFIX"
})

response = mailchimp.ping.get()
print(response)"""

import tkinter