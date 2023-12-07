import { useState, useEffect } from "react";
import { Box } from "@mui/material";
import { DataGrid, GridToolbar, GridColDef } from "@mui/x-data-grid";
import { useTheme } from "@mui/material";

import { tokens } from "../theme";
import Header from "../components/Header";
import { Contact } from "../types/Contact";
import { sendRequest } from "../helpers/request";

const Contacts = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [contacts, setContacts] = useState<Contact[]>([]);

    useEffect(() => {
        sendRequest(`${process.env.API_URL}/api/v1/contacts`, {
            method: "GET",
        })
            .then((data) => setContacts(data.results as Contact[]))
    }, []);

    const columns: GridColDef[] = [
        { field: "id", headerName: "ID", flex: 0.5 },
        { field: "registrarId", headerName: "Registrar ID" },
        {
            field: "name",
            headerName: "Name",
            flex: 1,
            cellClassName: "name-column--cell",
        },
        {
            field: "age",
            headerName: "Age",
            type: "number",
            headerAlign: "left",
            align: "left",
        },
        {
            field: "phone",
            headerName: "Phone Number",
            flex: 1,
        },
        {
            field: "email",
            headerName: "Email",
            flex: 1,
        },
        {
            field: "address",
            headerName: "Address",
            flex: 1,
        },
        {
            field: "city",
            headerName: "City",
            flex: 1,
        },
        {
            field: "zipCode",
            headerName: "Zip Code",
            flex: 1,
        },
    ];

    return (
        <Box m="20px">
            <Header
                title="CONTACTS"
                subtitle="List of Contacts for Future Reference"
            />
            <Box
                m="40px 0 0 0"
                height="75vh"
                sx={{
                    "& .MuiDataGrid-root": {
                        border: "none",
                    },
                    "& .MuiDataGrid-cell": {
                        borderBottom: "none",
                    },
                    "& .name-column--cell": {
                        color: colors.greenAccent[300],
                    },
                    "& .MuiDataGrid-columnHeaders": {
                        backgroundColor: colors.blueAccent[700],
                        borderBottom: "none",
                    },
                    "& .MuiDataGrid-virtualScroller": {
                        backgroundColor: colors.primary[400],
                    },
                    "& .MuiDataGrid-footerContainer": {
                        borderTop: "none",
                        backgroundColor: colors.blueAccent[700],
                    },
                    "& .MuiCheckbox-root": {
                        color: `${colors.greenAccent[200]} !important`,
                    },
                    "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
                        color: `${colors.grey[100]} !important`,
                    },
                }}
            >
                <DataGrid
                    rows={contacts}
                    columns={columns}
                    components={{ Toolbar: GridToolbar }}
                />
            </Box>
        </Box>
    );
};

export default Contacts;
