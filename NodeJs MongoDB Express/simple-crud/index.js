const express = require('express');
const mongoose = require('mongoose');
const Product = require('./models/product_model');

const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World');
});

app.get('/about', (req, res) => {
  res.send('About Us');
});

/* PRODUCT CRUD API */
//create a product 
app.post('/api/product/create', async (req, res) => {
  try {
    const product = await Product.create(req.body);
    res.status(201).send(product);
  } catch (error) {
    console.error('Error creating product:', error.message);
    res.status(500).send({ message: 'An error occurred', error: error.message });
  }
});

//view all products
app.get("/api/products", async (req, res) => {
  try {
    const products = await Product.find({});
    res.send(products);
  } catch (error) {
    console.error('Error retrieving products:', error.message);
    res.status(500).send({ message: 'An error occurred', error: error.message });
  }
});


// view each product
app.get("/api/product/:id", async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    res.send(product);
  } catch (error) {
    console.error('Error retrieving product:', error.message);
    res.status(500).send({ message: 'An error occurred', error: error.message });
  }
});


//delete each product
app.get("/api/product/delete/:id", async (req, res) => {
  try {
    const product = await Product.findByIdAndDelete(req.params.id);
    res.send(product);
  } catch (error) {
    console.error('Error deleting product:', error.message);
    res.status(500).send({ message: 'An error occurred', error: error.message });
  }
});

//update each product
app.put("/api/product/update/:id", async (req, res) => {  
  try {
    const product = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.send(product);
  } catch (error) {
    console.error('Error updating product:', error.message);
    res.status(500).send({ message: 'An error occurred', error: error.message });
  }
});

const startServer = async () => {
  try {
    await mongoose.connect('mongodb+srv://thawzinsoedev:ngHuWcHn.6fVj_P@simple-crud.eqetpc7.mongodb.net/simple-crud?retryWrites=true&w=majority', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('Connected to the database');

    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });
  } catch (error) {
    console.error('Database connection failed:', error.message);
    process.exit(1); // Exit the process with failure code
  }
};

startServer();
