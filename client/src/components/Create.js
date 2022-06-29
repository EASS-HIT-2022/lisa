import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import EventService from "../services/event.service";

const Create = () => {
    const [title, setTitle] = useState("");
    const [organizerEmail, setOrganizerEmail] = useState("");
    const [date, setDate] = useState("");
    const [description, setDescription] = useState("");

    const navigate = useNavigate();

    const handleCreate = async (e) => {
        e.preventDefault();
        try {
            await EventService.createEvent(title, organizerEmail, date, description).then(
                () => {
                    navigate("/eventCreated");
                    window.location.reload();
                },
                (error) => {
                    console.log(error);
                }
            );
        } catch (err) {
            console.log(err);
        }
        return (
            <div>Hello</div>
        )
    };

    return (
        <div style={{ display: "flex", justifyContent: "center", marginTop: 30}}>
            <form onSubmit={handleCreate}>
                <h3 style={{ display: "flex", justifyContent: "center", marginTop: 30}} >Create New Event</h3>
                <input
                    style={{ margin: 10}}
                    className={"input"}
                    type="text"
                    placeholder="Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
                <input
                    style={{ margin: 10}}
                    className={"input"}
                    type="email"
                    placeholder="email"
                    value={organizerEmail}
                    onChange={(e) => setOrganizerEmail(e.target.value)}
                />
                <input
                    style={{ margin: 10}}
                    className={"input"}
                    type="date"
                    placeholder="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                />
                <input
                    style={{ margin: 10}}
                    className={"input"}
                    type="text"
                    placeholder="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <div style={{ display: "flex", justifyContent: "center"}} >
                    <button type="submit" className={"button is-light"} style={{ margin: 10}} >Create</button>
                </div>
            </form>
        </div>
    );
};

export default Create;
