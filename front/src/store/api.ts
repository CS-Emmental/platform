import axios from 'axios';
import Vue from 'vue';

export const api = axios.create({
  baseURL: '/api/',
  withCredentials: true,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

api.interceptors.response.use(res => res, (error) => {
  Vue.toasted.show(`Code: ${error.response.data.error_code}</br>${error.response.data.error_message}`, {
    type: 'error',
  });
  return Promise.reject(error);
});

export default api;
