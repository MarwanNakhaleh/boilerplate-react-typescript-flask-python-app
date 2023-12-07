/*
{
    "metadata": {
        "path": "/transactions",
        "query": {
            "limit": null,
            "start": null
        }
    },
    "num_results": 8,
    "results": [
        {
            "cost": "43.95",
            "date": "2021-09-01",
            "txId": "01e4dsa",
            "user": "johndoe"
        },
        {
            "cost": "133.45",
            "date": "2022-04-01",
            "txId": "0315dsaa",
            "user": "jackdower"
        },
        {
            "cost": "43.95",
            "date": "2021-09-01",
            "txId": "01e4dsa",
            "user": "aberdohnny"
        },
        {
            "cost": "200.95",
            "date": "2022-11-05",
            "txId": "51034szv",
            "user": "goodmanave"
        },
        {
            "cost": "13.55",
            "date": "2022-11-02",
            "txId": "0a123sb",
            "user": "stevebower"
        },
        {
            "cost": "43.95",
            "date": "2021-09-01",
            "txId": "01e4dsa",
            "user": "aberdohnny"
        },
        {
            "cost": "24.20",
            "date": "2019-04-15",
            "txId": "120s51a",
            "user": "wootzifer"
        },
        {
            "cost": "133.45",
            "date": "2022-04-01",
            "txId": "0315dsaa",
            "user": "jackdower"
        }
    ]
}
*/
export type ApiResponse = {
    metadata: Metadata;
    num_results: number;
    results: object[];
}

type Metadata = {
    path: string;
    query: object;
}