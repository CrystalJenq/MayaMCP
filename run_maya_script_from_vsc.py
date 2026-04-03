import socket
import os

# --- 設定 ---
MAYA_PORT = 7001
# The path to the script you want to execute in Maya
SCRIPT_PATH = r"c:\VSC_Maya\open_uv_editor.py"

def main():
    """
    Main function to connect to Maya and execute the specified Python script.
    """
    print(f"Attempting to connect to Maya (Port: {MAYA_PORT})...")

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout so VS Code doesn't freeze if Maya is busy
        client.settimeout(10) 
        client.connect(("127.0.0.1", MAYA_PORT))
        print("Connection successful!")
    except (ConnectionRefusedError, socket.error):
        print(f"Connection failed. Please ensure Maya is running and 'commandPort -n \":{MAYA_PORT}\"' is active.")
        return

    if not os.path.exists(SCRIPT_PATH):
        print(f"Error: Script file not found: '{SCRIPT_PATH}'")
        return

    print(f"Reading script: '{SCRIPT_PATH}'")
    with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
        script_content = f.read()

    print("Sending script to Maya for execution...")
    try:
        client.sendall(script_content.encode('utf-8'))
        
        # Wait for a response, but don't hang forever
        try:
            response = client.recv(4096).decode('utf-8')
            if response:
                print(f"Maya Response: {response}")
        except socket.timeout:
            print("Script sent, but Maya is taking a long time to respond (Processing...)")
            
        print("--- Script execution complete ---")
    except Exception as e:
        print(f"An error occurred while executing the script in Maya: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
