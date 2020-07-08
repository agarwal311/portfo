from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    #return 'Hello, World!'
    #return 'Hello, Devyanshi Agarwal!'
    return render_template('index.html')

@app.route('/<string:page_name>')               # This is used to get rid of copying the function again and again.
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode = 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)     # inside the quotechar, we can give any thing.
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data =  request.form.to_dict()              # .to_dict() = to get the data in the form of dictionary.
            #write_to_file(data)
            write_to_csv(data)
            #return 'Form submitted hoorrrraaayyy..'
            return redirect('/thank_you.html')
        except:
            return 'Did not save to database'
    else:
        return 'Oops, something went wrong. Try again!!!'


'''
@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs..'

@app.route('/blog/2020/bunnies')
def blog2():
    return 'This is my bunny..'

'''