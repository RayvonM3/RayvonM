print("Welcome Python for Network Engineering")
#-------------------------------
#Begining w/ Variables
hostname = "Router01"
interface_count = 4
status = True
default_gateway = "192.168.1.1"
mac_address = "00:1A:2B:3C:4D:5E"
#-------------------------------
#Displaying Variables
print("Device:", hostname)
print("Interface Count:", interface_count)
print("Status Active?", status)
print("Management IP:", default_gateway)
print("MAC Address:", mac_address)
#-----------------------------
#Subnetwork
# The subnet mask defines which portion of the IP address is the Network and which is the Host
#Subnet is 192.168.1 = Network ID .1 = Host ID
#Clients may get .2, .3, .4, .50, etc, all with the same subnet
subnet_mask = "255.255.255.0"
#-----------------------------
print("Subnet Mask:", subnet_mask)
print("MAC Address:", mac_address)
print(f"Subnet Mask: {subnet_mask}")
print(f"MAC Address: {mac_address}")
#print(f" ") works to format strings with variables. 
#This helps in automation by reducing the need for repetition and making the code more readable.
#f stands for "formatted string literal" or "f-string"
#----------------------------
# Combining text and variables
print(f"{hostname} has {interface_count} interfaces.")
#-----------------------------
#Day 2 of pythong learning journey. 
print("Welcome to network Configuration Checker")

# user input
user_device = input("Entter device hostname:")
device_ip = input("Enter device IP address:")
device_status = input("Is the device active? (yes/no): ")
interface_count = int(input("Enter the number of interfaces: "))
if interface_count > 4:
        print("High-capacity device.")
else:
        print("Standard Network Device.")

#displaying summary
print("\n===== Device Summary ======")
print(f"Hostname: {user_device}")
print(f"IP Address: {device_ip}")
print(f"Status: {device_status}")
# Extending and normalizing status input.
if device_status.lower() == "yes":
    print("Online Connection Confirmed: Device is active")
else:
    print("Online Connection Denied: Device is inactive")
# Asking for interface count
    

    
