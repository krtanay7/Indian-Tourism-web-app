from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import bcrypt
import secrets
from email.mime.text import MIMEText
import smtplib
import time


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong, random secret key

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  #use your own userID
    'password': 'user123', # use your own database password
    'database': 'heritage',
}

# Helper function to get a database connection
def get_db_connection():
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def index1():
    return render_template('index.html')
@app.route('/try.html')
def try1():
    return render_template('try.html')


@app.route('/booking.html')
def booking():
    return render_template('booking.html')
'''
@app.route('/booking1.html')
def booking1():
    return render_template('booking1.html')
    '''
@app.route('/destination.html')
def destination():
    return render_template('destination.html')

@app.route('/booking1.html', methods=['GET', 'POST'])
def booking1():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        from_location = request.form.get('from_location')
        to_location = request.form.get('to_location')
        date = request.form.get('date')
        adult_count = request.form.get('adult_count', 0)
        child_count = request.form.get('child_count', 0)
        phone = request.form.get('phone')
        total_price = request.form.get('price')

        # Convert counts to integers
        adult_count = int(adult_count)
        child_count = int(child_count)

         # Calculate prices
        adult_price = 333  # Example price per adult
        child_price = 170  # Example price per child
        total_adult_price = adult_count * adult_price
        total_child_price = child_count * child_price
        total_price = total_adult_price + total_child_price
        
        # Insert data into MySQL database
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    INSERT INTO booking (name, email, from_location, to_location, date, adult, child, phone,total_price)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
                """
                cursor.execute(query, (name, email, from_location, to_location, date, adult_count, child_count, phone, total_price))
                conn.commit()
                price = (adult_count * 333) + (child_count * 170)  # Assuming price calculation
                flash(f'Booking confirmed successfully!   Name: {name},  From: {from_location},   To: {to_location},  Passengers: {adult_count}  Adults, {child_count} Children, Phone: {phone}, Email: {email}, Journey Date and Time: {date}, Price: Rs:{price}', 'success')

            #   flash('Booking confirmed successfully!', 'success')
              
                return render_template('booking1.html')
            except Exception as e:
                print(f"Error: {e}")
                flash('There was an error saving your booking.', 'error')
            finally:
                cursor.close()
                conn.close()
        else:
            flash('Unable to connect to the database.', 'error')
    
    return render_template('booking1.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM user WHERE email=%s", (email,))
            user = cursor.fetchone()
            
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                session['username'] = user['username']
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            
            else:
                flash('Invalid email or password', 'danger')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('login.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        phone = request.form['phone']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return render_template('signup.html')
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO user(username, password, email, phone) VALUES (%s, %s, %s, %s)",
                           (username, hashed_password.decode('utf-8'), email, phone))
            conn.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            conn.rollback()
            flash('Username already exists!', 'danger')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('signup.html')

@app.route('/reset_password.html')
def reset_password1():
    return render_template('reset_password.html')

@app.route('/andhrapradesh.html')
def andhrapradesh():
    return render_template('andhrapradesh.html')

@app.route('/bihar.html')
def bihar():
    return render_template('bihar.html')

@app.route('/gujarat.html')
def gujarat():
    return render_template('gujarat.html')



@app.route('/kerala.html')
def kerala():
    return render_template('kerala.html')

@app.route('/maharashtra.html')
def maharashtra():
    return render_template('maharashtra.html')

@app.route('/manipur.html')
def manipur():
    return render_template('manipur.html')

@app.route('/mp.html')
def mp():
    return render_template('mp.html')

@app.route('/odisha.html')
def odisha():
    return render_template('odisha.html')

@app.route('/punjab.html')
def punjab():
    return render_template('punjab.html')

@app.route('/rajasthan.html')
def rajasthan():
    return render_template('rajasthan.html')

@app.route('/tn.html')
def tn():
    return render_template('tn.html')

@app.route('/telangana.html')
def telangana():
    return render_template('telangana.html')

@app.route('/aboutUs.html')
def aboutUs():
    
    return render_template('aboutUs.html')
@app.route('/contact1.html')
def contact():
    return render_template('contact1.html')

@app.route('/contact1', methods=['GET', 'POST'])
def contact1():
    if request.method == 'POST':
        name = request.form['consumer_name']
        email = request.form['email']
        phone = request.form['phone']
        feedback = request.form['feedback']

        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO contactus (name, email, phone, feedback)
                           VALUES (%s, %s, %s, %s)"""
                cursor.execute(query, (name, email, phone, feedback))
                connection.commit()
                flash('Thank you for your feedback!', 'success')
                return redirect(url_for('contact1'))
            except mysql.connector.IntegrityError as e:
                print(f"Error: {e}")
                flash('An error occurred. Please try again.', 'danger')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Unable to connect to the database.', 'danger')

    return render_template('contact1.html')




# gmail forgot 

# Helper function to send email
# gmail forgot 
def send_email(subject, recipient, body):
    sender_email = 'kumar777788889999000@gmail.com'
    sender_password = 'abc@1234567'  # Replace with your email password
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
           # time.sleep(2)
            server.login(sender_email, sender_password)
           # time.sleep(3)
            server.send_message(msg)
            print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

@app.route('/forgot_password.html', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM user WHERE email=%s", (email,))
            user = cursor.fetchone()

            if user:
                token = secrets.token_urlsafe(20)
                cursor.execute("UPDATE user SET reset_token=%s WHERE email=%s", (token, email))
                conn.commit()
                
                reset_link = url_for('reset_password', token=token, _external=True)
                email_body = f'Click the following link to reset your password: {reset_link}'
                send_email('Password Reset Request', email, email_body)

                flash('A password reset link has been sent to your email address.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Email address not found.', 'danger')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('forgot_password.html')

@app.route('/reset_password.html/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return render_template('reset_password.html', token=token)

        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT email FROM user WHERE reset_token=%s", (token,))
            user = cursor.fetchone()

            if user:
                email = user['email']
                cursor.execute("UPDATE user SET password=%s, reset_token=NULL WHERE email=%s", (hashed_password.decode('utf-8'), email))
                conn.commit()
                
                flash('Password has been reset successfully! You can now log in.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Invalid or expired token.', 'danger')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('reset_password.html', token=token)

@app.route('/subscribe.html', methods=['POST'])
def subscribe():
    email = request.form['email'].strip()
    
    # Validate email
    if not email or '@' not in email:
        flash('Invalid email address.')
        return redirect(url_for('index'))
    
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            # Prepare and execute the SQL statement
            query = "INSERT INTO subscriptions (email) VALUES (%s)"
            cursor.execute(query, (email,))
            connection.commit()
            flash('Thank you for subscribing!')
    
    except Exception as e:
        flash(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return render_template('/subscribe.html')


if __name__ == '__main__':
    app.run(debug=True)

