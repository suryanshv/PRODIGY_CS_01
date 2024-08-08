from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.
    """
    result = []
    shift = shift % 26
    if not encrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        shift = int(request.form['shift'])
        action = request.form['action']
        
        if action == 'Encrypt':
            result = caesar_cipher(message, shift, encrypt=True)
        elif action == 'Decrypt':
            result = caesar_cipher(message, shift, encrypt=False)
        else:
            result = "Invalid action"
        
        return render_template('index.html', result=result)
    
    return render_template('index.html', result='')

if __name__ == '__main__':
    app.run(debug=True)
