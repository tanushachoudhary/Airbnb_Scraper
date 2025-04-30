import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api';

export default function ListingPage() {
  const { id } = useParams();
  const [listing, setListing] = useState(null);

  useEffect(() => {
    api.get('/listings').then(res => {
      const match = res.data.find(item => item.id.toString() === id);
      if (match) setListing(match);
    });
  }, [id]);

  if (!listing) return <div className="p-6">Loading...</div>;

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <img src={listing.image_urls[0]} alt={listing.title} className="w-full h-80 object-cover rounded-lg mb-4" />
      <h1 className="text-3xl font-bold">{listing.title}</h1>
      <p className="text-gray-600 mb-2">{listing.location} · {listing.property_type}</p>
      <p className="text-xl text-green-600 font-semibold mb-2">${listing.price_per_night} / night</p>
      <p className="text-yellow-500">★ {listing.ratings} · {listing.number_of_reviews} reviews</p>
      <p className="mt-4">{listing.description}</p>
      <div className="mt-4">
        <h2 className="text-lg font-semibold">Amenities:</h2>
        <ul className="list-disc list-inside">
          {listing.amenities.map((a, i) => <li key={i}>{a}</li>)}
        </ul>
      </div>
      <div className="mt-4 border-t pt-4">
        <h2 className="text-lg font-semibold">Host: {listing.host.name}</h2>
        <img src={listing.host.profile_url} alt="Host" className="h-16 w-16 rounded-full mt-2" />
        <p>{listing.host.is_superhost ? 'Superhost' : 'Host'}</p>
      </div>
    </div>
  );
}
