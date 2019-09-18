import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Connection to MongoDB

app.config["MONGO_DBNAME"] = 'beer_brewing'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home_page():
    """ Home page """
    return render_template("index.html",
                            types=mongo.db.types.find())


@app.route('/products', methods=["GET", "POST"])
def insert_products():
    if request.method == "POST":
        """ Proceed data from form to db """
        products=mongo.db.products
        brand_id=request.form.get('brand_id')
        type_id=request.form.get('type_id')
        dictionary = {
            'name': request.form.get('name'),
            'brand_id': ObjectId(brand_id),
            'image_url': request.form.get('image_url'),
            'type_id': ObjectId(type_id),
            'about': request.form.get('about'),
            'abv': request.form.get('abv'),
            'amount': request.form.get('amount'),
        }
        products.insert_one(dictionary)
        return redirect(url_for('insert_products'))
    
    """ Page with all products """
    return render_template("products.html",
                            types=mongo.db.types.find(),
                            products=mongo.db.products.find())


@app.route('/product/<product_id>')
def get_description(product_id):
    """ Single product description """
    return render_template("description.html",
                            brands=mongo.db.brands.find(),
                            types=mongo.db.types.find(),
                            product=mongo.db.products.find_one({"_id": ObjectId(product_id)}))   


@app.route('/product/add')
def add_product():
    """ Add product """
    return render_template("addproduct.html",
                            brands=mongo.db.brands.find(),
                            types=mongo.db.types.find())


@app.route('/product/<product_id>/edit', methods=["GET", "POST"])
def edit_product(product_id):
    if request.method == "POST":
        """ Update product information in db """
        products=mongo.db.products
        brand_id=request.form.get('brand_id')
        type_id=request.form.get('type_id')
        products.update({'_id': ObjectId(product_id)},
        {
            'name': request.form.get('name'),
            'brand_id': ObjectId(brand_id),
            'image_url': request.form.get('image_url'),
            'type_id': ObjectId(type_id),
            'about': request.form.get('about'),
            'abv': request.form.get('abv'),
            'amount': request.form.get('amount'),
        })
        return redirect(url_for('insert_products'))
    """ Edit product form """
    return render_template("editproduct.html",
                            product=mongo.db.products.find_one({"_id": ObjectId(product_id)}),
                            brands=mongo.db.brands.find(),
                            types=mongo.db.types.find())

    
@app.route('/product/<product_id>/delete')
def delete_product(product_id):
    """ Delete choosen product """
    mongo.db.products.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('insert_products'))


@app.route('/brands', methods=["GET", "POST"])
def insert_brands():
    if request.method == "POST":
        """ Proceed data from form to db """
        brands=mongo.db.brands
        brands.insert_one(request.form.to_dict())
        return redirect(url_for('insert_brands'))
    """ Brand page """
    return render_template("brands.html", 
                            brands=mongo.db.brands.find())


@app.route('/brand/add')
def add_brand():
    """ Add brand form """
    return render_template("addbrand.html")


@app.route('/brand/<brand_id>/edit', methods=["GET", "POST"])
def edit_brand(brand_id):
    if request.method == "POST":
        """ Update product information in db """
        brands=mongo.db.brands
        brands.update({'_id': ObjectId(brand_id)},
        {
            'name': request.form.get('name'),
            'country': request.form.get('country'),
            'website_URL': request.form.get('website_URL'),
            'instruction_URL': request.form.get('instruction_URL'),
        })
        return redirect(url_for('insert_brands'))
    """ Edit brand form """
    return render_template("editbrand.html",
                            brand=mongo.db.brands.find_one({"_id": ObjectId(brand_id)}))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
