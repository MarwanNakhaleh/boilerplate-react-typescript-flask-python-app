import React, { useEffect } from 'react';

import { GoogleLogin } from 'react-google-login';
import { gapi } from 'gapi-script'

const UnauthenticatedPage: React.FC = () => {
    const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID as string;

    useEffect(() => {
        function start() {
            gapi.client.init({
                clientId: clientId,
                scope: 'email',
            });
        }

        gapi.load('client:auth2', start);
    }, []);

    const onSuccess = (response: any) => {
        console.log('SUCCESS', response);
        localStorage.setItem('user', JSON.stringify(response));
        window.location.href = '/dashboard'; // or use React Router's useNavigate
    };
    const onFailure = (response: any) => {
        console.log('FAILED', response);
    };

    return (
        <GoogleLogin
            clientId={clientId} // Replace with your Google client ID
            buttonText="Login with Google"
            onSuccess={onSuccess}
            onFailure={onFailure}
            cookiePolicy={'single_host_origin'}
        />
    )
};

export default UnauthenticatedPage;
