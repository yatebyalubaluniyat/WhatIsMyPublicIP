from urllib import urlopen
import sys
import win32clipboard
try:
	out = urlopen('http://www.biranchi.com/ip.php').read()
	output = out[3:]
	print output
	
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(output)
	win32clipboard.CloseClipboard()
	print "IP has been copied to clipboard"
	
except:
	print "Check your internet connection"
	raw_input("Press enter to exit")
	sys.exit(0)
while True:
	pass