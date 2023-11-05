import { Box } from "@mui/material";
import { Navigate } from 'react-router-dom';
import Header from "../components/Header";
import BarChart from "../components/BarChart";

type BarProps = {
    user: any;
}
const Bar = ({ user }: BarProps) => {
    const checkUserIsAuthenticated = (user: any) => {
        if (user) return (
            <Box m="20px">
                <Header title="Bar Chart" subtitle="Simple Bar Chart" />
                <Box height="75vh">
                    <BarChart />
                </Box>
            </Box>
        )
        return (
            <Navigate to="/" />
        )
    }

    return checkUserIsAuthenticated(user);
};

export default Bar;