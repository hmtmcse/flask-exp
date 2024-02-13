from pathlib import Path

file_name_list = [
    "file.txt",
    "সাইবার ###সিকিউরিটি #অ্যান্ড -ইথিকস  - Copy (5).docx",
    "7zarchive_file .7z",
    "exampl.tar.gz",
    "test;pdf@.pdf",
]
for file_name in file_name_list:
    path = Path(file_name)
    filename = path.stem
    print(filename)
    print()
    print(file_name.rsplit('.', 1)[1].lower())
