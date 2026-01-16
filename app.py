from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- INVENTORY DATA ---
PREMIUM_RENTALS = [
    {
        "id": 1, "name": "Chanel Classic Flap", "price": "12,500", "category": "Rent",
        "condition": "Pristine", "dimensions": "15.5 × 25.5 × 6.5 cm",
        "desc": "The quintessential classic in caviar leather. Gold-tone hardware.",
        "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2, "name": "Hermès Birkin 30", "price": "35,000", "category": "Rent",
        "condition": "Like New", "dimensions": "30 × 22 × 16 cm",
        "desc": "Gold Togo leather. The ultimate symbol of status and craftsmanship.",
        "image": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 3, "name": "Lady Dior Mini", "price": "14,000", "category": "Rent",
        "condition": "Excellent", "dimensions": "17 x 15 x 7 cm",
        "desc": "Cannage lambskin in cloud blue. A poetic nod to the House's heritage.",
        "image": "https://images.unsplash.com/photo-1591561954557-26941169b49e?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 4, "name": "Bottega Veneta Jodie", "price": "11,500", "category": "Rent",
        "condition": "New Season", "dimensions": "23 x 28 x 8 cm",
        "desc": "The Teen Jodie in signature Intrecciato weave. Effortless chic.",
        "image": "https://images.unsplash.com/photo-1618214300609-026848149e91?q=80&w=800&auto=format&fit=crop"
    }
]

SHOP_ITEMS = [
    {
        "id": 101, "name": "Vintage LV Keepall 55", "price": "1,20,000", "category": "Shop",
        "condition": "Vintage (Grade A)", "dimensions": "55 x 31 x 24 cm",
        "desc": "Monogram canvas. The icon of modern travel since 1930.",
        "image": "https://images.unsplash.com/photo-1524498250077-390f9e378fc0?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 102, "name": "Gucci Jackie 1961", "price": "1,85,000", "category": "Shop",
        "condition": "Brand New", "dimensions": "28 x 19 x 4.5 cm",
        "desc": "The re-edition of the archive style with piston closure.",
        "image": "https://images.unsplash.com/photo-1605733513597-a8f8341084e6?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 103, "name": "YSL Envelope Chain", "price": "1,65,000", "category": "Shop",
        "condition": "New", "dimensions": "24 x 17 x 6 cm",
        "desc": "Mix of vertical, chevron and diamond quilted grain de poudre leather.",
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=800&auto=format&fit=crop"
    }
]

# --- JOURNAL ENTRIES (Editorial) ---
JOURNAL = [
    {"title": "The Art of the Archive", "date": "OCT 12", "img": "https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=800&auto=format&fit=crop"},
    {"title": "Paris Fashion Week Recap", "date": "OCT 05", "img": "https://images.unsplash.com/photo-1496747611176-843222e1e57c?q=80&w=800&auto=format&fit=crop"},
    {"title": "Investing in Hermès", "date": "SEP 28", "img": "https://images.unsplash.com/photo-1566150905458-1bf1dad1fb56?q=80&w=800&auto=format&fit=crop"}
]

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html', journal=JOURNAL, featured=PREMIUM_RENTALS[:2])

@app.route('/rent')
def rent():
    return render_template('rent.html', items=PREMIUM_RENTALS)

@app.route('/shop')
def shop():
    return render_template('shop.html', items=SHOP_ITEMS)

@app.route('/product/<type>/<int:id>')
def product_detail(type, id):
    inventory = PREMIUM_RENTALS if type == 'rent' else SHOP_ITEMS
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
