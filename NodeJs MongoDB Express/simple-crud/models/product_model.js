const mongoose = require('mongoose');

const ProductSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, "Please Enter The Name Of The Product"]
  },
  description: {
    type: String
  },
  price: {
    type: Number,
    required: true
  },
  stock: {
    type: Number,
    default: 1
  }
});

const Product = mongoose.model('Product', ProductSchema);
module.exports = Product;
