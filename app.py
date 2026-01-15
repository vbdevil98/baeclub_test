from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Real Luxury Images & INR Prices ---
PREMIUM_RENTALS = [
    {
        "id": 1, 
        "name": "Chanel Classic Flap", 
        "price": "12,500", 
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2, 
        "name": "Hermès Birkin 30", 
        "price": "35,000", 
        "image": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 3, 
        "name": "Dior Saddle Bag", 
        "price": "9,500", 
        "image": "https://images.unsplash.com/photo-1590739225287-bd2f51a7b818?q=80&w=800&auto=format&fit=crop"
    }
]

SHOP_ITEMS = [
    {
        "id": 1, 
        "name": "Vintage LV Keepall", 
        "price": "1,20,000", 
        "image": "https://images.unsplash.com/photo-1524498250077-390f9e378fc0?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2, 
        "name": "Gucci Jackie 1961", 
        "price": "1,85,000", 
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

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('lend.html')

if __name__ == '__main__':
    app.run(debug=True)
