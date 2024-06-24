import os
import time
import tabulate
from UI import homepage
from UI import steamyrat_ui
from UI import kali_whoami
import payload_creator1


home_directory = os.getenv("HOME")

while True:

    os.system("clear")
    print("""Merhaba bu framework içerisindeki kütüphaneler aşağıdaki gibidir

    1 - Figlet
    2 - Tabulate

    """)

    baslangic_secim = input("Bu kütüphanelerin indirilmezse program çalışamayacaktır kütüphanelerin indirilmesini onaylıyor musunuz [E/h]")

    if baslangic_secim == "E" or baslangic_secim == "e" or baslangic_secim == "":
        # Package installation
        # os.system("sudo apt update && sudo apt-get install figlet")   Dont forget to get it out of comment string
        # os.system("sudo pip install tabulate")     Dont forget to get it out of comment string

        # Program code
        while True:
            os.system("clear")
            os.system("figlet -c Steamy Framework")
            print(homepage.tools_table)
            print("Kullanmak istediğiniz aracın numarasını yazınız")
            print("(çıkmak için q, x, quit, exit yazabilirsiniz)")
            tool_secim = input("\n\n\n>>> ")

            if tool_secim == "1":
                os.system("clear && figlet -c Steamy RAT")
                print(steamyrat_ui.tools_table)
                print("Kullanmak istediğiniz aracın numarasını yazınız")
                tool_secim_1 = input("\n\n\n>>> ")
                
                if tool_secim_1 == "1":
                    paylaod_ip = input("Ip adresi : ")
                    payload_port = int(input("Port : "))
                    payload_name = input("Payload'ın ismi : ")
                    payload_creator1.payload_creator(paylaod_ip, payload_port, payload_name)
                    os.system(f"sudo netcat -lvnp {payload_port}")



            elif tool_secim == "2":
                os.system("clear && figlet -c Netcat Listening")
                netcat_port = input("Dinleme yapacağınız portu giriniz : ")
                os.system(f"sudo netcat -lvnp {netcat_port}")

            elif tool_secim == "3":
                os.system("clear && figlet -c Nmap Scan")
                nmap_taget_ip = input("Tarama yapmak istediğiniz ip adresini giriniz : ")
                os.system(f"sudo nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 {nmap_taget_ip}")
            
            elif tool_secim == "4":
                os.system("clear && figlet -c WHOAMI")
                    
                whoami_check = input("Bu bölüm who am i anonimlik aracını kullanmaktadır bu araç sisteminizde yüklü mü [E/h]")

                if whoami_check == "E" or whoami_check == "e" or whoami_check == "":
                    while True:
                        os.system("clear && figlet -c WHOAMI")
                        print("\n\n\n", kali_whoami.tools_table)
                        whoami_komut = input("\n\n>>> ")
                        if whoami_komut == "başlat" or whoami_komut == "baslat" or whoami_komut == "start":
                            os.system("sudo kali-whoami --start")
                        elif whoami_komut == "durdur" or whoami_komut == "stop":
                            os.system("sudo kali-whoami --stop")
                        elif whoami_komut == "durum" or whoami_komut == "status":
                            os.system("sudo kali-whoami --status")
                            input("Devam etmak için enter tuşuna basınız...")
                        elif whoami_komut == "düzelt" or whoami_komut == "duzelt" or whoami_komut == "fix":
                            os.system("sudo kali-whoami --fix")
                        elif whoami_komut == "çıkış" or whoami_komut == "çıkıs" or whoami_komut == "çıkiş" or whoami_komut == "çıkis" or whoami_komut == "çikış" or whoami_komut == "çikıs" or whoami_komut == "çikis" or whoami_komut == "cikis" or whoami_komut == "cıkış" or whoami_komut == "cıkıs" or whoami_komut == "cıkis" or whoami_komut == "cikis" or whoami_komut == "exit" or whoami_komut == "quit":
                            break


                        elif whoami_komut == "":
                            continue

                elif whoami_check == "H" or whoami_check == "h":
                    whoami_kurulum = input("Who am i aracı indirilecektir. Bunu onaylıyor musunuz [E/h] : ")
                    if whoami_kurulum == "E" or whoami_kurulum == "e" or whoami_kurulum == "":
                        os.system("sudo apt install tar tor curl python3 python3-scapy network-manager")
                        os.system(f"cd {home_directory} && git clone https://github.com/omer-dogan/kali-whoami && cd {home_directory}/kali-whoami && sudo make install")
                        exit()
                    elif whoami_kurulum == "H" or whoami_kurulum == "h":
                        exit()


            elif tool_secim == "5":
                zphisher_check = input("Bu bölüm zphisher oltalama aracını kullanmaktadır bu araç sisteminizde yüklü mü [E/h]")
                if zphisher_check == "E" or zphisher_check == "e" or zphisher_check == "":
                    zphisher_konum = input(f"Zphisherın konumunu giriniz örnek({home_directory}/zphisher/) varsayılan({home_directory}/zphisher/) : ")
                    if zphisher_konum == f"{home_directory}/zphisher/" or zphisher_konum == f"{home_directory}/zphisher" or zphisher_konum == "":
                        zphisher_directory = f"{home_directory}/zphisher/"
                        os.system(f"cd {zphisher_directory} && bash zphisher.sh")
                    else:
                        print(f"Lütfen Zphisher aracını {home_directory} klasörüne kurunuz ve klasörün isminin 'zphisher' olduğundan emin olunuz.")
                        input("Devam etmek için enter tuşuna basınız...")

                elif zphisher_check == "H" or zphisher_check == "h":
                    zphisher_kurulum = input("Zphisher aracı indirilecektir. Bunu onaylıyor musunuz [E/h] : ")
                    if zphisher_kurulum == "E" or zphisher_kurulum == "e" or zphisher_kurulum == "":
                        os.system(f"cd {home_directory} && git clone https://github.com/htr-tech/zphisher.git && cd {home_directory}/zphisher && bash zphisher.sh")

            elif tool_secim == "":
                continue
            elif tool_secim == "q" or tool_secim == "x" or tool_secim == "quit" or tool_secim == "exit":
                exit()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    elif baslangic_secim == "H" or baslangic_secim == "h":
        exit()
    