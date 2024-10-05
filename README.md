# FoodFlex (or FlexEat) - AI-Powered Recipe Customizer for Dietary Restrictions

// initial ideas
## Overview

**FoodFlex** is an AI-powered web app designed to help users customize recipes based on their dietary restrictions, allergies, and preferences. This application is perfect for individuals who need to modify recipes (e.g., for vegan, vegetarian, gluten-free, halal, kosher, or allergen-free diets). The app leverages AI to analyze and modify recipes, ensuring they match user-defined dietary profiles.

With a user-friendly interface, FoodFlex makes it easy for users to upload a recipe (via text, URL, or image) and receive a customized version that suits their specific needs. This tool is great for anyone with dietary restrictions and can be used by people looking to maintain specific nutritional goals.

## Features

- **User Authentication**
  - **Login/Sign-Up**: Users can register and log in with their accounts.
  - **Profile Setup**: Users can add dietary restrictions, allergy information, and religious restrictions (e.g., Halal, Kosher) to their profile.
  
- **Recipe Input Options**
  - **Recipe URL Upload**: Users can paste a recipe URL for automatic retrieval.
  - **Image Upload**: Users can upload a photo of a recipe, which will be processed with OCR to extract ingredients and instructions.
  - **Text Input**: Users can manually input recipe ingredients and instructions.

- **AI-Based Recipe Customization**
  - **Chatbot 1: Ingredient Checker**: This chatbot checks whether ingredients from a recipe match the user's dietary profile.
  - **Chatbot 2: Recipe Generator/Customizer**: Generates or modifies a recipe to match user dietary preferences (vegan, gluten-free, etc.).
  
- **Ingredient Database & Brand Recognition**
  - **Store-Specific Ingredients**: The app allows users to scan items (e.g., sauce brands) and store them for future reference to determine if they align with dietary restrictions.
  
- **Nutritional Information**
  - Provides a detailed nutritional breakdown of any modified recipe using APIs like Nutritionix, Edamam, or FoodData Central.

- **Recipe Storage & History**
  - **Recipe History**: Stores user-modified recipes, allowing them to access or share them with others.
  - **Search**: Users can search through saved recipes by dietary needs or keywords.

- **Camera Feature**
  - Users can take photos of recipes or ingredients with their phone camera for quick uploading and checking.

- **Visualization & Instructions**
  - Displays step-by-step cooking instructions along with ingredient details and nutritional information using Streamlit.

## Use Case

1. **Scenario**: A user with gluten and dairy allergies finds a recipe for lasagna online but needs it modified. They upload the recipe URL into FoodFlex, and the app uses AI to swap out ingredients (e.g., replacing wheat-based pasta with gluten-free options, dairy cheese with vegan alternatives). The user can save this modified version, along with its nutritional breakdown, for future use or share it with friends.

2. **Scenario 2**: A user at the grocery store scans a bottle of sauce and asks the chatbot if it fits their dietary profile. If it’s okay, the app stores that information for future purchases and checks.

## Requirements

### Back-end:
- **Django**: For user authentication, profile management, and API handling.
- **MongoDB Atlas**: For storing user profiles, recipe history, and ingredient data.
- **OpenAI API** or **Spoonacular API**: For recipe modification and AI-based ingredient replacement.
- **Edamam API** or **Nutritionix API**: For providing nutritional information about the modified recipes.
- **Tesseract (or any OCR API)**: For extracting text from uploaded recipe images.

### Front-end:
- **React.js** or **Next.js**: For building the user interface.
- **TypeScript**: For structured JavaScript development.
- **Streamlit**: For recipe visualization, step-by-step instructions, and nutritional breakdown.

### Other Technologies:
- **Cloudflare**: For DNS and security.
- **Databricks**: (Optional) For advanced AI model development, such as personalized dietary prediction based on historical data.
- **Twilio (Optional)**: For SMS or notification services, sending recipe recommendations.
