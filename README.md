# OSX Mail HTML Signature Updater

## Why?
OSX Mail's signature handling is abysmal. This is our attempt to fix it (and also automate our signature rollout across the office).

## What?
This is a simple python script that will download an HTML file to replace the content of your Mail signature with the HTML file. To make this work, you'll need to store the signature HTML on a server somewhere - i wrote a PHP script that accepts a username as an argument and outputs the company signature with the correct name. You can see the sample PHP file in the resources/ directory

## Installation
1. I put the python script into /usr/local/bin/
2. Create an Automator app that uses a shell script to call the python script.
3. Inside the Python script there's a CONFIG dictionary that. It is keyed with signature names and it's values are URLs to load for the HTML of that signature. You'll need to configure this.
3. Put the automator app into your user's startup (this should auto update your signature each time you login to OSX).

## WARNINGS
This has ONLY been tested on 6 machines in my office. It might explode. Use at your own risk, I accept NO responsibility.
