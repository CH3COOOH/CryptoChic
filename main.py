import os
import sys
import getpass
import base64

from azstd import tui, enc
from azstd.ope import getch

if __name__ == '__main__':
	if '-n' in sys.argv:
		cmd = tui.ask_input_line('[CMD]', desc=None)
		pwd = getpass.getpass('[AUTH]\n> ')
		x_cmd = enc.encrypt_by_pwd(cmd.encode('utf-8'), pwd)
		print(base64.b64encode(x_cmd).decode('utf-8'))
	else:
		x_cmd = sys.argv[-1]
		pwd = getpass.getpass('')
		cmd = enc.decrypt_by_pwd(base64.b64decode(x_cmd.encode('utf-8')), pwd).decode('utf-8')
		os.system(cmd)
	getch.pause(message='Press any key to continue...')