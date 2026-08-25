def main():
    file_name = input("File name: ")
    if image(file_name):
        print("image/" + file_name[(file_name.rfind(".")) + 1:].lower())
    elif jpg(file_name):
        print("image/jpeg")
    elif application(file_name):
        print("application/" + file_name[(file_name.rfind(".")) + 1:].lower())
    elif text(file_name):
        print("text/plain")
    else:
        print("application/octet-stream")

def image(fn):
    return fn.strip().lower().endswith((".gif", ".jpeg", ".png"))

def jpg(fn):
    return fn.strip().lower().endswith(".jpg")

def application(fn):
    return fn.strip().lower().endswith((".pdf", ".zip"))

def text(fn):
    return fn.strip().lower().endswith(".txt")

main()