import React, { Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './i18n/i18n';
import './App.css';
import Navbar from './components/Layout/Navbar';
import Footer from './components/Layout/Footer';
import { Toaster } from './components/ui/sonner';

const HomePage = React.lazy(() => import('./pages/HomePage'));
const EncyclopediaPage = React.lazy(() => import('./pages/EncyclopediaPage'));
const PeptideDetailPage = React.lazy(() => import('./pages/PeptideDetailPage'));
const StudiesPage = React.lazy(() => import('./pages/StudiesPage'));
const PapersPage = React.lazy(() => import('./pages/PapersPage'));
const NewsPage = React.lazy(() => import('./pages/NewsPage'));
const ComparePage = React.lazy(() => import('./pages/ComparePage'));
const GlossaryPage = React.lazy(() => import('./pages/GlossaryPage'));
const NotFoundPage = React.lazy(() => import('./pages/NotFoundPage'));

function LoadingFallback() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-background">
      <div className="flex flex-col items-center gap-4">
        <div className="w-10 h-10 border-2 border-primary border-t-transparent rounded-full animate-spin" />
        <p className="text-sm text-muted-foreground">Loading...</p>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-background flex flex-col">
        <Navbar />
        <main className="flex-1">
          <Suspense fallback={<LoadingFallback />}>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/encyclopedia" element={<EncyclopediaPage />} />
              <Route path="/encyclopedia/compare" element={<ComparePage />} />
              <Route path="/encyclopedia/:slug" element={<PeptideDetailPage />} />
              <Route path="/studies" element={<StudiesPage />} />
              <Route path="/papers" element={<PapersPage />} />
              <Route path="/news" element={<NewsPage />} />
              <Route path="/glossary" element={<GlossaryPage />} />
              <Route path="*" element={<NotFoundPage />} />
            </Routes>
          </Suspense>
        </main>
        <Footer />
        <Toaster />
      </div>
    </Router>
  );
}

export default App;
