from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
from flask_mysqldb import MySQL

import string

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '78520'
app.config['MYSQL_DB'] = 'bookreview'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

mysql = MySQL(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT Email FROM Users')
        email_results = cur.fetchall()
        for i in range(0, len(email_results)):
            if (email_results[i][0] == email):
                cur.close()
                return render_template('register.html', the_message='Email already registered')
        cur.execute('INSERT INTO Users(Name,UserName,Email,Password) VALUES(%s,%s,%s,%s)',
                    (name, username, email, password))
        mysql.connection.commit()
        cur.close()
        flash('You are now registered and can login!!!', 'success')
        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'email' in session:
        return redirect('/dashboard')
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT Email FROM Users')
        email_results = cur.fetchall()
        for i in range(0, len(email_results)):
            if (email_results[i][0] == email):
                cur.execute('SELECT Password FROM Users')
                password_result = cur.fetchall()
                cur.close()
                if (password_result[i][0] == password):
                    session.permanent = False
                    session['logged_in'] = True
                    session['email'] = email
                    flash('You are now logged in', 'success')
                    return redirect('/dashboard')
                else:
                    return render_template('login.html', the_message='Invalid Email or Password')
        cur.close()
        return render_template('login.html', the_message='Invalid Email or Password')
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'email' not in session:
        return redirect('/login')
    return render_template('dashboard.html')


@app.route('/dashboard/search', methods=['POST'])
def search():
    book_detail = request.form['book_detail']
    search_param = request.form['search_param']
    res = list()
    if (search_param == 'ISBN'):
        cur = mysql.connection.cursor()
        cur.execute('SELECT ISBN FROM Books')
        isbn_results = cur.fetchall()
        for i in range(0, len(isbn_results)):
            if (book_detail == isbn_results[i][0]):
                cur.execute('SELECT * FROM Books WHERE ISBN = %s',
                            (book_detail,))
                results = cur.fetchall()
                cur.close()
                return render_template('search.html', results=results)
        cur.close()
        flash('Book not found!!!')
        return redirect('/dashboard')
    elif (search_param == 'Author'):
        cur = mysql.connection.cursor()
        cur.execute('SELECT Author FROM Books')
        author_results = cur.fetchall()
        str1 = list(map(str, (book_detail.lower()).split(' ')))
        for i in range(0, len(author_results)):
            if (book_detail.lower() == author_results[i][0].lower()):
                cur.execute('SELECT * FROM Books WHERE Author = %s',
                            (author_results[i][0],))
                results = cur.fetchall()
                cur.close()
                return render_template('search.html', results=results)
            else:
                str2 = list(
                    map(str, (author_results[i][0].lower()).split(' ')))
                for name1 in str1:
                    for name2 in str2:
                        if (name1 == name2):
                            cur.execute(
                                'SELECT * FROM Books WHERE Author = %s', (author_results[i][0],))
                            results = cur.fetchall()
                            for r in results:
                                res.append(r)
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT Title FROM Books')
        title_results = cur.fetchall()
        str1 = list(map(str, (book_detail.lower()).split(' ')))
        for i in range(0, len(title_results)):
            if (book_detail.lower() == title_results[i][0].lower()):
                cur.execute('SELECT * FROM Books WHERE Author = %s',
                            (title_results[i][0],))
                results = cur.fetchall()
                cur.close()
                return render_template('search.html', results=results)
            else:
                str2 = list(map(str, (title_results[i][0].lower()).split(' ')))
                for name1 in str1:
                    for name2 in str2:
                        if (name1 == name2):
                            cur.execute(
                                'SELECT * FROM Books WHERE Title = %s', (title_results[i][0],))
                            results = cur.fetchall()
                            for r in results:
                                res.append(r)
    cur.close()
    if (len(res) != 0):
        return render_template('search.html', results=res)
    flash('Book not found!!!')
    return redirect('/dashboard')


@app.route('/dashboard/profile', methods=['GET', 'POST'])
def profile():
    if (request.method == 'POST'):
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE Users SET Name = %s,UserName = %s,Password = %s WHERE Email = %s', (name, username,
                                                                                                password, session['email']))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard/profile')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Users WHERE Email = %s', (session['email'],))
    user_details = cur.fetchall()
    cur.execute('SELECT * FROM Reviews WHERE Email = %s', (session['email'],))
    rev = cur.fetchall()
    cur.close()
    return render_template('profile.html', user_details=user_details, total_reviews=len(rev))


@app.route('/dashboard/myreviews')
def myreviews():
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT Review,Rating,ISBN FROM Reviews where Email = %s', (session['email'],))
    user_reviews = cur.fetchall()
    return render_template('myreviews.html', the_reviews=user_reviews, total_reviews=len(user_reviews))


@app.route('/info/<string:isbn>', methods=['GET', 'POST'])
def info(isbn):
    if 'email' not in session:
        return redirect('/login')
    if (request.method == 'POST'):
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM Reviews WHERE Email = %s AND ISBN = %s', (session['email'], isbn))
        rev_user = cur.fetchall()
        review = request.form['addreview']
        star = request.form['star']
        cur.execute('SELECT Title FROM Books WHERE ISBN = %s', (isbn,))
        title = cur.fetchall()
        if (len(rev_user) == 0):
            cur.execute('INSERT INTO Reviews(Book,Review,Email,Rating,ISBN) VALUES(%s,%s,%s,%s,%s)', (title[0][0],
                        review, session['email'], star, isbn))
            mysql.connection.commit()
            cur.close()
        else:
            cur.execute('UPDATE Reviews SET Review = %s,Rating = %s WHERE Email = %s AND ISBN = %s', (review, star,
                                                                                                      session['email'], isbn))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('info', isbn=isbn))
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Books WHERE ISBN = %s', (isbn,))
    book_details = cur.fetchall()
    cur.execute(
        'SELECT Review,Rating,Email FROM Reviews WHERE ISBN = %s', (isbn,))
    rev_rat = cur.fetchall()
    cur.execute('SELECT * FROM Reviews WHERE Email = %s AND ISBN = %s',
                (session['email'], isbn))
    rev_user = cur.fetchall()
    isReview = True
    if (len(rev_user) == 0):
        isReview = False
    names = list()
    avg_rat = 0
    n = 0
    for rev in rev_rat:
        cur.execute('SELECT Name FROM Users WHERE Email = %s', (rev[2],))
        temp = cur.fetchall()
        names.append(temp[0][0])
        avg_rat += float(rev[1])
        n += 1
    if (n):
        avg_rat /= n
        avg_rat = '{0:.2f}'.format(avg_rat)
    cur.close()
    return render_template('info.html', book_details=book_details, rev_rat=rev_rat, no_reviews=len(rev_rat),
                           names=names, avg_rat=avg_rat, isReview=isReview)


@app.route('/edit/<string:isbn>')
def edit(isbn):
    cur = mysql.connection.cursor()
    cur.execute('SELECT Review FROM Reviews WHERE ISBN = %s AND Email = %s',
                (isbn, session['email']))
    review = cur.fetchall()
    flash(review[0][0])
    return redirect(url_for('info', isbn=isbn))


@app.route('/delrev/<string:isbn>')
def delrev(isbn):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Reviews WHERE Email = %s AND ISBN = %s',
                (session['email'], isbn))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('info', isbn=isbn))


@app.route('/delrevmy/<string:isbn>')
def delrevmy(isbn):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Reviews WHERE Email = %s AND ISBN = %s',
                (session['email'], isbn))
    mysql.connection.commit()
    cur.close()
    flash('This review has been deleted!!!')
    return redirect('/dashboard/myreviews')


@app.route('/logout')
def logout():
    if session.get('logged_in'):
        del session['logged_in']
        del session['email']
    flash('You are successfully logged out!!!')
    return redirect('/login')


@app.route('/delacc')
def delacc():
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Users WHERE Email = %s', (session['email'],))
    cur.execute('DELETE FROM Reviews WHERE Email = %s', (session['email'],))
    mysql.connection.commit()
    cur.close()
    del session['logged_in']
    del session['email']
    flash('Your account is deleted successfully!!!')
    return redirect('/register')


@app.route("/api/<string:isbn>")
def api(isbn):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Books WHERE ISBN = %s', (isbn,))
    book = cur.fetchall()
    print(book)
    cur.close()

    if book is None:
        return jsonify({"error": "Invalid ISBN"}), 404

    return jsonify({
        "title": book[0][1],
        "author": book[0][2],
        "isbn": book[0][0]
    })


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)
