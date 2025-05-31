import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const ProtectedRoute = ({ requireRoles }) => {
  const { currentUser, loading, hasRole } = useAuth();
  
  // Show loading state
  if (loading) {
    return <div>Loading...</div>;
  }

  // If not authenticated, redirect to login
  if (!currentUser) {
    return <Navigate to="/login" replace />;
  }

  // If roles are required, check if user has the required role
  if (requireRoles && !hasRole(requireRoles)) {
    return <Navigate to="/unauthorized" replace />;
  }

  // User is authenticated and has the required role (if any)
  return <Outlet />;
};

export default ProtectedRoute;