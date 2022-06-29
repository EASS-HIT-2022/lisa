import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "/events";

const getAllEvents = () => {
  return axios.get(API_URL);
};

const createEvent = (title, organizer_email, date, description) => {
  return axios
      .post(API_URL,{
        title,
        organizer_email,
        date,
        description,
      }, { headers: authHeader() })
      .then((response) => {
        return response.data;
      });
};

const EventService = {
    getAllEvents,
    createEvent,
};

export default EventService;
