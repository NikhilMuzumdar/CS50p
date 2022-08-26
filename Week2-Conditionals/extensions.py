def main():
    user_input = input("Enter the file name with extension: ").strip().split(".")[-1]
    check_exists(user_input)

def check_exists(file_ext):

    details = {
        ".gif":'image/gif',
        ".jpg":'image/jpeg',
        ".jpeg":'image/jpeg',
        ".png":'image/png',
        ".pdf":'application/pdf',
        ".txt":'text/plain',
        ".zip":'application/zip',
    }

    key = "."+file_ext.lower()
    if key in details.keys():
        print(details[key])
    else:
        print('application/octet-stream')

main()