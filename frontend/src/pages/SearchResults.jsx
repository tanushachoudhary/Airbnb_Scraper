import React, { useEffect, useState } from 'react';
import api from '../api';
import ListingCard from '../components/ListingCard';

export default function SearchResults() {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    api.get('/listings').then(res => setListings(res.data));
  }, []);

  return (
    <div className="p-6 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      {listings.map((listing, index) => (
        <ListingCard key={index} data={listing} />
      ))}
    </div>
  );
}
