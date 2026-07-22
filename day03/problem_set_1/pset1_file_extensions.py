import time
filename = input("Type name of your file: ").strip().lower()
switch_formats = {
    "GIF": "image/gif",
    "JPG": "image/jpeg",
    "JPEG": "image/jpeg",
    "PNG": "image/png",
    "PDF": "application/pdf",
    "TXT": "text/plain",
    "ZIP": "application/zip",
}
if "." in filename:
    file_format = filename.split(".")[-1].upper()
    if file_format in switch_formats:
        time.sleep(1)
        print(switch_formats[file_format])
    else:
        time.sleep(1)
        print("application/octet-stream")
else:
        time.sleep(1)
        print("application/octet-stream")

    