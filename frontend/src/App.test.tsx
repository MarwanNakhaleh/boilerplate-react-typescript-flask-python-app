import { render, screen } from '@testing-library/react';
import UnauthenticatedPage from './pages/Unauthenticated';

test('renders Google login link', () => {
    render(<UnauthenticatedPage />);
    const linkElement = screen.getByText(/Login with Google/i);
    expect(linkElement).toBeInTheDocument();
});