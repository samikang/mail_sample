#!/bin/env python3
# ---------------------- ----------- #
# Description: The mail package
# Author : samikang
# Date   : 11/9/2015
# Email  : xiangxiangster@hotmail.com
# ------------------------------------------------------------ #

import smtplib
import os.path
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class Mail:
    MAIL_SERVER = '10.0.11.28'##user input
    FROM = 'qa@google.com'##user input
    DOMAIN_NAME = 'google.com'##user input

    TEMPLATE = dict()
    TEMPLATE['SAM_TEST_REPORT'] = ['sample_report.eml', 'Test Report: {HOST_NAME}:{TEST_BED}: {MODEL_NAME}-{FW_VERSION}']
    TEMPLATE['SAM_ERR_REPORT'] = ['sample_error.eml', 'Test Error: {HOST_NAME}:{TEST_BED}: {MODEL_NAME}-{FW_VERSION}']
      
    def __init__(self, template, mail_info):
        self._msg = MIMEMultipart()
        self._msg['From'] = Mail.FROM
        subject = Mail.TEMPLATE[template][1].format_map(mail_info)
        self._msg['Subject'] = subject
        self._msg['To'] = Mail.generate_recipient_addr(mail_info['RECEIPIENT'])
        
        path = (os.path.dirname(os.path.abspath(__file__)))
        eml_file = os.path.join(path, Mail.TEMPLATE[template][0])
        with open(eml_file) as f:
            content = f.read()
                    
        body_idx = content.find('<body')
        if body_idx != -1:
            head_end = body_idx - 1
            head = content[0:head_end]
            body = content[body_idx:-1]
            body = body.format_map(mail_info)
            content = '{}{}'.format(head, body)

        # This is the textual part:
        part = MIMEText(content, _subtype='html')
        self._msg.attach(part)
    
        # This is the attachment:
        if 'ATTACHMENT' in mail_info.keys():
            files = mail_info['ATTACHMENT']
            for file in files:
                try:
                    with open(file,'rb') as f:
                        data = f.read()
                    part = MIMEApplication(data)
                    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                    self._msg.attach(part)  
                except FileNotFoundError as e:
                    print(e)
       
        
    def send(self):
        try:
            with smtplib.SMTP(host=Mail.MAIL_SERVER, timeout=5) as smtp:
                print('Send email to {}'.format(self._msg['To']))
                smtp.send_message(self._msg)
        except ConnectionRefusedError as e:
            print('Error captured when sending email: {}'.format(e))     

    @staticmethod
    def generate_recipient_addr(recipients):
        mail_addr = list()
        for recipient in recipients:
            mail_addr.append('{}@{}'.format(recipient, Mail.DOMAIN_NAME))
        return ','.join(mail_addr)
