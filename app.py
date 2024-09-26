from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# إعدادات البريد الإلكتروني
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        
        msg = Message('New Contact Message from L E MW',
                      sender='your-email@gmail.com',
                      recipients=['lemwcompany@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        
        mail.send(msg)
        return redirect('/thankyou')
    
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return 'Thank you for your message!'

if __name__ == '__main__':
    app.run(debug=True)
