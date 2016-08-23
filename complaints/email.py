from django.core.mail import send_mail
 

complaint_message = 'Thank you for your complaint. Your complaint no is c4561101. In 24 hrs your complaint will be asssigned to head of department. By- XYZ Hospital'
assign_message = 'Hey your complaint is assignged to mr xyz person of this xyz department . Will solve this ASAP . XYZ hospital'


def sendEmail():
	send_mail('Complaint Registered', complaint_message , 'pythonistvinay@gmail.com', ['vxixnxaxy@gmail.com'], fail_silently=False)










