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

@app.get("/users")
def get_users():
  return data.users.main()

@app.get("/users/{user_id}")
def get_user(user_id: int):
  users = data.users.main()
  for user in users:
    if user['id'] == user_id:
      return user
