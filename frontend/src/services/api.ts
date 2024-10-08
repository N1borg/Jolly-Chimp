import axios, { AxiosRequestConfig } from 'axios';

// Create an instance of axios with a base URL
const apiClient = axios.create({
  baseURL: '/api', // Base URL for all API calls
  timeout: 10000,  // Set a timeout limit of 10 seconds (optional)
});

// Example function to get data from the API
export const fetchData = async <T>(endpoint: string, config?: AxiosRequestConfig): Promise<T> => {
  try {
    const response = await apiClient.get<T>(endpoint, config);
    return response.data;
  } catch (error: any) {
    if (error.response) {
      // Server responded with a status other than 2xx
      console.error('Error response:', error.response.status, error.response.data);
    } else if (error.request) {
      // Request was made but no response received
      console.error('Error request:', error.request);
    } else {
      // Something happened in setting up the request
      console.error('Error setting up request:', error.message);
    }
    throw error;
  }
};
