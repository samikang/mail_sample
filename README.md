# mail_sample


Python 3.4 or newer

This is an example of how to use REST to access a server

This is Class, can integrate to other python3 platform

for example:
	mail_info['RECEIPIENT'] = 'test_rec'
	mail_info['HOST_NAME'] = '10.0.11.11'
	mail_info['TEST_BED'] = 'testbed'
	mail_info['MODEL_NAME'] = 'model'
	mail_info['FW_VERSION'] = 'version'
	mail_info['BRANCH_NUM'] = 'branch'
	mail_info['START_TIME'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
	mail_info['STOP_TIME'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
	mail_info['ERROR_MSG'] = 'error_msg'
	m = mail.Mail('CDR_ERR_REPORT', mail_info)
	m.send()
