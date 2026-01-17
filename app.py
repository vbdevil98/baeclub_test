from flask import Flask, render_template, request, redirect, url_for, flash
import datetime

app = Flask(__name__)
app.secret_key = 'luxury_secret_key_change_this_in_prod' # Required for flash messages

# --- Mock Data ---
PREMIUM_RENTALS = [
    {"id": 1, "name": "Chanel Classic Flap", "price": 12500, "category": "Rent", "condition": "Pristine", "dimensions": "15.5 × 25.5 × 6.5 cm", "desc": "The quintessential classic. Crafted in black lambskin with gold-tone metal hardware.", "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800"},
    {"id": 2, "name": "Hermès Birkin 30", "price": 35000, "category": "Rent", "condition": "Like New", "dimensions": "30 × 22 × 16 cm", "desc": "The ultimate symbol of luxury. This Gold Togo leather piece creates an immediate statement.", "image": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?q=80&w=800"},
    {"id": 3, "name": "Dior Saddle Bag", "price": 9500, "category": "Rent", "condition": "Excellent", "dimensions": "25.5 x 20 x 6.5 cm", "desc": "Maria Grazia Chiuri’s fresh update to the iconic Saddle bag.", "image": "https://images.unsplash.com/photo-1590739225287-bd2f51a7b818?q=80&w=800"}
]

SHOP_ITEMS = [
    {"id": 1, "name": "Vintage LV Keepall", "price": 120000, "category": "Shop", "condition": "Vintage (Grade A)", "dimensions": "50 x 29 x 22 cm", "desc": "An icon since the 1930s, the Keepall embodies the spirit of modern travel.", "image": "https://images.unsplash.com/photo-1524498250077-390f9e378fc0?q=80&w=800"},
    {"id": 2, "name": "Gucci Jackie 1961", "price": 185000, "category": "Shop", "condition": "Brand New", "dimensions": "28 x 19 x 4.5 cm", "desc": "The re-edition of the archive style. A symbol of the House's design narrative.", "image": "https://images.unsplash.com/photo-1605733513597-a8f8341084e6?q=80&w=800"}
]

JOURNAL_POSTS = [
    {"title": "The Art of Authentication", "date": "Oct 12, 2025", "image": "https://images.unsplash.com/photo-1550614000-4b9519e02d48?q=80&w=800"},
    {"title": "Spring/Summer 2026 Forecast", "date": "Jan 05, 2026", "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=800"},
    {"title": "Care Guide: Exotic Leathers", "date": "Dec 28, 2025", "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?q=80&w=800"}
]

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rent')
def rent():
    # Helper to format price with commas for display
    return render_template('shop.html', items=PREMIUM_RENTALS, page_title="Rent the Runway")

@app.route('/shop')
def shop():
    return render_template('shop.html', items=SHOP_ITEMS, page_title="Statement Bags")

@app.route('/journal')
def journal():
    return render_template('journal.html', posts=JOURNAL_POSTS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Mock login logic
        flash('Welcome back to the club.', 'success')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/product/<type>/<int:id>')
def product_detail(type, id):
    inventory = PREMIUM_RENTALS if type == 'Rent' or type == 'rent' else SHOP_ITEMS
    item = next((i for i in inventory if i['id'] == id), None)
    if item:
        # Pass the 'type' to the template so we know if we should show 'Rent Now' or 'Buy Now'
        return render_template('product_detail.html', item=item, type=type)
    return redirect(url_for('index'))

@app.route('/availability/<int:id>', methods=['GET', 'POST'])
def availability(id):
    # Mock finding item
    item = next((i for i in PREMIUM_RENTALS if i['id'] == id), None)
    if request.method == 'POST':
        flash('Dates confirmed. Please proceed to checkout.', 'success')
        return redirect(url_for('index'))
    return render_template('availability.html', item=item)

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        # In a real app, you would handle the file upload here
        flash('Your submission has been received. Our curators will review it shortly.', 'success')
        return redirect(url_for('index'))
    return render_template('lend.html')

if __name__ == '__main__':
    app.run(debug=True)
