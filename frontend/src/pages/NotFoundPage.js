import React from 'react';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FlaskConical, ArrowLeft, Search } from 'lucide-react';
import { Button } from '../components/ui/button';

export default function NotFoundPage() {
  return (
    <div className="min-h-[60vh] flex items-center justify-center px-4">
      <Helmet>
        <title>Page Not Found — PeptideDB</title>
      </Helmet>
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="text-center max-w-md"
      >
        <FlaskConical className="w-16 h-16 text-muted-foreground mx-auto mb-6 opacity-40" />
        <h1 className="text-5xl font-bold mb-3 text-muted-foreground/30" style={{ fontFamily: 'Space Grotesk' }}>404</h1>
        <h2 className="text-xl font-semibold mb-2" style={{ fontFamily: 'Space Grotesk' }}>Page not found</h2>
        <p className="text-sm text-muted-foreground mb-8 leading-relaxed">
          The compound you're looking for doesn't exist in our database — or the URL may have changed.
        </p>
        <div className="flex flex-col sm:flex-row gap-3 justify-center">
          <Button asChild variant="default" className="rounded-xl gap-2">
            <Link to="/encyclopedia">
              <Search className="w-4 h-4" />
              Browse Encyclopedia
            </Link>
          </Button>
          <Button asChild variant="outline" className="rounded-xl gap-2">
            <Link to="/">
              <ArrowLeft className="w-4 h-4" />
              Back to Home
            </Link>
          </Button>
        </div>
      </motion.div>
    </div>
  );
}
