#!/usr/bin/python3
# City class definition

# Import BaseModel
from models.base_model import BaseModel

# Define City class
class City(BaseModel):
    # State ID
    state_id = ""
    # City name
    name = ""

    # Constructor for the class
    def __init__(self, *args, **kwargs):
        # Call parent constructor
        super().__init__(*args, **kwargs)