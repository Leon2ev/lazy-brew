import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Connection to MongoDB

app.config["MONGO_DBNAME"] = 'beer_brewing'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# App routes ------------------------------------------------------------

@app.route('/')

# Home page

@app.route('/home_page')
def home_page():
    return render_template("index.html",
    types=mongo.db.types.find())
# Product Routes 
# Product selection

@app.route('/get_products')
def get_products():
    return render_template("products.html",
    types=mongo.db.types.find(),
    products=mongo.db.products.find())

# Single product description
    
@app.route('/get_description/<product_id>')
def get_description(product_id):
    return render_template("description.html",
    brands=mongo.db.brands.find(),
    types=mongo.db.types.find(),
    product=mongo.db.products.find_one({"_id": ObjectId(product_id)}))   

# Add product

@app.route('/add_product')
def add_product():
    return render_template("addproduct.html",
    brands=mongo.db.brands.find(),
    types=mongo.db.types.find())

# Proceed inserted data to mongo
    
@app.route('/insert_product', methods=["POST"])
def insert_product():
    products=mongo.db.products
    brand_id = request.form.get('brand_id')
    type_id = request.form.get('type_id')
    gluten_free = request.form.get('gluten_free')
    dictionary = {
        'name': request.form.get('name'),
        'brand_id': ObjectId(brand_id),
        'image_url': request.form.get('image_url'),
        'type_id': ObjectId(type_id),
        'about': request.form.get('about'),
        'abv': request.form.get('abv'),
        'amount': request.form.get('amount'),
        'gluten_free': bool(gluten_free)
    }
    
    products.insert_one(dictionary)
    return redirect(url_for('get_products'))
    
# Edit product

@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    return render_template("editproduct.html",
    product=mongo.db.products.find_one({"_id": ObjectId(product_id)}),
    brands=mongo.db.brands.find(),
    types=mongo.db.types.find())

# Update product

@app.route('/update_product/<product_id>', methods=["POST"])
def update_product(product_id):
    products=mongo.db.products
    brand_id = request.form.get('brand_id')
    type_id = request.form.get('type_id')
    products.update({'_id': ObjectId(product_id)},
    {
        'name': request.form.get('name'),
        'brand_id': ObjectId(brand_id),
        'image_url': request.form.get('image_url'),
        'type_id': ObjectId(type_id),
        'about': request.form.get('about'),
        'abv': request.form.get('abv'),
        'amount': request.form.get('amount'),
        'gluten': request.form.get('gluten')
    })
    return redirect(url_for('get_products'))
    
# Delete product

@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.products.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('get_products'))

# Brand Routes    
# Add Brand

@app.route('/get_brands')
def get_brands():
    return render_template("brands.html", 
    brands=mongo.db.brands.find())

@app.route('/add_brand')
def add_brand():
    return render_template("addbrand.html")

# Proceed inserted data to mongo
    
@app.route('/insert_brand', methods=["POST"])
def insert_brand():
    brands=mongo.db.brands
    brands.insert_one(request.form.to_dict())
    return redirect(url_for('get_brands'))
    
# Edit brand

@app.route('/edit_brand/<brand_id>')
def edit_brand(brand_id):
    return render_template("editbrand.html",
    brand=mongo.db.brands.find_one({"_id": ObjectId(brand_id)}))

# Update brand

@app.route('/update_brand/<brand_id>', methods=["POST"])
def update_brand(brand_id):
    brands=mongo.db.brands
    brands.update({'_id': ObjectId(brand_id)},
    {
        'name': request.form.get('name'),
        'country': request.form.get('country'),
        'website_URL': request.form.get('website_URL'),
        'instruction_URL': request.form.get('instruction_URL'),
    })
    return redirect(url_for('get_brands'))
    
# Delete brand

@app.route('/delete_brand/<brand_id>')
def delete_brand(brand_id):
    mongo.db.brands.remove({'_id': ObjectId(brand_id)})
    return redirect(url_for('get_brands'))

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
