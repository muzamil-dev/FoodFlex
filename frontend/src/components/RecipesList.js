import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/RecipesList.css';

const RecipesList = () => {
  const [favoriteRecipes, setFavoriteRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  

  // Hardcoded user ID
  const userId = '6701394b0a532741992776cf';

  // useEffect(() => {
  //   const fetchFavoriteRecipes = async () => {
  //     try {
  //       const response = await axios.get(
  //         `http://localhost:8000/users/favorite_recipes/${userId}/`
  //       );
  //       setFavoriteRecipes(response.data);
  //     } catch (err) {
  //       console.error('Error fetching favorite recipes:', err);
  //       setError('Failed to load favorite recipes.');
  //     } finally {
  //       setLoading(false);
  //     }
  //   };

  //   fetchFavoriteRecipes();
  // }, [userId]);

  // const removeFromFavorites = async (recipeId) => {
  //   try {
  //     await axios.post('http://localhost:8000/users/remove_favorite_recipe/', {
  //       user_id: userId,
  //       recipe_id: recipeId,
  //     });
  //     // Update the favoriteRecipes state
  //     setFavoriteRecipes((prevFavorites) =>
  //       prevFavorites.filter((recipe) => recipe.id !== recipeId)
  //     );
  //   } catch (err) {
  //     console.error('Error removing recipe from favorites:', err);
  //     alert('Failed to remove recipe from favorites.');
  //   }
  // };
   // Using useEffect to simulate fetching data
   useEffect(() => {
    const fetchFavoriteRecipes = async () => {
      try {
        // Simulating API call with hardcoded data for now
        const response = {
          data: [
            {
              id: 1,
              title: 'Spaghetti Carbonara',
              description: 'A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.',
              ingredients: 'Spaghetti, Eggs, Pancetta, Parmesan, Pepper',
              instructions: 'Cook the spaghetti. In a bowl, mix eggs and cheese. Fry pancetta. Combine everything and serve.',
            },
            {
              id: 2,
              title: 'Vegan Avocado Toast',
              description: 'Healthy avocado toast topped with cherry tomatoes, sesame seeds, and olive oil.',
              ingredients: 'Avocado, Bread, Cherry Tomatoes, Olive Oil, Sesame Seeds',
              instructions: 'Toast the bread. Mash avocado and spread it on the toast. Add cherry tomatoes, olive oil, and sesame seeds.',
            },
            {
              id: 3,
              title: 'Chicken Alfredo',
              description: 'A creamy pasta dish made with fettuccine, chicken, butter, cream, and Parmesan cheese.',
              ingredients: 'Chicken, Fettuccine, Butter, Cream, Parmesan',
              instructions: 'Cook the fettuccine. Fry the chicken. Make the Alfredo sauce with butter, cream, and Parmesan. Mix and serve.',
            },
            {
              id: 4,
              title: 'Quinoa Salad',
              description: 'A refreshing salad with quinoa, cucumbers, tomatoes, and feta cheese.',
              ingredients: 'Quinoa, Cucumbers, Tomatoes, Feta, Olive Oil',
              instructions: 'Cook the quinoa. Chop cucumbers and tomatoes. Mix with olive oil and feta cheese. Serve chilled.',
            },
            {
              id: 5,
              title: 'Chocolate Chip Cookies',
              description: 'Crispy on the outside, chewy on the inside cookies loaded with chocolate chips.',
              ingredients: 'Flour, Sugar, Butter, Eggs, Chocolate Chips',
              instructions: 'Mix the ingredients, form cookies, and bake at 180°C for 12 minutes.',
            }
          ]
        };

        // Set the fetched data
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
      // Simulate removing a favorite recipe
      await new Promise((resolve) => setTimeout(resolve, 500)); // Simulating delay
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
        <div className="recipes-grid">
          {favoriteRecipes.map((recipe) => (
            <div key={recipe.id} className="recipe-card">
              {recipe.image && <img src={recipe.image} alt={recipe.title} className="recipe-image" />}
              <div className="recipe-body">
                <h2 className="recipe-title">{recipe.title}</h2>
                <p className="recipe-description"><strong>Description:</strong> {recipe.description}</p>
                <hr />
                <div className="recipe-ingredients">
                  <strong>Ingredients:</strong>
                  <ul>
                    {recipe.ingredients.split(',').map((ingredient, index) => (
                      <li key={index}>{ingredient.trim()}</li>
                    ))}
                  </ul>
                </div>
                <hr />
                <div className="recipe-instructions">
                  <strong>Instructions:</strong>
                  <p>{recipe.instructions}</p>
                </div>
                <button
                  className="remove-button"
                  onClick={() => removeFromFavorites(recipe.id)}
                >
                  Remove from Favorites
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default RecipesList;
