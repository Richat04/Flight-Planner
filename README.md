# 🛫 Flight Planner
This project implements a flight planning system that selects optimal travel routes between cities based on different customer preferences. Developed for COL106, it simulates real-world constraints like flight schedules, layovers, and pricing to find efficient itineraries.
## ✈️ Problem Overview
Given a set of flights with their departure and arrival details, the planner must suggest a route from a start city to an end city that departs no earlier than time t1 and arrives no later than time t2.

The planner provides 3 types of optimized routes:
- Fewest Flights & Earliest Arrival
- Cheapest Fare
- Fewest Flights & Cheapest Fare (Tie-breaker)
Layovers must be at least 20 minutes long.
## 🧠 Key Features
- Efficient algorithms for route finding using real-world flight constraints.
- Handles multiple flights between cities and overlapping time windows.
- Custom route logic for three distinct user priorities.
- Worst-case time complexities:
  - O(m) for fewest flights
  - O(m log m) for cheapest options
## ⚠ Constraints
- All flights and cities are represented as integers.
- Each city can have at most 100 incoming/outgoing flights.
- Layovers must be ≥ 20 minutes.
- You may add helper methods or classes, but do not change method signatures from the starter code.

## 🧱 Project Structure
> planner.py       # Core logic with Planner class and route finding algorithms
> 
> flight.py        # Flight class with flight metadata
> 
> main.py          # Debugging and test script

## 📦 Output Format
- All flights and cities are represented as integers.
- Each city can have at most 100 incoming/outgoing flights.
- Layovers must be ≥ 20 minutes.
- You may add helper methods or classes, but do not change method signatures from the starter code.
