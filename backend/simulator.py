from typing import Dict, List, Tuple, Any
from utils import calculate_distance


class DeliverySimulator:
    def __init__(
        self,
        warehouses: Dict[str, Tuple[float, float]],
        agents: Dict[str, Tuple[float, float]],
        packages: List[Dict[str, Any]],
    ):
        self.warehouses = warehouses
        self.agents = agents
        self.packages = packages

        # Track total distance traveled by each agent
        self.agent_distances = {agent_id: 0.0 for agent_id in agents}

        # Track which agent delivered which package
        self.package_assignments = []

    def find_nearest_agent(self, warehouse_location: Tuple[float, float]) -> str:
        """
        Find the nearest agent to a given warehouse location.
        """
        nearest_agent = None
        min_distance = float("inf")

        for agent_id, agent_location in self.agents.items():
            distance = calculate_distance(agent_location, warehouse_location)

            if distance < min_distance:
                min_distance = distance
                nearest_agent = agent_id

        return nearest_agent

    def simulate(self) -> Dict[str, Any]:
        """
        Run the full delivery simulation.
        """
        for package in self.packages:
            package_id = package["id"]
            warehouse_id = package["warehouse"]
            destination = tuple(package["destination"])

            warehouse_location = self.warehouses[warehouse_id]

            # Step 1: find nearest agent to warehouse
            agent_id = self.find_nearest_agent(warehouse_location)

            # Step 2: calculate distances
            agent_start = self.agents[agent_id]

            distance_to_warehouse = calculate_distance(agent_start, warehouse_location)
            distance_to_destination = calculate_distance(
                warehouse_location, destination
            )

            total_distance = distance_to_warehouse + distance_to_destination

            # Step 3: update agent distance
            self.agent_distances[agent_id] += total_distance

            # Step 4: store assignment result
            self.package_assignments.append(
                {
                    "package_id": package_id,
                    "assigned_agent": agent_id,
                    "distance": round(total_distance, 2),
                }
            )

        # Step 5: find most efficient agent
        best_agent = min(self.agent_distances, key=self.agent_distances.get)

        return {
            "packages": self.package_assignments,
            "agent_distances": {
                k: round(v, 2) for k, v in self.agent_distances.items()
            },
            "best_agent": best_agent,
        }
