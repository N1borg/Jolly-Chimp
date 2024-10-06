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
  const [timer, setTimer] = useState<number>(30); // Start with 30 seconds

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

    // Initial data fetch
    fetchApiData();

    // Set up interval for automatic data refresh every 30 seconds
    const interval = setInterval(() => {
      fetchApiData();
      setTimer(30); // Reset the timer
    }, 30000); // 30 seconds

    // Countdown timer for UI
    const countdown = setInterval(() => {
      setTimer((prev) => (prev > 0 ? prev - 1 : 30));
    }, 1000);

    // Clean up intervals on component unmount
    return () => {
      clearInterval(interval);
      clearInterval(countdown);
    };
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

      {/* Timer bar */}
      <div className="my-4">
        <p>Refreshing in {timer} seconds</p>
        <div className="w-full bg-gray-200 h-2 rounded">
          <div
            className="bg-blue-500 h-2 rounded transition duration-300 ease-in-out"
            style={{ width: `${((30 - timer) / 30) * 100}%` }}
          />
        </div>
      </div>

      <div className="mt-4">
        {data.map((item) => (
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
