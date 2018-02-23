# OSX Mail HTML Signature Updater

## Why?
OSX Mail's signature handling is abysmal. This is our attempt to fix it (and also automate our signature rollout across the office).

## What?
This is a simple python script that will download an HTML file to replace the content of your Mail signature with the HTML file. To make this work, you'll need to store the signature HTML on a server somewhere - i wrote a PHP script that accepts a username as an argument and outputs the company signature with the correct name. You can see the sample PHP file in the resources/ directory
