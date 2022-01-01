import update

if update.main():
    import example # Updated, so restart
    exit()
else:
    f = open("version.txt", "r")
    version = f.read()
    f.close()
    print(f'Version: {version}') # Did not update, start as normal
