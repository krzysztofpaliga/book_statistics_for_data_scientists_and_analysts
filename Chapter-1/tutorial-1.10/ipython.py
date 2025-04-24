import json
json_data = """
[
  {
    "Height": 170,
    "Weight": 60,
    "Age": 20,
    "Speed": 80,
    "Tax Amount": 1000
  },
  {
    "Height": 180,
    "Weight": 70,
    "Age": 25,
    "Speed": 90,
    "Tax Amount": 1500
  },
  {
    "Height": 190,
    "Weight": 80,
    "Age": 30,
    "Speed": 100,
    "Tax Amount": 2000
  },
  {
    "Height": 200,
    "Weight": 90,
    "Age": 35,
    "Speed": 110,
    "Tax Amount": 2500
  },
  {
    "Height": 210,
    "Weight": 100,
    "Age": 40,
    "Speed": 120,
    "Tax Amount": 3000
    }
    ]
    """
data = json.loads(json_data)
data
%history -f ipython.py
