import React from 'react';

const StatusUp: React.FC = () => (
  <div className="w-20 text-center font-bold py-1 px-2 rounded-md bg-green-500/20 text-green-900">
    up
  </div>
);

const StatusUnknown: React.FC = () => (
  <div className="w-20 text-center font-bold py-1 px-2 rounded-md bg-yellow-500/20 text-yellow-900">
    unknown
  </div>
);

const StatusDown: React.FC = () => (
  <div className="w-20 text-center font-bold py-1 px-2 rounded-md bg-red-500/20 text-red-900">
    down
  </div>
);

export { StatusUp, StatusUnknown, StatusDown };
