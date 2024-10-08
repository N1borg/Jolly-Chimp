import React from 'react';
import { PiHoleTableProps } from '../types/types';
import { StatusUp, StatusDown } from './StatusSticker';

const PiHoleTable: React.FC<PiHoleTableProps> = ({ data, loading, error }) => {
  if (loading)
    return <div>Loading...</div>;
  if (error)
    return <div>{error}</div>;

  return (
    <div className="w-full max-w-2xl mx-auto bg-white shadow-lg rounded-lg border border-gray-200">
      <header className="px-5 py-4 border-b border-gray-100">
        <h2 className="font-semibold text-gray-800">Pi-Hole</h2>
      </header>

      <div className="p-3">
        <div className="overflow-x-auto">
          <table className="table-auto w-full text-sm max-w-full overflow-x-auto">
            <thead className="font-semibold uppercase text-gray-400 bg-gray-50">
              <tr>
              <th className="p-2 whitespace-nowrap">
                <div className="font-semibold text-left">Name</div>
              </th>
              <th className="p-2 whitespace-nowrap">
                <div className="font-semibold text-left">Status</div>
              </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {data.map((item) => (
              <tr key={item.id}>
                <td className="p-2 whitespace-nowrap">
                  <div className="flex items-center">
                  <div className="h-10 flex-shrink-0 mr-2 sm:mr-3"></div>
                  <div className="font-semibold font-medium text-gray-800">{item.name}</div>
                  </div>
                </td>
                <td className="p-2 whitespace-nowrap">
                  {item.status ? <StatusUp /> : <StatusDown />}
                </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default PiHoleTable;
