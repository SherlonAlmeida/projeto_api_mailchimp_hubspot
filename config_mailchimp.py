from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

#Obtém as credenciais do MailChimp (Para não ser publicada na Web e ser Revogada)
from api_settings import *

#Integra com o arquivo do Hubspot
import config_hubspot

"""Apresenta os assinantes da lista desejada"""
def show_list_members(data):
  for member in data["members"]:
    print(member["full_name"])


#O programa começa a partir daqui
try:
  client = Client()
  client.set_config({
    "api_key": "1b8fa1c47faf718dc31ae1ad220f2f25-us21",
    "server": "us21"
  })

  #Obtem todas as listas (Identificar o id da lista desejada)
  #response = client.lists.get_all_lists()
  #print(response)

  #Obtem os membros assinantes da lista: https://mailchimp.com/developer/marketing/api/list-members/list-members-info/
  response = client.lists.get_list_members_info("b7523b0850")
  show_list_members(response)

  #TO DO: criar funções de integração com o hubspot
  config_hubspot.add_new_member_to_hubspot(response)


except ApiClientError as error:
  print("Error: {}".format(error.text))