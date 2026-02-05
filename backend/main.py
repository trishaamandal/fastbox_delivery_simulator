import os
from utils import load_json, save_json
from simulator import DeliverySimulator


def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "backend", "data")
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    input_file = "test_case_1.json"
    input_path = os.path.join(DATA_DIR, input_file)

    data = load_json(input_path)

    warehouses = {wid: tuple(coords) for wid, coords in data["warehouses"].items()}

    agents = {aid: tuple(coords) for aid, coords in data["agents"].items()}

    packages = data["packages"]

    # Ruun
    simulator = DeliverySimulator(warehouses, agents, packages)
    result = simulator.simulate()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "result.json")
    save_json(output_path, result)

    print("Simulation completed successfully.")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()
