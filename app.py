from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Expanded Mock Data (Now with Descriptions) ---
PREMIUM_RENTALS = [
    {
        "id": 1, 
        "name": "Chanel Classic Flap", 
        "price": "12,500", 
        "category": "Rent",
        "condition": "Pristine",
        "dimensions": "15.5 × 25.5 × 6.5 cm",
        "desc": "The quintessential classic. Crafted in black lambskin with gold-tone metal hardware. Perfect for galas and high-profile events.",
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2, 
        "name": "Hermès Birkin 30", 
        "price": "35,000", 
        "category": "Rent",
        "condition": "Like New",
        "dimensions": "30 × 22 × 16 cm",
        "desc": "The ultimate symbol of luxury. This Gold Togo leather piece creates an immediate statement of sophistication.",
        "image": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 3, 
        "name": "Dior Saddle Bag", 
        "price": "9,500", 
        "category": "Rent",
        "condition": "Excellent",
        "dimensions": "25.5 x 20 x 6.5 cm",
        "desc": "Maria Grazia Chiuri’s fresh update to the iconic Saddle bag. Features the emblematic D-stirrup magnetic clasp.",
        "image": "https://images.unsplash.com/photo-1590739225287-bd2f51a7b818?q=80&w=800&auto=format&fit=crop"
    }
]

SHOP_ITEMS = [
    {
        "id": 1, 
        "name": "Vintage LV Keepall", 
        "price": "1,20,000", 
        "category": "Shop",
        "condition": "Vintage (Grade A)",
        "dimensions": "50 x 29 x 22 cm",
        "desc": "An icon since the 1930s, the Keepall embodies the spirit of modern travel. Light patina on the leather handles.",
        "image": "https://images.unsplash.com/photo-1524498250077-390f9e378fc0?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2, 
        "name": "Gucci Jackie 1961", 
        "price": "1,85,000", 
        "category": "Shop",
        "condition": "Brand New",
        "dimensions": "28 x 19 x 4.5 cm",
        "desc": "The re-edition of the archive style. The Jackie 1961 is a symbol of the House's ever-evolving design narrative.",
        "image": "https://images.unsplash.com/photo-1605733513597-a8f8341084e6?q=80&w=800&auto=format&fit=crop"
    }
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

# NEW: Dynamic Product Page Route
@app.route('/product/<type>/<int:id>')
def product_detail(type, id):
    # Determine which list to search
    inventory = PREMIUM_RENTALS if type == 'rent' else SHOP_ITEMS
    # Find the item by ID
    item = next((i for i in inventory if i['id'] == id), None)
    if item:
        return render_template('product_detail.html', item=item)
    return redirect(url_for('index'))

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('lend.html')

if __name__ == '__main__':
    app.run(debug=True)
