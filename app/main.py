from fastapi import FastAPI

import data.users
import data.buses
import data.passengers
import data.drivers

app = FastAPI()

@app.get("/buses")
def get_buses():
  return data.buses.main()

@app.get("/buses/{bus_id}")
def get_bus(bus_id: int):
  buses = data.buses.main()
  for bus in buses:
    if bus['id'] == bus_id:
      return bus

@app.get("/drivers")
def get_drivers():
  return data.drivers.main()

@app.get("/drivers/{driver_id}")
def get_driver(driver_id: int):
  drivers = data.drivers.main()
  for driver in drivers:
    if driver['id'] == driver_id:
      return driver

@app.get("/users")
def get_users():
  return data.users.main()

@app.get("/users/{user_id}")
def get_user(user_id: int):
  users = data.users.main()
  for user in users:
    if user['id'] == user_id:
      return user

@app.get("/passengers")
def get_passengers():
  return data.passengers.main()

@app.get("/passengers/{passenger_id}")
def get_passenger(passenger_id: int):
  passengers = data.passengers.main()
  for passenger in passengers:
    if passenger['id'] == passenger_id:
      return passenger