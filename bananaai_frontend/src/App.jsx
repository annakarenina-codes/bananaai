import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import InventoryDashboard from './pages/InventoryDashboard';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<InventoryDashboard />} />
        <Route path="/inventory" element={<InventoryDashboard />} />
        <Route path="/forecast" element={<InventoryDashboard />} />
        <Route path="/invoice" element={<InventoryDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;