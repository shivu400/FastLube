build front end for shop inventory 
import React, { useState, useEffect } from 'react';

const ShopInventory = () => {
  const [inventory, setInventory] = useState({});
  const [newItem, setNewItem] = useState({
    itemId: '',
    name: '',
    price: '',
    quantity: ''
  });

  // Form handlers
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewItem(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would typically make an API call to add the item
    console.log('New item to add:', newItem);
  };

  return (
    <div className="shop-inventory">
      <h1>Shop Inventory Management</h1>

      {/* Add New Item Form */}
      <div className="add-item-form">
        <h2>Add New Item</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Item ID:</label>
            <input
              type="text"
              name="itemId"
              value={newItem.itemId}
              onChange={handleInputChange}
            />
          </div>
          <div>


