#Write a program to pronounce list of the names using win32 API.
#If youre a given a list as follows:

  

# from os import system
# for name in l:
#     system(f'Say Hello {name}')  #This will pronounce the name in the list using win32 API.


try:
    import win32com.client as wincl
except ImportError:
    raise ImportError(
        "win32com.client is not installed. Install pywin32 and try again."
    )

speak = wincl.Dispatch("SAPI.SpVoice")
l=["Pawan", "Peter", "Mary", "David", "Sarah"]
for name in l:
    speak.Speak(f"Hello {name}")  #This will pronounce the name in the list using win32 API.    