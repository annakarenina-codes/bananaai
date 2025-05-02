import { useState } from 'react';
import { FaSearch, FaBell, FaStar, FaEdit, FaTrash } from 'react-icons/fa';
import { FiChevronDown } from 'react-icons/fi';
import { IoSettingsOutline } from 'react-icons/io5';
import { AiOutlineQuestionCircle } from 'react-icons/ai';

const InventoryDashboard = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [notifications, setNotifications] = useState(1);

  const renderDashboardContent = () => {
    return (
      <div className="p-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Sales Forecast Card */}
        <div className="bg-white rounded-lg shadow p-5">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-xl font-semibold text-gray-700">Sales Forecast</h3>
            <button className="text-blue-400 hover:text-blue-600 text-sm">See more</button>
          </div>
          <p className="text-gray-600 text-sm">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          </p>
        </div>

        {/* Inventory Summary Card */}
        <div className="bg-white rounded-lg shadow p-5">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">Inventory Summary</h3>
          <div className="space-y-3">
            <div className="flex items-center">
              <div className="w-36 text-gray-600 text-sm">Quantity in hand</div>
              <div className="flex-1 bg-blue-400 text-white py-1 px-3 rounded text-center">
                198375
              </div>
            </div>
            <div className="flex items-center">
              <div className="w-36 text-gray-600 text-sm">Quantity to be Restocked</div>
              <div className="flex-1 bg-blue-400 text-white py-1 px-3 rounded text-center">
                258
              </div>
            </div>
          </div>
        </div>

        {/* Upcoming Demand Spike Card */}
        <div className="bg-white rounded-lg shadow p-5">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">Upcoming Demand Spike</h3>
          <div className="border border-gray-300 rounded p-4 h-32 flex items-center justify-center text-gray-500">
            Forecast shows month of XXX...
          </div>
          
          <h3 className="text-xl font-semibold text-gray-700 mt-6 mb-4">Restock Alerts</h3>
          <div className="border border-gray-300 rounded p-4 h-32 flex items-center justify-center text-gray-500">
            Product X requires...
          </div>
        </div>

        {/* Weekly Sales & Purchases Card - Full Width */}
        <div className="bg-white rounded-lg shadow p-5 md:col-span-2 lg:col-span-3">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">Weekly Sales & Purchases</h3>
          <div className="flex flex-col md:flex-row gap-6">
            <div className="flex-1">
              <div className="flex items-center mb-2">
                <div className="w-6 h-6 bg-blue-200 mr-2"></div>
                <span>Series 1</span>
                <div className="w-6 h-6 bg-blue-400 mx-2"></div>
                <span>Series 2</span>
              </div>
              <div className="h-60 flex items-end space-x-1">
                <div className="flex flex-col items-center">
                  <div className="flex space-x-1">
                    <div className="h-8 w-10 bg-blue-200"></div>
                    <div className="h-12 w-10 bg-blue-400"></div>
                  </div>
                  <div className="mt-2">Item 1</div>
                </div>
                <div className="flex flex-col items-center">
                  <div className="flex space-x-1">
                    <div className="h-16 w-10 bg-blue-200"></div>
                    <div className="h-28 w-10 bg-blue-400"></div>
                  </div>
                  <div className="mt-2">Item 2</div>
                </div>
                <div className="flex flex-col items-center">
                  <div className="flex space-x-1">
                    <div className="h-32 w-10 bg-blue-200"></div>
                    <div className="h-36 w-10 bg-blue-400"></div>
                  </div>
                  <div className="mt-2">Item 3</div>
                </div>
                <div className="flex flex-col justify-end h-full">
                  <div className="grid grid-cols-6 gap-1">
                    <div className="text-right text-gray-500 text-xs">0</div>
                    <div className="text-right text-gray-500 text-xs">5</div>
                    <div className="text-right text-gray-500 text-xs">10</div>
                    <div className="text-right text-gray-500 text-xs">15</div>
                    <div className="text-right text-gray-500 text-xs">20</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="flex-1">
              <div className="h-60 relative">
                <svg className="w-full h-full" viewBox="0 0 200 100">
                  <polyline
                    points="0,80 40,65 80,55 120,60 160,30 200,35"
                    fill="none"
                    stroke="#4fa8e0"
                    strokeWidth="2"
                  />
                  <circle cx="0" cy="80" r="3" fill="#4fa8e0" />
                  <circle cx="40" cy="65" r="3" fill="#4fa8e0" />
                  <circle cx="80" cy="55" r="3" fill="#4fa8e0" />
                  <circle cx="120" cy="60" r="3" fill="#4fa8e0" />
                  <circle cx="160" cy="30" r="3" fill="#4fa8e0" />
                  <circle cx="200" cy="35" r="3" fill="#4fa8e0" />
                </svg>
                <div className="absolute bottom-0 left-0 w-full grid grid-cols-5 text-center text-xs text-gray-500">
                  <div>Item 1</div>
                  <div>Item 2</div>
                  <div>Item 3</div>
                  <div>Item 4</div>
                  <div>Item 5</div>
                </div>
                <div className="absolute left-0 h-full flex flex-col justify-between text-right text-xs text-gray-500 -mt-2">
                  <div>40</div>
                  <div>30</div>
                  <div>20</div>
                  <div>10</div>
                  <div>0</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  };

  const renderForecastContent = () => {
    return (
      <div className="p-4 grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Product Performance Card */}
        <div className="bg-white rounded-lg shadow p-5">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">Product Performance</h3>
          <div className="flex items-center mb-2">
            <div className="w-6 h-6 bg-blue-200 mr-2"></div>
            <span>Series 1</span>
            <div className="w-6 h-6 bg-blue-400 mx-2"></div>
            <span>Series 2</span>
          </div>
          <div className="h-48 flex items-end space-x-1">
            <div className="flex flex-col items-center">
              <div className="flex space-x-1">
                <div className="h-8 w-10 bg-blue-200"></div>
                <div className="h-12 w-10 bg-blue-400"></div>
              </div>
              <div className="mt-2">Item 1</div>
            </div>
            <div className="flex flex-col items-center">
              <div className="flex space-x-1">
                <div className="h-16 w-10 bg-blue-200"></div>
                <div className="h-28 w-10 bg-blue-400"></div>
              </div>
              <div className="mt-2">Item 2</div>
            </div>
            <div className="flex flex-col items-center">
              <div className="flex space-x-1">
                <div className="h-32 w-10 bg-blue-200"></div>
                <div className="h-36 w-10 bg-blue-400"></div>
              </div>
              <div className="mt-2">Item 3</div>
            </div>
            <div className="flex flex-col justify-end h-full ml-4">
              <div className="grid grid-cols-5 gap-1">
                <div className="text-right text-gray-500 text-xs">0</div>
                <div className="text-right text-gray-500 text-xs">5</div>
                <div className="text-right text-gray-500 text-xs">10</div>
                <div className="text-right text-gray-500 text-xs">15</div>
                <div className="text-right text-gray-500 text-xs">20</div>
              </div>
            </div>
          </div>
        </div>

        {/* Profit Analysis Card */}
        <div className="bg-white rounded-lg shadow p-5">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">Profit Analysis</h3>
          <div className="relative h-48 flex items-center justify-center">
            <svg viewBox="0 0 100 100" width="180" height="180">
              <circle cx="50" cy="50" r="40" fill="transparent" stroke="#e5e7eb" strokeWidth="20" />
              <circle cx="50" cy="50" r="40" fill="transparent" stroke="#60a5fa" strokeWidth="20" strokeDasharray="50.26 251.3" strokeDashoffset="0" />
              <circle cx="50" cy="50" r="40" fill="transparent" stroke="#3b82f6" strokeWidth="20" strokeDasharray="50.26 251.3" strokeDashoffset="-50.26" />
              <circle cx="50" cy="50" r="40" fill="transparent" stroke="#2563eb" strokeWidth="20" strokeDasharray="50.26 251.3" strokeDashoffset="-100.52" />
              <circle cx="50" cy="50" r="40" fill="transparent" stroke="#1d4ed8" strokeWidth="20" strokeDasharray="50.26 251.3" strokeDashoffset="-150.78" />
              <circle cx="50" cy="50" r="40" fill="transparent" stroke="#1e40af" strokeWidth="20" strokeDasharray="50.26 251.3" strokeDashoffset="-201.04" />
            </svg>
            <div className="absolute top-0 right-4 text-xs text-gray-600">
              <div>Item 1 <br/>20%</div>
            </div>
            <div className="absolute top-1/4 right-2 text-xs text-gray-600">
              <div>Item 2 <br/>20%</div>
            </div>
            <div className="absolute bottom-1/4 right-2 text-xs text-gray-600">
              <div>Item 3 <br/>20%</div>
            </div>
            <div className="absolute bottom-0 right-4 text-xs text-gray-600">
              <div>Item 4 <br/>20%</div>
            </div>
            <div className="absolute bottom-1/4 left-4 text-xs text-gray-600">
              <div>Item 5 <br/>20%</div>
            </div>
          </div>
        </div>

        {/* Customer Behavior Card */}
        <div className="bg-white rounded-lg shadow p-5 lg:col-span-2">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">Customer Behavior</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="relative overflow-x-auto">
              <div className="flex mb-1">
                <div className="w-8 text-xs text-gray-400"></div>
                <div className="flex space-x-2 text-xs text-gray-400">
                  <div className="w-6 text-center">4am</div>
                  <div className="w-6 text-center">8am</div>
                  <div className="w-6 text-center">noon</div>
                  <div className="w-6 text-center">4pm</div>
                  <div className="w-6 text-center">8pm</div>
                  <div className="w-6 text-center">12am</div>
                </div>
              </div>
              {['S', 'M', 'T', 'W', 'T', 'F', 'S'].map((day, idx) => (
                <div key={idx} className="flex mb-1">
                  <div className="w-8 text-xs text-gray-400">{day}</div>
                  <div className="flex space-x-1">
                    {Array(24).fill().map((_, i) => (
                      <div 
                        key={i} 
                        className={`w-1 h-1 rounded-full ${Math.random() > 0.1 ? 'bg-green-500' : 'bg-green-900'}`}
                      ></div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <div className="flex flex-col justify-center">
              <h4 className="text-gray-700 mb-2">Net Sales</h4>
              <div className="text-blue-400 text-2xl font-semibold mb-4">PHP XXX,XXX</div>
              <h4 className="text-gray-700 mb-2">One sale every</h4>
              <div className="text-blue-400 text-2xl font-semibold">XX hour</div>
            </div>
          </div>
        </div>
      </div>
    );
  };

  const renderInventoryContent = () => {
    return (
      <div className="p-4">
        <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center mb-6 space-y-4 lg:space-y-0">
          <h2 className="text-3xl font-bold text-gray-700">INVENTORY</h2>
          <div className="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 w-full lg:w-auto">
            <div className="relative flex-grow md:w-64">
              <input
                type="text"
                placeholder="Search products"
                className="w-full pl-4 pr-10 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
              />
              <FaSearch className="absolute right-3 top-3 text-gray-400" />
            </div>
            <button className="bg-blue-100 text-blue-500 px-4 py-2 rounded hover:bg-blue-200 transition-colors">
              Update Inventory
            </button>
            <div className="relative inline-block text-left">
              <div>
                <button
                  type="button"
                  className="inline-flex justify-between w-full rounded border border-gray-300 px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-400"
                >
                  Sort by:
                  <FiChevronDown className="ml-2 -mr-1 h-5 w-5" aria-hidden="true" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow overflow-hidden">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-white">
              <tr>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  ID
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Product Image
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Product Name
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  QTY
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {[1, 2, 3, 4].map((item) => (
                <tr key={item}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    XXX-XXX
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="h-16 w-16 border border-gray-300 flex items-center justify-center">
                      <span className="text-gray-400 text-2xl">✕</span>
                    </div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                    Product X
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    XX
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <div className="flex space-x-3">
                      <button className="text-gray-600 hover:text-yellow-500">
                        <FaStar />
                      </button>
                      <button className="text-gray-600 hover:text-blue-500">
                        <FaEdit />
                      </button>
                      <button className="text-gray-600 hover:text-red-500">
                        <FaTrash />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  };

  const renderInvoiceContent = () => {
    return (
      <div className="p-4">
        <h2 className="text-3xl font-bold text-gray-700 mb-6">Invoice and Sales</h2>
        <div className="bg-white rounded-lg shadow p-6">
          <p className="text-gray-600">Invoice and Sales content would go here.</p>
        </div>
      </div>
    );
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-16 md:w-64 bg-white shadow-md flex flex-col">
        <div className="p-4 border-b border-gray-200">
          <div className="flex justify-center md:justify-start">
            <svg className="h-8 w-8" viewBox="0 0 100 100">
              <path d="M30,20 Q45,10 60,20 T90,40 Q75,50 60,40 T30,20" fill="#d946ef" />
              <path d="M30,60 Q45,50 60,60 T90,80 Q75,90 60,80 T30,60" fill="#f97316" />
            </svg>
          </div>
        </div>
        <nav className="flex-1 overflow-y-auto py-4">
          <div className={`flex items-center px-4 py-3 ${activeTab === 'dashboard' ? 'bg-blue-50 border-l-4 border-blue-500' : ''}`}>
            <button 
              onClick={() => setActiveTab('dashboard')}
              className="flex items-center w-full text-left"
            >
              <span className={`text-sm font-medium ${activeTab === 'dashboard' ? 'text-blue-500' : 'text-gray-600'}`}>
                <span className="hidden md:inline">Dashboard</span>
              </span>
            </button>
          </div>
          <div className={`flex items-center px-4 py-3 ${activeTab === 'inventory' ? 'bg-blue-50 border-l-4 border-blue-500' : ''}`}>
            <button 
              onClick={() => setActiveTab('inventory')}
              className="flex items-center w-full text-left"
            >
              <span className={`text-sm font-medium ${activeTab === 'inventory' ? 'text-blue-500' : 'text-gray-600'}`}>
                <span className="hidden md:inline">Inventory</span>
              </span>
            </button>
          </div>
          <div className={`flex items-center px-4 py-3 ${activeTab === 'forecast' ? 'bg-blue-50 border-l-4 border-blue-500' : ''}`}>
            <button 
              onClick={() => setActiveTab('forecast')}
              className="flex items-center w-full text-left"
            >
              <span className={`text-sm font-medium ${activeTab === 'forecast' ? 'text-blue-500' : 'text-gray-600'}`}>
                <span className="hidden md:inline">Forecast</span>
              </span>
            </button>
          </div>
          <div className={`flex items-center px-4 py-3 ${activeTab === 'invoice' ? 'bg-blue-50 border-l-4 border-blue-500' : ''}`}>
            <button 
              onClick={() => setActiveTab('invoice')}
              className="flex items-center w-full text-left"
            >
              <span className={`text-sm font-medium ${activeTab === 'invoice' ? 'text-blue-500' : 'text-gray-600'}`}>
                <span className="hidden md:inline">Invoice and Sales</span>
              </span>
            </button>
          </div>
        </nav>
        <div className="p-4 flex justify-center md:justify-between space-x-4 border-t border-gray-200">
          <button className="text-gray-500 hover:text-gray-700">
            <AiOutlineQuestionCircle className="h-6 w-6" />
          </button>
          <button className="text-gray-500 hover:text-gray-700">
            <IoSettingsOutline className="h-6 w-6" />
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Navbar */}
        <header className="bg-white shadow-sm z-10">
          <div className="flex items-center justify-between px-4 py-3">
            <div className="relative flex-1 max-w-2xl">
              <div className="relative">
                <input
                  type="text"
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400"
                  placeholder="Search"
                />
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <FaSearch className="h-4 w-4 text-gray-400" />
                </div>
                <button className="absolute inset-y-0 right-0 pr-3 flex items-center">
                  <FiChevronDown className="h-5 w-5 text-gray-400" />
                </button>
              </div>
            </div>
            <div className="flex items-center ml-4 space-x-4">
              <div className="relative">
                <button className="text-gray-600 hover:text-gray-800">
                  <FaBell className="h-6 w-6" />
                  {notifications > 0 && (
                    <span className="absolute top-0 right-0 block h-2 w-2 rounded-full bg-red-500"></span>
                  )}
                </button>
              </div>
              <div className="flex items-center">
                <span className="mr-2 text-gray-700">Hello, User!</span>
                <div className="h-10 w-10 rounded-full bg-gray-300 flex items-center justify-center text-gray-600">
                  <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* Page Content */}
        <main className="flex-1 overflow-y-auto bg-gray-100">
          {activeTab === 'dashboard' && renderDashboardContent()}
          {activeTab === 'forecast' && renderForecastContent()}
          {activeTab === 'inventory' && renderInventoryContent()}
          {activeTab === 'invoice' && renderInvoiceContent()}
        </main>
      </div>
    </div>
  );
};

export default InventoryDashboard;