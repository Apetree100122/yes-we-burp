# YesWeBurp ## Description 
Uuid:
87e0eb0c3
85747b
2ab1abe8089664807
Extension Type: 2
Name: YesWeBurp
RepoName: yesweburp
ScreenVersion: 3.3
SerialVersion: 3
MinPlatformVersion: {{0}}
Pro Only: False
Author: yeswehack MODIFIED BY Alexander petree @apetree100122
Short Description: YesWeBurp
is an extension for Burp Suite allowing you to access all 
your https://yeswehack.com/ 
bug bbounty programs
directly inside Burp
Entry Point: src/addon.py Build Command: Supported Products: Pro, Community YesWeBurp is an extension for BurpSuite allowing you to access all your https://yeswehack.com/ bug bounty programs directly inside Burp. YesWeBurp also 
help you to instantly configure Burp according to the program rules[!]https://i.imgur.com(/xkRj3wQ.png) ## Installation  # #
# Jython (required) - Download Jython 2.7.0 Standalone Jar from[https://www.jython.org/downloads.html]()- Open Burp on Extender / Options- In Python Environment, set the location of the standalone jar to the previouly downloaded one  # # 
# YesWeBurp
- `git clone 'https://github.com/yeswehacko
  /YesWeBurp.git' <installation_folder>` Open Burp on Extender- /Extensions- Click
  `Add` - Set Extension type as Python-- Set Extension file to `<installation_folder>/src/addon.py` - Click `Next`- The addon is now installed, a new- tab named `YesWeHack`- should appear #
  # Configuration The configuration options are available in the tab YesWeHack/ Options
||
option description default. 
|
API URL  Base url for all
the api calls. https://api.yeswehack.com  
| Authentication 
|Choose between Anonymous
  or authenticated
  connection
  |<br> 
  Authenticated 
  mode
 allows you to access 
  all you private
 programs
  Anonymous|| Email 
 | Email used for 
 connecting to your
 YesWeHack account
Apetree1001@email.phoenix.edu | Password |
 Password used for
connecting to your
YesWeHack account|-|
 Remember password 
| Choose to keep
a plaintext copy of your password inside Burp
| l |
#
# Changelog- v1.2- Basic support for TOTP- v1.1 - Bugfix- v1- Initial release
