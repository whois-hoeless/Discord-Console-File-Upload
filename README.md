# Discord-Console-File-Upload
- This is a small project I have made in a few hours (most of the time I used researching how multipart/form-data works which isn't actually that bad to use)
- I made it because I was kind of annoyed to always switch from my terminal to my file explorer, then find a file in my current console dir and then send that, so I made a python script that automates this for me.
- The script is focused on sending dms, so it doesn't work on servers, for servers you can just simply set up a discord.py script.
- I made it with requests for dms because I didn't find a function that gives me the option to get direct message channel ID's and then I also didn't want to spend 5 hours in the docs searching stuff etc..
- It was also a nice little challange for me since I hardly ever work with requests
- Enough of my backstory, let's dive into the setup!

## Setup
- Enter your personal discord token into the token variable inside of the script
- Select your nitro plan (I made the script check file sizes), valid options are 'none' for no nitro, 'basic' for nitro basic and 'nitro' for normal nitro users
- You're good to go!

## Usage
- python main.py <file_to_upload>
- you will get prompted with any file size errors (if you have any)
- The script will ask you for a friends name, you don't need to provide the # because I wouldn't be able to remember those numbers
- also, it isn't case sensitive, so you can just write the name the way you want to
- if you have multiple friends with the same name, it could happen that only 1 friend gets the file, to fix that just remove the .lower() which makes the script case sensitive again
- Then the script asks you if you want to send an additional message, just press enter to skip if you only want to send the file

### If there are any questions or bugs, feel free to open a ticket.

## Enjoy!
