export interface Location {
  _id: string;
  location_name: string;
  lat: number;
  long: number;
}

export default interface ILocationResponse {
  type?: string;
  status_code?: number;
  message: string;
  result: Location;
}
