import smtplib , ssl , csv ,time

def return_list(filepath):
    try:
        with open(filepath) as csvfile:
            datas = list(csv.reader(csvfile))
    except Exception  as e:
        print(e)
        return False
    emails = []
    for i in range(0, len(datas)):
        for ele in datas[i]:
            test = ""
            test += ele
        emails.append(test)
    print("The Email list Contains " + str(len(emails)) + " Entries")
    return emails

def sendMail(email,password,email_list,message) :
    try:
        context = ssl.create_default_context()
        print('Connecting to Server')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        print("Connected Successfully to smtp.gmail.com")
        print('Logging You In')
        server.login(email, password)
        print('Logged In Successfully\n Sending Emails')
        for single_email in email_list:

            try:
                server.sendmail(email, 'To:' + single_email, message)
                print('Email Successfully sent to : ' + email)
                time.sleep(10)
            except Exception as e:
                print(e)
                return False
        server.close()
        print("Task Completed Successfully")
        return True
    except Exception as ex:
        print("Error : " + str(ex))


print("\t\t\tWelcome to Batch Email Sender\n\t\t\tA Program by Shariq Khan")
email = input("Enter your Email Address : ")
password = input("Enter your Email Password: ")
filepath = input("Enter the path of your .csv file: ")
emailList = return_list(filepath)

while(emailList == False):
    filepath = input("Enter the path of your .csv file: ")
    emailList = return_list(filepath)



subject = input("Enter the Subject of your Email : ")
body = input("Copy/Paste the body of the Email here in ascii encoding / Plaintext format : ")
message = f"Subject: {subject} \n\n\n {body}"
message.encode('utf-8')


while(not sendMail(email,password,emailList,message)):
    print("Failed to Send Email . Please check any problems with internet. Try again? (Y/N) : ")
    if(input().lower() != "y"):
        print("Exiting...")
        exit()


