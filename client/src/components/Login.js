import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import AuthService from "../services/auth.service";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await AuthService.login(email, password).then(
        () => {
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
      <form onSubmit={handleLogin}>
        <h3 style={{ display: "flex", justifyContent: "center", marginTop: 30}} >Login</h3>
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
          <button type="submit" className={"button is-light"} style={{ margin: 10}} >Log in</button>
        </div>
      </form>
    </div>
  );
};

export default Login;
