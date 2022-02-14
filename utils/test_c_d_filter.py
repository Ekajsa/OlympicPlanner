def main():
    events = [{
        "discipline": "Curling",
        "description": "Mixed doubles",
        "competition_type": "round robin, session 1",
        "sex": [
            "women",
            "men"
        ],
        "date": "2022-02-02",
        "local_start_time": "20:05",
        "local_end_time": "22:00",
        "participating_countries": [
            "Sweden",
            "Great Britain"
        ]
    },
        {
            "discipline": "Curling",
            "description": "Mixed doubles",
            "competition_type": "round robin, session 1",
            "sex": [
                "women",
                "men"
            ],
            "date": "2022-02-02",
            "local_start_time": "20:05",
            "local_end_time": "22:00",
            "participating_countries": [
                "Australia",
                "USA"
            ]
        }]
    countries = ["sweden", "norway"]
    disciplines = ["curling", "biathlon"]
    filtered_events = []
    for event in events:
        if event["discipline"].lower() in disciplines:
            event_participators = [post.lower() for post in event["participating_countries"]]
            for country in countries:
                if country.lower() in event_participators:
                    filtered_events.append(event["discipline"])
    print(filtered_events)


if __name__ == '__main__':
    main()
