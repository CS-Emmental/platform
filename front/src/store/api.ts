import axios from 'axios';

export default () => axios.create({
  baseURL: 'http://localhost/api/',
  withCredentials: true,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});
