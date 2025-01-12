import cv2
from pyzbar import pyzbar
import datetime
from status_display import StatusDisplay
import tkinter as tk
import threading
import time

def create_if_not_exists(filename):
    with open(filename, mode ='a') as file:
        pass
        #Open the file to create it if not exists


def read_file_into_set(filename):
    return set(line.strip() for line in open(filename))


whitelist = set('abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789')
def my_filter(input_string):
    to_filter = str(input_string).lower()
    return ''.join(filter(whitelist.__contains__, to_filter))


def get_ths_members():
    ths_members_file_name = "ths_members_kth_emails.txt"
    create_if_not_exists(ths_members_file_name)

    return read_file_into_set(ths_members_file_name)


def is_already_verified_attendee(potential_attendee):
    attendees_filename = "verified_attendees.txt"
    create_if_not_exists(attendees_filename)
    
    attendees = read_file_into_set(attendees_filename)
    if potential_attendee in attendees:
        return True
    
    return False


def is_already_scanned(kth_email):
    scanned_kth_emails_filename = "scanned_kth_emails.txt"

    create_if_not_exists(scanned_kth_emails_filename)
    
    scanned_kth_emails = read_file_into_set(scanned_kth_emails_filename)
    if kth_email in scanned_kth_emails:
        return True
    
    return False


def read_barcodes(frame, status_display):
    barcodes = pyzbar.decode(frame)
    barcode_found = False
    for barcode in barcodes:
        barcode_found = True
        x, y , w, h = barcode.rect
    
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3


        # Log scans and attendees and display info
        ths_members = get_ths_members()
        kth_mail_scanned = my_filter(barcode_info)
        # Register scan
        if not is_already_scanned(kth_mail_scanned):
            # If not in scanned_kth_mails already, add to 
            with open("scanned_kth_emails.txt", mode ='a') as file:
                file.writelines(kth_mail_scanned + "\n")

        if kth_mail_scanned in ths_members:
            # If the kth_mail_scanned is a registered THS member
            if not is_already_verified_attendee(kth_mail_scanned):
                with open("verified_attendees.txt", mode ='a') as file:
                    file.writelines(kth_mail_scanned + "\n")
            status_display.show_status("lightgreen", "Welcome, " + kth_mail_scanned + "!", 0)
        else:
            # not ths member 
            print("NOT IN THS MEMBER LIST: " + kth_mail_scanned)
            status_display.show_status("red", kth_mail_scanned + " not found. Please show THS membership card or payment.", 0)        

        print(barcode_info)
        with open("scan_log.txt", mode ='a') as file:
            file.writelines(str(datetime.datetime.now()) + "," + kth_mail_scanned + "\n")
    if not barcode_found:
        status_display.show_status('white', 'Waiting for scan', 0)

    return frame


def main(status_display):
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame, status_display)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("SM-scan Status Display")
    status_display = StatusDisplay(root)
    x = threading.Thread(target=main(status_display))
    x.start()
    root.mainloop()
