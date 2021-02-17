import os
print("\n\033[32;1mUpdating Wordlist...\n\n\033[0m")
os.system('mv wordlist.txt hasillistkcfinder.txt')
os.system('wget https://raw.githubusercontent.com/rabeltester44/kcfinder/main/wordlist.txt --no-check-certificate')
print("\033[32;1mUpdate Wordlist Success\n\033[0m")
