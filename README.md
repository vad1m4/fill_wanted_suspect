# Description
This script fills a template for a wanted poster.
I made it purely to enhance my LSPDFR experience, I don't know how can it be used in other cases, but yeah. 
Decided to upload this just for myself tbh, but maybe somebody would find this useful so I made it public.

# UI Version
1. If you have a mugshot, upload it to the "mugshots" folder and make sure the file's name is the suspect's **EXACT full name in all lowercase with underscores (_) instead of spaces** (e.g firstname_secondname.png), otherwise it won't work. Script only accepts .png, .jpg and .jpeg files, other file formats will **NOT** work.
2. The UI is pretty self-explanatory. Fill all the entries, choose all the options in dropboxes and click "Generate!". The generated file can be found in the "wanted" folder where you can make your finishing touches if needed.
*note: date and time can only be filled in HH:MM format and DD/MM/YYYY formats. you can put the years between 2000-current year. script checks the year every time it runs so it won't break next year.*

# Non UI version
1. If you have a mugshot, upload it to the "mugshots" folder and make sure the file's name is the suspect's **EXACT full name in all lowercase with underscores (_) instead of spaces** (e.g firstname_secondname.png), otherwise it won't work. Script only accepts .png, .jpg and .jpeg files, other file formats will **NOT** work.
2. Run the non_ui_main.py file and simply answer all of the questions. Tip: don't write the postal when it asks for the location of the incident, it will ask for postal in the next question.
3. After it says "Done with *your suspect's name*", you can check the .docx file in the "wanted" folder and make corrections if needed.
