import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send(filename):


	from_add='xxx@gmail.com'#header
	to_add="yyy@gmail.com"#header
	subject="Finance Stock Report"# header
	  
	msg=MIMEMultipart()
	msg["From"] = from_add
	msg["To"] = to_add
	msg["Subject"] = subject


	body=" <b> Today's Finance Report Attached </b>"
	msg.attach(MIMEText(body,"html"))

	my_file = open(filename, "rb")

	part=MIMEBase("application","octet-stream")
	part.set_payload((my_file).read())
	encoders.encode_base64(part)
	part.add_header("Content-Dispostion","attachment; filename= " + filename)
	msg.attach(part)

	message = msg.as_string()

	server = smtplib.SMTP("smtp.gmail.com", 587)#to make an object(host in parameters, we are using gmail therefore host from google)
	server.starttls()#to make server secure 
	server.login(from_add,"xyz")


	server.sendmail(from_add,to_add, message)

	server.quit()