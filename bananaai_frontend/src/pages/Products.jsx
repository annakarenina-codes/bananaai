// src/pages/Products.jsx
import React, { useState, useEffect } from 'react';
import { 
  Box, Grid, Typography, Button, TextField, InputAdornment, 
  Dialog, DialogTitle, DialogContent, DialogActions,
  FormControl, InputLabel, Select, MenuItem, FormHelperText
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import AddIcon from '@mui/icons-material/Add';
import { productAPI } from '../services/api';
import ProductCard from '../components/ProductCard';
import { useNavigate } from 'react-router-dom';


const Products = () => {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [categoryFilter, setCategoryFilter] = useState('all');
  const [openDialog, setOpenDialog] = useState(false);
  const [newProduct, setNewProduct] = useState({
    name: '',
    category: '',
    product_type: 'non-perishable',
    expiry_date: '',
    price: '',
    total_stock: '',
    available_stock: '',
    location: ''
  });
  const [errors, setErrors] = useState({});
  const [categories, setCategories] = useState(['Fruits', 'Snacks', 'Bakery']);
  
  const navigate = useNavigate();

  useEffect(() => {
    fetchProducts();
  }, []);

  useEffect(() => {
    filterProducts();
  }, [searchTerm, categoryFilter, products]);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const response = await productAPI.getAll();
      setProducts(response.data);
      
      // Extract unique categories
      const uniqueCategories = [...new Set(response.data.map(product => product.category).filter(Boolean))];
      setCategories(uniqueCategories);
      
      setLoading(false);
    } catch (error) {
      console.error('Error fetching products:', error);
      setLoading(false);
    }
  };

  const filterProducts = () => {
    let result = [...products];
    
    // Apply search filter
    if (searchTerm) {
      result = result.filter(product => 
        product.name.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }
    
    // Apply category filter
    if (categoryFilter && categoryFilter !== 'all') {
      result = result.filter(product => product.category === categoryFilter);
    }
    
    setFilteredProducts(result);
  };

  const handleOpenDialog = () => {
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
    setNewProduct({
      name: '',
      category: '',
      product_type: 'non-perishable',
      expiry_date: '',
      price: '',
      total_stock: '',
      available_stock: '',
      location: ''
    });
    setErrors({});
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewProduct(prev => ({
      ...prev,
      [name]: value
    }));
    
    // Clear error for this field
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: null
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!newProduct.name) newErrors.name = 'Name is required';
    if (!newProduct.price) newErrors.price = 'Price is required';
    else if (isNaN(parseFloat(newProduct.price))) newErrors.price = 'Price must be a number';
    
    if (newProduct.total_stock && isNaN(parseInt(newProduct.total_stock))) {
      newErrors.total_stock = 'Stock must be a number';
    }
    
    if (newProduct.available_stock && isNaN(parseInt(newProduct.available_stock))) {
      newErrors.available_stock = 'Available stock must be a number';
    }
    
    if (newProduct.product_type === 'perishable' && !newProduct.expiry_date) {
      newErrors.expiry_date = 'Expiry date is required for perishable products';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async () => {
    if (!validateForm()) return;
    
    try {
      // Ensure available_stock equals total_stock for new products if not specified
      const productToSubmit = { ...newProduct };
      if (productToSubmit.total_stock && !productToSubmit.available_stock) {
        productToSubmit.available_stock = productToSubmit.total_stock;
      }
      
      await productAPI.create(productToSubmit);
      handleCloseDialog();
      fetchProducts();
    } catch (error) {
      console.error('Error creating product:', error);
    }
  };

  return (
    <Box sx={{ p: 3 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 3 }}>
        <Typography variant="h4" component="h1">
          Products
        </Typography>
        <Button 
          variant="contained" 
          color="primary" 
          startIcon={<AddIcon />}
          onClick={handleOpenDialog}
        >
          Add Product
        </Button>
      </Box>
      
      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 2, mb: 3 }}>
        <TextField
          label="Search Products"
          variant="outlined"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          sx={{ flexGrow: 1 }}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            ),
          }}
        />
        
        <FormControl sx={{ minWidth: 200 }}>
          <InputLabel>Category</InputLabel>
          <Select
            value={categoryFilter}
            label="Category"
            onChange={(e) => setCategoryFilter(e.target.value)}
          >
            <MenuItem value="all">All Categories</MenuItem>
            {categories.map((category) => (
              <MenuItem key={category} value={category}>{category}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>
      
      {/* Products Grid */}
      <Grid container spacing={3}>
        {loading ? (
          <Typography variant="body1">Loading products...</Typography>
        ) : filteredProducts.length === 0 ? (
          <Typography variant="body1">No products found</Typography>
        ) : (
          filteredProducts.map((product) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={product.id}>
              <ProductCard product={product} />
            </Grid>
          ))
        )}
      </Grid>
      
      {/* Add Product Dialog */}
      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>Add New Product</DialogTitle>
        <DialogContent>
          <Box sx={{ mt: 2, display: 'flex', flexDirection: 'column', gap: 2 }}>
            <TextField
              label="Product Name"
              name="name"
              value={newProduct.name}
              onChange={handleInputChange}
              fullWidth
              required
              error={!!errors.name}
              helperText={errors.name}
            />
            
            <TextField
              label="Category"
              name="category"
              value={newProduct.category}
              onChange={handleInputChange}
              fullWidth
            />
            
            <FormControl fullWidth>
              <InputLabel>Product Type</InputLabel>
              <Select
                name="product_type"
                value={newProduct.product_type}
                label="Product Type"
                onChange={handleInputChange}
              >
                <MenuItem value="perishable">Perishable</MenuItem>
                <MenuItem value="non-perishable">Non-Perishable</MenuItem>
              </Select>
            </FormControl>
            
            {newProduct.product_type === 'perishable' && (
              <TextField
                label="Expiry Date"
                name="expiry_date"
                type="date"
                value={newProduct.expiry_date}
                onChange={handleInputChange}
                fullWidth
                InputLabelProps={{ shrink: true }}
                error={!!errors.expiry_date}
                helperText={errors.expiry_date}
              />
            )}
            
            <TextField
              label="Price"
              name="price"
              value={newProduct.price}
              onChange={handleInputChange}
              fullWidth
              required
              InputProps={{
                startAdornment: <InputAdornment position="start">$</InputAdornment>,
              }}
              error={!!errors.price}
              helperText={errors.price}
            />
            
            <TextField
              label="Total Stock"
              name="total_stock"
              value={newProduct.total_stock}
              onChange={handleInputChange}
              fullWidth
              type="number"
              error={!!errors.total_stock}
              helperText={errors.total_stock}
            />
            
            <TextField
              label="Available Stock"
              name="available_stock"
              value={newProduct.available_stock}
              onChange={handleInputChange}
              fullWidth
              type="number"
              error={!!errors.available_stock}
              helperText={errors.available_stock || "Defaults to Total Stock if not specified"}
            />
            
            <TextField
              label="Location"
              name="location"
              value={newProduct.location}
              onChange={handleInputChange}
              fullWidth
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancel</Button>
          <Button onClick={handleSubmit} variant="contained" color="primary">
            Add Product
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default Products;