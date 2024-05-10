import socket
import threading
import tkinter as tk

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Application")
        
        self.message_listbox = tk.Listbox(master, width=50, height=20)
        self.message_listbox.pack(pady=10)
        
        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack(pady=5)
        
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()
        
        # Create a socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        self.client_socket.connect(("127.0.0.1", 5555))
        
        # Start a thread to receive messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
    
    def send_message(self):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        self.client_socket.send(message.encode())
    
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                self.message_listbox.insert(tk.END, message)
            except ConnectionResetError:
                break

def main():
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
