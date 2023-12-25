s = input("File name: ")
end = s.split(".")[-1]
match end:
    case "png":
        print("image/png")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/x-7z-compressed")
    case "txt":
        print("text/plain")
    case "gif":
        print("image/gif")