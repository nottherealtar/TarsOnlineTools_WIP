class TarsOnlineTools():
   __version__ = "v1.0.0"

"""  
Hey there! it seems you found my Github: https://github.com/nottherealtar

This Project is a simple Python Console Application that I made for personal use to monitor my network and the online presence of of other devices connected to it.
Along with this I am learning new python libraries and concepts to improve my skills as well as combining it with networking to make it more useful.

This Tool will have the following features:
1. IP TOOLS - A set of tools to monitor the network and Identify devices connected to it.
2. LAN TOOLS - A set of tools to test and monitor the Local Area Network and Identify devices connected to it.
3. SPEEDTEST - A tool to test the speed & ping of the network via LAN & Wi-Fi.
4. SPEEDTEST ADVANCED - A tool to test the speed & ping of the network via LAN & Wi-Fi with more advanced options and a visual spectrum.
5. DEVICE INFORMATION - A tool to get the information of your device in terms of what is public and shown to others. (display back your own info as if someone used this tool on you)

UI/UX:
1. Banner + Title using rgbprint gradient + gradient scroll and most app visuals, use colorama to tidy up the console.
2. Menu with options to select the tools. use colorama to tidy up the console. enter 1 - 5 for respective features.
3. Each tool will have its own UI and will be displayed in a clean and readable format. use colorama to tidy up the console. use rich for advanced visuals and make sure that speedtest advanced has a visual spectrum to display the speeds in an advanced smart way.
4. Proper Error handling, exception handling and input validation to make sure the user does not break the application and the application can be self sufficient when hitting errors.
5. Proper Documentation and comments to make sure that the code is readable and understandable by others and myself in the future.
"""

if __name__ == "__main__":
   import console