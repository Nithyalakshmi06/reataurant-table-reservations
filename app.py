from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

DATA_FILE = "reservations.txt"

def get_next_id():
    """Get the next reservation ID, ignoring blank lines."""
    if not os.path.exists(DATA_FILE):
        return 1
    with open(DATA_FILE, "r") as f:
        lines = [line for line in f if line.strip()]  # remove blank lines
    return len(lines) + 1

# ✅ Home Page
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Handle Quick Booking from Index Page
@app.route('/submit_quick_booking', methods=['POST'])
def submit_quick_booking():
    name = request.form.get('name', '').strip()
    phone = request.form.get('phone', '').strip()

    reservation_id = get_next_id()

    with open(DATA_FILE, "a") as f:
        f.write(f"{reservation_id} | {name} |  |  |  |  |  | {phone}\n")

    return redirect(url_for('index'))

# ✅ Menu Page
@app.route('/menu')
def menu():
    return render_template('menu.html')

# ✅ Shop Page
@app.route('/shop')
def shop():
    return render_template('shop.html')

# ✅ About Page
@app.route('/about')
def about():
    return render_template('about.html')

# ✅ Reservation Page
@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

# ✅ Handle Reservation Form Submission
@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    name = request.form.get('name', '').strip()
    date = request.form.get('date', '').strip()
    time = request.form.get('time', '').strip()
    rtype = request.form.get('type', '').strip()
    location = request.form.get('location', '').strip()
    message = request.form.get('message', '').strip()

    reservation_id = get_next_id()

    with open(DATA_FILE, "a") as f:
        f.write(f"{reservation_id} | {name} | {date} | {time} | {rtype} | {location} | {message} | \n")

    return redirect(url_for('index'))

# ✅ Manager Page - View Reservations
@app.route('/reserved')
def reserved():
    reservations = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.strip():
                    reservations.append(line.strip().split(" | "))
    return render_template('reserved.html', reservations=reservations)

# ✅ Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
