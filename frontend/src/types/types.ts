// Interface for Website Data Items
export interface WebsitesDataItem {
  id: number;
  name: string;
  url: string;
  status: boolean;
  latency: number;
}

// Interface for Websites Table Props
export interface WebsitesTableProps {
  data: WebsitesDataItem[];
  loading: boolean;
  error: string | null;
}

// Interface for Pi-hole Data Items
export interface PiHoleDataItem {
  id: number;
  name: string;
  status: boolean;
  dns_queries_today: number;
  ads_blocked_today: number;
  ads_percentage_today: number;
}

// Interface for Pi-hole Table Props
export interface PiHoleTableProps {
  data: PiHoleDataItem[];
  loading: boolean;
  error: string | null;
}
