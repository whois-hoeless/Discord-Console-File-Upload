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
- I recommend putting the script somewhere, where you don't delete it and then put a symbolic link to the script's location inside of /usr/local/bin so you can use it as a command
- Otherwise you can just add the .py extension to the script and use it in your console like that or however you want :>
- You're good to go!

### Warning

names are preffered over numbers that can bring up following issue for example:

- you have a friends list of 25 friends
- one of your friend's name is 13
- you want to message the friend with the index 13
- it will send the file to the friend whose name is 13 (name not index) because the script prioritizes names over indexes.
- Fix:
- write the friend's name whose index is 13
- remove the friend with the number as their name from your friendslist: number as name == bad person (jk)
- Also, just as a side note, if you ever found yourself using the "nickname" feature that discord provides, that also gets ignored by the script. Only the username is accepted.

### Experimental

- I have no experience with people having unicode or ascii characters as their name. The index should help with that but I don't know what the script outputs when it encounters ascii / unicode whatsoever. Probably dependent on your shell..

## Usage

- python main.py <file_to_upload>
- you will get prompted with any file size errors (if you have any)
- The script will ask you for a friends name, you don't need to provide the # because I wouldn't be able to remember those numbers
- also, it isn't case sensitive, so you can just write the name the way you want to
- if you have multiple friends with the same name, it could happen that only 1 friend gets the file, to fix that just remove the .lower() which makes the script case sensitive again
- Then the script asks you if you want to send an additional message, just press enter to skip if you only want to send the file

## Btw

- I also added a bash script, so if you put both of those files inside of /usr/bin/ and allow it to execute, then you can have an universal command in linux :>

### If there are any questions or bugs, feel free to open a ticket.

## Enjoy!
