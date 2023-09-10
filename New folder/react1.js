import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TrainList.css';  // Import the CSS

const TrainList = () => {
  // ... (rest of your code)
  
  return (
    <div>
      <h1>All Trains</h1>
      {trains.map(train => (
        <div key={train.id} className="train-container">
          <p className="train-name">Train Name: {train.name}</p>
          <p className="price">Price: {train.price}</p>
          <p className="seatsAvailable">Seats Available: {train.seatsAvailable}</p>
          {/* Add more details */}
        </div>
      ))}
    </div>
  );
};

export default TrainList;