from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Data: Rentals (Includes new ₹1200 range statement bags) ---
PREMIUM_RENTALS = [
    {
        "id": 1, 
        "name": "Chanel Classic Flap", 
        "price": "12,500", 
        "category": "Iconic",
        "condition": "Pristine",
        "dimensions": "15.5 × 25.5 × 6.5 cm",
        "desc": "The quintessential classic. Crafted in black lambskin with gold-tone metal hardware.",
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2, 
        "name": "Hermès Birkin 30", 
        "price": "35,000", 
        "category": "Iconic",
        "condition": "Like New",
        "dimensions": "30 × 22 × 16 cm",
        "desc": "The ultimate symbol of luxury. This Gold Togo leather piece creates an immediate statement.",
        "image": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 3, 
        "name": "Dior Saddle Bag", 
        "price": "9,500", 
        "category": "Iconic",
        "condition": "Excellent",
        "dimensions": "25.5 x 20 x 6.5 cm",
        "desc": "Maria Grazia Chiuri’s fresh update to the iconic Saddle bag.",
        "image": "https://images.unsplash.com/photo-1591561954557-26941169b49e?q=80&w=800&auto=format&fit=crop"
    },
    # NEW: Statement Bags (Lower Price Range for Rent)
    {
        "id": 4, 
        "name": "Jacquemus Le Chiquito", 
        "price": "1,200", 
        "category": "Statement",
        "condition": "Good",
        "dimensions": "12 x 6 cm",
        "desc": "The micro bag that started it all. A perfect pop of color for brunch.",
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 5, 
        "name": "YSL Monogram Clutch", 
        "price": "1,500", 
        "category": "Statement",
        "condition": "Vintage",
        "dimensions": "24 x 14 cm",
        "desc": "Classic evening wear. Black grain de poudre textured matelassé leather.",
        "image": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?q=80&w=800&auto=format&fit=crop"
    }
]

# --- Data: Shop (Selling) ---
SHOP_ITEMS = [
    {
        "id": 101, 
        "name": "Vintage LV Keepall", 
        "price": "1,20,000", 
        "category": "Travel",
        "condition": "Vintage (Grade A)",
        "desc": "An icon since the 1930s, the Keepall embodies the spirit of modern travel.",
        "image": "https://images.unsplash.com/photo-1524498250077-390f9e378fc0?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 102, 
        "name": "Gucci Jackie 1961", 
        "price": "1,85,000", 
        "category": "Archive",
        "condition": "Brand New",
        "desc": "The re-edition of the archive style. A symbol of the House's ever-evolving design.",
        "image": "https://images.unsplash.com/photo-1605733513597-a8f8341084e6?q=80&w=800&auto=format&fit=crop"
    }
]

# --- Data: Journal ---
JOURNAL_POSTS = [
    {"id": 1, "title": "The Rise of Quiet Luxury", "date": "Oct 12", "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=800"},
    {"id": 2, "title": "Care Guide: Lambskin vs. Caviar", "date": "Sep 28", "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800"},
    {"id": 3, "title": "Investment Pieces for 2026", "date": "Sep 15", "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800"}
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

@app.route('/journal')
def journal():
    return render_template('journal.html', posts=JOURNAL_POSTS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/product/<type>/<int:id>')
def product_detail(type, id):
    inventory = PREMIUM_RENTALS if type == 'rent' else SHOP_ITEMS
    item = next((i for i in inventory if i['id'] == id), None)
    if item:
        return render_template('product_detail.html', item=item)
    return redirect(url_for('index'))

@app.route('/check_availability/<int:id>', methods=['GET', 'POST'])
def check_availability(id):
    item = next((i for i in PREMIUM_RENTALS if i['id'] == id), None)
    if request.method == 'POST':
        # Logic to process dates would go here
        return redirect(url_for('index'))
    return render_template('availability.html', item=item)

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('lend.html')

if __name__ == '__main__':
    app.run(debug=True)
