import React, { useState } from 'react';
import SneakerPicker from './components/SneakerPicker';

function App() {
  const [selectedSneaker, setSelectedSneaker] = useState(null);

  const handleSelectSneaker = (sneaker) => {
    setSelectedSneaker(sneaker);
  };

  return (
    <div className="App">
      <h1>Random Sneaker Picker</h1>
      <SneakerPicker onSelectSneaker={handleSelectSneaker} />
      {selectedSneaker && (
        <div>
          <h2>Selected Sneaker:</h2>
          <p>{selectedSneaker.name} by {selectedSneaker.brand}</p>
          <img src={selectedSneaker.image} alt={selectedSneaker.name} />
        </div>
      )}
    </div>
  );
}

export default App;