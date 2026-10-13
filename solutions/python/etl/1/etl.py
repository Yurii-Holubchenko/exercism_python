def transform(legacy_data):
    new_points = {}
    
    for points, letters in legacy_data.items():
        new_points.update(
            dict.fromkeys(
                [letter.lower() for letter in letters],
                points
            )
        )

    return new_points
