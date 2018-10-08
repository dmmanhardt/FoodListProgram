DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS recipe;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE recipe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_name TEXT UNIQUE NOT NULL,
  meal_served TEXT NOT NULL,
  serving_size INTEGER NOT NULL,
  recipe_ingredients TEXT NOT NULL,
  recipe_measurements TEXT NOT NULL,
  recipe_amounts TEXT NOT NULL
);
