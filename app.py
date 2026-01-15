from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Mock Data (Replace with Database later) ---
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
    # Premium Rentals Catalog
    return render_template('rent.html', items=PREMIUM_RENTALS)

@app.route('/shop')
def shop():
    # E-commerce Section
    return render_template('shop.html', items=SHOP_ITEMS)

@app.route('/lend', methods=['GET', 'POST'])
def lend():
    # Peer-to-Peer Lending Form
    if request.method == 'POST':
        # Logic to save user submission would go here
        return redirect(url_for('index'))
    return render_template('lend.html')

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TheBaëclub | Luxury Fashion House</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <nav class="navbar fade-in">
        <div class="logo">
            <a href="/">TheBaëclub</a>
        </div>
        <ul class="nav-links">
            <li><a href="{{ url_for('rent') }}">Rent</a></li>
            <li><a href="{{ url_for('lend') }}">Lend</a></li>
            <li><a href="{{ url_for('shop') }}">Shop</a></li>
            <li><a href="#" class="btn-outline">Login</a></li>
        </ul>
        <div class="hamburger">
            <span></span>
            <span></span>
        </div>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <div class="footer-content">
            <p>&copy; 2026 TheBaëclub. Redefining Ownership.</p>
            <div class="socials">
                <a href="#">Instagram</a>
                <a href="#">TikTok</a>
            </div>
        </div>
    </footer>

</body>
</html>
{% extends 'base.html' %}

{% block content %}
<section class="hero">
    <div class="hero-overlay"></div>
    <div class="hero-content fade-in-up">
        <h1>Curated Luxury.<br>Accessible to the Few.</h1>
        <p>Rent the runway’s finest or monetize your own collection.</p>
        <div class="cta-group">
            <a href="{{ url_for('rent') }}" class="btn-primary">Explore Collection</a>
            <a href="{{ url_for('lend') }}" class="btn-secondary">List Your Bag</a>
        </div>
    </div>
</section>

<section class="philosophy">
    <h2>The Baë Standard</h2>
    <p>We bridge the gap between ownership and experience. <br>Authentication guaranteed.</p>
</section>
{% endblock %}
{% extends 'base.html' %}

{% block content %}
<section class="catalog-header">
    <h2>The Premium Collection</h2>
</section>
<section class="product-grid">
    {% for item in items %}
    <div class="product-card fade-in">
        <div class="image-wrapper">
            <img src="{{ item.image }}" alt="{{ item.name }}">
        </div>
        <div class="product-info">
            <h3>{{ item.name }}</h3>
            <p>${{ item.price }} / Day</p>
            <button class="btn-text">Reserve Now</button>
        </div>
    </div>
    {% endfor %}
</section>
{% endblock %}
/* --- Variables & Reset --- */
:root {
    --brand-copper: #BA7C4D; 
    --brand-cream: #F9F7F2;
    --text-dark: #1C1C1C;
    --text-light: #FFFFFF;
    --font-serif: 'Playfair Display', serif;
    --font-sans: 'Lato', sans-serif;
    --transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: var(--brand-cream);
    color: var(--text-dark);
    font-family: var(--font-sans);
    line-height: 1.6;
    overflow-x: hidden;
}

h1, h2, h3, .logo {
    font-family: var(--font-serif);
    font-weight: 400;
}

/* --- Navigation --- */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem 5%;
    background: transparent;
    position: absolute;
    width: 100%;
    z-index: 10;
}

.logo a {
    font-size: 2rem;
    text-decoration: none;
    color: var(--text-dark);
    letter-spacing: -1px;
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 3rem;
}

.nav-links a {
    text-decoration: none;
    color: var(--text-dark);
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: var(--transition);
}

.nav-links a:hover {
    color: var(--brand-copper);
}

/* --- Hero Section --- */
.hero {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    /* Placeholder for a luxury fashion background image */
    background: url('https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=2069&auto=format&fit=crop') no-repeat center center/cover;
    position: relative;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.2); /* Slight dark tint for text readability */
}

.hero-content {
    position: relative;
    z-index: 2;
    color: var(--text-light);
}

.hero h1 {
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 1.5rem;
}

/* --- Buttons --- */
.cta-group {
    margin-top: 2rem;
    display: flex;
    gap: 1.5rem;
    justify-content: center;
}

.btn-primary, .btn-secondary {
    padding: 1rem 2.5rem;
    text-decoration: none;
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 2px;
    transition: var(--transition);
}

.btn-primary {
    background-color: var(--brand-copper);
    color: var(--text-light);
    border: 1px solid var(--brand-copper);
}

.btn-primary:hover {
    background-color: transparent;
    border-color: var(--text-light);
}

.btn-secondary {
    background-color: transparent;
    color: var(--text-light);
    border: 1px solid var(--text-light);
    backdrop-filter: blur(5px);
}

.btn-secondary:hover {
    background-color: var(--text-light);
    color: var(--text-dark);
}

/* --- Product Grid (For Shop/Rent) --- */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 3rem;
    padding: 5% 10%;
}

.product-card {
    cursor: pointer;
}

.image-wrapper {
    overflow: hidden;
    margin-bottom: 1rem;
}

.image-wrapper img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.product-card:hover img {
    transform: scale(1.05);
}

.product-info h3 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.product-info p {
    color: var(--brand-copper);
    font-weight: bold;
}

/* --- Animations --- */
.fade-in {
    opacity: 0;
    animation: fadeIn 1.2s ease forwards;
}

.fade-in-up {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 1s ease forwards 0.5s;
}

@keyframes fadeIn {
    to { opacity: 1; }
}

@keyframes fadeInUp {
    to { 
        opacity: 1; 
        transform: translateY(0); 
    }
}

/* --- Footer --- */
footer {
    padding: 3rem;
    text-align: center;
    border-top: 1px solid #ddd;
    margin-top: 4rem;
}
