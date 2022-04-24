from pyrogram import Client
from .functions import get_member_info, send_message, change_username, login

mobile = input('Please Enter Your PhoneNumber : ')
app_id = ''
hash_id = ''
app = Client(session_name=str(mobile) , api_id = app_id , api_hash = hash_id)
##########################
def get_action() : 
    action = input('What do you want to do : \n 1.Login \n 2.Send message to chat \n 3.Change chat username \n 4.Get members informations from chat \n 5.Check BOT status \n 6.shutdown \nplease just enter the number : ')
    return action
##########################
def do_action(action) :
    if action == '1' :
        login(app,mobile)
    elif action == '2' :
        send_message(app)
    elif action == '3' :
        change_username(app)
    elif action == '4' :
        get_member_info(app)
##########################
def start():
    action = get_action()
    while action != '6' :
        do_action(action)
        action = get_action()

start()