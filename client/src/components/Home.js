import React, { useState, useEffect } from "react";
import EventService from "../services/event.service";

const Home = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
      EventService.getAllEvents().then(
      (response) => {
        setEvents(response.data.data);
      },
      (error) => {
        console.log(error);
      }
    );
  }, []);


  return (
    <div>
        <h3 style={{ display: "flex", justifyContent: "center", marginTop: 30}} >Events</h3>
        <h3>
        {events.map((event, index) => (
            <div className={"card"} style={{ background: event.active ? "lightgreen" :"lightpink"}}>
                <div className={"card-content"} key={index}>
                    <div className="media-content">
                        <p className="title is-4">{event.title}</p>
                        <p className="subtitle is-6">{event.organizer_email}</p>
                        <p className="subtitle is-6">{event.date}</p>
                    </div>

                    <div className={"content is-medium"}>
                        {event.description}
                        <br></br>
                    </div>
                </div>
            </div>
        ))}
      </h3>
    </div>
  );
};

export default Home;
