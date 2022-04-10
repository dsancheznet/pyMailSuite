# pyMailSuite
An email suite with superpowers for devs and those who spend lots of time in a terminal session.

# Installation

To install this utility, you just need to have pyqt5 installed and copy the executables to your local/bin directory.

# Configuration

Each user may should create a configuration file containing the following data

```
{
"SMTPaccounts":[     
      {
        "NAME":"Set this to the label you want to show up",
        "SENDER": "your complete email address",
        "USERNAME": "the username to send email from (this server)",
        "PASSWD": "your plaintext password",
        "SERVER": "your smtp server",
        "PORT": your server port (no quotation marks)
      },
      {
        "NAME":"Set this to the label you want to show up",
        "SENDER": "your complete email address",
        "USERNAME": "the username to send email from (this server)",
        "PASSWD": "your plaintext password",
        "SERVER": "your smtp server",
        "PORT": your server port (no quotation marks)
      }
  ]
}
```
The configuration file is hardcoded and has to be set to `~/.config/mailto.json`


_(c)_ D.Sanchez 2022
