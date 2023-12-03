import { useState } from "react";
import { Routes, Route, Navigate } from 'react-router-dom';
import Bar from "./pages/Bar";
import Calendar from "./pages/Calendar";
import Contacts from "./pages/Contacts";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import Topbar from "./layout/Topbar";
import Unauthenticated from './pages/Unauthenticated';

import { GoogleLoginResponse, GoogleLoginResponseOffline, useGoogleLogin } from 'react-google-login';

function App() {
  const [theme, colorMode] = useMode();
  const [user, setUser] = useState<GoogleLoginResponse | GoogleLoginResponseOffline | null>(null);

  const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID as string;

  const { signIn } = useGoogleLogin({
    onSuccess: (response) => {
      setUser(response as GoogleLoginResponse);
    },
    clientId: clientId, // Replace with your Google client ID
    isSignedIn: true,
    onFailure: (error) => {
      console.error(error);
    },
  });

  const signOut = () => {
    setUser(null);
  };

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <main className="content">
            <Topbar user={user} signIn={signIn} signOut={signOut} />
            <Routes>
              <Route
                path="/"
                element={user ? <Navigate to="/bar" /> : <Unauthenticated />}
              />
              <Route path="/bar" element={user ? <Bar /> : <Unauthenticated />} />
              <Route path="/calendar" element={<Calendar />} />
              <Route path="/contacts" element={<Contacts />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
