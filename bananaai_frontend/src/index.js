import React from 'react';
import ReactDOM from 'react-dom/client'; // React 18+ updated syntax
import App from './App';
import './index.css'; // Your global styles

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
