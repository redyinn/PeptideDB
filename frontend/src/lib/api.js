import axios from 'axios';

const API_BASE = process.env.REACT_APP_BACKEND_URL || '';

const api = axios.create({
  baseURL: API_BASE,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Peptides
export const getPeptides = (params = {}) => api.get('/api/peptides', { params });
export const getPeptideDetail = (slug) => api.get(`/api/peptides/${slug}`);
export const generatePeptide = (name, forceRefresh = false) =>
  api.post('/api/peptides/generate', { name, force_refresh: forceRefresh });
export const seedPeptides = () => api.post('/api/peptides/seed');
export const getSeedStatus = () => api.get('/api/peptides/seed/status');
export const getCategories = () => api.get('/api/peptides/categories');

// Trials
export const getTrials = (params = {}) => api.get('/api/trials', { params });

// Papers
export const getPapers = (params = {}) => api.get('/api/papers', { params });

// News
export const getNews = (params = {}) => api.get('/api/news', { params });

// Stats
export const getStats = () => api.get('/api/stats');

// Health
export const healthCheck = () => api.get('/api/health');

export default api;
