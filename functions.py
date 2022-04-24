import re
###################################################
#Regex:
r_id = '(?<![\w\d])id\\\":(?![\w\d])(.*)'
r_username = '(?<![\w\d])username\\\":(?![\w\d])(.*)'
r_firstname = '(?<![\w\d])first_name\\\":(?![\w\d])(.*)'
r_lastname = '(?<![\w\d])last_name\\\":(?![\w\d])(.*)'
r_file_id = '(?<![\w\d])file_id\\\":(?![\w\d])(.*)'
r_file_unique_id = '(?<![\w\d])file_unique_id\\\":(?![\w\d])(.*)'
###################################################
#Func to get member's informations :
def get_member_info(app) :
    try :
        app.start()
        chat_id =  str(input("Enter chat ID"))
        members = app.get_chat_members(chat_id=chat_id)
        for member in members :
            id = re.search(r_id , str(member))
            username = re.search(r_username,str(member))
            first_name = re.search(r_firstname , str(member))
            last_name = re.search(r_lastname,str(member))
            if username == None :
                print('username : ' + str(username))
            else :
                print('username : ' + str(username).split(',')[2].split(':')[1])
            if first_name == None :
                print('first_name : ' + str(first_name))
            else :
                print('first_name : ' + str(first_name).split(',')[2].split(':')[1])
            if last_name == None :
                print('last_name : ' + str(last_name))
            else :
                print('last_name : ' + str(last_name).split(',')[2].split(':')[1])
            print('id : ' + str(id).split(',')[2].split(':')[1])
            app.stop()
    except :
        print('Failed to get members informations')
###################################################
#Func to change username :
def change_username(app) :
    app.start()
    try: 
        chat_id =  str(input("Enter chat ID"))
        username = input('Enter your username : ')
        app.update_chat_username(chat_id=chat_id , username=username)
        app.stop()
        print('Username Changed')
    except:
        app.stop()
        print('Failed to change username')
###################################################
#Funcs for Login :
def enter_phone(app,mobile) : 
        phone = mobile
        sent_code = app.send_code(phone)
        phone_code_hash = sent_code.phone_code_hash
        return phone_code_hash
##########
def get_code() :
    code = input('Please Enter Code : ')
    return code
##########
def get_password():
    password = input('Please Enter Your Password : ')
    return password
##########
def enter_code(app,code,phone,phone_code_hash,verify) :
    app.sign_in(phone_number = phone, phone_code_hash = phone_code_hash, phone_code=code)
##########
#Main Func
def login(app,mobile) :
    try :
        app.connect()
        phone = mobile
        hash = enter_phone(phone)
        code = get_code()
        status = input('Do You Have Two Auth Password? y/n : ')
        if status.lower() == 'y':
            verfy_code = get_password()
            app.check_password(verfy_code)
        enter_code(code,phone,hash)
        app.disconnect()
        return 'Logged in'
    except :
        return 'Failed to Login'
###################################################
#Funcs to send message :
#1
def send_text_message(app,chat_id) :
    text = input('Enter you text message : ')
    app.send_message(chat_id,text)
#2
def send_photo(app,chat_id) :
    try:
        photo = input('Enter you photo path : ')
        caption = input('Enter you caption for this photo : ')
        send = app.send_photo(chat_id,photo=photo,caption=caption)
        file_id = re.search(r_file_id,str(send))
        file_unique_id = re.search(r_file_unique_id,str(send))
        print('File ID : ' + str(file_id).split(',')[2].split(':')[1])
        print('File unique ID : ' + str(file_unique_id).split(',')[2].split(':')[1])
    except :
        print('Failed to send photo')
#3
def send_video_file(app,chat_id) :
    try:
        video = input('Enter your video path : ')
        caption = input('Enter your caption : ')
        filename = input('Enter filename : ')
        send = app.send_video(chat_id=chat_id , video=video , caption=caption , file_name=filename)
        file_id = re.search(r_file_id,str(send))
        file_unique_id = re.search(r_file_unique_id,str(send))
        print('File ID : ' + str(file_id).split(',')[2].split(':')[1])
        print('File unique ID : ' + str(file_unique_id).split(',')[2].split(':')[1])
    except :
        print('Failed to send video file')
#4
def send_video_message(app,chat_id) :
    try:
        video = input('Enter your video message path : ')
        app.send_video_note(chat_id=chat_id , video_note= video)
        print('Video message sent')
    except :
        print('Failed to send video message')
#5
def send_gif_message(app,chat_id) :
    try:
        animation = input('Enter your animation path : ')
        caption = input('Enter your caption : ')
        app.send_animation(chat_id=chat_id , animation=animation , caption=caption)
        print('Gif message sent')
    except :
        print('Failed to gif message')
#6
def send_document_file(app,chat_id) :
    try:
        document = input("Enter your document path : ")
        caption = input("Enter your caption : ")
        file_name = input("Enter name for file : ")
        send = app.send_document(chat_id=chat_id , document=document , file_name=file_name , caption=caption)
        file_id = re.search(r_file_id,str(send))
        file_unique_id = re.search(r_file_unique_id,str(send))
        print('File ID : ' + str(file_id).split(',')[2].split(':')[1])
        print('File unique ID : ' + str(file_unique_id).split(',')[2].split(':')[1])
    except :
        print('Failed to send document') 
#7  
def send_audio_file(app,chat_id) :
    try :
        audio = input("Enter your audio path : ")
        caption = input("Enter your caption : ")
        file_name = input("Enter name for file : ")
        send = app.send_audio(chat_id=chat_id , audio=audio , caption=caption , file_name=file_name)
        file_id = re.search(r_file_id,str(send))
        file_unique_id = re.search(r_file_unique_id,str(send))
        print('File ID : ' + str(file_id).split(',')[2].split(':')[1])
        print('File unique ID : ' + str(file_unique_id).split(',')[2].split(':')[1])
    except :
        print('Failed to send Audio message')
#8
def send_voice_message(app,chat_id) :
    try :
        voice = input('Enter your voice message path : ')
        app.send_voice(chat_id=chat_id , voice=voice)
        print('Voice message sent')
    except : 
        print('Failed to send voice message')
#Main Func :
def send_message(app):
    app.start()
    chat_id = input('Enter chat ID : ')
    kind = input('Witch kind of message you want to send : \n 1.text \n 2.photo \n 3.video file \n 4.video message \n 5.gif \n 6.document \n 7.audio file \n 8.voice message \nplease just enter number : ')
    if   kind == '1' :
        send_text_message(app,str(chat_id))
    elif kind == '2' :
        send_photo(app,str(chat_id))
    elif kind == '3' : 
        send_video_file(app,str(chat_id))
    elif kind == '4' :
        send_video_message(app,str(chat_id))
    elif kind == '5' :
        send_gif_message(app,str(chat_id))
    elif kind == '6' :
        send_document_file(app,str(chat_id))
    elif kind == '7' :
        send_audio_file(app,str(chat_id))
    elif kind == '8' :
        send_voice_message(app,str(chat_id))
    app.stop()
###################################################
def check_info(app) :
    try : 
        app.send_message(chat_id="me", text="Hi there!") 
        print('Bot is up')
    except :
        print('Bot is down try to login again')