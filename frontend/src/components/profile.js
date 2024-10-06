// src/components/Profile.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/Profile.css'; // Ensure this path is correct

const Profile = () => {
  const [profile, setProfile] = useState({
    username: '',
    email: '',
    religious_restrictions: 'None',
    diet: 'None',
    allergies: [],
  });
  const [allergyOptions] = useState([
    'Peanuts',
    'Tree Nuts',
    'Milk',
    'Eggs',
    'Wheat',
    'Soy',
    'Fish',
    'Shellfish',
    'Gluten',
    'Sesame',
  ]);
  const [religiousOptions] = useState([
    'None',
    'Halal',
    'Kosher',
    'Hindu Vegetarian',
    // Add other options as needed
  ]);
  const [dietOptions] = useState([
    'None',
    'Vegetarian',
    'Vegan',
    'Paleo',
    'Keto',
    'Gluten-Free',
    // Add other options as needed
  ]);
  const [isLoading, setIsLoading] = useState(true);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  // Fetch user profile on component mount
  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem('token'); // Adjust if using a different storage method
        const response = await axios.get('/api/profile/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setProfile(response.data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching profile:', error);
        setErrorMessage('Failed to load profile.');
        setIsLoading(false);
      }
    };

    fetchProfile();
  }, []);

  // Handle form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  // Handle allergy checkbox changes
  const handleAllergyChange = (e) => {
    const { value, checked } = e.target;
    if (checked) {
      setProfile((prevState) => ({
        ...prevState,
        allergies: [...prevState.allergies, value],
      }));
    } else {
      setProfile((prevState) => ({
        ...prevState,
        allergies: prevState.allergies.filter((allergy) => allergy !== value),
      }));
    }
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccessMessage('');
    setErrorMessage('');

    try {
      const token = localStorage.getItem('token'); // Adjust if using a different storage method
      await axios.put(
        '/api/profile/',
        {
          religious_restrictions: profile.religious_restrictions,
          diet: profile.diet,
          allergies: profile.allergies,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setSuccessMessage('Profile updated successfully!');
    } catch (error) {
      console.error('Error updating profile:', error);
      setErrorMessage('Failed to update profile.');
    }
  };

  if (isLoading) {
    return <div>Loading profile...</div>;
  }

  return (
    <div className="profile-container">
      <h2>Your Profile</h2>
      {successMessage && <div className="success-message">{successMessage}</div>}
      {errorMessage && <div className="error-message">{errorMessage}</div>}
      <form onSubmit={handleSubmit} className="profile-form">
        <div className="form-group">
          <label>Username:</label>
          <input type="text" value={profile.username} disabled />
        </div>
        <div className="form-group">
          <label>Email:</label>
          <input type="email" value={profile.email} disabled />
        </div>
        <div className="form-group">
          <label>Religious Restrictions:</label>
          <select
            name="religious_restrictions"
            value={profile.religious_restrictions}
            onChange={handleChange}
          >
            {religiousOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label>Diet:</label>
          <select name="diet" value={profile.diet} onChange={handleChange}>
            {dietOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label>Allergies:</label>
          <div className="allergies-options">
            {allergyOptions.map((allergy) => (
              <label key={allergy} className="checkbox-label">
                <input
                  type="checkbox"
                  value={allergy}
                  checked={profile.allergies.includes(allergy)}
                  onChange={handleAllergyChange}
                />
                {allergy}
              </label>
            ))}
          </div>
        </div>
        <button type="submit" className="submit-button">
          Update Profile
        </button>
      </form>
    </div>
  );
};

export default Profile;
