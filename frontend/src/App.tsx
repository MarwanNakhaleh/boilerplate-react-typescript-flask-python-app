import { useState, useEffect } from "react";
import { Routes, Route, Navigate } from 'react-router-dom';
import Bar from "./pages/Bar";
import Calendar from "./pages/Calendar";
import Contacts from "./pages/Contacts";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import Topbar from "./layout/Topbar";
import Unauthenticated from './pages/Unauthenticated';

import { GoogleLoginResponse, GoogleLoginResponseOffline, useGoogleLogin } from 'react-google-login';
import Dashboard from "./pages/Dashboard";

function App() {
  const [theme, colorMode] = useMode();
  const [user, setUser] = useState<GoogleLoginResponse | GoogleLoginResponseOffline | null>(null);

  const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID as string;

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const { signIn } = useGoogleLogin({
    onSuccess: (response: GoogleLoginResponse | GoogleLoginResponseOffline) => {
      localStorage.setItem('user', JSON.stringify(response));
      setUser(response);
    },
    clientId: clientId, // Replace with your Google client ID
    isSignedIn: true,
    onFailure: (error: any) => {
      console.error(error);
    },
  });

  const signOut = () => {
    localStorage.removeItem('user');
    setUser(null);
    window.location.href = '/'; // or use React Router's useNavigate
  };

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <main className="content">
            <Topbar user={user} signIn={signIn} signOut={signOut} />
            <Routes>
              <Route path="/" element={user ? <Navigate to="/dashboard" /> : <Unauthenticated />} />
              <Route path="/bar" element={user ? <Bar /> : <Unauthenticated />} />
              <Route path="/calendar" element={user ? <Calendar /> : <Unauthenticated />} />
              <Route path="/contacts" element={user ? <Contacts /> : <Unauthenticated />} />
              <Route path="/dashboard" element={user ? <Dashboard /> : <Unauthenticated />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
