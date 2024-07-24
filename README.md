[![Deploy Jekyll with GitHub Pages dependencies preinstalled](https://github.com/Apetree100122/yes-we-burp/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/Apetree100122/yes-we-burp/actions/workflows/jekyll-gh-pages.yml)

# YesWeBurp Description YesWeBurp is an extension for
BurpSuite allowing you to access all your https://yeswehack.com/ bug bounty programs directly inside Burp. YesWeBurp also 
help you to instantly configure Burp according to the program rules.
![](https://i.imgur.com/xkRj3wQ.png) ## Installation  ### Jython (required) 
- Download Jython 2.7.0 Standalone Jar from [https://www.jython.org/downloads.html]()
- Open Burp on Extender / Options
- In Python Environment, set the location of the standalone jar to the previouly downloaded one  ### YesWeBurp
- `git clone 'https://github.com/yeswehacko
  /YesWeBurp.git' <installation_folder>` Open Burp on Extender
- / Extensions- Click `Add`
- Set Extension type as Python-
- Set Extension file to
 `<installation_folder>/src/addon.py`
- Click `Next`-
- The addon is now installed, a new
- tab named `YesWeHack`
- should appear ## Configuration
The configuration options are availablein the tab YesWeHack/ Options| option
|description|default|---------|-------------|---------|| API URL | Base url for all |the api calls. | https://api.yeswehack.com  |
| Authentication |Choose between
  Anonymous or authenticated
  connection.|<br>Authenticated mode
 allows you to access all you private
 programs. | Anonymous|
| Email | Email used for connecting to your YesWeHack account.|Apetree1001@email.phoenix.edu | Password | Password used for
connecting to your YesWeHack account| - |
| Remember password | Choose to keep a plaintext copy of your password
inside. Burp | l-
 |## Changelog- v1.2- Basic support for TOTP- v1.1 - Bugfix- v1- Initial release
