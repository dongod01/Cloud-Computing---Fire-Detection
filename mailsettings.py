DEBUG = True
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'firedetect.kgp@gmail.com'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_ASCII_ATTACHMENTS = True

#updated July 23
MAIL_PASSWORD = None

with open('C:/Users/DELL/Desktop/Codes/Info/firedetect_info.txt') as file:
        MAIL_PASSWORD = file.readlines()[1]
        # Copying app pw from another dir
