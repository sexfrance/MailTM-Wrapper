from mailtmwrapper import MailTM
import time

def check_inbox(token):
    mail = MailTM(token) # Initialize mailTM token is optional

    # Wait a bit and check messages
    print("Checking messages...")
    time.sleep(2)
    messages = mail.get_messages()
    print(f"Messages: {messages}")

if __name__ == "__main__":
    mail = MailTM()  # Initialize mailTM
    
    # Create random account
    account = mail.create_account(email = None, password='test!')
    print(f"Created account: {account['address']}")
    
    # Get auth token
    token = mail.create_token(account['address'], password='test!')
    print(f"Got auth token: {token}...")
    

    check_inbox(token)