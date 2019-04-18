import os
from itertools import product
import time

def reboot():
    return os.system('fastboot reboot-bootloader')

def unlock(password):
    return os.system('fastboot oem unlock {}'.format(password))

def success(status):
    return True if status == 0 else False

if __name__ == '__main__':
    digit = 16
    attempted = 0
    reboot_counter = 0

    for attempt in product('0123456789', repeat=digit):
        attempt = ''.join(attempt)
        attempted += 1

        print('\n#{} attempts, code: {}'.format(attempted, attempt))
        if success(unlock(attempt)):
            print('Ray! unlock password found!\npassword: {}'.format(attempt))
            exit()
        # make logs look better
        print('\n')
        reboot_counter += 1
        
        if reboot_counter >= 3:
            #reboot to pass the lockup
            reboot()
            time.sleep(1)
            reboot_counter = 0
	    
