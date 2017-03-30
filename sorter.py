import shutil
import os

directory = "C:/example/example"

def sorter(directory):
    files = os.listdir(directory)
    srcfile = ""

    for file in files:
        srcfile = directory + "/" + file
        if "png" in file or "jpg" in file:
            dst = f"{directory}/Pics"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)
        elif "pdf" in file:
            dst = f"{directory}/PDF"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)
        elif "exe" in file:
            dst=f"{directory}/programs"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)
        elif "zip" in file or "rar" in file:
            dst=f"{directory}/archive_files"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)
        elif ".xls" in file or ".csv" in file:
            dst = f"{directory}/spreadsheets"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)
        elif ".doc" in file:
            dst=f"{directory}/word"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)
        elif file != "desktop.ini" and "." in file:
            dst=f"{directory}/misc_files"
            shutil.copy2(srcfile, dst)
            os.remove(srcfile)

if __name__ == "__main__":
    sorter(directory)
