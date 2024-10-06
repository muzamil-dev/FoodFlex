import React from 'react';
import '../styles/Items.css';

const Items = () => {
  // Placeholder data with product names, ingredients, and whether the user can eat them or not
  const items = [
    { name: 'Gluten-Free Bread', ingredients: ['Rice Flour', 'Yeast', 'Water'], canEat: true },
    { name: 'Cheddar Cheese', ingredients: ['Milk', 'Salt', 'Rennet'], canEat: false },
    { name: 'Vegan Burger', ingredients: ['Soy Protein', 'Beetroot Juice', 'Spices'], canEat: true },
    { name: 'Milk Chocolate', ingredients: ['Cocoa', 'Milk', 'Sugar'], canEat: false },
    { name: 'Quinoa Salad', ingredients: ['Quinoa', 'Tomatoes', 'Cucumbers'], canEat: true },
  ];

  return (
    <div className="items-container">
      <h1>Items Page</h1>
      
      {/* Grid container for the items */}
      <div className="items-grid">
        {/* Render a card for each item */}
        {items.map((item, index) => (
          <div key={index} className={`item-box ${item.canEat ? 'good' : 'bad'}`}>
            <h2>{item.name}</h2>
            <p><strong>Ingredients:</strong> {item.ingredients.join(', ')}</p>
            <p><strong>Status:</strong> {item.canEat ? 'You can eat this' : 'You cannot eat this'}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Items;  // Ensure it's a default export
