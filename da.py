from flask import Flask, render_template, request, redirect
from database import add_url , get_url


app = Flask(__name__) 



@app.route('/')
def method_name():
    return render_template('main.html')

@app.route('/new_link', methods=['GET', 'POST'])
def link():
    if request.method == 'GET':
        return render_template('create_url.html')
    elif request.method == 'POST':
        url2 = request.form['url']
        link = add_url(url2)
        host = request.host
        return render_template('url.html', link=link, host=host)

@app.route('/link/<url>', methods=['GET', 'POST'])
def url_check(url):
    print(url)
    link_for_redirect = get_url(url)
    if link_for_redirect: return redirect(link_for_redirect)
    else: return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
