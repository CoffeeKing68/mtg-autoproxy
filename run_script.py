from argparse import ArgumentParser
from json import load
import os
import platform
import subprocess
from pathlib import Path
from pprint import pprint

CONFIG_JSON = "config.json"


def get_args():
    parser = ArgumentParser(description='Make some mtg proxies!')

    parser.add_argument(
        '--photoshop', '-ps', help='Target Photoshop app (only need end code `eg. CS6`)')
    parser.add_argument('--javascript', '-js', help='Script to run')

    args = parser.parse_args()

    try:
        with open(CONFIG_JSON, "r") as f:
            config = load(f)
    except:
        # There should be a better way to do this
        config = {
            "photoshopTarget": "",
            "javascriptToRun": "",
        }

    # args take precedent
    if args.photoshop:
        ps = args.photoshop
        if not ps.startswith("Adobe Photoshop "):
            ps = "Adobe Photoshop " + ps
    elif config["photoshopTarget"]:
        ps = config["photoshopTarget"]
    else:
        print("Tell me what photoshop to use!")
        exit()

    if args.javascript:
        # Apple script at least wants a full path
        js = Path(args.javascript).resolve()
    elif config["javascriptToRun"]:
        js = Path(config["javascriptToRun"]).resolve()
    else:
        print("Tell me what javascript to run!")
        exit()
    
    if not Path(js).exists():
        print("Javascript file doesn't exist!") 
        exit()

    return ps, js


def main():
    ps, js = get_args()

    system = platform.system()
    if system == "Darwin":  # MacOS
        # Applescript is so silly, have to do it like this so it doesn't complain
        # Looking for any alternatives
        applescript_string = f"""tell application "{ps}"
            with timeout of 3600 seconds
                activate
                set js to "#include '{js}'; main();"
                do javascript js
            end timeout
        end tell"""
        command = ["osascript"]
        for line in applescript_string.splitlines():
            command.append("-e")
            command.append(line.strip())

        subprocess.call(command)
    elif system == "Windows":
        pass
    elif system == "Linux":
        pass


if __name__ == "__main__":
    main()
