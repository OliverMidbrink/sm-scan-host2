# Instructions

### Installation 
* install pyzbar using this guide https://pypi.org/project/pyzbar/ (for mac `brew install zbar` then `pip install pyzbar`)
* install cv2 (opencv) using `pip install opencv-python`
* instapp keyboard using `pip install keyboard`


### For visitors/attendees of SM
1. Head to smqr.iare.se and fill in kth-email as instructed. (Source code can be found here https://github.com/isektionen/sm-scan)
2. Show to administrator that has the scanning device (probably laptop)

### Setting up your scan device (probably laptop)
1. Clear all text files if any (they will be created upon first run)
2. Insert ths members as kth emails without suffix in each row of the ths_members... file
3. Run main.py as administrator i terminal to start scanning
4. scanned and verified attendees will appear in verified_attendees.txt (see the scan logs if you think something was missed/or wierd, as well as scanned kth emails)
5. All scanned kth_emails will appear in scanned_kth_emails.txt
(6.) run auto_fill.py and click in the attencance box on demokrati.iare.one/admin page to autofill attendees (this will automatically type in the attendance in demokrati admin)
