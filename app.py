from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Mock Database ---
# Note: Prices are in INR (₹)
PREMIUM_RENTALS = [
    {
        "id": 1, 
        "name": "Chanel Classic Flap", 
        "price": "12,500", 
        "category": "Rent", 
        "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop",
        "desc": "Black lambskin with gold-tone metal hardware."
    },
    {
        "id": 2, 
        "name": "Hermès Birkin 30", 
        "price": "35,000", 
        "category": "Rent", 
        "image": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?q=80&w=800&auto=format&fit=crop",
        "desc": "Gold Togo leather with palladium hardware."
    },
    {
        "id": 3, 
        "name": "Dior Saddle Bag", 
        "price": "9,500", 
        "category": "Rent", 
        # Updated to a reliable high-res image
        "image": "https://images.unsplash.com/photo-1591561954557-26941169b49e?q=80&w=800&auto=format&fit=crop",
        "desc": "Blue Dior Oblique Jacquard."
    }
]

STATEMENT_BAGS = [
    {
        "id": 101, 
        "name": "Jacquemus Le Chiquito", 
        "price": "1,200", 
        "category": "Statement", 
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=800&auto=format&fit=crop",
        "desc": "The micro bag icon. Perfect for events."
    },
    {
        "id": 102, 
        "name": "YSL Envelope Clutch", 
        "price": "1,500", 
        "category": "Statement", 
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop",
        "desc": "Matelassé leather in classic noir."
    },
    {
        "id": 103, 
        "name": "Vintage LV Pochette", 
        "price": "950", 
        "category": "Statement", 
        "image": "https://images.unsplash.com/photo-1583573636246-18cb2246697f?q=80&w=800&auto=format&fit=crop",
        "desc": "The Y2K classic. Monogram canvas."
    }
]

JOURNAL_POSTS = [
    {"id": 1, "title": "The Quiet Luxury Trend", "date": "OCT 2025", "image": "https://images.unsplash.com/photo-1469334031218-e382a71b716b?q=80&w=800"},
    {"id": 2, "title": "Caring for Lambskin", "date": "SEP 2025", "image": "https://images.unsplash.com/photo-1550614000-4b9519e02a48?q=80&w=800"}
]

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rent')
def rent():
    return render_template('catalog.html', title="Premium Rentals", subtitle="The core collection.", items=PREMIUM_RENTALS, type='rent')

@app.route('/shop')
def shop():
    return render_template('catalog.html', title="Statement Bags", subtitle="Curated accessories starting at ₹950.", items=STATEMENT_BAGS, type='shop')

@app.route('/journal')
def journal():
    return render_template('journal.html', posts=JOURNAL_POSTS)

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('lend.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/check_availability/<int:id>')
def check_availability(id):
    # Determine source list
    item = next((i for i in PREMIUM_RENTALS if i['id'] == id), None)
    if not item:
        item = next((i for i in STATEMENT_BAGS if i['id'] == id), None)
    return render_template('availability.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
