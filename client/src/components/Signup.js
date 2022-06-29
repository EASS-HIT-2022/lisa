import React, { useState } from "react";
import AuthService from "../services/auth.service";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      await AuthService.signup(email, password).then(
        (response) => {
          // check for token and user already exists with 200
          //   console.log("Sign up successfully", response);
          navigate("/home");
          window.location.reload();
        },
        (error) => {
          console.log(error);
        }
      );
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div style={{ display: "flex", justifyContent: "center", marginTop: 30}}>
      <form onSubmit={handleSignup}>
        <h3 style={{ display: "flex", justifyContent: "center", marginTop: 30}} >Sign up</h3>
        <input
            style={{ margin: 10}}
            className={"input"}
            type="email"
            placeholder="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
        />
        <input
            style={{ margin: 10}}
            className={"input"}
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
        />
        <div style={{ display: "flex", justifyContent: "center"}} >
          <button type="submit" className={"button is-light"} style={{ margin: 10}} >Sign up</button>
        </div>
      </form>
    </div>
  );
};

export default Signup;
