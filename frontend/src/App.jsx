import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SearchResults from './pages/SearchResults';
import ListingPage from './pages/ListingPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SearchResults />} />
        <Route path="/listing/:id" element={<ListingPage />} />
      </Routes>
    </Router>
  );
}

export default App;
