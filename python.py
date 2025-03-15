import webbrowser
import subprocess
import time
import pyautogui


# 1. O programa irá abrir os sites que mais uso na hora de programar 
# 2. Ele vai abrir o teams, caso não tenha instalado ele irá abrir no Chrome
# 3. Ele irá abrir o VScode
# 4. Ele irá abrir os sticks e avisar que todos os programas foram abertos com sucesso

# Lista de sites que você deseja abrir
sites = [
    "https://teams.microsoft.com/v2/",
    "https://www.github.com"
]

# Abre cada site em uma nova guia do navegador padrão (no meu caso é o OperaGx)
for site in sites:
    webbrowser.open_new_tab(site)



#O subprocess aqui abre o VSCode pelo seu executável hihi
subprocess.run([r"C:\Users\otavv\AppData\Local\Programs\Microsoft VS Code\Code.exe"])



# Tenta abrir o Sticky Notes se estiver no local certo claro!!!!
try:
    subprocess.run(["explorer.exe", "shell:AppsFolder\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App"])
    time.sleep(5)
    pyautogui.click(x=1418, y=29, duration=2)
    time.sleep(1)
    pyautogui.click
    pyautogui.click(x=933, y=470, duration=2)
    pyautogui.write("Todos os programa foram abertos com sucesso!")


except FileNotFoundError:
    print("Deu erro")
