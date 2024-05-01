from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are correct
        if username == 'Prince143' and password == 'Prince143':
            # Redirect to the specified link if login is successful
            return redirect('https://PRINCE-ALL-SERVER-HERE.replit.app/')
        else:
            return 'Invalid username or password. Please try again.'

    return '''
    <html>
    <head>
        <style>
        body {
        background-image: url('https://r2.easyimg.io/1n8cljykg/51606761c64d53f37337be66a75abdeb.jpg');
        background-size: cover;
    }
    body {
      font-family: Arial, sans-serif;
    }
    
    .container {
      width: 300px;
      margin: 0 auto;
      margin-top: 100px;
      border: 1px solid #ccc;
      padding: 20px;
    }
    
    .container label, .container input[type="text"], .container input[type="password"] {
      display: block;
      width: 100%;
      margin-bottom: 10px;
    }
    
    .container button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }

    .container button:hover {
      background-color: #45a049;
    }
  </style>
    </head>
    <body>
        <div class="container">
            <h1 style="color: white;"> SERVER 2 LOGIN </h1>
            <form method="POST" action="/">
                <div class="form-group">
                    <label for="username"style="color: white;">Username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="password"style="color: white;">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit" class="btn">Login</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
