# machine-learning

## Usage

### Sending a json object containing the"track_key" that looks like:
```sh
{
  "track_key": 1
}
```

to `http://127.0.0.1:5000/recommend`

will return an jsonified list of track_ids of the closest related 10songs from songs.csv

Output:
```sh
[
    "2RM4jf1Xa9zPgMGRDiht8O",
    "02s1Voowwhr0qTSOrMVEXk",
    "6PIdcDdMuoyAWeVqMRMLlR",
    "0MiAP4EQGIuikH23RTyP53",
    "2lD4dQpcac8H2Rq5nttJJh",
    "07lPxulz2gpCAVvgemzedl",
    "5MccaBOgJh4MsJNoj72eij",
    "3QBTZEqaCbJxztWh5NTKHs",
    "6yoM6KoDpWXKIWo9UnZ3Ef",
    "7Jbt6KWzS8cpP1xnW0tQ96"
]
```

### Sending 
```sh
{
  "track_key": 1
}
```

to `http://127.0.0.1:5000/recommend`

will return a list of averaged features for the closest related 10songs for visualizations.

Output:
```sh
[
    0.06,
    0.73,
    0.42,
    0.0,
    0.12,
    1.0,
    0.41,
    0.25
]
```