CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8
approved = ["coding app", "math app", "reading app", "science app"]
restricted = ["gaming app", "shopping app", "social media app"]
name = input("Enter your name: ")
app = input("Enter the app you want to access: ").lower()
print("Name is str:", type(name) is str)
print("App is not int:", type(app) is not int)
if app in approved:
    print("Approved app")
else:
    print("Not an approved app")
if app not in restricted:
    print("Not restricted")
else:
    print("Restricted")
perms = CAMERA | MICROPHONE | STORAGE
print("Permissions:", perms)
print("Binary:", bin(perms))
if perms & CAMERA:
    print("Camera on")
if perms & MICROPHONE:
    print("Microphone on")
if perms & STORAGE:
    print("Storage on")
if perms & LOCATION:
    print("Location on")
else:
    print("Location off")
print("Camera shifted left:", bin(CAMERA << 1))
print("Storage shifted right:", bin(STORAGE >> 1))
if app in approved and app not in restricted:
    print("Access granted")
else:
    print("Access denied")