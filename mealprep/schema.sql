DROP TABLE IF EXISTS recipe;

CREATE TABLE recipe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_name TEXT UNIQUE NOT NULL,
  meal_served TEXT NOT NULL,
  serving_size INTEGER NOT NULL
);

CREATE TABLE ingredient (
  recipe_id INT REFERENCES recipe(id),
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ingredient TEXT NOT NULL,
  measurement TEXT,
  amount FLOAT
);
