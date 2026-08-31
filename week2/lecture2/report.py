def main():
    spacecraft = {"name": "Trailblazer 1", "distance": "177"}
    spacecraft.update({"orbit": "Neptune"})
    print(create_report(spacecraft))

def create_report(sc):
    return f"""
    ========= REPORT =========

    Name: {sc.get("name", "Unknown")}
    Distance: {sc.get("distance", "Unknown")} AU
    Orbit: {sc.get("orbit", "Unknown")}

    ==========================
    """

main()