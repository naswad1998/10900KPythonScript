import bs4, requests, smtplib, time

def sendEmail():
    #Message to be sent
    message = "10900k in stock at Memory Express!"
    #initialize connection to Gmail
    conn = smtplib.SMTP('smtp.gmail.com', 587) 
    #Start TLS encryption
    conn.starttls() 
    #Login to Gmail
    conn.login('yourEmailGoesHere', 'yourPasswordGoesHere')
    #Send email; change SenderEmail and RecieverEmail as you like
    conn.sendmail('SenderEmail', 'RecieverEmail', message)
    #End connection
    conn.quit()
    print('Email Sent')
    
def getStatus():
    #Run forever
    while True:
        #open web page of product
        getPage = requests.get('ProductURLGoesHere')
        
        #initialize the HTML parser that will search the HTML content of the web page
        #Nothing to change here
        item = bs4.BeautifulSoup(getPage.text, 'html.parser')
        
        #Select the content of the class that contains the stock availability
        #Check article on how to find name of this class
        stock = item.select(".InventoryState_InStock")
        
        #return length of stock, if 0, item is out of stock, otherwise, at least 1 in stock
        #This part is also specific to the retailer I chose, but you should have a similar if-statement to check when to send the email.
        if len(stock) != 0:
            #send email
            sendEmail()
        #delay 10 seconds
        time.sleep(10)    
            
#Run the loop        
getStatus()
