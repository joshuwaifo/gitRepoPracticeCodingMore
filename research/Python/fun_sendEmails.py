import smtplib
import sys

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


def send_email_with_attachment(subject_type_str, body_text_type_str, to_emails_type_list, file_to_attach_type_str):
    """
    Send an email with an attachment
    """
    header_type_tuple = f"Content-Disposition", "attachment; filename={file_to_attach}"

    # extract server and from_addr from config
    host_type_str = "smtp.your_isp.com"
    from_addr_type_str = "o.j.uwaifo@gmail.com"

    # create the message
    msg_type_MIMEMultipart = MIMEMultipart()
    msg_type_MIMEMultipart["From"] = from_addr_type_str
    msg_type_MIMEMultipart["Subject"] = subject_type_str
    msg_type_MIMEMultipart["Date"] = formatdate(localtime=True)

    if body_text_type_str != "":
        msg_type_MIMEMultipart.attach(MIMEText(body_text_type_str))

    # connect each string item in the list in such a way that the result is one string where each (string) item is seperated by a column
    msg_type_MIMEMultipart["To"] = ", ".join(to_emails_type_list)

    attachment_type_MIMEBase = MIMEBase("application", "octet-stream")

    try:
        with open(file_to_attach_type_str, "rb") as fh_type_BufferedReader:
            data_type_bytes = fh_type_BufferedReader.read()
        attachment_type_MIMEBase.set_payload(data_type_bytes)
        encoders.encode_base64(attachment_type_MIMEBase)
        attachment_type_MIMEBase.add_header(*header_type_tuple)
        msg_type_MIMEMultipart.attach(attachment_type_MIMEBase)
    except IOError:
        msg_type_str = "Error opening attachment file %s" % file_to_attach_type_str
        print(msg_type_str)
        sys.exit(1)

    emails = to_emails_type_list

    # use a server host that works, I think the one defined above has an error

    server = smtplib.SMTP(host_type_str)
    server.sendmail(from_addr_type_str, emails, msg_type_MIMEMultipart.as_string())
    server.quit()

if __name__ == "__main__":
    emails_type_list = ["joshua@move.ai", "joshua.uwaifo@crover.tech"]

    subject_type_str = "Test email with attachment from Python"
    body_text_type_str = "This email contains an attachment!"
    path_type_str = "data/empire.jpg"
    send_email_with_attachment(subject_type_str, body_text_type_str, emails_type_list, path_type_str)

