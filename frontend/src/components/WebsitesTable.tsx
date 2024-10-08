import React from 'react';
import { WebsitesTableProps } from '../types/types';
import { StatusUp, StatusUnknown, StatusDown } from './StatusSticker';

const WebsitesTable: React.FC<WebsitesTableProps> = ({ data, loading, error }) => {
  if (loading)
    return <div>Loading...</div>;
  if (error)
    return <div>{error}</div>;

  return (
    <div className="w-full max-w-2xl mx-auto bg-white shadow-lg rounded-lg border border-gray-200">
      <header className="px-5 py-4 border-b border-gray-100">
        <h2 className="font-semibold text-gray-800">Websites</h2>
      </header>

      <div className="p-3">
        <div className="overflow-x-auto">
          <table className="table-auto w-full text-sm">
            <thead className="font-semibold uppercase text-gray-400 bg-gray-50">
              <tr>
                <th className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <div className="font-semibold text-left">Name</div>
                </th>
                <th className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <div className="font-semibold text-left">URL</div>
                </th>
                <th className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <div className="font-semibold text-left">Status</div>
                </th>
                <th className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <div className="font-semibold text-left">Latency</div>
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 max-h-96 overflow-y-auto">
              {data.map((item) => (
              <tr key={item.id}>
                <td className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <div className="flex items-center">
                    <div className="h-8 flex-shrink-0 mr-2 sm:mr-3"></div>
                    <div className="font-semibold font-medium text-gray-800">{item.name}</div>
                  </div>
                </td>
                <td className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <a href={item.url} className="text-left text-blue-500 hover:underline" target="_blank" rel="noopener noreferrer">
                    {item.url}
                  </a>
                </td>
                <td className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                    <div className="w-20 text-center font-bold py-1 px-2 rounded-md">
                    {item.status ? (
                      <StatusUp />
                    ) : item.latency > 0 ? (
                      <StatusUnknown />
                    ) : (
                      <StatusDown />
                    )}
                    </div>
                </td>
                <td className="p-2 whitespace-nowrap max-w-xs overflow-hidden overflow-ellipsis">
                  <div className="text-center font-semibold py-1 px-2 rounded-md">
                    {item.latency} ms
                  </div>
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

export default WebsitesTable;
