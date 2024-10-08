import React, { useEffect, useState } from 'react';
import { fetchData } from '../services/api';
import PiHoleTable from '../components/PiHoleTable';
import WebsitesTable from '../components/WebsitesTable';
import { WebsitesDataItem, PiHoleDataItem } from '../types/types';

const Dashboard: React.FC = () => {
  const [loadingWebsites, setLoadingWebsites] = useState<boolean>(true);
  const [loadingPiHole, setLoadingPiHole] = useState<boolean>(true);
  const [errorWebsites, setErrorWebsites] = useState<string | null>(null);
  const [errorPiHole, setErrorPiHole] = useState<string | null>(null);
  const [timer, setTimer] = useState<number>(30); // Start with 30 seconds
  const [websitesData, setWebsitesData] = useState<WebsitesDataItem[]>([]);
  const [piHoleData, setPiHoleData] = useState<PiHoleDataItem[]>([]);

  useEffect(() => {
    const fetchWebsitesData = async () => {
      try {
        const result = await fetchData<WebsitesDataItem[]>('/websites/');
        setWebsitesData(result);
        setErrorWebsites(null);
      } catch (err) {
        setErrorWebsites('Error fetching websites data');
      } finally {
        setLoadingWebsites(false);
      }
    };

    const fetchPiHoleData = async () => {
      try {
        const result = await fetchData<PiHoleDataItem[]>('/pihole/');
        setPiHoleData(result);
        setErrorPiHole(null);
      } catch (err) {
        setErrorPiHole('Error fetching PiHole data');
      } finally {
        setLoadingPiHole(false);
      }
    };


    // Initial data fetch
    fetchWebsitesData();
    fetchPiHoleData();

    // Set up interval for automatic data refresh every 30 seconds
    const interval = setInterval(() => {
      fetchWebsitesData();
      fetchPiHoleData();
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

  if (loadingWebsites || loadingPiHole)
    return <div className="text-center">Loading...</div>;

  if (errorWebsites || errorPiHole)
    return (
      <div className="text-center text-red-500">
        {errorWebsites || errorPiHole}
      </div>
    );

  return (
    <div className="container mx-auto mt-4">
      <h1 className="text-2xl font-bold text-left">Jolly Chimp</h1>

      <div className="my-10 text-center">
        <p className="text-lg mb-2">Refreshing in {timer} seconds</p>
        <div className="w-3/4 mx-auto bg-gray-200 rounded h-2">
          <div
            className="bg-blue-500 h-2 rounded transition duration-300 ease-in-out"
            style={{ width: `${((30 - timer) / 30) * 100}%` }}
          />
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3 lg:gap-8">
        <WebsitesTable data={websitesData} loading={loadingWebsites} error={errorWebsites} />
        <PiHoleTable data={piHoleData} loading={loadingPiHole} error={errorPiHole} />
        </div>
    </div>
  );
};

export default Dashboard;
