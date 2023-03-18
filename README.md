This is a simple project made with help of Chat GPT-4

## Context
Once I wanted to know how many emails there were in my Gmail inbox for the past 15 years. I had around 30k emails there. I searched for some easy/ready solution but none could give me the number. So I decided to solve it somehow.

## What does the script do?
It's a simple python script that traverses subdirectories containing emails and generates a .csv at the end with certain information for each email

## How to use it

First, you will need to have all your emails as .eml

The Vivaldi browser has built-in an email client which once configured you can download all of your emails from your Gmail, Outlook, Yahoo, or any other email provider

It will save the .eml files in a certain folder on your machine. If you're using macOS it will be something like

```
/Users/<your-user>/Library/Application Support/Vivaldi/Default/Mail/<folder>/
```

Once you get the full path of this folder, you can substitute it on the script and run it.

It will generate a .csv at the end, which then you can use to get the number and understand who has sent you more emails, for example.