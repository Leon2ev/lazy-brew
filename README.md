<h1>Lazy Brew</h1>
<p>
    Craft beer is become very popular this days. And homebrewing growing with it.
    To make your own beer at home it's very rewarding process because it's nice 
    to see and try the product that you made by yourself and can share with your 
    friends in the end of the week. But to do it from scratch takes a time, 
    investments, knowledge, space and more. Even you wish to make a beer you can
    face some problems that can stop you. To make your life easier and safe your 
    time and money you can skip brewing proccess and start straight away from 
    fermentations. By buying "Extracts" of beer that you would like to make, pour 
    it in to the bucket add water and wait.
</p>
<p>
    This project is made to collect different brands and products from around the 
    world. Here people can add products and reviews(not implemented) to share they
    experience or get information about the product they looking for. Main goal 
    is to collect data from users(most popular beer or brand) for further use.
</p>

<h2>UX</h2>
<p>
    This website focusing on people who are interested to begin make a beer using 
    "Extract" sets to help them find product that they looking for and for people 
    who would like to share they experience with product that they had been used.
</p>
<ul>
    <li>
        I decided to make a beer but first I have to find out what I can choose 
        from. I can go to Product page and see all products, I can select specific 
        type using filter and continue to make a research.
    </li>
    <li>
        I used some product and like it/didn't like so I want share my experience 
        I can go to Product page and try to find product that I used if it not 
        there I can easily add it but using Insert product functionality.
    </li>
</ul>
<a href="https://balsamiq.cloud/scx22fx/ph7vnox/r2278">Wireframe</a>
<h2>Features</h2>
<h3>Existing Features</h3>
<ul>
    <li>
        Home page 
        <ul>
            <li>Action button that send you to Product page</li>
        </ul>
    </li>
    <li>
        Product page
        <ul>
            <li>Filter - That help you to filter beer types</li>
            <li>
                Add product - redicrect you to "Add product" form where you can 
                fill it out and send it to database. 
            </li>
            <li>Read more - redirect to description page of choosen product</li>
        </ul>
    </li>
    <li>
        Description page
        <ul>
            <li>
                Edit - redirect you to "Edit" page where you can change information 
                about the product.
            </li>
            <li>Delete - Product will be delete product from database</li>
        </ul>
    </li>
    <li>
        Brands page 
        <ul>
            <li>
                Add brand - redicrect you to "Add brand" form where you can 
                fill it out and send it to database. 
            </li> 
            <li>
                Edit - redirect you to "Edit" page where you can change information 
                about the brand.
            </li>
        </ul>
    </li>
    
</ul>
<h3>Features Left to Implement</h3>
<ul>
    <li>
        Add log in functionality.
    </li>
    <li>
        Product comment functionality.     
    </li>
    <li>
        Product rating/score functionality.     
    </li>
</ul>
<h2>Technologies Used</h2>
<ul>
    <li>
        <a href="http://archives.materializecss.com/0.100.2/helpers.html">Materialize</a>
        <ul>
            <li>For template and to make website mobile responsive</li>
        </ul>
    </li>
    <li>
        <a href="http://flask.palletsprojects.com/en/1.1.x/">Flask</a>
        <ul>
            <li>Microframework for making web services in Python.</li>
        </ul>
    </li>
    <li>
        <a href="https://api.mongodb.com/python/current/">PyMongo</a>
        <ul>
            <li>
                Python distribution containing tools for working with MongoDB, 
                and is the recommended way to work with MongoDB from Python.
            </li>
        </ul>
    </li>
    <li>
        <a href="https://docs.mongodb.com/manual/reference/method/ObjectId/">ObjectId</a>
        <ul>
            <li>Used to work with mongo ObjectId</li>
        </ul>
    </li>
    <li>
        <a href="https://pypi.org/project/python-dotenv/">Dotenv</a>
        <ul>
            <li>
                Reads the key,value pair from .env file and adds them to 
                environment variable. It is great for managing app settings during 
                development and in production using 12-factor principles.
            </li>
        </ul>
    </li>
    <li>
        <a href="https://caolan.github.io/async/queue.js.html">JQuery</a>
        <ul>
            <li>Used for simplify DOM manipulation.</li>
        </ul>
    </li>
    <li>
        <a href="https://www.mongodb.com/">MongoDB</a>
        <ul>
            <li>For storing data.</li>
        </ul>
    </li>
</ul>
<h2>Testing</h2>
<p>
    All tests going from top and from left to right
</p>
<p>
    During the test on different devices and browsers no problems has been found.
</p>
<h5>Navigation</h5>
<ul>
    <li>
        Logo, links on navigation bar and on footer working well.    
    </li>
</ul>
<h5>Home Page</h5>
<ul>
    <li>
        Action button working well.
    </li>
</ul>
<h5>Products Page</h5>
<ul>
    <li>
        Filter working well. I can select beer type and see the result.
    </li>
    <li>
        Add Product button open a page form how it should be.
    </li>
    <li>
        Read more button open a product description page how it should be.
    </li>
</ul>
<h5>Brand Page</h5>
<ul>
    <li>
        Add Brand button open a page form how it should be.    
    </li>
    <li>
        Collapsible working well.   
    </li>
    <li>
        Edit button open a page form how it should be.  
    </li>
    <li>
        Links working well.
    </li>
</ul>
<h5>Add Product Page</h5>
<ul>
    <li>
        After filling up the form and submit, it appears in database and it 
        visible on the web page.
    </li>
    <li>
        Cancel button calls dialogue about further actions, by pressing pressing 
        "Agree" it redirect to Products Page and when pressed "Go back" opens 
        form page how it should be.
    </li>
</ul>
<h5>Add Brand Page</h5>
<ul>
    <li>
        After filling up the form and submit, it appears in database and it 
        visible on the web page.
    </li>
    <li>
        Cancel button calls dialogue about further actions, by pressing pressing 
        "Agree" it redirect to Products Page and when pressed "Go back" opens 
        form page how it should be.
    </li>
</ul>
<h5>Description Page</h5>
<ul>
    <li>
        Edit button open a page form how it should be.
    </li>
    <li>
        Delete button calls dialogue about further actions, by pressing pressing 
        "Agree" it delete record from database and this product removed from web 
        page and when pressed "Go back" opens description page how it should be.
    </li>
</ul>
<h5>Edit Pages both Product and Brand</h5>
<ul>
    <li>
        All fields are filled up with data that belongs to this specific product.
    </li>
    <li>
        Cancel button calls dialogue about further actions, by pressing pressing 
        "Agree" it redirect to Description/Brands Page and when pressed "Go back" 
        opens form page how it should be.
    </li>
</ul>
<h3>Bugs</h3>
<ul>
    <li>
        Require.txt contains a lot of thinks that I didn't use because from the 
        beginning it was inside AWS. My mentor explain me that next time i should 
        create a virtual environment.
    </li>
</ul>
<h2>Deployment</h2>
<ol>
    <li>Log in to Heroku</li>
    <li>Create new app. Select App name and server region.</li>
    <li>Create file with dependencies. pip freeze > requirements.txt</li>
    <li>Create Profile. web: python app.py</li>
    <li>Create git repository. Git init, git add.</li>
    <li>Log in to heroku. heroku login -i</li>
    <li>Connect to heroku repository. heroku git:remote -a {your-project-name}</li>
    <li>Push to heroku. git push heroku master</li>
    <li>
        <a href="https://lazy-brew.herokuapp.com/">Lazy Brew</a>
    </li>
</ol>
<h2>Credits</h2>
<h3>Media</h3>
<ul>
    <li><a href="https://mangrovejacks.com/">Pictures Mangrove</a></li>
    <li><a href="https://mangrovejacks.com/">Pictures Muntos</a></li>
</ul>


