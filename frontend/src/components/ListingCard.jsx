import React from "react";
import { Link } from "react-router-dom";

export default function ListingCard({ data }) {
  return (
    <div className="border rounded-xl p-4 shadow-md hover:shadow-lg">
      <Link to={`/listing/${data.id}`}>
        <img src={data.image_urls[0]} alt={data.title} className="..." />
        <h3 className="...">{data.title}</h3>
      </Link>

      <p>{data.location}</p>
      <p>${data.price_per_night} / night</p>
      <p className="text-yellow-500">★ {data.ratings}</p>
    </div>
  );
}
