import random
import string
import sqlite3
from flask import Flask, render_template , request , redirect

def random_url() -> str:
    characters = string.ascii_letters + string.digits
    url = ''.join(random.choice(characters) for _ in range(5))
    return url



app = Flask(__name__)

conn = sqlite3.connect('urls.db',check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def method_name():
    return render_template('main.html')
    
@app.route('/new_link', methods=['GET', 'POST'])
def link():
    if request.method == 'GET': return render_template('create_url.html')
    elif request.method ==  'POST':
        url2 = request.form['url']
        link = random_url()
        cursor.execute('INSERT INTO urls_code VALUES(? , ?  )', (url2,link))
        conn.commit()
        return render_template('url.html',link=link)
        
@app.route('/link/<url>',methods=['GET', 'POST'])
def url_check(url):
    url1 = cursor.execute('SELECT urls FROM urls_code WHERE code = ?',(url,)).fetchone()
    if not url1:
        return redirect('/')
    else:
        return redirect(url1[0])


      

if __name__ == '__main__':
    app.run(debug=True)
 
