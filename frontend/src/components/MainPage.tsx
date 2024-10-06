import React, { useEffect, useState } from 'react';
import { fetchData } from '../api';

interface DataItem {
  id: number;
  name: string;
  url: string;
  status: string;
}

const MainPage: React.FC = () => {
  const [data, setData] = useState<DataItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchApiData = async () => {
      try {
        const result = await fetchData('/websites/');
        setData(result);
      } catch (err) {
        setError('Error fetching data');
      } finally {
        setLoading(false);
      }
    };

    fetchApiData();
  }, []);

  if (loading) {
    return <div className="text-center">Loading...</div>;
  }

  if (error) {
    return <div className="text-center text-red-500">{error}</div>;
  }

  return (
    <div className="container mx-auto mt-4">
      <h1 className="text-2xl font-bold text-center">Service Monitoring</h1>
      <div className="mt-4">
        {data.map(item => (
          <div key={item.id} className="p-4 border rounded shadow mb-4">
            <h2 className="font-semibold">{item.name} ({item.url})</h2>
            <p>Status: {item.status ? 'up' : 'down'}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MainPage;
