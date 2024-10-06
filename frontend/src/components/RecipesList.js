import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


import '../styles/RecipesList.css';

const RecipesList = () => {
  const [favoriteRecipes, setFavoriteRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Hardcoded user ID
  const userId = '6701394b0a532741992776cf';

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
                <Card className="h-100 shadow-sm">
                  {recipe.image && <Card.Img variant="top" src={recipe.image} />}
                  <Card.Body>
                    <Card.Title>{recipe.title}</Card.Title>
                    <Card.Text>
                      <strong>Description:</strong> {recipe.description}
                    </Card.Text>
                    <hr />
                    <Card.Text>
                      <strong>Ingredients:</strong>
                      <ul>
                        {recipe.ingredients.split(',').map((ingredient, index) => (
                          <li key={index}>{ingredient.trim()}</li>
                        ))}
                      </ul>
                    </Card.Text>
                    <hr />
                    <Card.Text>
                      <strong>Instructions:</strong>
                      <p>{recipe.instructions}</p>
                    </Card.Text>
                    <Button
                      variant="danger"
                      className="btn mt-3"
                      onClick={() => removeFromFavorites(recipe.id)}
                      style={{ width: '100%' }}
                    >
                      Remove from Favorites
                    </Button>
                  </Card.Body>
                </Card>
              </Col>
            ))}
          </Row>
        </Container>
      )}
    </div>
  );
};

export default RecipesList;
