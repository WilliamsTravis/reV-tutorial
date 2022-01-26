## A List of Common Problems When Configuring and Running reV

### 1) Unneeded commas in the json configuration:
    {
        "this": [
            "will",
            "not",
            "work",  # Because of this comma
        ]
    }
    
### 2) SAM Config Parameter Name Spelling

    "fixed_operating_costs": 1404000.0,  # This extra "s" caused an hour of confusion
    "fixed_charge_rate": 0.051,
    "system_capacity": 18000,
