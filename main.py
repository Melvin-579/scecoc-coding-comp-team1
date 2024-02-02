# the following code awas joint contribution by all authors that collaborated
import threading

# Store highest allocated ip address
highest_ip = "0.0.0.0"

# Keeps a list of free ip addresses that have expired and not re-allocated
free_ip = list()

# Tracks current place value for ip updating
curr_ip_place_value = 3

import time

def release_ip(self):
    None


# Increments highest ip address according to base 256 convention
def increment_ip(current_ip: str) -> str:
    global curr_ip_place_value

    # Split ip by periods
    broken_ip = current_ip.split('.')
    update_value = int(broken_ip[curr_ip_place_value])

    # If current place value has filled move to the next
    if int(update_value) == 255:
        curr_ip_place_value = curr_ip_place_value - 1
        update_value = broken_ip[curr_ip_place_value]

    update_value += 1
    broken_ip[curr_ip_place_value] = str(update_value)

    final_ip = ""
    for i in broken_ip:
        final_ip += f"{i}."

    return final_ip.rstrip('.')


def release(ip: str):
    global free_ip

    free_ip.append(ip)


# Delegate ip addresses
def delegate():
    global highest_ip
    global free_ip
    print(free_ip)

    given_ip = ""

    # If an IP is available allocate it
    if free_ip:
        given_ip = free_ip.pop(0)
    # Increment and allocate the highest IP
    else:
        given_ip = increment_ip(highest_ip)
        highest_ip = given_ip
    print(given_ip)
    return given_ip
    
