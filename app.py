from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Mock Data ---
PREMIUM_RENTALS = [
    {"id": 1, "name": "Chanel Classic Flap", "price": "150", "image": "https://via.placeholder.com/400x500?text=Chanel"},
    {"id": 2, "name": "Hermès Birkin 30", "price": "400", "image": "https://via.placeholder.com/400x500?text=Hermes"},
    {"id": 3, "name": "Dior Saddle Bag", "price": "120", "image": "https://via.placeholder.com/400x500?text=Dior"}
]

SHOP_ITEMS = [
    {"id": 1, "name": "Vintage LV Keepall", "price": "1200", "image": "https://via.placeholder.com/400x500?text=LV+Keepall"},
    {"id": 2, "name": "Gucci Jackie 1961", "price": "1800", "image": "https://via.placeholder.com/400x500?text=Gucci+Jackie"}
]

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rent')
def rent():
    return render_template('rent.html', items=PREMIUM_RENTALS)

@app.route('/shop')
def shop():
    return render_template('shop.html', items=SHOP_ITEMS)

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        # Logic to save user submission would go here
        return redirect(url_for('index'))
    return render_template('lend.html')

if __name__ == '__main__':
    app.run(debug=True)
