# bajson
library for converting to/from json

[![pypi](http://img.shields.io/pypi/v/bajson.png)](https://pypi.python.org/pypi/bajson)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/bajson.svg)](https://pypi.python.org/pypi/bajson/)

## Install
```bash
 $ pip install bajson
```

## Usage

### JSON to CSV
* the root of the input json should be in list format

  *Invalid* 
  ```json
  "data": [
      {
        "data": "value",
        "data1": "value1"
      },
      {
        "data": "value2",
        "data1": "value3"
      },
    ]
  ``` 
  *Valid*
  ```json
  [
    {
      "data": "value",
      "data1": "value1"
    },
    {
      "data": "value2",
      "data1": "value3"
    },
  ]
  ```
* Converting nested json objects
  ```json
  [
    {
      "data": {
            "firstkey": "firstvalue",
            "secondvalue": "secondvalue",
          },           
      "data1": "value1"
    },
    {
      "data": {
            "firstkey": "firstvalue1",
            "secondvalue": "secondvalue1",
          },           
      "data1": "value2"
    },
  ]
  ```
  

    | data.firstkey | data.secondkey | data1 |
    | -------- | ----------- | ----------- |
    | firstvalue | secondvalue | value1 |
    | firstvalue1 | secondvalue1 | value2 |
    
    
* Converting arrays in json objects
  ```json
  [
    {
      "data": [
            "firstvalue",
            "secondvalue",
          ],           
      "data1": "value1"
    },
    {
      "data": [
            "firstvalue1",
          ],           
      "data1": "value2"
    },
  ]
  ```
  

    | data.0 | data.1 | data1 |
    | -------- | ----------- | ----------- |
    | firstvalue | secondvalue | value1 |
    | firstvalue1 |  | value2 |


**Code Example**
```python
from bajson.libcsv import json_to_csv

json_to_csv("input.json", "output.csv")
```

### CSV to JSON

bajson can convert csv file to json format vice versa. Formats above are valid for this operation too. However there is one exception about array conversion,

If csv headers are as follows

  | data.0 | data.1 | data1 |
  | -------- | ----------- | ----------- |
  | firstvalue | secondvalue | value1 |
  | firstvalue1 |  | value2 |
    
This will be converted to object form instead of array form
  ```json
  [
    {
      "data": {
            "0": "firstvalue",
            "1": "secondvalue",
          },           
      "data1": "value1"
    },
    {
      "data": {
            "0": "firstvalue1",
          },           
      "data1": "value2"
    },
  ]
  ```
  
**Code Example**
```python
from bajson.libcsv import csv_to_json

csv_to_json("input.csv", "output.json")
```


### Future features
- [ ] Support string input/output parameters
- [ ] JSON <==> XML
