test_cases = {
        "test_1": (
            [  # Input Names
                "Courtney Mackstutis",
                "Angela Gimbel",
                "Hector Koba"
            ],
            [  # DMV Records
                "Courtney Mackstutis;4766 Moctezuma",
                "Angela Gimbel;1270 Finazzo",
                "Hector Koba;7074 Turrill"
            ],
            [  # Expected Output
                "4766 Moctezuma",
                "1270 Finazzo",
                "7074 Turrill"
            ]
        ),
        "test_2": (
            [  # Input Names
                "Courtnet Mackstutis",
                "Angela Gimbrel",
                "Hector Kba"
            ],
            [  # DMV Records
                "Courtney Mackstutis;4766 Moctezuma",
                "Angela Gimbel;1270 Finazzo",
                "Hector Koba;7074 Turrill"
            ],
            [  # Expected Output
                "4766 Moctezuma",
                "1270 Finazzo",
                "7074 Turrill"
            ]
        ),
        "test_3": (
            [  # Input Names
                "Kourtnie Makstuttis",
                "Anjelica Gimbell",
                "Hector Cobrah"
            ],
            [  # DMV Records
                "Courtney Mackstutis;4766 Moctezuma",
                "Angela Gimbel;1270 Finazzo",
                "Hector Koba;7074 Turrill"
            ],
            [  # Expected Output
                "4766 Moctezuma",
                "1270 Finazzo",
                "7074 Turrill"
            ]
        )
    }