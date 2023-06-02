# Discord-Console-File-Upload

- This is a small project I have made in a few hours (most of the time I used researching how multipart/form-data works which isn't actually that bad to use)
- I made it because I was kind of annoyed to always switch from my terminal to my file explorer, then find a file in my current console dir and then send that, so I made a python script that automates this for me.
- The script is focused on sending dms, so it doesn't work on servers, for servers you can just simply set up a discord.py script.
- I made it with requests for dms because I didn't find a function that gives me the option to get direct message channel ID's and then I also didn't want to spend 5 hours in the docs searching stuff etc..
- It was also a nice little challange for me since I hardly ever work with requests
- Enough of my backstory, let's dive into the setup!

## Setup

- The script asks you for your settings when needed. You should be able to figure out what to do.
- If you don't know how to obtain your discord token, look into the "how do I get my discord token" section.

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
- Also I don't know if there is a cap in the amount of friends that get returned in the list of friends when you make a request, I don't think so but I don't know for sure.

## Usage

- dcsf <file_to_upload>
- you will get prompted with any file size errors (if you have any)
- The script will ask you for a friends name, you don't need to provide the # because I wouldn't be able to remember those numbers
- also, it isn't case sensitive, so you can just write the name the way you want to
- if you have multiple friends with the same name, it could happen that only 1 friend gets the file, to fix that just remove the .lower() which makes the script case sensitive again
- Then the script asks you if you want to send an additional message, just press enter to skip if you only want to send the file
- If you have any problems with your token or nitro plan, the script should work you through it. You can always manually edit the values in /home/you/.config/dcsf/.env if you want to.

## How do I get my discord token?

The easiest way is to use the developer tools in your browser. This is for firefox, but it should be similar in chrome:

- Open discord in your browser and log in.
- Open the developer tools (F12 or Ctrl + Shift + I)
- Go to the "Storage" tab
- Click on "Local Storage"
- At the top is a filter or a search bar, type in "token" and press enter.
- If nothing comes up, you need to click on the "Responsive Design mode" button (the one with the phone and the tablet) and then refresh the page. Ctrl + Shift + M might work too.
- Then you should receive your discord token.
- It will be surrounded by 2 double quotes ( " " ), remove those and copy the token. And paste it into the program. Also, never share your token with anyone, it's like your password, but worse.
- If you don't, you might have to search for a tutorial on how to get your discord token.

### If there are any questions or bugs, feel free to open a ticket

## Enjoy
