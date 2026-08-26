file_name = input("File name: ")
fn = file_name.lower().strip()
if fn.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif fn.endswith(".gif"):
    print("image/gif")
elif fn.endswith(".png"):
    print("image/png")
elif fn.endswith(".pdf"):
    print("application/pdf")
elif fn.endswith(".txt"):
    print("text/plain")
elif fn.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")