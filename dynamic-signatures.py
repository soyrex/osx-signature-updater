#!/usr/bin/python
import sys
import re
import pwd
import os
import glob
import plistlib
import urllib2

####################################################################
####################################################################
# Configuration:
####################################################################
sigs = {
       'Test': 'http://yourdomain.com/sigs/?name=%s'
}
####################################################################
# End Configuration.
####################################################################
####################################################################

# Get the current username:
username = pwd.getpwuid(os.getuid()).pw_name
home = os.path.expanduser("~")


def process_dir(path):
    """
    process a directory and check for matching signatures.
    """
    # Read the plist:
    plist = plistlib.readPlist('%s/AllSignatures.plist' % path)
    # loop my config items:
    for my_sig,url in sigs.items():
        # loop each plist item:
        for sig in plist:
            if re.match(r'%s' % my_sig, sig['SignatureName']):
                # get the UID:
                uid = sig['SignatureUniqueId']

                # get the remote url and sub in the username:
                full_url = url % username

                # Build a request (adding header support to avoid cloudflare etc):
                q = urllib2.Request(full_url)
                q.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36')

                # Read the HTML:
                f = urllib2.urlopen(q)
                html = f.read()

                # Prepare the target file and write the HTML out:
                target_file = '%s/%s.mailsignature' % (path,uid)
                os.system('chflags nouchg "%s"' % target_file)

                sig_file = open(target_file,'w')
                sig_file.write(html)
                sig_file.close()

                os.system('chflags uchg "%s"' % target_file)

                f.close()



# Now run the process function on each
# matching path. This will be done against
# both the Mobile Documents and the standard
# configuration location. This is because 
# I can't figure out how to determine
# which directory is actually in use, so we 
# just clobber both! :)

# We run this on the latest V in Mobile Documents:
if os.path.exists('%s/Library/Mobile Documents/com~apple~mail/Data/' % home):
    # checking the mobile docs locaation
    dirs = sorted(glob.glob('%s/Library/Mobile Documents/com~apple~mail/Data/V*' % (home)))[::-1]
    full_path = dirs[0]+'/Signatures'
    process_dir(full_path)

# We also run it on the standard Mail data area.
if os.path.exists('%s/Library/Mail/' % home):
    # checking the mobile docs locaation
    dirs = sorted(glob.glob('%s/Library/Mail/V*' % (home)))[::-1]
    full_path = dirs[0]+'/MailData/Signatures'
    process_dir(full_path)

