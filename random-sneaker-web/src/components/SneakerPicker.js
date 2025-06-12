import React, { useState } from 'react';
import sneakers from '../data/sneakers';

const SneakerPicker = () => {
    const [selectedSneaker, setSelectedSneaker] = useState(null);

    const pickRandomSneaker = () => {
        const randomIndex = Math.floor(Math.random() * sneakers.length);
        setSelectedSneaker(sneakers[randomIndex]);
    };

    return (
        <div>
            <h1>Random Sneaker Picker</h1>
            <button onClick={pickRandomSneaker}>Pick a Sneaker</button>
            {selectedSneaker && (
                <div>
                    <h2>{selectedSneaker.name}</h2>
                    <p>Brand: {selectedSneaker.brand}</p>
                    <img src={selectedSneaker.image} alt={selectedSneaker.name} />
                </div>
            )}
        </div>
    );
};

export default SneakerPicker;