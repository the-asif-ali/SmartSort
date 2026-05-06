import os
import shutil

# --------------
# Get all Files
# --------------

def get_files(folder):
    files = []
    all_items = os.listdir(folder)

    for item in all_items:
        path = os.path.join(folder, item)

        if os.path.isfile(path):
            files.append(item)
    
    return files


#------------------------------------
# Decide folder based on extendion
#------------------------------------

def get_folder(ext):
    ext = ext.lower()

    # Images
    if ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"]:
        return "Images"

    # Videos
    elif ext in [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"]:
        return "Videos"

    # Audio
    elif ext in [".mp3", ".wav", ".aac", ".flac", ".ogg"]:
        return "Audio"

    # Documents
    elif ext in [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"]:
        return "Documents"

    # Compressed / Archives
    elif ext in [".zip", ".rar", ".7z", ".tar", ".gz"]:
        return "Archives"

    # PC Applications / Executables
    elif ext in [".exe", ".msi", ".bat", ".cmd"]:
        return "PC Apps"

    # Mobile Applications
    elif ext in [".apk", ".xapk", ".ipa"]:
        return "Mobile Apps"

    # Code / Programming Files
    elif ext in [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".dart", ".php"]:
        return "Code Files"

    # System Files
    elif ext in [".dll", ".sys", ".ini"]:
        return "System Files"

    # Fonts
    elif ext in [".ttf", ".otf", ".woff"]:
        return "Fonts"

    # Disk Images
    elif ext in [".iso", ".img"]:
        return "Disk Images"

    else:
        return "Others"
    
#----------------------------
# Move Files
#----------------------------
def move_files(folder, files):
    for file in files:
        path = os.path.join(folder, file)

        # Get extension
        ext = os.path.splitext(file)[1]

        # Get folder name
        new_folder = get_folder(ext)

        folder_path = os.path.join(folder, new_folder)
        os.makedirs(folder_path, exist_ok=True)

        new_path = os.path.join(folder_path, file)

        # First tweak
        if os.path.exists(new_path):
            print("Skipping (Already Exists) : ", file)
            continue

        try:
            shutil.move(path, new_path)
            print(file, "-->", new_folder)

        except Exception as e:
            print("Error Moving", file,":", e)



#--------------------------
# Main Function
#--------------------------

def main():
    folder = input("Enter the destination folder : ") # Enter folder path

    if not os.path.exists(folder):
        print("Invalid folder path!")
        return

    files = get_files(folder)

    if len(files) == 0:
        print("No Files Found")
        return
    
    move_files(folder, files)

    print("Done!")


#---------------
# Run Program
#---------------
if __name__ == "__main__":
        main()
