read_emails_from_filename = "verified_attendees.txt"
sql_add_template_filename = "SQL_statement_add_user_if_not_exists.txt"
sql_set_attendance_filename = "SQL_statement_set_attendance.txt"

sql_aggregate_add_string = ""
sql_aggregate_set_attendance_string = ""

sql_aggregate_add_filename = "sql_aggregate_add_filename.txt"
sql_aggregate_set_attendance_filename = "sql_aggregate_set_attendance_file.txt"

def create_if_not_exists(filename):
    with open(filename, mode ='a') as file:
        pass
        #Open the file to create it if not exists


def read_file_into_set(filename):
    return set(line.strip() for line in open(filename))



create_if_not_exists(sql_aggregate_add_filename)
create_if_not_exists(sql_aggregate_set_attendance_filename)

verified_emails = read_file_into_set(read_emails_from_filename)

## Generate sql from template

for email in verified_emails:
    # Do this for each verified email

    # Read template for add user
    with open(sql_add_template_filename, 'r', encoding='utf-8') as file:
        sql_add = file.read().replace('\n', '').replace('template_email', email)
        sql_aggregate_add_string += sql_add
        print(sql_add)

    # Read template for update attendance for user
    with open(sql_set_attendance_filename, 'r', encoding='utf-8') as file:
        sql_set_attendance = file.read().replace('\n', '').replace('template_email', email)
        sql_aggregate_set_attendance_string += sql_set_attendance
        print(sql_set_attendance)
    

## Save to file
with open(sql_aggregate_add_filename, 'w', encoding='utf-8') as file:
    file.write(sql_aggregate_add_string)

with open(sql_aggregate_set_attendance_filename, 'w', encoding='utf-8') as file:
    file.write(sql_aggregate_set_attendance_string)