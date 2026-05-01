import webview
import os

# Config
WINDOW_TITLE = 'TokenCord'
LOGIN_URL = 'https://discord.com/login'

def inject_token(window, token):
    print('[+] injecting on : ' + token)
    js_code = """
    function login(token) {
        setInterval(() => {
            document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"${token}"`;
        }, 50);
        setTimeout(() => { location.reload(); }, 2500);
    }
    """ + f"\nlogin('{token}');"
    window.evaluate_js(js_code)

def handle_token_file(window):
    file_types = ('Text files (*.txt)', 'All files (*.*)')
    file_path = window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=False, file_types=file_types)

    if not file_path:
        return

    path = file_path[0]
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print('[-] File is empty')
            return

        raw_line = lines[0].strip()
        token = raw_line.split(':')[-1] if ':' in raw_line else raw_line

        inject_token(window, token)

        if len(lines) > 1:
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(lines[1:])
            
    except Exception as e:
        print(f'[-] Erreur : {e}')

def main():
    window = webview.create_window(
        WINDOW_TITLE, 
        LOGIN_URL, 
        width=1000, 
        height=1000
    )
    
    webview.start(handle_token_file, window, debug=True)

if __name__ == '__main__':
    main()