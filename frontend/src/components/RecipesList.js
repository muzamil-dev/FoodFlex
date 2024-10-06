import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Button, Modal } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/RecipesList.css';

const RecipesList = () => {
  const [favoriteRecipes, setFavoriteRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedRecipe, setSelectedRecipe] = useState(null); // Track the currently selected recipe
  const [showModal, setShowModal] = useState(false);

  // Hardcoded user ID
  const userId = localStorage.getItem('userId');
  
  useEffect(() => {
    const fetchFavoriteRecipes = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/users/favorite_recipes/${userId}/`
        );
        setFavoriteRecipes(response.data);
      } catch (err) {
        console.error('Error fetching favorite recipes:', err);
        setError('Failed to load favorite recipes.');
      } finally {
        setLoading(false);
      }
    };

    fetchFavoriteRecipes();
  }, [userId]);

  const removeFromFavorites = async (recipeId) => {
    try {
      await axios.post('http://localhost:8000/users/remove_favorite_recipe/', {
        user_id: userId,
        recipe_id: recipeId,
      });
      // Update the favoriteRecipes state
      setFavoriteRecipes((prevFavorites) =>
        prevFavorites.filter((recipe) => recipe.id !== recipeId)
      );
    } catch (err) {
      console.error('Error removing recipe from favorites:', err);
      alert('Failed to remove recipe from favorites.');
    }
  };

  // Function to handle clicking a recipe to open the modal
  const handleRecipeClick = (recipe) => {
    setSelectedRecipe(recipe);
    setShowModal(true);
  };

  if (loading) {
    return <div>Loading favorite recipes...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div className="main-content">
      <h1>Your Favorite Recipes</h1>
      {favoriteRecipes.length === 0 ? (
        <p>You have no favorite recipes.</p>
      ) : (
        <Container>
          <Row>
            {favoriteRecipes.map((recipe) => (
              <Col key={recipe.id} xs={12} sm={6} className="mb-4">
                <Card className="h-100 shadow-sm hashbox">
                  <Card.Body onClick={() => handleRecipeClick(recipe)} style={{ cursor: 'pointer' }}>
                    <Card.Title>{recipe.title}</Card.Title>
                    <Card.Text>
                      <strong>Description:</strong> {recipe.description}
                    </Card.Text>
                  </Card.Body>
                  <Button
                    variant="danger"
                    className="btn mt-3 custbtn"
                    onClick={() => removeFromFavorites(recipe.id)}
                    style={{ width: '100%' }}
                  >
                    Remove from Favorites
                  </Button>
                </Card>
              </Col>
            ))}
          </Row>
        </Container>
      )}

      {/* Modal to display the full recipe details */}
      {selectedRecipe && (
        <Modal show={showModal} onHide={() => setShowModal(false)}>
          <Modal.Header closeButton>
            <Modal.Title>{selectedRecipe.title}</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <p><strong>Description:</strong> {selectedRecipe.description}</p>
            <hr />
            <p><strong>Ingredients:</strong></p>
            <ul>
              {selectedRecipe.ingredients.split(',').map((ingredient, index) => (
                <li key={index}>{ingredient.trim()}</li>
              ))}
            </ul>
            <hr />
            <p><strong>Instructions:</strong></p>
            <p>{selectedRecipe.instructions}</p>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={() => setShowModal(false)}>
              Close
            </Button>
          </Modal.Footer>
        </Modal>
      )}
    </div>
  );
};

export default RecipesList;
