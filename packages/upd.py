#["upd", "packages.upd", ["upd"]]
# Made By Blurple
import os, sys, requests

fileList = [
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/builtin.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/echo.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/nano.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/netget.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/pip.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/upd.py"
]

def upd(command: list):
    input(f"Settings: {[url for url in fileList]}, {os.path.dirname(os.path.realpath(__file__))}\nPress enter to continue")
    for urls in fileList:
        r = requests.get(urls)
        print(r.text)
        print('Requests:' in r.text)
        print(r.headers['Content-Type'])
        fileInstallingCreator = "." + urls[59:]
        with open(fileInstallingCreator, "w") as newFile:
            newFile.write(r.text)
            newFile.close()