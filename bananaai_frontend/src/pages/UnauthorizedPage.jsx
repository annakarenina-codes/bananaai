import { Link, useNavigate } from 'react-router-dom';
import { FaExclamationTriangle, FaHome, FaSignInAlt } from 'react-icons/fa';
import { useAuth } from '../context/AuthContext';

const UnauthorizedPage = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleGoBack = () => {
    navigate(-1);
  };

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
      <div className="max-w-md w-full text-center">
        {/* Logo */}
        <div className="flex justify-center mb-8">
          <svg className="h-16 w-16" viewBox="0 0 100 100">
            <path d="M30,20 Q45,10 60,20 T90,40 Q75,50 60,40 T30,20" fill="#d946ef" />
            <path d="M30,60 Q45,50 60,60 T90,80 Q75,90 60,80 T30,60" fill="#f97316" />
          </svg>
        </div>

        {/* Error Icon */}
        <div className="flex justify-center mb-6">
          <div className="bg-red-100 rounded-full p-6">
            <FaExclamationTriangle className="h-16 w-16 text-red-600" />
          </div>
        </div>

        {/* Main Content */}
        <div className="bg-white rounded-lg shadow-md p-8">
          <h1 className="text-4xl font-bold text-gray-700 mb-4">403</h1>
          <h2 className="text-2xl font-semibold text-gray-700 mb-4">Access Denied</h2>
          
          <p className="text-gray-600 mb-6">
            Sorry, you don't have permission to access this page. This area is restricted to authorized users only.
          </p>

          {user ? (
            <div className="mb-6 p-4 bg-blue-50 rounded-lg">
              <p className="text-sm text-blue-800">
                <strong>Current User:</strong> {user.email || user.username}
              </p>
              <p className="text-sm text-blue-600 mt-1">
                You may need additional permissions to access this resource.
              </p>
            </div>
          ) : (
            <div className="mb-6 p-4 bg-yellow-50 rounded-lg">
              <p className="text-sm text-yellow-800">
                You are not currently signed in. Please log in to access this page.
              </p>
            </div>
          )}

          {/* Action Buttons */}
          <div className="space-y-4">
            {user ? (
              <>
                <Link
                  to="/dashboard"
                  className="w-full flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
                >
                  <FaHome className="mr-2" />
                  Go to Dashboard
                </Link>
                
                <button
                  onClick={handleGoBack}
                  className="w-full flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-lg text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
                >
                  Go Back
                </button>

                <button
                  onClick={handleLogout}
                  className="w-full flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-lg text-red-600 bg-white hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors"
                >
                  <FaSignInAlt className="mr-2" />
                  Sign Out & Login as Different User
                </button>
              </>
            ) : (
              <>
                <Link
                  to="/login"
                  className="w-full flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
                >
                  <FaSignInAlt className="mr-2" />
                  Sign In
                </Link>
                
                <Link
                  to="/register"
                  className="w-full flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-lg text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
                >
                  Create Account
                </Link>
              </>
            )}
          </div>

          {/* Additional Help */}
          <div className="mt-8 pt-6 border-t border-gray-200">
            <p className="text-sm text-gray-500 mb-2">Need help?</p>
            <div className="flex justify-center space-x-4 text-sm">
              <a href="#" className="text-blue-600 hover:text-blue-500">
                Contact Support
              </a>
              <a href="#" className="text-blue-600 hover:text-blue-500">
                FAQ
              </a>
              <a href="#" className="text-blue-600 hover:text-blue-500">
                Documentation
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UnauthorizedPage;