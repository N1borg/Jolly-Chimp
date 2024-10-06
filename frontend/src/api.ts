import axios from 'axios';

// const API_BASE_URL = import.meta.env.NODE_ENV === 'development'
// ? 'http://localhost:8000/' // For local development
// : 'http://api:8000/'; // When running in Docker

// const API_BASE_URL = 'http://localhost:8000/';

// console.log('API_BASE_URL:', API_BASE_URL);
// console.log('NODE_ENV:', import.meta.env.NODE_ENV);

// Create an instance of axios with the base URL
// const api = axios.create({
//   baseURL: API_BASE_URL,
// });

// Example function to get data from the API
export const fetchData = async (endpoint: string) => {
  try {
    const response = await axios.get('/api' + endpoint);
    console.log('response:', response);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

// Export the axios instance if needed for other requests
// export default api;
