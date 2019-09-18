{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\napp = Flask(__name__)\n\n# Connection to MongoDB\n\napp.config[\"MONGO_DBNAME\"] = 'beer_brewing'\napp.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')\n\nmongo = PyMongo(app)\n\n\n@app.route('/')\n@app.route('/home')\ndef home_page():\n    \"\"\" Home page \"\"\"\n    return render_template(\"index.html\",\n                            types=mongo.db.types.find())\n\n\n@app.route('/products', methods=[\"GET\", \"POST\"])\ndef insert_products():\n    if request.method == \"POST\":\n        \"\"\" Proceed data from form to db \"\"\"\n        products=mongo.db.products\n        brand_id = request.form.get('brand_id')\n        type_id = request.form.get('type_id')\n        dictionary = {\n            'name': request.form.get('name'),\n            'brand_id': ObjectId(brand_id),\n            'image_url': request.form.get('image_url'),\n            'type_id': ObjectId(type_id),\n            'about': request.form.get('about'),\n            'abv': request.form.get('abv'),\n            'amount': request.form.get('amount'),\n        }\n        products.insert_one(dictionary)\n        return redirect(url_for('insert_products'))\n    \n    \"\"\" Page with all products \"\"\"\n    return render_template(\"products.html\",\n                            types=mongo.db.types.find(),\n                            products=mongo.db.products.find())\n\n\n@app.route('/product/<product_id>')\ndef get_description(product_id):\n    \"\"\" Single product description \"\"\"\n    return render_template(\"description.html\",\n                            brands=mongo.db.brands.find(),\n                            types=mongo.db.types.find(),\n                            product=mongo.db.products.find_one({\"_id\": ObjectId(product_id)}))   \n\n\n@app.route('/product/add')\ndef add_product():\n    \"\"\" Add product \"\"\"\n    return render_template(\"addproduct.html\",\n                            brands=mongo.db.brands.find(),\n                            types=mongo.db.types.find())\n\n\n@app.route('/product/<product_id>/edit')\ndef edit_product(product_id):\n    \"\"\" Edit product form \"\"\"\n    return render_template(\"editproduct.html\",\n                            product=mongo.db.products.find_one({\"_id\": ObjectId(product_id)}),\n                            brands=mongo.db.brands.find(),\n                            types=mongo.db.types.find())\n\n\n@app.route('/product/<product_id>/update', methods=[\"POST\"])\ndef update_product(product_id):\n    \"\"\" Update product information in db \"\"\"\n    products=mongo.db.products\n    brand_id=request.form.get('brand_id')\n    type_id=request.form.get('type_id')\n    products.update({'_id': ObjectId(product_id)},\n    {\n        'name': request.form.get('name'),\n        'brand_id': ObjectId(brand_id),\n        'image_url': request.form.get('image_url'),\n        'type_id': ObjectId(type_id),\n        'about': request.form.get('about'),\n        'abv': request.form.get('abv'),\n        'amount': request.form.get('amount'),\n    })\n    return redirect(url_for('get_products'))\n    \n\n@app.route('/product/<product_id>/delete')\ndef delete_product(product_id):\n    \"\"\" Delete choosen product \"\"\"\n    mongo.db.products.remove({'_id': ObjectId(product_id)})\n    return redirect(url_for('insert_products'))\n\n\n@app.route('/brands')\ndef get_brands():\n    \"\"\" Brand page \"\"\"\n    return render_template(\"brands.html\", \n                            brands=mongo.db.brands.find())\n\n\n@app.route('/brand/add')\ndef add_brand():\n    \"\"\" Add brand form \"\"\"\n    return render_template(\"addbrand.html\")\n\n\n    \n@app.route('/insert_brand', methods=[\"POST\"])\ndef insert_brand():\n    \"\"\" Proceed data from form to db \"\"\"\n    brands=mongo.db.brands\n    brands.insert_one(request.form.to_dict())\n    return redirect(url_for('get_brands'))\n    \n\n@app.route('/brand/<brand_id>/edit')\ndef edit_brand(brand_id):\n    \"\"\" Edit brand form \"\"\"\n    return render_template(\"editbrand.html\",\n                            brand=mongo.db.brands.find_one({\"_id\": ObjectId(brand_id)}))\n\n\n@app.route('/brand/<brand_id>/update', methods=[\"POST\"])\ndef update_brand(brand_id):\n    \"\"\" Update product information in db \"\"\"\n    brands=mongo.db.brands\n    brands.update({'_id': ObjectId(brand_id)},\n    {\n        'name': request.form.get('name'),\n        'country': request.form.get('country'),\n        'website_URL': request.form.get('website_URL'),\n        'instruction_URL': request.form.get('instruction_URL'),\n    })\n    return redirect(url_for('get_brands'))\n\n\nif __name__ == \"__main__\":\n    app.run(host=os.environ.get('IP'),\n        port=int(os.environ.get('PORT')),\n        debug=True)\n","undoManager":{"mark":99,"position":100,"stack":[[{"start":{"row":131,"column":8},"end":{"row":131,"column":12},"action":"insert","lines":["    "],"id":2556}],[{"start":{"row":131,"column":12},"end":{"row":131,"column":16},"action":"insert","lines":["    "],"id":2557}],[{"start":{"row":131,"column":16},"end":{"row":131,"column":20},"action":"insert","lines":["    "],"id":2558}],[{"start":{"row":131,"column":20},"end":{"row":131,"column":24},"action":"insert","lines":["    "],"id":2559}],[{"start":{"row":131,"column":24},"end":{"row":131,"column":28},"action":"insert","lines":["    "],"id":2560}],[{"start":{"row":126,"column":0},"end":{"row":126,"column":12},"action":"remove","lines":["# Edit brand"],"id":2561},{"start":{"row":125,"column":4},"end":{"row":126,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":132,"column":0},"end":{"row":132,"column":14},"action":"remove","lines":["# Update brand"],"id":2562},{"start":{"row":131,"column":0},"end":{"row":132,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":128,"column":25},"end":{"row":129,"column":0},"action":"insert","lines":["",""],"id":2563},{"start":{"row":129,"column":0},"end":{"row":129,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":129,"column":4},"end":{"row":129,"column":6},"action":"insert","lines":["\"\""],"id":2564}],[{"start":{"row":129,"column":6},"end":{"row":129,"column":7},"action":"insert","lines":["\""],"id":2565},{"start":{"row":129,"column":7},"end":{"row":129,"column":8},"action":"insert","lines":["\""]},{"start":{"row":129,"column":8},"end":{"row":129,"column":9},"action":"insert","lines":["\""]},{"start":{"row":129,"column":9},"end":{"row":129,"column":10},"action":"insert","lines":["\""]}],[{"start":{"row":71,"column":21},"end":{"row":71,"column":22},"action":"insert","lines":["d"],"id":2566},{"start":{"row":71,"column":22},"end":{"row":71,"column":23},"action":"insert","lines":["a"]},{"start":{"row":71,"column":23},"end":{"row":71,"column":24},"action":"insert","lines":["t"]},{"start":{"row":71,"column":24},"end":{"row":71,"column":25},"action":"insert","lines":["a"]}],[{"start":{"row":71,"column":25},"end":{"row":71,"column":26},"action":"insert","lines":[" "],"id":2567}],[{"start":{"row":129,"column":7},"end":{"row":129,"column":8},"action":"insert","lines":[" "],"id":2568},{"start":{"row":129,"column":8},"end":{"row":129,"column":9},"action":"insert","lines":["E"]},{"start":{"row":129,"column":9},"end":{"row":129,"column":10},"action":"insert","lines":["d"]},{"start":{"row":129,"column":10},"end":{"row":129,"column":11},"action":"insert","lines":["i"]},{"start":{"row":129,"column":11},"end":{"row":129,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":129,"column":12},"end":{"row":129,"column":13},"action":"insert","lines":[" "],"id":2569},{"start":{"row":129,"column":13},"end":{"row":129,"column":14},"action":"insert","lines":["b"]},{"start":{"row":129,"column":14},"end":{"row":129,"column":15},"action":"insert","lines":["r"]},{"start":{"row":129,"column":15},"end":{"row":129,"column":16},"action":"insert","lines":["a"]},{"start":{"row":129,"column":16},"end":{"row":129,"column":17},"action":"insert","lines":["n"]},{"start":{"row":129,"column":17},"end":{"row":129,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":129,"column":18},"end":{"row":129,"column":19},"action":"insert","lines":[" "],"id":2570},{"start":{"row":129,"column":19},"end":{"row":129,"column":20},"action":"insert","lines":["d"]},{"start":{"row":129,"column":20},"end":{"row":129,"column":21},"action":"insert","lines":["a"]},{"start":{"row":129,"column":21},"end":{"row":129,"column":22},"action":"insert","lines":["t"]},{"start":{"row":129,"column":22},"end":{"row":129,"column":23},"action":"insert","lines":["a"]},{"start":{"row":129,"column":23},"end":{"row":129,"column":24},"action":"insert","lines":["n"]}],[{"start":{"row":129,"column":23},"end":{"row":129,"column":24},"action":"remove","lines":["n"],"id":2571}],[{"start":{"row":129,"column":23},"end":{"row":129,"column":24},"action":"insert","lines":[" "],"id":2572}],[{"start":{"row":129,"column":19},"end":{"row":129,"column":23},"action":"remove","lines":["data"],"id":2573},{"start":{"row":129,"column":19},"end":{"row":129,"column":20},"action":"insert","lines":["f"]},{"start":{"row":129,"column":20},"end":{"row":129,"column":21},"action":"insert","lines":["o"]},{"start":{"row":129,"column":21},"end":{"row":129,"column":22},"action":"insert","lines":["r"]},{"start":{"row":129,"column":22},"end":{"row":129,"column":23},"action":"insert","lines":["m"]}],[{"start":{"row":71,"column":24},"end":{"row":71,"column":25},"action":"remove","lines":["a"],"id":2574},{"start":{"row":71,"column":23},"end":{"row":71,"column":24},"action":"remove","lines":["t"]},{"start":{"row":71,"column":22},"end":{"row":71,"column":23},"action":"remove","lines":["a"]},{"start":{"row":71,"column":21},"end":{"row":71,"column":22},"action":"remove","lines":["d"]}],[{"start":{"row":71,"column":21},"end":{"row":71,"column":22},"action":"insert","lines":["f"],"id":2575},{"start":{"row":71,"column":22},"end":{"row":71,"column":23},"action":"insert","lines":["o"]},{"start":{"row":71,"column":23},"end":{"row":71,"column":24},"action":"insert","lines":["r"]},{"start":{"row":71,"column":24},"end":{"row":71,"column":25},"action":"insert","lines":["m"]}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":14},"action":"remove","lines":["# Delete brand"],"id":2576},{"start":{"row":145,"column":4},"end":{"row":146,"column":0},"action":"remove","lines":["",""]},{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":135,"column":27},"end":{"row":136,"column":0},"action":"insert","lines":["",""],"id":2577},{"start":{"row":136,"column":0},"end":{"row":136,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":136,"column":4},"end":{"row":136,"column":6},"action":"insert","lines":["\"\""],"id":2578}],[{"start":{"row":136,"column":6},"end":{"row":136,"column":7},"action":"insert","lines":["\""],"id":2579},{"start":{"row":136,"column":7},"end":{"row":136,"column":8},"action":"insert","lines":["\""]},{"start":{"row":136,"column":8},"end":{"row":136,"column":9},"action":"insert","lines":["\""]},{"start":{"row":136,"column":9},"end":{"row":136,"column":10},"action":"insert","lines":["\""]}],[{"start":{"row":136,"column":7},"end":{"row":136,"column":8},"action":"insert","lines":[" "],"id":2580}],[{"start":{"row":81,"column":38},"end":{"row":81,"column":39},"action":"remove","lines":["m"],"id":2581},{"start":{"row":81,"column":37},"end":{"row":81,"column":38},"action":"remove","lines":["o"]},{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"remove","lines":["r"]},{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"remove","lines":["f"]}],[{"start":{"row":81,"column":35},"end":{"row":81,"column":36},"action":"insert","lines":["i"],"id":2582},{"start":{"row":81,"column":36},"end":{"row":81,"column":37},"action":"insert","lines":["n"]}],[{"start":{"row":136,"column":8},"end":{"row":136,"column":41},"action":"insert","lines":["Update product information in db "],"id":2583}],[{"start":{"row":149,"column":27},"end":{"row":150,"column":0},"action":"insert","lines":["",""],"id":2584},{"start":{"row":150,"column":0},"end":{"row":150,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":150,"column":4},"end":{"row":150,"column":6},"action":"insert","lines":["\"\""],"id":2585}],[{"start":{"row":150,"column":6},"end":{"row":150,"column":7},"action":"insert","lines":["\""],"id":2586},{"start":{"row":150,"column":7},"end":{"row":150,"column":8},"action":"insert","lines":["\""]},{"start":{"row":150,"column":8},"end":{"row":150,"column":9},"action":"insert","lines":["\""]},{"start":{"row":150,"column":9},"end":{"row":150,"column":10},"action":"insert","lines":["\""]}],[{"start":{"row":150,"column":7},"end":{"row":150,"column":8},"action":"insert","lines":[" "],"id":2587}],[{"start":{"row":150,"column":10},"end":{"row":150,"column":11},"action":"remove","lines":["\""],"id":2588},{"start":{"row":150,"column":9},"end":{"row":150,"column":10},"action":"remove","lines":["\""]},{"start":{"row":150,"column":8},"end":{"row":150,"column":9},"action":"remove","lines":["\""]},{"start":{"row":150,"column":7},"end":{"row":150,"column":8},"action":"remove","lines":[" "]},{"start":{"row":150,"column":6},"end":{"row":150,"column":7},"action":"remove","lines":["\""]},{"start":{"row":150,"column":5},"end":{"row":150,"column":6},"action":"remove","lines":["\""]},{"start":{"row":150,"column":4},"end":{"row":150,"column":5},"action":"remove","lines":["\""]},{"start":{"row":150,"column":0},"end":{"row":150,"column":4},"action":"remove","lines":["    "]},{"start":{"row":149,"column":27},"end":{"row":150,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":148,"column":0},"end":{"row":151,"column":42},"action":"remove","lines":["@app.route('/delete_brand/<brand_id>')","def delete_brand(brand_id):","    mongo.db.brands.remove({'_id': ObjectId(brand_id)})","    return redirect(url_for('get_brands'))"],"id":2589},{"start":{"row":147,"column":0},"end":{"row":148,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":146,"column":0},"end":{"row":147,"column":0},"action":"remove","lines":["",""],"id":2590}],[{"start":{"row":55,"column":4},"end":{"row":55,"column":49},"action":"remove","lines":["gluten_free = request.form.get('gluten_free')"],"id":2591},{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"remove","lines":["    "]},{"start":{"row":54,"column":41},"end":{"row":55,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"insert","lines":["    "],"id":2658}],[{"start":{"row":20,"column":8},"end":{"row":20,"column":12},"action":"insert","lines":["    "],"id":2659}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":16},"action":"insert","lines":["    "],"id":2660}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":20},"action":"insert","lines":["    "],"id":2661}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":24},"action":"insert","lines":["    "],"id":2662}],[{"start":{"row":20,"column":24},"end":{"row":20,"column":28},"action":"insert","lines":["    "],"id":2663}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"remove","lines":["e"],"id":2664},{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":["g"]},{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["a"]},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"remove","lines":["p"]},{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"remove","lines":["_"]}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["_"],"id":2665},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["t"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"remove","lines":["e"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["g"]}],[{"start":{"row":32,"column":27},"end":{"row":32,"column":28},"action":"remove","lines":["n"],"id":2666},{"start":{"row":32,"column":26},"end":{"row":32,"column":27},"action":"remove","lines":["o"]},{"start":{"row":32,"column":25},"end":{"row":32,"column":26},"action":"remove","lines":["i"]},{"start":{"row":32,"column":24},"end":{"row":32,"column":25},"action":"remove","lines":["t"]},{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"remove","lines":["p"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"remove","lines":["i"]},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"remove","lines":["r"]},{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"remove","lines":["c"]},{"start":{"row":32,"column":19},"end":{"row":32,"column":20},"action":"remove","lines":["s"]},{"start":{"row":32,"column":18},"end":{"row":32,"column":19},"action":"remove","lines":["e"]},{"start":{"row":32,"column":17},"end":{"row":32,"column":18},"action":"remove","lines":["d"]},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"remove","lines":["_"]},{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"remove","lines":["t"]},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"remove","lines":["e"]},{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"remove","lines":["g"]}],[{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":["p"],"id":2667},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["r"]},{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":["o"]},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"insert","lines":["d"]},{"start":{"row":32,"column":17},"end":{"row":32,"column":18},"action":"insert","lines":["u"]},{"start":{"row":32,"column":18},"end":{"row":32,"column":19},"action":"insert","lines":["c"]},{"start":{"row":32,"column":19},"end":{"row":32,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"remove","lines":["_"],"id":2668},{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"remove","lines":["d"]},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"remove","lines":["d"]},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"remove","lines":["a"]}],[{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":["/"],"id":2669},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["i"]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["n"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":["s"]},{"start":{"row":41,"column":24},"end":{"row":41,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":["r"],"id":2670},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":68,"column":17},"end":{"row":68,"column":18},"action":"remove","lines":["_"],"id":2671},{"start":{"row":68,"column":16},"end":{"row":68,"column":17},"action":"remove","lines":["t"]},{"start":{"row":68,"column":15},"end":{"row":68,"column":16},"action":"remove","lines":["i"]},{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"remove","lines":["d"]},{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"insert","lines":["/"],"id":2672},{"start":{"row":68,"column":34},"end":{"row":68,"column":35},"action":"insert","lines":["e"]},{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":["f"]}],[{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"remove","lines":["f"],"id":2673}],[{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":["d"],"id":2674},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"insert","lines":["i"]},{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":76,"column":0},"end":{"row":77,"column":0},"action":"remove","lines":["# Update product",""],"id":2675}],[{"start":{"row":77,"column":19},"end":{"row":77,"column":20},"action":"remove","lines":["_"],"id":2676},{"start":{"row":77,"column":18},"end":{"row":77,"column":19},"action":"remove","lines":["e"]},{"start":{"row":77,"column":17},"end":{"row":77,"column":18},"action":"remove","lines":["t"]},{"start":{"row":77,"column":16},"end":{"row":77,"column":17},"action":"remove","lines":["a"]},{"start":{"row":77,"column":15},"end":{"row":77,"column":16},"action":"remove","lines":["d"]},{"start":{"row":77,"column":14},"end":{"row":77,"column":15},"action":"remove","lines":["p"]},{"start":{"row":77,"column":13},"end":{"row":77,"column":14},"action":"remove","lines":["u"]}],[{"start":{"row":77,"column":33},"end":{"row":77,"column":34},"action":"insert","lines":["/"],"id":2677},{"start":{"row":77,"column":34},"end":{"row":77,"column":35},"action":"insert","lines":["u"]},{"start":{"row":77,"column":35},"end":{"row":77,"column":36},"action":"insert","lines":["p"]}],[{"start":{"row":77,"column":36},"end":{"row":77,"column":37},"action":"insert","lines":["d"],"id":2678},{"start":{"row":77,"column":37},"end":{"row":77,"column":38},"action":"insert","lines":["a"]},{"start":{"row":77,"column":38},"end":{"row":77,"column":39},"action":"insert","lines":["t"]},{"start":{"row":77,"column":39},"end":{"row":77,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":96,"column":19},"end":{"row":96,"column":20},"action":"remove","lines":["_"],"id":2679},{"start":{"row":96,"column":18},"end":{"row":96,"column":19},"action":"remove","lines":["e"]},{"start":{"row":96,"column":17},"end":{"row":96,"column":18},"action":"remove","lines":["t"]},{"start":{"row":96,"column":16},"end":{"row":96,"column":17},"action":"remove","lines":["e"]},{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["l"]},{"start":{"row":96,"column":14},"end":{"row":96,"column":15},"action":"remove","lines":["e"]},{"start":{"row":96,"column":13},"end":{"row":96,"column":14},"action":"remove","lines":["d"]}],[{"start":{"row":96,"column":33},"end":{"row":96,"column":34},"action":"insert","lines":["/"],"id":2680},{"start":{"row":96,"column":34},"end":{"row":96,"column":35},"action":"insert","lines":["d"]},{"start":{"row":96,"column":35},"end":{"row":96,"column":36},"action":"insert","lines":["e"]},{"start":{"row":96,"column":36},"end":{"row":96,"column":37},"action":"insert","lines":["l"]},{"start":{"row":96,"column":37},"end":{"row":96,"column":38},"action":"insert","lines":["e"]},{"start":{"row":96,"column":38},"end":{"row":96,"column":39},"action":"insert","lines":["t"]},{"start":{"row":96,"column":39},"end":{"row":96,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"remove","lines":["_"],"id":2681},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"remove","lines":["t"]},{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"remove","lines":["e"]},{"start":{"row":103,"column":13},"end":{"row":103,"column":14},"action":"remove","lines":["g"]}],[{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"remove","lines":["_"],"id":2682},{"start":{"row":110,"column":15},"end":{"row":110,"column":16},"action":"remove","lines":["d"]},{"start":{"row":110,"column":14},"end":{"row":110,"column":15},"action":"remove","lines":["d"]},{"start":{"row":110,"column":13},"end":{"row":110,"column":14},"action":"remove","lines":["a"]}],[{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"insert","lines":["/"],"id":2683},{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["i"]},{"start":{"row":110,"column":20},"end":{"row":110,"column":21},"action":"insert","lines":["n"]},{"start":{"row":110,"column":21},"end":{"row":110,"column":22},"action":"insert","lines":["s"]},{"start":{"row":110,"column":22},"end":{"row":110,"column":23},"action":"insert","lines":["e"]},{"start":{"row":110,"column":23},"end":{"row":110,"column":24},"action":"insert","lines":["r"]},{"start":{"row":110,"column":24},"end":{"row":110,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":110,"column":24},"end":{"row":110,"column":25},"action":"remove","lines":["t"],"id":2684},{"start":{"row":110,"column":23},"end":{"row":110,"column":24},"action":"remove","lines":["r"]},{"start":{"row":110,"column":22},"end":{"row":110,"column":23},"action":"remove","lines":["e"]},{"start":{"row":110,"column":21},"end":{"row":110,"column":22},"action":"remove","lines":["s"]},{"start":{"row":110,"column":20},"end":{"row":110,"column":21},"action":"remove","lines":["n"]},{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"remove","lines":["i"]}],[{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["a"],"id":2685},{"start":{"row":110,"column":20},"end":{"row":110,"column":21},"action":"insert","lines":["d"]},{"start":{"row":110,"column":21},"end":{"row":110,"column":22},"action":"insert","lines":["d"]}],[{"start":{"row":125,"column":17},"end":{"row":125,"column":18},"action":"remove","lines":["_"],"id":2686},{"start":{"row":125,"column":16},"end":{"row":125,"column":17},"action":"remove","lines":["t"]},{"start":{"row":125,"column":15},"end":{"row":125,"column":16},"action":"remove","lines":["i"]},{"start":{"row":125,"column":14},"end":{"row":125,"column":15},"action":"remove","lines":["d"]},{"start":{"row":125,"column":13},"end":{"row":125,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":125,"column":29},"end":{"row":125,"column":30},"action":"insert","lines":["/"],"id":2687}],[{"start":{"row":125,"column":30},"end":{"row":125,"column":31},"action":"insert","lines":["e"],"id":2688},{"start":{"row":125,"column":31},"end":{"row":125,"column":32},"action":"insert","lines":["d"]},{"start":{"row":125,"column":32},"end":{"row":125,"column":33},"action":"insert","lines":["i"]},{"start":{"row":125,"column":33},"end":{"row":125,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":132,"column":19},"end":{"row":132,"column":20},"action":"remove","lines":["_"],"id":2689},{"start":{"row":132,"column":18},"end":{"row":132,"column":19},"action":"remove","lines":["e"]},{"start":{"row":132,"column":17},"end":{"row":132,"column":18},"action":"remove","lines":["t"]},{"start":{"row":132,"column":16},"end":{"row":132,"column":17},"action":"remove","lines":["a"]},{"start":{"row":132,"column":15},"end":{"row":132,"column":16},"action":"remove","lines":["d"]},{"start":{"row":132,"column":14},"end":{"row":132,"column":15},"action":"remove","lines":["p"]},{"start":{"row":132,"column":13},"end":{"row":132,"column":14},"action":"remove","lines":["u"]}],[{"start":{"row":132,"column":29},"end":{"row":132,"column":30},"action":"insert","lines":["/"],"id":2690},{"start":{"row":132,"column":30},"end":{"row":132,"column":31},"action":"insert","lines":["u"]},{"start":{"row":132,"column":31},"end":{"row":132,"column":32},"action":"insert","lines":["p"]},{"start":{"row":132,"column":32},"end":{"row":132,"column":33},"action":"insert","lines":["d"]}],[{"start":{"row":132,"column":33},"end":{"row":132,"column":34},"action":"insert","lines":["a"],"id":2691},{"start":{"row":132,"column":34},"end":{"row":132,"column":35},"action":"insert","lines":["t"]},{"start":{"row":132,"column":35},"end":{"row":132,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"remove","lines":["t"],"id":2692},{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"remove","lines":["r"]},{"start":{"row":41,"column":24},"end":{"row":41,"column":25},"action":"remove","lines":["e"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"remove","lines":["s"]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"remove","lines":["n"]},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"remove","lines":["i"]}],[{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["a"],"id":2693},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["d"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":["d"]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["s"],"id":2694}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"remove","lines":["s"],"id":2695}],[{"start":{"row":26,"column":4},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":2697},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":51,"column":4},"end":{"row":66,"column":44},"action":"remove","lines":["insert_product():","    \"\"\" Proceed data from form to db \"\"\"","    products=mongo.db.products","    brand_id = request.form.get('brand_id')","    type_id = request.form.get('type_id')","    dictionary = {","        'name': request.form.get('name'),","        'brand_id': ObjectId(brand_id),","        'image_url': request.form.get('image_url'),","        'type_id': ObjectId(type_id),","        'about': request.form.get('about'),","        'abv': request.form.get('abv'),","        'amount': request.form.get('amount'),","    }","    products.insert_one(dictionary)","    return redirect(url_for('get_products'))"],"id":2698}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":19},"action":"remove","lines":["get_products():"],"id":2699},{"start":{"row":25,"column":4},"end":{"row":40,"column":44},"action":"insert","lines":["insert_product():","    \"\"\" Proceed data from form to db \"\"\"","    products=mongo.db.products","    brand_id = request.form.get('brand_id')","    type_id = request.form.get('type_id')","    dictionary = {","        'name': request.form.get('name'),","        'brand_id': ObjectId(brand_id),","        'image_url': request.form.get('image_url'),","        'type_id': ObjectId(type_id),","        'about': request.form.get('about'),","        'abv': request.form.get('abv'),","        'amount': request.form.get('amount'),","    }","    products.insert_one(dictionary)","    return redirect(url_for('get_products'))"]}],[{"start":{"row":25,"column":21},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":2700},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["i"]},{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"insert","lines":[" "],"id":2701}],[{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["m"],"id":2702},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["e"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["t"]},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["h"]},{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["o"]},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"insert","lines":[" "],"id":2703},{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"insert","lines":["="]},{"start":{"row":26,"column":15},"end":{"row":26,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":26,"column":16},"end":{"row":26,"column":17},"action":"insert","lines":[" "],"id":2704}],[{"start":{"row":26,"column":17},"end":{"row":26,"column":19},"action":"insert","lines":["\"\""],"id":2705}],[{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"insert","lines":["P"],"id":2706},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["O"]},{"start":{"row":26,"column":20},"end":{"row":26,"column":21},"action":"insert","lines":["S"]},{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"insert","lines":["T"]}],[{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["r"],"id":2707},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["e"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["q"]},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["u"]},{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["e"]},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":["s"]},{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"insert","lines":["."],"id":2708}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":[":"],"id":2709}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "],"id":2710},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":66,"column":28},"end":{"row":66,"column":46},"action":"remove","lines":[", methods=[\"POST\"]"],"id":2711}],[{"start":{"row":24,"column":22},"end":{"row":24,"column":40},"action":"insert","lines":[", methods=[\"POST\"]"],"id":2712}],[{"start":{"row":24,"column":33},"end":{"row":24,"column":35},"action":"insert","lines":["\"\""],"id":2713}],[{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["G"],"id":2714},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["E"]},{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"insert","lines":["T"]}],[{"start":{"row":24,"column":38},"end":{"row":24,"column":39},"action":"insert","lines":[","],"id":2715}],[{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":[" "],"id":2716}],[{"start":{"row":66,"column":0},"end":{"row":67,"column":4},"action":"remove","lines":["@app.route('/insert_product')","def "],"id":2717},{"start":{"row":65,"column":4},"end":{"row":66,"column":0},"action":"remove","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":64,"column":0},"end":{"row":65,"column":0},"action":"remove","lines":["",""],"id":2718}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":2719},{"start":{"row":64,"column":0},"end":{"row":65,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["s"],"id":2720}],[{"start":{"row":41,"column":33},"end":{"row":41,"column":45},"action":"remove","lines":["get_products"],"id":2721},{"start":{"row":41,"column":33},"end":{"row":41,"column":48},"action":"insert","lines":["insert_products"]}],[{"start":{"row":98,"column":29},"end":{"row":98,"column":41},"action":"remove","lines":["get_products"],"id":2722},{"start":{"row":98,"column":29},"end":{"row":98,"column":44},"action":"insert","lines":["insert_products"]}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"remove","lines":["",""],"id":2723}]]},"ace":{"folds":[],"customSyntax":"python","scrolltop":286.5,"scrollleft":0,"selection":{"start":{"row":41,"column":4},"end":{"row":41,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1568823044922}